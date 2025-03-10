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


