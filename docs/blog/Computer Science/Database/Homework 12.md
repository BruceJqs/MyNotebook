---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
--- 

# Homework 12

## 16.5

> Consider the relations $r_1(A,B,C),r_2(C,D,E)$, and $r_3(E,F)$, with primary keys $A,C,$ and $E$, respectively. Assume that $r_1$ has 1000 tuples, $r_2$ has 1500 tuples, and $r_3$ has 750 tuples. Estimate the size of $r_1\Join r_2\Join r_3$, and give an efficient strategy for computing the join.

首先估计 $r_1\Join r_2$，使用属性 $C$ 进行连接，对于 $r_1$ 中的每一个 $C$ 值，直接在 $r_2$ 中查找对应的行，且因为 $C$ 是主键最多返回一行，假设 $r_1$ 的 $C$ 值都在 $r_2$ 中存在，则 $r_1\Join r_2$ 的结果大约为 1000 行

再用 $E$ 属性进行连接，同理，假设中间结果的 $E$ 都在 $r_3$ 中存在，最终连接结果仍然大约为 1000 行
***
## 16.16

> Suppose that a B+-tree index on (dept_name, building) is available on relation department. What would be the best way to handle the following selection?
> 
> $\sigma_{(\text{building}<\text{Watson})\land(\text{budget}<55000)\land(\text{dept_name}=\text{Music})}(\text{department})$
> 
> branch(<u>branch name</u>, branch_city, assets)
> 
> customer(<u>customer_name</u>, customer_street, customer_city)
> 
> loan(<u>loan_number</u>, branch name, amount)
> 
> borrower(<u>customer_name</u>, <u>loan number</u>)
> 
> account(<u>account_number</u>, branch_name, balance)
> 
> depositor(<u>customer_name</u>, <u>account_number</u>)

- 首先利用 B+ 树索引查找 `dept_name = 'Music'` 的记录
- 再利用索引查找 `building < 'Watson'` 的记录
- 检索对应的数据记录
- 最后对检索到的数据记录进行 `budget < 55000` 的过滤
