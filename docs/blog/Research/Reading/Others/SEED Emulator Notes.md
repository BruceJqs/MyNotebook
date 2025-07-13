---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
---  

# SEED emulator : an internet emulator for research and education

## Introduction

用杜老师上课例子作引

- 互联网仿真和网络仿真是不一样的
- Paper 目的是给更大的社区呈现这个设计，获取更多反馈和意见
* * *
## Related Work and Our Approach

### Comparison with Relate Work

一个好的互联网仿真器得有三个元素：

- 网络仿真
    - 包含主机、路由器、网络、路由
    - 目前的网络仿真器例如 Mininet、Common Open Research Emulator、NS-3、GNS-3、NetSim、OPNET 在这里做的很好
    - 我们的仿真器在这里有些许功能欠缺例如网络带宽和速度有限（很有用但是目前没有实现），但是这并不是我们仿真器的重点
- 互联网设施仿真
    - 包含自治系统、互联网交换中心、BGP 路由（核心）、对等关系
    - Greybox 和 Mini-Internet Project 有所涉及
- 服务设施仿真
    - 包含 DNS、区块链、Darknet、Botnet、CDN（Content Delivery Network）
    - 这是我们仿真器的亮点
* * *
### Our Approach

分为三个部分：组建仿真，运行仿真和与仿真器交互

![](../../../../assets/Pasted%20image%2020250713111350.png)
* * *
## Emulating Internet Infrastructure

顶层模块调用语句：

- 互联网交换中心：

![](../../../../assets/Pasted%20image%2020250713111404.png)

- 自治系统：

![](../../../../assets/Pasted%20image%2020250713111417.png)

- 不平等对等关系：

![](../../../../assets/Pasted%20image%2020250713111430.png)

- 平等对等关系：

![](../../../../assets/Pasted%20image%2020250713111439.png)

通过 BGP Large Communities Protocol 实现对等关系

- 主机可调用的 API（可用于自定义）：

![](../../../../assets/Pasted%20image%2020250713111449.png)

- 将网络接到真实环境中：将数据包引到一个出口（自治系统）然后接入真实互联网中
    
    - 该自治系统宣称所有 IPv4 地址空间：0.0.0.0/1 和 128.0.0.0/1，如果数据包的目标 IP 地址不在仿真器网络中就会被引到这个自治系统当中，如果想要限制到达现实网络中的 IP 地址范围可以缩小地址空间范围

![](../../../../assets/Pasted%20image%2020250713111458.png)

- 分布式仿真：将大网络中的某个互联网交换中心的网络拆成两部分，然后进行桥接即可（支持物理桥接和虚拟桥接）

![](../../../../assets/Pasted%20image%2020250713111507.png)

- 可视化：通过标准 docker API，然后利用 tcpdump 过滤表达式来进行过滤
* * *

## Emulating Internet Service Infrastructure

### DNS Infrastructure

- 每一个 DNS 服务器都是一个虚拟的节点，然后在这个虚拟节点上安装域名

![](../../../../assets/Pasted%20image%2020250713111524.png)

如上图所示的 DNS 架构可以被直接插入到一个基本网络中，只要将虚拟节点和 Emulator 中的一个物理节点（即 Docker 容器）绑定在一起即可，绑定过后这个选定主机（Emulator 会自动在自治系统当中选取，没有合适的就自己创建一个）就成为 DNS 根服务器

![](../../../../assets/Pasted%20image%2020250713111535.png)