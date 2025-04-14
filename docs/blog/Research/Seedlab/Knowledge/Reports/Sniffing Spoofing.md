---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
---  

# Sniffing Spoofing

首先我们启动容器：

![](../../../../../assets/Pasted%20image%2020250413211040.png)

在宿主机上使用 `ifconfig` 查看网络配置，找到具有 IP 地址为 10.9.0.1 的接口为 `br-1cf2b5a26687`：

![](../../../../../assets/Pasted%20image%2020250413211440.png)

或者使用 `docker network ls` 查看所有网络：

![](../../../../../assets/Pasted%20image%2020250413211641.png)

同样可以得到接口为 `br-1cf2b5a26687`
***
## 任务 1.1：嗅探包

### 任务 1.1A

首先在 hostA 容器中编写一个简单的发送数据包的程序：

```python title="send_packet.py"
import socket

data = b"Hello World!\n"
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp.sendto(data, ("10.9.0.6", 8080))
```

然后根据我们之前得到的接口在宿主机编写嗅探数据包程序：

```python title="sniffer.py"
from scapy.all import *

def print_pkt(pkt):
    pkt.show()

pkt = sniff(iface = 'br-1cf2b5a26687', filter = 'udp', prn = print_pkt)
```

在宿主机 root 下运行嗅探数据包程序，同时在 hostA 容器中发送数据包，得到：

![](../../../../../assets/Pasted%20image%2020250413220312.png)

可以看到我们成功捕获到了数据包，如果我们不使用 root 权限运行嗅探数据包程序，则会出现报错：

![](../../../../../assets/Pasted%20image%2020250413221325.png)

这说明我们没有足够的权限来嗅探数据包

- 后记：后来发现不需要编程序也可以发 UDP 包，使用 `echo "data" > /dev/udp/10.9.0.6/8080` 即可，同样能达到效果
***
### 任务 1.1B

那我们使用 ping 来发送 ICMP 包，改动原来的 sniffer.py 将 filter 改为 "icmp"，再次运行，如果我们首先 `echo "data" > /dev/udp/10.9.0.6/8080` 再次发送 UDP 包：

![](../../../../../assets/Pasted%20image%2020250413223642.png)

可以看到得到的是 ICMP 的错误响应包，如果我们纯使用 ping 命令发送 ICMP 包：

![](../../../../../assets/Pasted%20image%2020250413223801.png)

可以看到我们捕获到了真正的 ICMP 包

我们再次改动 sniffer.py 将 filter 改为 "tcp src host 10.9.0.5 and dst port 23"，并在 hostA 中使用 `echo "data" > /dev/udp/10.9.0.6/23`，并未捕获到数据包，使用 `echo "data" > /dev/tcp/10.9.0.6/8080` 直接显示 Connection Refused：

![](../../../../../assets/Pasted%20image%2020250413225212.png)

在 hostB 中使用 `echo "data" > /dev/tcp/10.9.0.5/23`，也没有捕获到数据包，但是我们在 hostA 中使用 `echo "data" > /dev/tcp/10.9.0.6/23`，可以捕获到数据包：

![](../../../../../assets/Pasted%20image%2020250413225658.png)

我们再设定 filter 为 "net 128.230.0.0/16" 运行 sniffer.py，在 hostA 中使用 `echo "data" > /dev/tcp/10.9.0.6/23`，捕获不到数据包，改为 `echo "data" > /dev/udp/128.230.0.127/8080` 即可捕获：

![](../../../../../assets/Pasted%20image%2020250413230337.png)
***
## 任务 1.2：伪造 ICMP 包

先在宿主机上运行 sniffer.py 捕获所有数据包

进入 hostA 的 python 交互界面，向 hostB 发送一个 ICMP 包：

![](../../../../../assets/Pasted%20image%2020250413231541.png)

可以在宿主机中看到：

![](../../../../../assets/Pasted%20image%2020250413231652.png)

这说明我们成功伪造了 ICMP echo 请求包并且得到了响应
***
## 任务 1.3：Traceroute

我们直接在宿主机当中编写一个 traceroute.py 的程序，去寻找到达 www.baidu.com 的 IP 地址 223.109.82.16 的路径：

```python title="traceroute.py"
from scapy.all import *

target = '223.109.82.16'

for ttl in range(1, 100):
    pkt = IP(dst = target, ttl = ttl) / ICMP()
    reply = sr1(pkt, timeout = 2, verbose = 0)
    if reply is None:
        print(f"{ttl}: *")
    elif reply.type == 0:
        print(f"{ttl}: {reply.src} Arrived!")
        break
    else:
        print(f"{ttl}: {reply.src}")
```

其中 `timeout = 2` 表示 2 秒未回应就放弃，`verbose = 0` 表示输出尽量简洁，运行得到结果：

![](../../../../../assets/Pasted%20image%2020250413233640.png)

和我们直接用 mtr 工具是一样的：

![](../../../../../assets/Pasted%20image%2020250413233705.png)
***
## 任务 1.4：窃听和伪造结合

在 seed-attacker 中编写程序 attack.py：

```python title="attack.py"
from scapy.all import *

def spoof_reply(pkt):
        if ICMP in pkt and pkt[ICMP].type == 8:
                ip = IP(src = pkt[IP].dst, dst = pkt[IP].src)
                icmp = ICMP(type = 0, id = pkt[ICMP].id, seq = pkt[ICMP].seq)
                data = pkt[Raw].load
                send(ip/icmp/data, iface = "br-1cf2b5a26687", verbose = 0)

sniff(filter = "icmp and icmp[0] = 8", prn = spoof_reply, iface = "br-1cf2b5a26687")
```

运行 attack.py，在 hostA 中尝试 `ping 1.2.3.4`，一个不存在的互联网主机，得到结果如下：

![](../../../../../assets/Pasted%20image%2020250413235611.png)

这代表着我们对于一个不存在的主机都成功嗅探和伪造了一个 ICMP 响应包

我们接着 `ping 10.9.0.99`，一个不存在的局域网主机，得到结果如下：

![](../../../../../assets/Pasted%20image%2020250413235756.png)

这是因为 10.9.0.99 首先被认为是位于局域网当中的主机，那么就发送 ARP 请求将 IP 地址动态映射到 MAC 地址，首先会去寻找 ARP 缓存，缓存没有再去直接访问主机，因为 10.9.0.99 本身就不存在，所以无响应，返回 ICMP 错误

我们可以用 `arp -a` 查看 ARP 缓存：

![](../../../../../assets/Pasted%20image%2020250414010445.png)

可以看到确实有查询，但是并没有 10.9.0.99

我们再 `ping 8.8.8.8`，一个存在的互联网主机，得到结果如下：

![](../../../../../assets/Pasted%20image%2020250413235926.png)

可以看到嗅探伪造成功，但是因为本身互联网主机也存在且可以 ping 通，所以我们伪造的回应和实际的回应都出现了，但是因为我们的 attacker 跟 hostA 在同一个局域网中，所以我们可以看到我们的回应包比实际的回应包先到达 hostA
***
## 任务 2.1：编写数据包嗅探程序

### 任务 2.1A

