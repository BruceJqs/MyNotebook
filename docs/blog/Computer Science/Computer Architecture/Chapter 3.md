---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
--- 

# Chapter 03 : Memory Hierarchy Design

## Main Memory

- 主存储器（Main Memory）是缓存和服务器之间的 I/O 接口
- 输入的数据被放在主存储器中，然后被处理器读取输出

![](../../../assets/Pasted%20image%2020250304165804.png)

- 性能指标：
	- 延迟（Latency）：接收到块的第一个字的时间
		- 对于缓存来说很重要
		- 比较难优化
		- 分为获取时间（Access Time）和循环时间（Cycle Time）
			- 获取时间：发送读请求到字到达需要的时间
			- 循环时间：不相关的内存请求需要的最小时间，即获取开始和下一次获取开始之间的最小时间
	- 吞吐率（Bandwidth）：接收剩下块的时间
		- 对于多核处理器、I/O 和 Blocks 比较大的缓存
		- 重新组织能更简单优化

一般来说，SRAM 为缓存，DRAM 为主存

- SRAM（Static Random Access Memory）
	- 每比特六个晶体管，以防止信息在读取时受到干扰
	- 不需要刷新，因此访问时间非常接近循环时间
	- 有关缓存的内容可以看[计组](https://brucejqs.github.io/MyNotebook/blog/Computer%20Science/Computer%20Organization/Chapter%205/#the-basics-of-cache)
- DRAM（Dynamic Random Access Memory）
	- 每比特一个晶体管
	- 读操作会破坏信息
	- 定期刷新
	- 循环时间>访问时间