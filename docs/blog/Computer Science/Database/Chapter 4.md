---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
--- 

# Chapter 04 : Intermediate SQL

## Joined Relations

- 连接操作输入两个关系，并返回另一个关系
- 连接操作通常用作 from 子句中的子查询表达式
- 连接条件（Join Condition）——定义两个关系中的哪些元组匹配，以及连接结果中存在哪些属性
- 连接类型（Join type）——定义如何处理每个关系中与另一个关系中的任何元组不匹配的元组（基于连接条件）

![](../../../assets/Pasted%20image%2020250310100639.png)
***
### Natural Join

- `from` 子句获得的是求解好后的新关系，因此有些实现不支持再用原来的关系名访问原属性
- 可以用多个 `natural join` 来连接多个关系

```sql
select A1, A2, ..., An
from r1 natural join r2 natural join ... natural join rm
where P;
```

- 另外，使用 `join ... using` 子句可以从两个关系的同名属性中选择指定的属性，作为连接的依据，更加灵活

```sql
select name, title
from (student natural join takes) join course using (course_id);
```
***
### Join Conditions

- 除了 `join ... using` 外，还有更加通用的 `join ... on` 运算。只要 `where` 支持的谓词，`on` 条件均支持，因此能够表达更为丰富的连接条件

```sql
select *
from student join takes on student.ID = takes.ID;
```
***
### Outer Join

> 自然连接仅保留那些同名属性值相等的元组，那些不相等的元组都会被抛弃，但有时我们需要保留这些不相等的元组。这个时候，就需要用到**外连接**（Outer Joins）

外连接的作用类似自然连接，区别在于它会保留那些两个关系的同名属性值不相等的元组，将其放入新的关系中，并将其未被拼接的属性设为 null。SQL 提供了以下三种形式的外连接：

- **左外连接**（Left Outer Join）：使用 `left outer join` 运算符，仅保留第一个关系的所有元组
- **右外连接**（Right Outer Join）：使用 `right outer join` 运算符，仅保留第二个关系的所有元组
- **全外连接**（Full Outer Join）：使用 `full outer join` 运算符，保留所有关系的元组
    - 可以把它的返回结果看作是左外连接和右外连接结果的并集
    - 有些数据库系统不支持全外连接（比如 MySQL）

对应地，前面介绍的那些没有保留不匹配元组的连接方式称为**内连接**（Inner Join）。

- 在 SQL 语法中可以显式指出 `inner join`，但可以省略 `inner`，因为 `join` 子句默认是内连接的

在外连接中，`on` 和 `where` 子句的区别在于：

- `on` 子句会保留那些不符合条件的元组
- 而 `where` 子句会丢掉那些不符合条件的元组

!!! example "Example"

	我们有如下两个关系：
	
	![](../../../assets/Pasted image 20250310102938.png)
	
	可以发现课程 CS-315 对应的 prereq 不存在，以及 CS-437 的课程信息不存在
	
	- 如果我们使用 `course natural left outer join prereq`，这将 prereq 的结果保存下来，没有信息的课程 CS-315 结果设为 NULL：
	
	![](../../../assets/Pasted image 20250310103157.png)
	
	- 如果我们使用 `course natural right outer join prereq`，这将 course 的结果保存下来，没有信息的课程 CS-437 结果设为 NULL：
	
	![](../../../assets/Pasted image 20250310103248.png)
	
	- 如果我们使用 `course natural full outer join prereq`，这将 course 和 prereq 的结果保存下来，没有信息的课程 CS-315 和 CS-437 结果设为 NULL：
	
	![](../../../assets/Pasted image 20250310103357.png)
***
## SQL Data Types and Schemas

### User-Defined Types

- SQL 支持两种形式的用户**定义数据类型**（User-Defined Data Types）：
	- **区分类型**（Distinct Types）
	- **结构化数据类型**（Structured Data Types）：复杂的数据类型，包括嵌套记录结构、数组、多重集
- 不同的属性可能有相同的类型，但有时我们希望讲这些属性的类型区分开来，我们使用 `create type` 语句来定义用户定义数据类型中的区分类型
	
	```sql
	create type Dollars as numeric(12, 2) final;
	create type Pounds as numeric(12, 2) final;
	```
	
	- 定义了 `Dollars` 这个类型后，我们就可以把它当作元类型使用：
	
	```sql
	create table department  
	(dept_name varchar (20),  
	building varchar (15),  
	budget Dollars);
	```
	
	- 用户定义的这两个类型 `Dollars` 和 `Pounds`，虽然底层类型相同，但会被视为不同的类型。因此这两种类型不能直接进行运算，甚至不能与 `numeric` 类型运算，这时就需要用 `cast` 子句进行强制类型转换
***
### Domains

- SQL 的 `domain` 关键字提供了与 `type` 类似的功能，用于为底层类型添加完整性约束：
	
	```sql
	create domain person_name char(20) not null
	```
	
	- 我们还可以使用 `check` 子句来添加额外的约束条件：
	
	```sql
	create domain degree_level varchar(10)  
	constraint degree_level_test  
	check (value in (’Bachelors’, ’Masters’, ’Doctorate’));
	```

`type` 和 `domain` 之间的区别为：

- 域可以有约束，并且可以使用域类型的默认值
- 域并没有强制的类型要求。因此，只要底层类型是可兼容的，在某个域的值就可以被赋予另一个域类型的值
***
### Large-Object Types

> 很多数据库系统需要存储包含大数据项的属性，比如照片、高分辨率的图像或视频等。因此 SQL 为字符数据（`CLOB`）和二进制数据（`BLOB`）提供了**大对象数据类型**（Large-Object Data Types）

- BLOB：二进制大对象（Binary Large Object）——对象是未解释的二进制数据的大型集合（其解释由数据库系统之外的应用程序定义）
	- 在 MySQL 中，BLOB 数据类型有：
		- TinyBlob：0～255 字节
		- Blob：0～64K 字节
		- MediumBlob：0～16M 字节
		- LargeBlob：0～4G 字节
- CLOB：字符大对象（Character Large Object）——对象是大型字符数据的集合
- 当查询返回大型对象时，将返回指针，而不是大型对象本身。
***
### Integrity Constraints

- 完整性约束通过确保对数据库的授权更改不会导致数据一致性的丢失，来防止对数据库的意外损坏。对于一个关系来说，有以下几种：
	- not null：定义键值不允许为空
	- primary key
	- unique
		- `unique(A1, A2, ..., Am)` 指出属性 A1、A2、...Am 形成一个超级键（不一定是一个候选键）
		- 候选键允许为 null（与主键不同）
	- check(P)，其中 P 是一个谓词
	
	!!! example "Example"
	
		- 确保每个课程的学期为春夏秋冬其中之一
		
		```sql
		create table section (
		    course_id varchar (8),
		    sec_id varchar (8),
		    semester varchar (6),
		    year numeric (4,0),
		    building varchar (15),
		    room_number varchar (7),
		    time slot id varchar (4),
		    primary key (course_id, sec_id, semester, year),
		    check (semester in (’Fall’, ’Winter’, ’Spring’, ’Summer’))  
		);
		```
	
	- foreign key
***







