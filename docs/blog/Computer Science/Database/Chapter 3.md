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





