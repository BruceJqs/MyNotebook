---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
---  
# Chapter 01 : Computer abstractions and Technology
## Introduction
### Von Neumann Architecture（冯·诺依曼架构）

- 计算与存储分离
- 数据和指令放在同一个存储器

![](../../../assets/2023-06-23_12-05-34.png)
## Computer Organization
### Hardware

![](../../../assets/Screenshot.png)

![](../../../assets/Screenshot6.png)
#### I/O Interfaces（Input/Output）

- I/O 主导该设备（直译过来不懂什么意思 qaq ，大概是 I/O 接口非常重要）
- 输入设备：一种向计算机提供信息的设备
	- 触摸屏
	- 前置摄像头
	- 麦克风
	- 陀螺仪
	- 蓝牙
- 输出设备：将计算机结果传达给用户或另一台计算机的设备
	- 扬声器
	- 触摸屏
	- 蓝牙
#### Logical Board

- 由集成电路组成：
	- CPU
	- Flash（闪存）
	- Power Controller
	- I/O Controller

![](../../../assets/Screenshot8.png)
#### CPU（Processor）

- 计算机的活跃部分，包含数据通路（执行数学运算）和控制通路（根据程序要求给予通路、内存、I/O 设备指令），执行数字加法，检测 I/O 设备激活需要的数字、信号等。
#### Memory

- 程序的存储区域，其中包含运行程序所需的数据
- Main Memory（主存）：易失性，用于在程序运行时保存它们。（例如 DRAM，SRAM）
- Second Memory：非易失性，用于在运行前后存储程序和数据。（例如闪存、磁盘）

![](../../../assets/Screenshot9.png)
### Software

![](../../../assets/Screenshot7.png)
#### Software Categorization

- 按照用途分类：
	- 系统软件（针对开发者）
	- 应用软件（针对用户）
- 操作系统：
	- 处理基本输入和输出操作
	- 分配存储和内存
	- 在同时使用计算机的多个应用程序之间共享计算机
- 编译器：翻译高级编程语言编写的程序
- Firmware（驱动）：专为硬件设计的软件

![](../../../assets/Screenshot10.png)
#### From a High-Level Language to the Language of Hardware

![](../../../assets/Screenshot11.png)


## How build processors?
