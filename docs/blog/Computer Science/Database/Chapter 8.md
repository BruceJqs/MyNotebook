---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
--- 

# Chapter 08 : Physical Storage Systems

## Classification of Physical Storage Media

- 我们可以将存储分为：
	- 易失存储（Volatile Storage）：关闭电源时丢失内容
	- 非易失存储（Non-Volatile Storage）：
		- 即使关闭电源，内容仍然存在
		- 包括二级和三级存储，以及电池备份的主内存
- 访问数据的速度
- 每单位数据成本
- 可靠性
	- 电源故障或系统崩溃时数据丢失
	- 存储设备的物理故障
***
## Storage Hierarchy

![](../../../assets/Pasted%20image%2020250414100609.png)

- 一级存储：最快的媒体，但不稳定（缓存、主内存）
- 二级存储：层次结构的下一级别，非易失性，适中快的访问时间
	- 也称为在线存储
	- 例如闪存、磁盘
- 三级存储：层次结构中的最低级别，非易失性，访问时间慢
	- 也称为离线存储
	- 例如磁带、光存储

这一块跟[计组](https://brucejqs.github.io/MyNotebook/blog/Computer%20Science/Computer%20Organization/Chapter%205/)真是一模一样，PPT 懒得整了（x）