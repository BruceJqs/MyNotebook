---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
--- 

# Chapter 1 : Introduction

## Database Systems

- 数据库是有关企业的相互关联的数据的集合，由数据库管理系统（DBMS，Database Management System）管理
- DBMS 的主要目标是提供一种既方便又高效的存储和检索数据库信息的方法
- 数据管理涉及定义信息存储结构和提供信息管理机制
- 即使系统崩溃或受到未经授权的访问，数据库系统必须确保所存储信息的安全
- 如果要在多个用户之间共享数据，系统必须提供并发控制机制以避免可能的异常结果
***
## Purpose of Database Systems

在数据库系统出现之前，数据库应用是在文件系统之上直接建立的，这就导致了：

- 数据冗余（Data Redundancy）和不一致（Inconsistency）
	- 多种文件格式，不同文件之间的数据重复
- 数据孤立/数据孤岛（Data Isolation）
	- 多样的文件和格式
- 存取数据困难（Difficulty in Accessing Data）
	- 需要一个新的程序来执行每一个新任务
- 完整性问题（Integrity Problems）
	- 完整性约束被“埋没”在程序代码中，而不是被显式地声明
	- 难以添加新约束或更改现有约束
	- e.g. “account balance $\geq$ 1” 
- 原子性问题（Atomicity Problems）
	- 发生错误可能会使数据库处于不一致的状态，此时部分更新已经被执行
	- e.g. 资金从一个账户转移到另一个账户应该要么完成，要么根本不发生，如果出现故障，应该要么退回这个资金（即转移失败），要么把资金转过去（即完成转移），不能一边资金减少另一边不变
	
	![](../../../assets/Pasted%20image%2020250217110521.png)
	
- 并发访问异常（Concurrent Access Anomalies）
	- 性能所需的并发访问
	- 不受控制的并发访问可能会导致不一致
	- e.g. 两个人读取余额（比如 100）并同时通过存钱（比如每人 50）来更新它，那么理论上总账户应该增加 100 而非 50
	
	![](../../../assets/Pasted%20image%2020250217110836.png)
	
- 安全性问题（Security Problems）
	- 难以为用户提供对部分（但不是全部）数据的访问权限
	- 认证（Authentication）、权限（Privilege）、审计（Audit）

> 数据库系统为上面的问题都提供了解决方法
***
## Characteristics of Databases

- 数据持久性（Data Persistence）
- 数据访问便利性（Convenience in Accessing Data）
- 数据完整性（Data Integrity）
- 多用户并发控制（Concurrency Control for Multiple User）
- 故障回复（Failure Recovery）
- 安全控制（Security Control）
***
## View of Data


