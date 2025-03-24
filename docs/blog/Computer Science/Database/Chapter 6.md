---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
--- 

# Chapter 06 : Entity-Relationship Model

## Database Design Process

![](../../../assets/Pasted%20image%2020250324100511.png)
***
### Design Phases

- 初始阶段（需求规范）——充分描述潜在数据库用户的数据需求
- 第二阶段（概念设计）——选择数据模型
	- 应用所选数据模型的概念
	- 将这些需求转换为数据库的概念模式
	- 完全开发的概念模式代表了企业的功能要求
		- 描述对数据执行的操作（或事务）类型
- 最后阶段（数据库设计）——从抽象数据模型转向数据库的实现
	- 逻辑设计（Logical Design）——决定数据库模式
		- 数据库设计要求我们找到一个 “好的” 关系模式集合
		- 业务决策——我们应该在数据库中记录哪些属性？
		- 计算机科学决策——我们应该拥有哪些关系模式，以及属性应该如何在各种关系模式之间分配？
	- 物理设计 – 决定数据库的物理布局
***
### Design Alternatives

- 在设计数据库架构时，我们必须确保避免两个主要陷阱：
	- 冗余：糟糕的设计可能会导致重复的信息
		- 信息的冗余表示可能会导致各种信息副本之间的数据不一致
	- 不完整：糟糕的设计可能会使企业的某些方面难以或无法建模
- 避免糟糕的设计是不够的。可能有很多好的设计让我们必须从中进行选择
- 数据库设计可能是一个具有挑战性的问题
	- 巨大的设计空间
***
### Design Approaches

- 实体关系模型
	- 将企业建模为实体和关系的集合
		- 实体：企业中可与其他对象区分开来的“事物”或“对象”
			- 由一组属性描述
		- 关系：多个实体之间的关联
	- 用实体关系图以图示方式表示
- 归一化理论
	- 正式确定哪些设计是坏的，并对其进行测试

!!! example "E-R Diagram for a University Enterprise"

	![](../../../assets/Pasted%20image%2020250324101514.png)
	
	- 一个方形框就是一个实体的集合，下面列出其属性
	- 实体与实体之间有关系，一个菱形框表示关系
		- 一对一($\leftrightarrow$)/一对多/多对一($\leftarrow$,$\rightarrow$)  
	    - 这里 `instructor` 实体里不需要 `dept` 属性，因为在 `department` 实体里有了，否则会冗余
	- 每个实体直接转换为关系模式。关系转换为元组，元素为两个表的 primary key. 对于一对多的情况（如 `instructor` 和 `department`）转换后 primary key 仍为 ID
	- 为了减少表的数量，可以把 primary key 相同的表合并
	- 双横线与单横线不同  
		- 双横线表示每个对象都必须参与关系，而单横线则表示对象可以不参与关系，如 `course_dept` 和 `course` 为双横线，表示每一个课程都必须有一个开课部门，而 `department` 和 `course_dept` 为单横线，表示一个部门可以没有课程
	- 有些联系是隐含的，如授课老师和听课的学生
	- `section` 不足以唯一确定元组，称为弱实体，依赖于另一个实体（如 OOP、DB 都可以有同样年份学期的 1 班）。因为课程号 `course_id` 放在 `section` 会有冗余，因此没有这个属性，导致形成了一个弱实体。 `sec_course` 表示联系的是弱实体（双框），`section` 不能离开 `course` 存在
	- relationship 上也可以带属性，如 `takes` 上的 `grade`.
	- 关系双方可以是相同的实体集合，`course` 这里的 `prereq` 是多对多，表示一门课可以有多门预修课，一门课也可以是多门课的预修课。`{}` 里面是多个值，表示复合属性。这里表示 `time_slot_id` 实际上可以由这三个属性复合而成。
***
## Database Modeling

### Entities

- 数据库可以建模为：
	- 实体的集合
	- 实体之间的关系
- 实体是存在且可与其他对象区分开来的对象
	- e.g. 特定人员、公司、事件、工厂
- 实体具有属性
	- e.g. 对于一个人来说有地址、姓名、性别等
- 实体集是一组共享相同属性的相同类型的实体
	- e.g. 所有人员、公司、树、假日的集合
- 实体集可以按如下方式以图形方式表示：
	- 矩形表示实体集
	- 实体矩形内列出的属性
	- 下划线表示主键属性

![](../../../assets/Pasted%20image%2020250324105605.png)
***
### Relationship Sets

- 关系是多个实体之间的关联

![](../../../assets/Pasted%20image%2020250324105742.png)

- 关系集是 $n\geq 2$ 个实体之间的数学关系，每个实体都取自实体集，即 $\{(e_1,e_2,...,e_n)|e_1\in E_1,e_2\in E_2,...,e_n\in E_n\}$，其中 $(e_1,e_2,...,e_n)$ 是一个关系
	- e.g. 按照上面的例子，$(44553,22222)\in\text{advisor}$

在实体-关系图当中，关系集用菱形表示：

![](../../../assets/Pasted%20image%2020250324110047.png)
***
#### Relationship Sets with Attributes

关系集也可以拥有属性，例如，实体集 instructor 和 student 之间的 advisor 关系集可能具有属性 date，该属性跟踪 student 开始与 advisor 关联的时间：

![](../../../assets/Pasted%20image%2020250324111016.png)

![](../../../assets/Pasted%20image%2020250324111033.png)
***
#### Roles

- 关系的实体集不需要是不同的
	- 实体集的每次出现都在关系中扮演一个 "Role"
- e.g. 标签 "course_id" 和 "prereq_id" 称为 "Role"

![](../../../assets/Pasted%20image%2020250324111225.png)
***
#### Degree of a Relationship Set

- 二元联系（Binary Relationship）
	- 涉及两个实体集（或称为度为 2）
	- 数据库系统中的大多数关系集都是二元的
- 在某些情况下，将关系表示为非二元关系会更方便
- e.g. 具有三元关系的关系-实体图：

![](../../../assets/Pasted%20image%2020250324111658.png)
***
### Attributes

- 实体由一组属性表示，这些属性是实体集的所有成员都拥有的属性
	- e.g. `instructor = (ID, name, street, city, salary), course = (course_id, title, credits)`
- 域（Domain）——每个属性的允许值集
- 属性类型： 
	- 简单（Simple）和复合（Composite）属性
	- 单值（Single-valued）和多值（Multivalued）属性
		- e.g.多值属性：phone_numbers
	- 派生（Derived）属性
		- 可以从其他属性计算
		- e.g. 年龄，给定 date_of_birth

在关系-实体图中，属性可以表示如下：

![](../../../assets/Pasted%20image%2020250324113001.png)
***
### Mapping Cardinality Constraints

- 二元关系集的映射基数约束表示另一个实体可以通过关系集关联到的实体数
- 在描述二元关系集时最有用
- 对于二元关系集，映射基数必须是一对一、一对多、多对一、多对多类型之一
- 我们通过在关系集和实体集之间绘制一条有向线 （$\rightarrow$） 来表示“一”，或这绘制一条无向线（—） 来表示“多”

!!! example "Example"

	=== "一对一关系"
	
		- 教师和学生之间的一对一关系：
			- 一个学生通过 advisor 最多与一名教师关联
			- 一名教师通过 advisor 最多与一名学生关联
		
		![](../../../assets/Pasted%20image%2020250324113448.png)
	
	=== "一对多关系"
	
		- 教师和学生之间的一对多关系：
			- 一名教师通过 advisor 与多个（包括 0 个）学生关联
			- 一个学生通过 advisor 最多与一名教师关联
		
		![](../../../assets/Pasted%20image%2020250324113620.png)
	
	=== "多对一关系"
	
		- 教师和学生之间的多对一关系：
			- 一名教师通过 advisor 最多与一名学生关联
			- 一个学生通过 advisor 与多个（包括 0 个）教师关联
		
		![](../../../assets/Pasted%20image%2020250324113654.png)
	
	=== "多对多关系"
	
		- 教师和学生之间的多对多关系：
			- 一名教师通过 advisor 与多个（包括 0 个）学生关联
			- 一个学生通过 advisor 与多个（包括 0 个）教师关联
		
		![](../../../assets/Pasted%20image%2020250324113722.png)
***
### Total and Partial Participation





