---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
---  

# BGP and Attacks

## 自治系统及自治系统号

自治系统（Autonomous System，简称 AS）一共有四个类别：

- 残桩自治系统（Stub AS）
	- 仅作为客户，不给其他人提供转送服务（可以理解为拓扑图转换成类似树的结构的叶节点）
	- 下面是 AS11872，Syracuse University 残桩自治系统的邻居（即相连自治系统）和拓扑图：
	
	![](../../../../../assets/Pasted%20image%2020241130011446.png)
- 专送（过境）自治系统（Transit AS）
	- 为其他自治系统提供转送服务
	- 分为小型（Small）转送/过境自治系统和大型（Large）转送/过境自治系统
	- 下面是 AS3754，Nysernet 小型转送自治系统和 AS174，Cogent 大型转送自治系统的示意图：
	
	![](../../../../../assets/Pasted%20image%2020241130011235.png)
	
	![](../../../../../assets/Pasted%20image%2020241130011924.png)
- 互联网交换中心（Internet Exchange/Internet Exchange Point，简称 IX/IXP）

一般情况下，每个自治系统都有自己的编号，我们称其为自治系统号（Autonomous System Number，简称 ASN），起初是以 16 位二进制存储的，后面（应该是装不下了）扩展到 32 位。

!!! tip "ASN 和 IP"

	=== "根据 ASN 找到 IP 前缀"
	
		使用命令行 `whois -h whois.radb.net -- '-i origin ASN'|grep route` 可以通过 ASN 查询到自治系统的 IP 前缀（即路由器信息）
		
		![](../../../../../assets/Pasted image 20241130010055.png)
	
	=== "根据 IP 地址找到 ASN"
	
		使用命令行 `whois -h whois.radb.net IP` 可以通过 IP 地址找到所属 AS 的相关信息
		
		![](../../../../../assets/Pasted image 20241130011131.png)

我们可以通过命令行 `mtr -zb host` 来查看从自己这台机器到 `host` 所经过的各个自治系统

!!! example "Example"

	杜老师在美国的家中使用命令行 `mtr -zb www.ustc.edu.cn` 连接到中科大网站所经过的自治系统如下所示：
	
	![](../../../../../assets/Pasted image 20241130000215.png)
	
	其中以第十行为分界，第 1-2 行是在杜老师家内部传递数据包，第 3-9 行经过了两个美国的自治系统（可以根据域名看出来层层从镇到市最后到纽约市），然后来到中国境内（chinaunicom 即为中国联通），12-17 行再经过两个自治系统来到中科大网站。
	
	出现 `???` 的情况是因为这是一个没有在 `mtr` 数据库的自治系统（在这个例子里面也是正常的，因为这是杜老师家的内网），第 10 行（`waiting for reply`）可能是因为那个自治系统做了一些安全措施使得无法访问。
	
	!!! tip "`mtr` 的机制"
	
		`mtr` 的机制其实在于一个叫 TTL（Time To Live）的字段，它规定了一个包最多能传输经过的节点个数，每经过一个节点 TTL 自减。
		
		当来到一个节点且 TTL 为 0 时，当前节点会给源主机发送回应报文，里面有当前节点的相关信息。主机不断发送 TTL 从 1 开始递增的数据包，并接收回应报文，整理就可以得到整条路径的相关信息。
***
## 对等关系与互联网交换中心

两个自治系统可以通过直接或间接（通过另一个自治系统，其实就是转送自治系统）的方式互联。对于直接连接的方式，即两个网络需要在物理意义上被连接，这被称为<font color="red">对等互连</font>，两个自治系统的关系被称为对等关系（Peer）。全球自治系统连接情况（即每个自治系统与哪些自治系统连接）可以参见 [https://stat.ripe.net/widget/asn-neighbours](https://stat.ripe.net/widget/asn-neighbours)

对等互连可以在数据中心（在此两个自治系统相互连接）秘密地完成，也可以在一个公共的地点（该地
点为自治系统提供对等互连的设施）进行对等互连。这种公开的场所称为互联网交换点（IXP）或互联
网交换中心（IX）。全球互联网交换中心地图可以参见 [http://www.datacentermap.com](http://www.datacentermap.com/)

![](../../../../../assets/Pasted%20image%2020241130004723.png)
***
从顶层模块来看，整个互联网其实就是不同的主机通过网络组成一个残桩自治系统，每个自治系统的 BGP 路由器连接到互联网交换中心进行对等互连相互联系，也可以通过转送自治系统和其他残桩自治系统对等互连相互联系，这便编织成了整个互联网。
***
## BGP 工作原理

