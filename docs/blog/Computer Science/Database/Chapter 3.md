---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
--- 

# Chapter 03 : Introduction to SQL

## Data Definition

SQL 数据定义语言（Data Definition Language, DDL）指定以下的信息：

- 每个关系的**模式**
- 关联每个属性的类型值
- **完整性约束**
- 用于维护关系的**索引**
- 每个关系的**安全**和**授权**信息
- 每个关系在硬盘上的物理**存储**结构
***
### Domain Types in SQL

- `char(n)`：定长字符串，由用户指定长度 `n`
    - 当比较两个 `char` 类型的值时，如果它们的长度不同，那么会给短的那个加上额外的空格，使得它们一样长
- `varchar(n)`：变长字符串，由用户指定最大长度 `n`
    - 当比较 `char` 类型和 `varchar` 类型时，有可能会在 `varchar` 值上添加额外的空格，但也有可能不会，这取决于系统。因此即使用 `char` 和 `varchar` 表示两个相同的字符串，比较结果也有可能是 `false`。建议一直使用相同类型的值比较
    - SQL 还提供了 `nvarchar` 类型以表示 Unicode 编码的多语言数据，但是很多数据库支持用 `varchar` 表示 Unicode 编码（尤其是 UTF-8）的字符
- `int`：整数（实际上是依赖于机器的整数的有限子集）
- `smallint`：较小的整数（实际上是依赖于机器的整数的有限子集）
- `numeric(p, d)`：定点 (fixed point) 数，由用户指定位数 `p`（包括符号位）以及十进制小数点右侧的位数 `d`
- `real` / `double precision`：分别对应单精度浮点数和双精度浮点数，其精度依赖于机器
- `float(n)`：浮点数，由用户指定最低精度位数 `n`
***
### Built-in Data Types in SQL

- `date`：日期，包含年（4 位数字）月日，比如 `2025-03-03`
- `time`：时间，包含时分秒，比如 `10:08:54`、`10:08:54.75`
- `timestamp`：时间戳，即日期 + 时间，比如 `2025-03-03 10:08:54.75`
    - 在 SQL Server 2000 里，这个类型被称为 `datetime`
- `interval`：时间间隔，比如 1 天
	- 将一个日期/时间/时间戳减去另一个值，得到一个间隔值
	- 可以将间隔值添加到日期/时间/时间戳
- 时间、日期函数：
	- `current_date()`，`current_time()`
	- `year(x)`，`month(x)`，`day(x)`，`hour(x)`，`minute(x)`，`second(x)`
***
### Create Table Construct

我们用 `create table` 命令来定义一个 SQL 关系：

```SQL
CREATE TABLE r(A1 D1, A2 D2, ..., An Dn,
    (integrity constraints_1),
    ...,
    (integrity constraints_k));
```

- `r` 是关系的名称
- `Ai` 是关系 `r` 的模式中的一个属性名，而 `Di` 是 属性 `Ai` 值域的数据类型
- 可用的完整性约束有（SQL 会阻止不满足完整性约束的更新）：
	- `primary key(A_1, A_2, ..., A_n)`
        - 该属性声明主键后，该属性自动被规定为非空和唯一
        - 虽然是可选的，但建议每个关系都要加一个主键
	- `foreign key(A_m, ..., A_n) references r`
        - 外键从关系 `r` 中参考而来
    - `not null`：不允许属性出现空值

!!! example "Example"

	=== "Example 01"
	
		```SQL
		create table instructor (
			ID char(5),
			name varchar(20) not null,
			dept_name varchar(20),
			salary numeric(8,2),
			primary key (ID),
			foreign key (dept_name) references department);
		```
	
	=== "Example 02"
	
		- 如果不符合完整性约束条件，插入可能会失败。可以给一个缺省值，例如 `default 0`
		
		```SQL
		create table student (
			ID varchar(5),
			name varchar(20) not null,
			dept_name varchar(20),
			tot_cred numeric(3,0) default 0,
			primary key (ID),
			foreign key (dept_name) references department));
		```
	
	=== "Example 03"
	
		```SQL
		create table takes (
			ID varchar(5),
			course_id varchar(8),
			sec_id varchar(8),
			semester varchar(6),
			year numeric(4,0),
			grade varchar(2),
			primary key (ID, course_id, sec_id, semester, year),  
			foreign key (ID) references student,
			foreign key (course_id, sec_id, semester, year) references section);
		```
		
		- 可以从上面的 `primary key` 中删除 `sec_id`，以确保学生不能在同一学期注册同一课程的两个 section

如果引用的表中有条目被删除，可能会破坏完整性约束条件。有下面的方法：

- `restrict`: 如果有条目是被引用的，那么不允许删除。
- `cascade`: 引用的条目被删了之后，引用者也一并删除
- `set null`: 引用者的指针设为 `null`.
- `set default`

如果引用的表中有更新，也有类似上面的四种方法。我们可以在 `create table` 中定义：

- `on delete cascade |set null |restrict |set default`
- `on update cascade |set null |restrict |set default`

!!! example "Example"

	```SQL
	create table course (
		course_id varchar(8) primary key,
		title varchar(50),
		dept_name varchar(20),
		credits numeric(2,0),
		foreign key (dept_name) references department (dept_name));
	
	foreign key (dept_name) references department
		on delete cascade |set null |restrict |set default
		on update cascade |set null |restrict |set default,
	```
***
### Drop and Alter Table Constructs

- 我们用 `drop table` 语句从 SQL 数据库中删除关系
	- e.g. `drop table student;`
	- 另一种类似的方法是使用 `delete from student;`，该语句的结果是删除 student 内的所有元组，即清空关系 student 的内容，但不删除 student 本身；而前者会直接删掉 student 本身
- 我们用 `alter table` 已有关系中的属性
    - 增加属性：`alter table r add A D;`
	    - 其中 A 是要添加到关系 r 的属性的名称，D 是 A 的域
	    - 关系中的所有元组都被分配为 null 作为新属性的值
	    - e.g. `alter table student add resume varchar(256);`
	- 删除属性：`alter table r drop A;`
        - 其中 A 是关系 r 的属性名称
        - 很多数据库系统不支持删除属性的操作，但是我们可以生成一个新的表，然后把除了要删的列以外的列搬移过去
***
## Basic Query Structure

一条典型的 SQL 查询语句格式为：

```SQL
select A1, A2, ..., An
from r1, r2, ..., rm
where P
```

- `Ai` 表示属性，`Ri` 表示关系，`P` 是谓词
- 查询结果也是一个关系
- 查询语句的运算顺序为：`from`（笛卡尔积） -> `where`（选择谓词） -> `select`（指定属性）
    - SQL 的实际实现不会遵循上述方式，为了优化求解过程而仅生成满足 `where` 子句谓词的笛卡尔积的元素

!!! note "SQL and Relational Algebra"

	=== "Example 01"
	
		`select A1, A2, ..., An from r1, r2, ..., rm where P` 和语句 $\prod_{A_1,...,A_n}(\sigma_P(r_1\times r_2\times ...\times r_m))$ 等价
	
	=== "Example 02"
	
		`select A1, A2, sum(A3) from r1, r2, ..., rm where P group by A1, A2` 和语句$\text{ }_{A_1,A_2}\mathcal{G}_{\text{sum}(A_3)}(\sigma_P(r_1\times r_2\times ...\times r_m))$ 等价
	
	=== "Example 03"
	
		- 更一般地说，select 子句中的非聚合属性可能是 group by 属性的子集，在这种情况下，`select A1, sum(A3) from r1, r2, ..., rm where P group by A1, A2` 和语句$\prod_{A_1,\text{sumA3}}(\text{ }_{A_1,A_2}\mathcal{G}_{\text{sum}(A_3)\text{as sumA3}}(\sigma_P(r_1\times r_2\times ...\times r_m))$ 等价
***
### The Select Clause

- `select` 子句列出了查询结果中所需的属性
	- 对应于关系代数中的投影运算
- 需要注意的是，SQL 语句不允许名称中出现 `-` 字符，请用 `_` 替代
- 并且 SQL 对名称**大小写不敏感**（Case Insensitive），也就是说 SQL 将同一字符的大小写形式看作是同一个字符
- SQL 允许关系和查询结果中出现**重复**记录（Duplicates）（默认使用 `all` 关键字，因为消除重复记录太耗费时间了）。要想强制消除重复记录，可以在 `select` 后使用 `distinct` 关键字，即 `select distinct ...`
- 使用 `*` 表示选择所有属性，比如 `select * from r` 表示选择 `r` 中的所有属性
- SQL 允许查询语句中对常量或属性使用简单的算术表达式，包括加减乘除，对应关系代数的**广义投影**（Generalized Projection）
    - 比如 `select ID, name, salary / 12 from instructor;`
***
### The Where Clause

- `where` 从句指定结果必须要满足的条件，对应于关系代数的**选择谓词**（Selection Predicate）
- 在 `where` 从句的比较表达式内，可以使用逻辑连接词 `and`、`or`、`not` 以及 `between`（用于指定范围）
- 在 `where` 从句的比较表达式内，可以进行元组比较

!!! example "Example"

	=== "Example 01"
	
		- 找到 Comp. Sci. dept 中薪资大于 80000 的所有老师
		
		```SQL
		select name from instructor
		where dept_name = 'Comp. Sci.' and salary > 80000;
		```
	
	=== "Example 02"
	
		- 找到薪资在 $90,000 到 $100,000 之间（闭区间）的老师
		
		```SQL
		select name from instructor
		where salary between 90000 and 100000;
		```
	
	=== "Example 03"
	
		- 元组比较
		
		```SQL
		select name, course_id  
		from instructor, teaches  
		where (instructor.ID, dept_name) = (teaches.ID, ’Biology’);
		```
***
### The From Clause

- `from` 从句列出包含在查询语句内的关系，对应于关系代数的**笛卡尔积**（Cartesian product）（如果指定多个关系的话）
- 如果查询语句的多个关系中有相同的属性名，且都要在查询语句中用到，那么在属性名前需要加上关系名和点号作为前缀，比如：

```SQL
SELECT name, course_id
FROM instructor, teaches
WHERE instructor.ID = teaches.ID;
```
***
### Natural Join

- e.g. `select * from instructor natural join teaches;` 
- `select name, course_id from instructor, teaches where instructor.ID = teaches.ID;` 和 `select name, course_id from instructor natural join teaches;` 是等价的

> 具有相同名称的不相关属性会错误地等同起来

!!! example "Example"

	`course(course_id,title, dept_name,credits)`，`teaches(ID, course_id,sec_id,semester, year)`，`instructor(ID, name, dept_name,salary)` 三者的 department 含义各有不同，不能直接自然连接
	
	可以写成 `select name, title from (instructor natural join teaches）join course using(course_id);` 即规定连接的属性，对应于 σθ

Find students who takes courses across his/her department.  
可写作





