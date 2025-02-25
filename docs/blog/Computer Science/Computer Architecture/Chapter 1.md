---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
--- 

# Chapter 01 : Fundamentals of Computer Design

!!! abstract "Abstract"

	感觉跟[计组](https://brucejqs.github.io/MyNotebook/blog/Computer%20Science/Computer%20Organization/Chapter%201/)大差不差，第一章都在扯有的没的（x），也提到了计组学的一些概念

![](../../../assets/Pasted%20image%2020250225133527.png)

## RISC-V Architecture

- RISC（Reduced Instruction Set Computer，精简指令集计算机）架构诞生于 1980s
- RISC-V 的指令相对更加简单
- RISC 提供了两个重要的性能技术：指令级并行（流水线以及多重指令问题）和缓存
***
### Pipelining

- 流水线将指令的执行分划为若干个阶段，在上一个指令执行完成之前就开始当前指令的执行
- 多指令的重叠执行
- CPI $\geq$ 1

![](../../../assets/Pasted%20image%2020250225135239.png)

![](../../../assets/Pasted%20image%2020250225135524.png)
***
### Multiple Instruction Issue

- 启动多个数据通路（Datapath）
- 并行执行多条流水线
- 每个时钟周期完成多于一个指令
- CPI < 1

!!! example "Example : 2-way superscalar"

	![](../../../assets/Pasted image 20250225135747.png)
	
	![](../../../assets/Pasted image 20250225135854.png)
***
### Data Processing & Storage

在没有 Cache 的情况下，永久存储（Permanent Storage）架构如下：

![](../../../assets/Pasted%20image%2020250225140153.png)

在有 Cache 的情况下，加速了数据的访问，即临时存储（Temporary Storage）：

![](../../../assets/Pasted%20image%2020250225140259.png)
***
## Processor Perf Growth

几十年来计算机处理器性能的提升图：

![](../../../assets/Pasted%20image%2020250225140352.png)

- 关于半导体的两大定律已经失效
    - **丹纳德缩放定律**（Dennard Scaling）
	    - 由于每个晶体管的尺寸较小，即使增加晶体管的数量，给定硅面积的功率密度也是恒定的
	    - 在 2004 年，该定律就失效了，因为电流和电压无法一直小下去，同时仍然保持集成电路的可靠性
    - **摩尔定律**（Moore's Law）： 1965 年预测芯片上的晶体管数量每年（1975 年修正为“每两年”）翻一倍，在 2015 年失效
***
## Multi-core Processor

- 多个高效处理器，而不是单个低效处理器
- 从指令级并行到数据级和线程级并行
***
### Amdahl's Law

- 多核并行要求对应用程序进行重组，这对程序员来说是一个新的重大负担
- 使用某种更快的执行模式所获得的性能改进受到可以使用更快模式的时间的限制

$$
\begin{aligned}
\text{Speedup}_{\text{overall}} &= \frac{\text{Execution Time}_{\text{old}}}{\text{Execution Time}_{\text{new}}} = \frac{1}{1-\text{Fraction}_{\text{enhanced}}+\frac{\text{Fraction}_{\text{enhanced}}}{\text{Speedup}_{\text{enhanced}}}}\\
&\stackrel{\text{limit}}{=} \frac{1}{1-\text{Fraction}_{\text{enhanced}}}
\end{aligned}
$$

- 根据上面的公式，如果有 10% 的任务是必须顺序执行的，那么需要至少 10 倍的 speedup
- 体现了 “Make Common Case Fast” 的设计思想

!!! example "Example"

	=== "Example 01"
	
		10% 的部分 speedup 为 20
		
		- $\text{Speedup}_{\text{overall}}=\frac{1}{1-0.1+\frac{0.1}{20}}=1.11$
	
	=== "Example 02"
	
		80% 的部分 speedup 为 1.6
		
		- $\text{Speedup}_{\text{overall}}=\frac{1}{1-0.8+\frac{0.8}{1.6}}=1.43$
***
## Classes of Computers

- 台式（Desktop）计算机
    - 第一类出现在市场的计算机，且仍然占据最大的市场
    - 需要考虑更高的性价比
    - 新的挑战：
	    - 以 Web 为中心的交互式应用程序
	    - 如何评估性能
- 服务器（Servers）
	- 提供更大规模、更可靠的文件和计算服务
    - 需要考虑的因素：
	    - 可靠性（Dependability），以防服务器故障导致的巨大损失
	    - 可扩展性（Scalability），通过扩大计算能力、内存和 I/O 带宽来应对日益增长的需求
	    - 吞吐量（Throughput），在单位时间内处理更多请求，按每分钟事务数或每秒服务的网页数计算
- 物联网（Internet of Things, IoT）/ 嵌入式（Embedded）计算机
    - 物联网通过传感器（Sensors）和执行器（Actuators）收集有用的数据，并与物理世界互动，具有最广泛的处理能力和成本
    - 处理器内核和专用电路的使用
	    - DSP，移动计算
    - 需要考虑的因素
        - （软 / 硬）实时性能
        - 严格的资源限制（内存大小、低功耗）
- 个人移动设备（Personal Mobile Device, PMD）
	- 一组具备多媒体用户界面的无线设备，能运行第三方软件，包括智能手机、平板
	- 具有台式计算机的许多特性
		- 基于网络和面向媒体
		- 能够运行第三方软件（APP），这是其与嵌入式计算机的主要区别
    - 需要考虑的因素：
        - 成本（更便宜的封装方式、减少或是去除散热风扇）
        - 响应能力（Responsiveness）和可预测性（Predictability）
	        - 实时性能（Real-time Performance）：每个应用程序段的最大执行时间
		        - e.g. 处理每个视频帧的时间应该受到限制，因为处理器必须很快接受并处理下一帧
	        - 软实时（Soft Real-time）
		        - 将某一事件的时间换成其他事件的时间
				- 容忍偶尔超过的事件时间限制，但不能太多
- 集群（Clusters）/ 仓储式（Warehouse-scaling）计算机（WSCs）
    - 软件即服务（Software as a Service, SaaS）包括搜索、社交网络、媒体分享、多媒体游戏、在线购物等，它促进了集群的发展
    - 集群：通过局域网连接的一组台式计算机或服务器，表现得像一台单个更大的计算机
    - 与服务器的区别在于 WSCs 利用了冗余
    - 强调交互式应用程序的大规模存储、可靠性和高互联网带宽
    - 与超级计算机（SuperComputer）的区别在于其强调浮点性能，能运行大型、通信密集型的聊天程序，一次可以运行数周
    - 需要考虑的因素：性价比、功率





