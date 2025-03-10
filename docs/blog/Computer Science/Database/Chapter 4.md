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
## Integrity Constraints

- 完整性约束通过确保对数据库的授权更改不会导致数据一致性的丢失，来防止对数据库的意外损坏。对于一个关系来说，有以下几种：
	- not null：定义键值不允许为空
	- primary key
	- unique
		- `unique(A1, A2, ..., Am)` 指出属性 A1、A2、...Am 形成一个超级键（不一定是一个候选键）
		- 候选键允许为 null（与主键不同）
	- check(P)，其中 P 是一个谓词
		- 也可以有复杂查询，但许多数据库不支持。e.g. `check ((course_id, sec_id, semester, year) in (select course_id, sec_id, semester, year from teaches))`
	
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
### Referential Integrity

- **参照完整性**（Referential Integrity）确保在给定属性集的一个关系中出现的值也出现在另一个关系中的特定属性集中
	- 例如，如果 “Biology” 是出现在关系 instructor 的某个元组中的部门名称，则 “Biology” 的关系 department 中存在一个元组
- 在 SQL 中，参照完整性约束由外键实现，语法为：`FOREIGN KEY (dept_name) REFERENCES department`
	- 设 A 为一组属性。 设 R 和 S 是包含属性 A 的两个关系，其中 A 是 S 的主键。如果 A 的任何值出现在 R 中，这些值也出现在 S 中，则称 A 是 R 的外键
- 执行违反参照完整性约束的语句时会被拒绝。然而，对于在被参照关系上的更新和删除行为，如果违反约束，系统必须采取行动来改变参照关系的元组，以恢复约束。对于以下语句：
	
	```sql
	create table course (
	    foreign key (dept_name) references department
	    on delete cascade
	    on update cascade
	    ...
	);
	```
	
	以删除操作为例，如果要删除 `department` 里的元组，那么就会违背参照完整性约束，不过系统不会拒绝这个操作，而是通过级联（Cascade）删除的方式删除在 `course` 中参照在 `department` 中被删除元组的元组。更新操作与之同理
- 除了 `cascade` 关键字外，还可以设置 `set null` 或 `set default`，当违反约束时会触发这些操作

!!! question "如何避免违反约束？"

	例如，我们有如下关系：
	
	```sql
	create table person (
		ID char(10),
		name char(40),
		mother char(10),
		father char(10),
		primary key (ID),
		foreign key (father) references person,
		foreign key (mother) references person);
	```
	
	我们想要避免违反约束地插入一个元组，可以：
	
	- 在插入 person 之前插入一个人的父亲和母亲
	- 或者一开始将 father 和 mother 设置为 null，在插入所有人员后更新（如果 father 和 mother 属性声明为不为空，则无法进行）
	- 或者将约束检查推迟到事务结束
***
### Assertions

**断言**（Assertion）是表达一种希望数据库一直满足的条件的一种谓词。创建断言的语法为：

```sql
create assertion <assertion-name> check <predicate>;
```

!!! example "Example"

	- 验证一个学生获得的总学分，要等于获得的每门课的学分的总和
	
	```sql
	create assertion credits_earned_constraint check (
	    not exists (
	        select ID from student
	        where tot_cred <> (
	            select coalesce(sum(credits), 0)
	            from takes natural join course
	            where student.ID = takes.ID and grade is not null and grade <> 'F'
	        )
	    )
	);
	```
	
	因为 SQL 不提供一种 `for all X, P(X)` 的构造，因此只能用 `not exists X such that not P(X)` 这一等价形式表示
***
## Views

- 视图提供了一种机制，用于从某些用户的视图中隐藏某些数据。例如，考虑一个人，他需要知道 instructor 的姓名和部门，但不需要知道薪水。 此人应该会看到一个关系，在 SQL 中可以通过：
	
	```sql
	select ID, name, dept_name from instructor
	```
	
- 任何不属于概念模型但作为 “虚拟关系” 对用户可见的关系都称为视图
- view 可以隐掉一些细节，或者加上一些统计数据。可以把 view 当作表进行查询
	- 隐藏不必要的细节，简化用户视野
	- 方便查询书写
	- 有利于权限控制（如用户可以看到工资总和，但不能看到每个人的工资）
	- 有独立性，使得数据库应用具有较强的适应性
***
### View Definition

创建视图的语法为：

```sql
create view <view-name> as <query-expression>;
```

其中 `<query-expression>` 是任意一个合法的 SQL 表达式

- 定义视图后，视图名称可用于引用视图生成的虚拟关系，数据库系统只存储视图自身的定义，而不会存储查询表达式的求解结果
	- 当视图关系出现在其他查询语句时就会被替换为被存储的查询表达式
- 可以用视图定义其他视图，例如：
	
	```sql
	create view physics_fall_2009 as  
		select course.course_id, sec_id, building, room_number
		from course, section 
		where course.course_id = section.course_id
			and course.dept_name = ’Physics’
			and section.semester = ’Fall’
			and section.year = ’2009’;
	
	create view physics_fall_2009_watson as 
		select course_id, room_number
		from physics_fall_2009
		where building= ’Watson’;
	```
	
- 虽然看起来与 `with` 子句很像，但 `with` 子句创建的只是临时的关系，而 `create view` 创建的视图可以在后面一直使用，直到被手动销毁或程序中止
- 创建视图时还可以指定属性名：
	
	```sql
	create view departments_total_salary(dept_name, total_salary) as
    select dept_name, SUM(salary) from instructor
	group by dept_name;
	```
***
### Update of a View

- 对一个 view 进行修改，相当于通过这个窗口对原表继续修改

!!! example "Example"

	- 我们有如下视图：
	
	```sql
	create view faculty as
	select ID, name, dept_name from instructor
	```
	
	我们用 `insert into faculty values (’30765’, ’Green’, ’Music’);` 进行插入，插入后，原表也会有这条数据，对于其缺少的 `salary` 属性，我们设定为 `NULL`. 如果这个属性的约束是 `not NULL` 的，那么我们无法执行这次插入

事实上，更新一个视图非常麻烦，如果创建的视图涉及到多个关系，并且还用 `where` 子句指定一些条件，那么插入语句很有可能无法满足 `where` 给出的条件而无法达到预期效果。

综上，除了以下列出的有限情况，通常不允许对视图关系进行修改：

- `from` 子句仅包含一个数据库关系
- `select` 子句仅包含来自这个关系的属性名，并且不允许出现任何表达式、聚合函数或者 `distinct` 约束
- 任何没有出现在 `select` 子句的属性会被设为 null，因此也不允许使用 `not null` 或 `primary key` 约束
- 查询语句不能有 `group by` 或 `having` 子句

我们称满足这些情况的视图是**可更新的**（Updatable）
***
### *Materialized Views

有些数据库系统允许存储视图关系，且仍然确保视图保持更新的特点，这样的视图称为**实体化视图** （Materialized Views）

- 由于结果被存储在数据库中，不需要重新计算，因此使用此类视图的查询语句的运行速度可能会更快，适用于需要快速响应的情景
- 但如果实体化视图对应的关系发生改动，那么实体化视图中的内容就过时了，视图里的内容必须被更新

!!! example "Example"

	```sql
	create materialized view departments_total_salary(dept_name, total_salary) as 
		select dept_name, sum (salary) 
		from instructor
		group by dept_name;
	
	select dept_name  
	from departments_total_salary  
	where total_salary > (select avg(total_salary) from departments_total_salary);
	```
***
### *View and Logical Data Independence

!!! question "视图如何实现逻辑数据独立性？"

	如果我们有关系 `S(a,b,c)` 被拆成了两个子关系 `S1(a,b)` 和 `S2(b,c)`，那么我们可以这么做：
	
	```sql
	create table S1 ...;
	create table S2 ...;
	
	insert into S1 select a,b from S;
	insert into S2 select b,c from S;
	
	drop table S;
	
	create view S as select a, b, c from S1 natural join S2;
	```
	
	这样之后，语句 `select * from S where...` 实际上是在做 `select * from S1 natural join S2 where ...` （系统会帮我们这样做，程序不用改，只是执行改变了）；语句 `insert into S values (1,2,3)` 实际上是在做 `insert into S1 values (1,2)` 和 `insert into S2 values (1,3)`
***
## Indexes

- 在关系中，某个属性的**索引**（Index）是指一种能让数据库系统高效寻找具有特定属性值的元组的数据结构，无需遍历关系内的所有元组
- 索引的实际实现方式为 B+ 树

!!! example "Example"

	- 我们有如下关系：
	
	```sql
	create table student (
	ID varchar (5),
	name varchar (20) not null,
	dept_name varchar (20),
	tot_cred numeric (3,0) default 0,
	primary key (ID));
	```
	
	`select * from student where ID = ‘12345’` 在数据库内不同的物理实现有不同的查找方法
	
	如果没有定义索引，只能顺序查找。如果有索引，系统内会利用索引查找
***
## Transactions

**事务**（Transaction）是一个查询 / 更新语句的序列。当 SQL 语句被执行的时候，我们就开启了一个事务。用以下 SQL 语句之一作为事务的结束：

- `commit work`：**提交**（Commit）当前事务，也就是说，它让由事务实现的更新操作变为对数据库的永久修改。事务提交之后，新的事务就开始了
    - 就是保存对被编辑文档的更改
    - 在大多数数据库上默认每单个 SQL 语句都会自动提交
	    - 如果需要让多条 SQL 语句构成一个事务的话，需要关闭这种对于单个 SQL 语句的**自动提交**（Automatic Commit）。关闭操作取决于具体的 SQL 实现，但大多数数据库支持 `set autocommit off` 命令
	    - 更好的替代方法时将这些语句放在关键字 `begin atomic ... end` 之中，此时这些语句会被视为一个事务。但只有部分数据库支持这一语法；其他数据库可能用 `commit work` 或 `rollback work` 替代 `end` 语句
    - 其中 `work` 是可省略的（Rollback 同理）
- `rollback work`：**回滚**（Rollback）当前事务，也就是说，它撤销所有先前由事务内的 SQL 语句执行的更新。因此，数据库的状态就会恢复到事务的第一条语句被执行之前的状态
    - 就是退出编辑会话，并且不保存更改
    - 一旦事务被提交之后，该事务就无法被回滚

!!! example "Example"

	```sql
	SET AUTOCOMMIT=0;
	UPDATE account SET balance=balance -100 WHERE ano=‘1001’;
	UPDATE account SET balance=balance+100 WHERE ano=‘1002’;
	COMMIT;
	
	UPDATE account SET balance=balance -200 WHERE ano=‘1003’;
	UPDATE account SET balance=balance+200 WHERE ano=‘1004’;
	COMMIT;
	
	UPDATE account SET balance=balance+balance*2.5%;
	COMMIT;
	```
***
### ACID Properties

事务是访问并可能更新各种数据项的程序执行单元。为了保持数据的完整性，数据库系统必须确保：

- **原子性**（Atomicity）：事务的所有操作都正确反映在数据库中，或者没有正确反映
- **一致性**（Consistency）：独立执行事务保持了数据库的一致性，即数据库从一个一致性状态转移到另一个一致性状态
- **隔离性**（Isolation）：尽管多个事务可以并发执行，但每个事务必须不知道其他并发执行的事务。 中间事务结果必须对其他并发执行的事务隐藏
	- 也就是说，对于每对交易 $T_i$ 和 $T_j$，在 $T_i$ 看来，要么 $T_j$ 在 $T_i$ 开始之前完成执行，要么 $T_j$ 在 $T_i$ 完成之后开始执行
- **持久性**（Durability）：事务成功完成后，即使存在系统故障，它对数据库所做的更改也会保留。
***
## Authorization

对**数据**的**授权**（Authorization）分为以下四类：

- 读取数据的授权
- 插入新数据的授权
- 更新数据的授权
- 删除数据的授权

对数据库架构的授权分为以下五类：

- 建立（Resources，在 MySQL 中为 Create）：允许创建新关系
- 改动（Alteration）：允许在关系中添加或删除属性
- 删除（Drop）：允许删除关系
- 索引（Index）：允许创建和删除索引
- 视图（在 MySQL 为 Create view）：允许创建视图
***
### Authorization Specification in SQL

在 SQL 中，授予特权的语法为：

```sql
grant <privilige list>
on <relation name or view name>
to <user/role list>;
```

其中：

- 特权表（Privilige List）可以包含以下特权中的一个或多个：`select`、`insert`、`update`、`delete`
    - 如果要授予全部特权的话，可以用关键字 `all privileges` 表示
    - `select` 特权允许用户读取关系中的元组
    - `update` 特权允许用户更新关系。默认可以更新所有属性；如果仅允许用户更新部分属性的话，需要在 `update` 关键字后紧跟用圆括号包裹的属性列表
    - `insert` 特权允许用户向关系插入元组。语法要求与 `update` 类似。但如果只允许用户插入部分属性，那么剩下那些不被允许插入的属性就会被设为 null 值
    - `delete` 特权允许用户向关系删除元组
- 用户 / 角色表（User / Role List）
    - 用户名 `public` 指代全体用户，包括将来使用数据库系统的用户
    - 默认情况下，用户无法向其他用户授予自己已有的特权

!!! example "Example"

	```sql
	grant select on instructor to U1, U2, U3
	grant select on department to public
	grant update (budget) on department to U1,U2
	grant all privileges on department to U1
	```
***
### Revoking Authorization in SQL

撤回特权的语法与授予特权的语法基本一致：

```sql
revoke <privilige list>
on <relation name or view name>
from <user/role list>;
```

- 如果不同的授权者两次向同一用户授予相同的权限，则用户在撤销后可能仍然保留该权限
- 所有依赖于被撤销的权限的权限也将被撤销
***
### Roles

> 如果只能按用户来授予特权的话，会带来一定的不便。因此 SQL 支持按**角色**（Roles）授予特权的功能，使得授予特权这件事变得更加方便灵活。所谓“角色”，可以类比 Linux 系统的用户组，每个用户可以同时有不同的角色，而每个角色对应不同的特权

!!! example "Example"

	```sql
	create role instructor; 
	grant select on takes to instructor; // 授予权限给角色
	grant instructor to Amit; //将角色的权限授予给用户
	
	create role teaching_assistant; 
	grant teaching_assistant to instructor; // 可以将角色的权限授予给其他角色，从而 instructor 继承了 teaching_assistant 的所有权限
	```

角色和用户、角色与角色之间是一个链式的关系：

![](../../../assets/Pasted%20image%2020250310140106.png)

```sql
create role dean;
grant instructor to dean;
grant dean to Satoshi;
```
***
### Authorization on Views

- 创建视图的用户不一定享有对该视图的所有特权，比如没有被授予更新特权的用户创建了一个视图后，他之后就无法对该视图进行更新

!!! example "Example"

	```sql
	create view geo_instructor as 
	(select * from instructor where dept_name = ’Geology’);
	
	grant select on geo_instructor to geo_staff
	```
***
### Other Authorization Features

#### Reference

SQL 的 `reference` 特权支持用户在创建关系时声明外键，语法上与 `update` 特权类似，比如：

```sql
grant references(dept_name) on department to Mariano;
```

这样的一个语句给予了用户 Mariano 使用外键 dept_name 来引用其他关系

- 如果不作为权限，我们可以通过间接的外键约束和 cascade 删掉被引用的数据
***
#### Transfer of Privileges

- `grant select on department to Amit with grant option;`：加上 `with grant option` 后，用户可以把获得的权限传递下去
- `revoke select on department from Amit, Satoshi cascade;`：`cascade` 把该用户及其授予的权限全部收回，级联反应
- `revoke select on department from Amit, Satoshi restrict;`：`restrict` 只收回该用户的权限
- `revoke grant option for select on department from Amit;`：收回用户转授的权力

特定授权在用户之间的传递关系可以用**授权图**（Authorization graph）来表示。当且仅当在授权图中有一条从根节点到用户的路径时，该用户才具备特定的授权

![](../../../assets/Pasted%20image%2020250310141212.png)















