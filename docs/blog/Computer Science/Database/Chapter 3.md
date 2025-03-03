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