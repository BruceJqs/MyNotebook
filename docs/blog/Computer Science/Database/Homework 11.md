---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
# comments: true
--- 

# Homework 11

## 15.2

> Consider the bank database of Figure 15.14, where the primary keys are underlined, and the 
> following SQL query: 
> 
```sql 
SELECT T.branch_name
FROM branch T, branch S
WHERE T.assets > S.assets AND S.branch_city = "Brooklyn"
```
> 
> Write an efficient relational-algebra expression that is equivalent to this query. 
> Justify your choice. 
> 
 ![](../../../assets/Pasted%20image%2020250427220509.png)

$\prod_{T.\text{branch_name}}((\prod_{\text{branch_name,assets}}(\rho_T(\text{branch})))\Join_{T.\text{assets}>S.\text{assets}}(\prod_{\text{assets}}(\sigma_{\text{branch_city}=\text{Brooklyn}}(\rho_S(\text{branch})))))$

这个表达式以尽可能少的数据量进行 Theta 连接，通过将连接右侧的操作数限制为仅包含 Brooklyn 的分支来实现。 这将减少连接的结果集的大小，从而提高查询效率。 
***
## 15.3

> Let relations $r_1(A, B, C)$ and $r_2(C, D, E)$ have the following properties: 
> $r_1$ has $20,000$ tuples, $r_2$ has $45,000$ tuples, $25$ tuples of $r_1$ fit on 
> one block, and $30$ tuples of $r_2$ fit on one block. Estimate the number of 
> block transfers and seeks required using each of the following join strategies 
> for $r_1 \bowtie r_2$: 
> 
> a. Nested-loop join. 
> 
> b. Block nested-loop join. 
> 
> c. Merge join. 
> 
> d. Hash join. 

（a）$b_{r_1}=\frac{20000}{25}=800,b_{r_2}=\frac{45000}{30}=1500$

$$
\begin{aligned}
\text{block transfers}_{r_1} &= b_{r_1} + n_{r_1} \times b_{r_2} = 800 + 20000 \times 1500 = 30000800\\
\text{seeks}_{r_1} &= b_{r_1} + n_{r_1} = 800 + 20000 = 20800\\
\text{block transfers}_{r_2} &= b_{r_2} + n_{r_2} \times b_{r_1} = 1500 + 45000 \times 800 = 36001500\\
\text{seeks}_{r_2} &= b_{r_2} + n_{r_2} = 1500 + 45000 = 46500\\
\end{aligned}
$$

（b）对 $r_1$ 需要 $\lceil\frac{b_{r_1}}{M-2}\rceil*b_{r_2}+b_{r_1}$ 次块转移和 $2*\lceil\frac{b_{r_1}}{M-2}\rceil$ 次寻道

对 $r_2$ 需要 $\lceil\frac{b_{r_2}}{M-2}\rceil*b_{r_1}+b_{r_2}$ 次块转移和 $2*\lceil\frac{b_{r_2}}{M-2}\rceil$ 次寻道

（c）如果 $r_1$ 和 $r_2$ 没有排序好，且 $b_b=1$，那么有：

- $T_\text{Sort}(r_i)=b_{r_i}(2\lceil\log_{M-1}\frac{b_{r_i}}{M}\rceil+1)$
- $S_\text{Sort}(r_i)=2\lceil\frac{b_{r_i}}{M}\rceil+b_{r_i}(2\lceil\log_{M-1}\frac{b_{r_i}}{M}\rceil-1)$

我们需要 $T_\text{Sort}(r_1)+T_\text{Sort}(r_2)+b_{r_1}+b_{r_2}$ 次块转移和 $S_\text{Sort}(r_1)+S_\text{Sort}(r_2)$ 次寻道

如果 $r_1$ 和 $r_2$ 已经排序好，且 $b_b=1$，那么需要 $b_{r_1}+b_{r_2}$ 次块转移和 $b_{r_1}+b_{r_2}$ 次寻道

（d）如果 $r_1$ 作为探测输入，$r_2$ 作为构建输入，如果使用递归划分，需要 $2(b_{r_1}+b_{r_2})\lceil\log_{M-1}\frac{b_{r_2}}{M}\rceil+b_{r_1}+b_{r_2}$ 次磁盘访问和 $2(b_{r_1}+b_{r_2})\lceil\log_{M-1}\frac{b_{r_2}}{M}\rceil$ 次寻道

如果不使用递归划分，那么需要 $3(b_{r_1}+b_{r_2})=6900$ 次磁盘访问和 $2(b_{r_1}+b_{r_2})=4600$ 次寻道

如果 $r_1$ 作为构建输入，$r_2$ 作为探测输入，如果使用递归划分，需要 $2(b_{r_1}+b_{r_2})\lceil\log_{M-1}\frac{b_{r_1}}{M}\rceil+b_{r_1}+b_{r_2}$ 次磁盘访问和 $2(b_{r_1}+b_{r_2})\lceil\log_{M-1}\frac{b_{r_1}}{M}\rceil$ 次寻道

如果不使用递归划分，那么需要 $3(b_{r_1}+b_{r_2})=6900$ 次磁盘访问和 $2(b_{r_1}+b_{r_2})=4600$ 次寻道








