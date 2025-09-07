---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
# comments: true
--- 

# Chapter 06 : Entity-Relationship Model

!!! abstract "Abstract"

	这一章概念绕来绕去的，翻译过来非常离谱，感觉还是得看例子比较清楚一些=)
	
	整一章都是围绕着一个例子来讲的

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

- 在设计数据库模式时，我们必须确保避免两个主要陷阱：
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
- 我们通过在关系集和实体集之间绘制一条有向线 （$\rightarrow$） 来表示“一”，或绘制一条无向线（—） 来表示“多”

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

- 完全参与（Total Participation）通常使用双线表示，表示实体集中的每个实体都至少参与关系集中的一个关系
	- 例如，每一个学生都应当有至少一个相关的 advisor：
	
	![](../../../assets/Pasted%20image%2020250324115011.png)
	
- 部分参与（Partial Participation）通常使用单线表示，表示某些实体可能不参与关系集中的任何关系
	- 例如，一个教师可能没有相关的 advisor

- 一条线可能具有关联的最小和最大基数，以 l..h 的形式表示，其中 l 是最小基数，h 是最大基数
	- 最小值 1 表示完全参与
	- 最大值 1 表示实体最多参与一个关系
	- 最大值 * 表示无限制
	- 例如，教师可以为 0 个或更多学生提供建议。 学生必须有 1 名 advisor，不能有多个 advisor：
	
	![](../../../assets/Pasted%20image%2020250324115940.png)
	
- 我们最多允许三元（或更高度数）关系中的一个箭头来表示基数约束
- 例如，从 proj_guide 到 instructor 的箭头表示每个学生最多有一个项目的 instructor：

![](../../../assets/Pasted%20image%2020250324120120.png)

- 为避免混淆，我们禁止多个箭头
***
### Primary Key

- 主键提供了一种指定如何区分实体和关系的方法，我们将考虑实体集、关系集、弱实体集
- 根据定义，各个实体是不同的
- 从数据库的角度来看，它们之间的差异必须用它们的属性来表示
- 实体的属性值必须使其能够唯一标识实体
	- 实体集中的任何两个实体都不允许所有属性具有完全相同的值
- 实体的键是一组足以将实体彼此区分开来的属性
- 为了区分关系集的各种关系，我们使用关系集中实体的各个主键
	- 设 $R$ 为涉及实体集 $E_1,E_2,...,E_n$ 的关系集...
	- $R$ 的主键由实体集 $E_1,E_2,...,E_n$ 的主键组成
	- 如果关系集 $R$ 具有与其关联的属性 $a_1,a_2,...,a_m$，则 $R$ 的主键还包括属性 $a_1,a_2...,a_m$
	- e.g. advisor 关系集的主键是 `instructor.ID` 和 `student.ID`：
	
	![](../../../assets/Pasted%20image%2020250324210940.png)
	
- 关系集的主键选择取决于关系集的映射基数
	- 如果二元关系为一对一关系，任一参与实体集的主键都构成一个最小超级键（Minimal Superkey），并且可以选择其中任何一个作为主键
	- 如果二元关系为一对多关系，“多”关系一端的主键是最小超级键，作为主键
	- 如果二元关系为多对一关系，“多”关系一端的主键是最小超级键，作为主键
	- 如果二元关系为多对多关系，两个实体集的主键的并集是最小超级键，作为主键
***
### Weak Entity Sets

- 没有主键的实体集称为弱实体集
- 弱实体集的存在取决于标识性实体集（Identifying Entity Set）的存在
	- 它必须通过从标识到弱实体集的一对多关系集与标识实体集相关
	- 我们使用双菱形来描绘的标识性联系（Identifying Relationship）
- 弱实体集的分辨符（Discriminator，或称部分键）是指当弱实体集所依赖的标识实体已知时区分弱实体集的所有实体的属性集
- 弱实体集的主键由弱实体集依赖的强实体集的主键加上弱实体集的分辨符组成
- 我们用虚线为弱实体集的分辨符划下划线
- 我们将弱实体的识别关系放在双菱形中

!!! example "Example"

	![](../../../assets/Pasted%20image%2020250324213001.png)
	
	注意：强实体集的主键不会与弱实体集一起显式存储，因为它隐含在标识关系中
	
	如果显式存储 course_id，则 section 可以成为强实体，但 section 和 course 之间的关系将由 course 和 section 通用属性定义的隐式关系 course_id 复制
***
### Redundant Attributes

- 假设我们有实体集：
	- student，属性为：ID, name, tot_cred, dept_name
	- department，属性为：dept_name, building, budget
- 我们使用关系集 stud_dept 对每个学生都有一个关联部门这一事实进行建模
- 下面 student 中的属性 dept_name 复制了关系中存在的信息，因此是多余的，并且需要被删除
- 但是，当转换回表时，在某些情况下，该属性会重新引入

![](../../../assets/Pasted%20image%2020250324214624.png)
***
## Reduction to Relational Schemas

- 实体集和关系集可以统一表示为表示数据库内容的关系模式
- 符合 E-R 图的数据库可以由模式集合表示
- 对于每个实体集和关系集，都有一个唯一的模式，该模式分配有相应实体集或关系集的名称
- 每个模式都有许多列（通常对应于属性），这些列具有唯一的名称
***
### Representing Entity Sets with Simple Attributes

- 强实体集将简化为具有相同属性的模式
- 弱实体集将变成一个表，该表包含标识强实体集的主键列
	- 表的主键是弱实体集的分辨符与标识强实体集的主键的并集

![](../../../assets/Pasted%20image%2020250324215646.png)
***
### Representing Relationship Sets

一个多对多关系集表示为一个模式，其中包含两个参与实体集的主键的属性，以及关系集的任何描述性属性

- e.g. 对于一个关系集 advisor 的模式：advisor=(<u>s_id,i_id</u>)

![](../../../assets/Pasted%20image%2020250324220019.png)
***
### Redundancy of Schemas

在多端总计的多对一和一对多关系集可以通过向“多”的一端添加一个额外的属性来表示，该属性包含 “一”的一端的主键

- e.g. 与其为关系集 inst_dept 创建模式，而是将属性 dept_name 添加到由实体集 instructor 产生的模式

![](../../../assets/Pasted%20image%2020250324220316.png)

- 对于一对一关系集，可以选择任何一方作为 “多” 的一端
	- 也就是说，可以将更多的属性添加到与两个实体集对应的任一表中
- 如果参与在“多”的一端是部分参与，则在与“多”的一端对应的模式中用额外的属性替换模式可能会导致 null 值
- 与将弱实体集链接到其标识的强实体集的关系集对应的模式是多余的
	- e.g. section 模式已包含将显示在 sec_course 模式中的属性
***
### Composite and Multivalued Attributes

- 通过为每个组件属性创建单独的属性来扁平化复合属性
	- 就像在 C 语言里定义一个结构。但是关系数据库里每个属性都必须是简单数据类型，就必须把这些复合属性铺平
	- e.g. 给定的实体集 instructor，其复合属性名称为组件属性 first_name, last_name 与实体集对应的模式具有两个属性 name_first_name 和 name_last_name
	- 如果没有歧义，则省略前缀
	- 忽略多值属性，扩展 instructor 模式为：`instructor(ID, first_name, middle_initial,  last_name, street_number, street_name, apt_number, city, state, zip_code, date_of_birth, age)`
- 实体 E 的多值属性 M 由单独的模式 EM 表示
	- 模式 EM 具有对应于 E 的主键的属性和对应于多值属性 M 的属性
		- e.g. instructor 的多值属性 phone_number 由模式 inst_phone 表示：`inst_phone(ID, phone_number)`
	- 多值属性的每个值都映射到模式 EM 上关系的单独元组
		- e.g. 主键为 22222、电话号码为 456-7890 和 123-4567 的 instructor 实体映射到两个元组：`(22222, 456-7890)` 和 `(22222, 123-4567)`
- 特殊情况：实体 time_slot 只有一个除主键属性之外的属性，并且该属性是多值的
	- `time_slot(time_slot_id)` 和 `time_slot_detail(time_slot_id, day, start_time, end_time)`
	- 优化：不创建实体对应的关系，只创建多值属性对应的关系
		- `time_slot(time_slot_id, day, start_time, end_time)`
	- 但是因为此优化，`section(from sec_time_slot)` 的 `time_slot` 属性不能是外键

![](../../../assets/Pasted%20image%2020250324231752.png)
***
## Design Issues

### Common Mistakes in E-R Diagrams

!!! example "Examples"

	=== "信息冗余"
	
		![](../../../assets/Pasted%20image%2020250324231856.png)
		
		student 的 `dept_name` 应该去掉
	
	=== "关系属性使用不当"
	
		![](../../../assets/Pasted%20image%2020250324231945.png)
		
		这里一门课可能有很多次作业，不能只用一个实体
		
		解决方法：
		
		![](../../../assets/Pasted%20image%2020250324232032.png)
***
### Use of Entity Sets V.S. Attributes

![](../../../assets/Pasted%20image%2020250324232222.png)

- 第一种方法，明确放一个电话号码
- 第二种方法，电话号码可以附属更多属性，一个电话号码可以由多人共享（如办公室的公共电话）
***
### Use of Entity Sets V.S. Relationship Sets

- 指定一个关系集来描述实体之间发生的操作

![](../../../assets/Pasted%20image%2020250324232422.png)

实体可以便于与其他实体建立联系。

如电商，我们可以简单的把客户和商品用 `buy` 联系起来，但后续还会有付款、物流等情况，我们最好把 `buy` 实体化为订单。
***
### Placement of Relationship Attributes

![](../../../assets/Pasted%20image%2020250324232509.png)

- 第一种方法，可以记录每次访问的访问日期
- 第二种方法，只能记录用户最近一次访问日期，不完整
***
### Binary V.S. Non-Binary Relationships

- 尽管可以用多个不同的二元关系集替换任何非二元（n 元，其中 n>2）关系集，但 n 元关系集可以更清楚地显示多个实体参与单个关系
- 一些看起来非二元的关系可能更适合使用二元关系来表示
	- 例如，将孩子与他/她的父亲和母亲联系起来的三元关系父母最好用两种二元关系（父亲和母亲）来代替
	- 使用两个二元关系允许出现部分信息（例如，只有母亲知道的信息）
- 但是有些关系天生就是非二元的
***
#### Converting Non-Binary Relationships to Binary Form

通常，任何非二元关系都可以通过创建人工实体集来使用二元关系来表示

- 将实体集 A、B 和 C 之间的 R 替换为实体集 E 和三个关系集：
	- $R_A$，联系 $E$ 和 $A$；$R_B$，联系 $E$ 和 $B$；$R_C$，联系 $E$ 和 $C$
- 为 E 创建特殊标识属性
- 将 R 的所有属性添加到 E
- 对于每一个 R 中的关系 $(a_i,b_i,c_i)$
	- 在实体集 E 中建立新实体 $e_i$
	- 将 $(e_i,a_i)$ 添加到 $R_A$；将 $(e_i,b_i)$ 添加到 $R_B$；将 $(e_i,c_i)$ 添加到 $R_C$

![](../../../assets/Pasted%20image%2020250324233409.png)

我们还需要转换所有的约束

- 可能无法转换所有约束
- 已翻译的模式中可能存在不能对应于 R 的任何实例
- 我们可以通过使 E 成为由三个关系集标识的弱实体集来避免创建标识属性
***
### E-R Design Decisions

- 使用属性或实体集来表示对象
- 实际概念是用实体集还是关系集最好地表达
- 使用三元关系或二元关系
- 使用强实体集或弱实体集
***
## Extended ER Features

### Specialization / Generalization

- 特化（Specialization）
	- 自上而下的设计过程：我们在实体集中指定与集合中的其他实体不同的子分组
	- 属性继承：较低级别的实体集继承其链接到的较高级别实体集的所有属性和关系参与
- 概化（Generalization）
	- 自下而上的设计过程：相同特征的多个实体集合并到更高级别的实体集中
- 特化和泛化是彼此的简单倒置;它们在 ER 图中以相同的方式表示
- 术语特化和概化可以互换使用

![](../../../assets/Pasted%20image%2020250324234732.png)
***
### Design Constraints on Specialization / Generalization

- 对实体是否可以属于单个泛化中的多个较低级别实体集的约束
	- 不相交（Disjoint） 
		- 一个实体只能属于一个较低级别的实体集
		- 在 ER 图中，通过让多个较低级别的实体集链接到同一个三角形来表示
	- 重叠（Overlapping）
		- 一个实体可以属于多个较低级别的实体集
- 完全性约束（Completeness Constraint）
	- 指定较高级别实体集中的实体是否必须至少属于泛化中的至少一个较低级别实体集
	- 全部（Total）：实体必须属于较低级别的实体集之一
	- 部分（Partial）：实体不必属于较低级别的实体集之一
