---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
# comments: true
--- 

# Homework 10

## 14.3(a)

> Construct a B+-tree for the following set of key values: 
>
$$
(2, 3, 5, 7, 11, 17, 19, 23, 29, 31)
$$
>
> Assume that the tree is initially empty and values are added in ascending order. Construct B+-trees for the case where the number of pointers that will fit in one node is as follows: 
> 
> a. Four

![](../../../assets/Pasted%20image%2020250421184516.png)
***
## 14.4

> For each B+-tree of Exercise 14.3, show the form of the tree after each of the following series of operations: 
> 
> a. Insert 9. 
> 
> b. Insert 10. 
> 
> c. Insert 8. 
> 
> d. Delete 23. 
> 
> e. Delete 19. 

（a）

![](../../../assets/Pasted%20image%2020250421184630.png)

（b）

![](../../../assets/Pasted%20image%2020250421184700.png)

（c）

![](../../../assets/Pasted%20image%2020250421184719.png)

（d）

![](../../../assets/Pasted%20image%2020250421184742.png)

（e）

![](../../../assets/Pasted%20image%2020250421184837.png)
***
## 14.11

> In write-optimized trees such as the LSM tree or the stepped-merge index, entries in one level are merged into the next level only when the level is full. Suggest how this policy can be changed to improve read performance during periods when there are many reads but no updates. 

如果有一段时间没有更新，但在一个索引上有很多索引查找操作，那么一层的条目可以合并到下一个层，即使该层未满
***
## 24.10

> The stepped merge variant of the LSM tree allows multiple trees per level. What are the tradeoffs in having more trees per level?

优点：

- 提高写入吞吐量
- 减小写操作的花费

缺点：

- 读取性能下降
- 内存开销增加