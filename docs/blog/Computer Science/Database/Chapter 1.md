---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
# comments: true
--- 

# Chapter 01 : Introduction

## Database Systems

- 基于文件建立的应用 VS 基于数据库建立的应用

![](../../../assets/Pasted%20image%2020250217111757.png)

- 数据库是有关企业的相互关联的数据的集合，由数据库管理系统（DBMS，Database Management System）管理
- DBMS 的主要目标是提供一种既方便又高效的存储和检索数据库信息的方法
- 数据管理涉及定义信息存储结构和提供信息操作机制
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
- 故障恢复（Failure Recovery）
- 安全控制（Security Control）
***
## View of Data

数据库有三个抽象层级，具有强适应能力：

![](../../../assets/Pasted%20image%2020250217112035.png)

- 物理级别（Physical Level）：描述记录的存储方式（比如磁盘）
- 逻辑级别（Logical Level）：描述存储在数据库中的数据以及与上层数据的关系
- 视图级别（View level）：应用程序隐藏数据类型的详细信息
	- 视图级别还可以出于安全目的隐藏信息（比如员工的薪水）
***
### Schema and Instance

- 类似于编程语言中的类型和变量
- 模式（Schema）——数据库的逻辑结构 
	- e.g. 数据库包含有关一组客户和帐户以及它们之间的关系的信息
	- 类似于程序中变量的类型信息
	- 物理模式（Physical Schema）：物理级别的数据库设计
	- 逻辑模式（Logical Schema）：逻辑级别的数据库设计
- 实例（Instance）——数据库在特定时间点的实际内容 
	- 类似于变量的值
***
### Data Independence

- 物理数据独立性（Physical Data Independence）——在不更改逻辑架构的情况下修改物理架构的能力
	- 应用程序依赖于逻辑架构
	- 通常，应明确定义各个层级和组件之间的接口，以便某些部分的变化不会严重影响其他部分
- 逻辑数据独立性（Logical Data Independence）——在不更改用户视图架构的情况下修改逻辑架构的能力

> 映射修改不需要修改 Schema
***
## Data Models

- 用于描述数据（Data）、联系（Data Relationships）、语义（Data Semantics）、约束（Data Constraints）的工具集合
- 关系模型（Relational Model）
- 实体-联系（Entity-Relationship）数据模型 
- 基于对象的数据模型
	- 面向对象数据模型（Object-oriented）
	- 对象-关系模型模型（Object-relational）
- 半结构化数据模型 （Semistructured data model）（XML）
- 其他旧模型：
	- 网状模型（Network Model）
	- 层次模型（Hierarchical Model）
***
### Relational Model

![](../../../assets/Pasted%20image%2020250217114311.png)

***
## Database Languages

### Data Definition Language（DDL）

- 用于定义数据库架构的规范表示法

![](../../../assets/Pasted%20image%2020250217115332.png)

- DDL 编译器生成一组存储在数据字典（Data Dictionary）中的表模板
- 数据字典包含元数据（Metadata，即有关数据的数据）
	- 数据库架构（Database Schema）
	- 完整性约束（Integrity Constraints）
		- 主键（Primary Key）
			- e.g. ID 唯一标识 instructor
		- 参照完整性（Referential Integrity）（References Constraint in SQL）
			- e.g. 任何 instructor 元组中的 dept_name 值都必须出现在 Department relation 中
		- 权限（Authorization）
***
### Data Manipulation Language（DML）

- 用于访问和作由相应数据模型组织的数据的语言
	- DML 也称为查询语言
- 两类语言
	- 过程式（Procedural）——用户指定需要哪些数据以及如何获取这些数据
		- 分为顺序结构、分支结构、循环结构
	- 陈述式/非过程式（Declarative/Nonprocedural）——用户指定需要哪些数据，但不指定如何获取这些数据
- SQL 是使用最广泛的非过程式查询语言

!!! example "Example of SQL"

	=== "找到 ID 为 22222 的 instructor"
	
		```sql
		select name
		from instructor
		where instructor.ID = '22222'
		```
	
	=== "找到 Physics Dept. 的 instructors 的 ID 和 building"
	
		```sql
		select instructor.ID, department.building  
		from instructor, department  
		where instructor.dept_name = department.dept_name and department.dept_name = ‘Physics’
		```
***
### Database Access from Application Program

- 非过程式查询语言（如 SQL）不如通用图灵机强大
- SQL 不支持用户输入、输出到显示器或通过网络进行通信等操作
	- 此类计算和操作必须以主机语言编写，例如 C/C++、Java 或 Python
- 应用程序通常通过以下操作与数据库通信：
	- 允许嵌入式 SQL 的语言扩展
	- API（应用程序接口）（例如 ODBC/JDBC），允许将 SQL 查询发送到数据库
***
## Database Design

- 实体-联系模型（Entity Relationship Model）
	- 将企业建模为数据实体和关系的集合
	- 由实体关系图以图示方式表示
	
	![](../../../assets/Pasted%20image%2020250217120744.png)
	
- 规范化理论（Normalized Theory）
	- 规定哪些设计是坏的，并对其进行测试
	- e.g. 下图的设计有数据冗余（dept_name 就已经对应 building 和 budget），应该分为两个表，前四列一张表后三列一张表
	
	![](../../../assets/Pasted%20image%2020250217120946.png)
***
## Database Engine

- 数据库系统（数据库引擎）被划分为多个模块，这些模块处理整个系统的每个职责
- 数据库系统的功能组件可以分为存储管理器（Storage Manager）、查询处理器（Query Processor）和事务管理组件（Transaction Management Component）

![](../../../assets/Pasted%20image%2020250217121329.png)
***
### Storage Manager

- 一个程序模块，它提供数据库中存储的低级数据与提交给系统的应用程序和查询之间的接口
- 存储管理器负责以下任务：
	- 与 OS 文件管理器交互
	- 高效存储、检索和更新数据
- 存储管理器组件包括文件管理器（File Manager）、缓冲区管理器（Buffer Manager）授权和完整性管理器（Authorization and Integrity Manager）、事务管理器（Transaction Manager）
- 存储管理器实现多种数据结构作为物理系统实现的一部分：
	- 数据文件（Data Files）——存储数据本身
	- 数据字典 （Data Dictionary）——存储有关数据库结构（特别是数据库架构）的元数据
	- 索引（Indices）——可以提供对数据项的快速访问，数据库索引提供指向持有特定值的数据项的指针，用于数据库的查询处理
	- 统计数据（Statistical Data）
***
### Query Processor

- 查询处理器组件包括：
	- DDL 解释器（DDL Interpreter）——解释 DDL 语句并将定义记录在数据字典中
	- DML 编译器（DML Compiler）——将查询语言中的 DML 语句转换为由查询评估引擎理解的低级指令组成的评估计划（Evaluation Plan）
		- DML 编译器执行查询优化（Query Optimization），也就是说，它从各种备选方案中挑选成本最低的评估计划
	- 查询评估引擎（Query Evaluation Engine）——执行 DML 编译器生成的低级指令

处理查询分为解析和翻译、优化、评估三步：

![](../../../assets/Pasted%20image%2020250217131610.png)
***
### Transaction Management

- 事务（Transaction）是在数据库应用程序中执行单个逻辑功能的作集合
- 恢复管理器（Recover Manager）确保数据库在系统故障（e.g. 电源故障和操作系统崩溃）和事务故障的情况下保持一致（正确）状态
- 并发控制管理器（Concurrency-Control Manager）控制并发事务之间的交互，以保证数据库的一致性
***
## Database Users

![](../../../assets/Pasted%20image%2020250217132903.png)

用户的区分在于他们希望与系统交互的方式：

- 应用程序程序员（Application Programmers）——通过 DML 调用与系统交互
- 天真用户（Naive Users）——调用以前编写的永久应用程序之一
	- 例如，通过 Web 访问数据库的人、银行出纳员、文员
- 数据库管理员（Database Administrator）——协调数据库系统的所有活动
	- 数据库管理员对企业的信息资源和需求有很好的了解
***
## Database Administrator（DBA）

数据库管理员的职责包括：

- Schema 定义
- 存储结构和访问方法定义
- 架构和物理组织修改
- 授予用户访问数据库的权限
- 日常维护
	- 性能调优——监控性能并响应需求变化 
	- 定期将数据库备份到远程服务器上 
	- 确保有足够的可用磁盘空间用于正常作，并根据需要升级磁盘空间
***
## History of Database Systems

- 1973 Turing Award: Charles W. Bachman——“Father of Databases”
- 1981 Turing Award: Edgar F. Codd
- 1998 Turing Award: Jim Gray
- 2014 Turing Award: Michael Stonebraker