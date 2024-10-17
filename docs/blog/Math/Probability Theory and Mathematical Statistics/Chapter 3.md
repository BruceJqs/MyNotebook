---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
---  
# Chapter 03 : 多元随机变量及其分布

## 二元离散型随机变量

### 联合分布律

设 $(X,Y)$ 所有可能取值为 $(x_i,y_j),P(X=x_i,Y=y_j)=p_{ij},i,j=1,2,…$ 为二元离散型随机变量 $(X,Y)$ 的联合分布律（Joint Mass Function），可以用如下表格表示：

![](../../../assets/Pasted%20image%2020241017112253.png)
***
### 边际分布律

对于离散型随机变量 $(X,Y)$，分布律为 $P(X=x_i,Y=y_j)=p_{ij},i,j=1,2,...$

$X,Y$ 的边际（边缘）分布律（Marginal Mass Function）为：

- $P(X=x_i)=P(X=x_i,Y<+\infty)=\sum\limits_{j=1}^\infty p_{ij}$，记为 $p_{·i},i=1,2,...$；
-  $P(Y=y_j)=P(X<+\infty,Y=y_j)=\sum\limits_{i=1}^\infty p_{ij}$，记为 $p_{·j},j=1,2,...$；

边际分布律本质是联合分布律的行/列求和。
***
### 条件分布律

对于两个事件 $A,B$，若 $P(A)>0$，可以考虑条件概率 $P(B|A)$，对于二元离散型随机变量 $(X,Y)$，设其分布律为 $P(X=x_i,Y=y_j)=p_{ij},i,j=1,2,...$

若 $P(Y=y_j)=p_{·j}>0$，条件概率 $P(X=x_i|Y=y_j)=\frac{P(X=x_i​,Y=y_j​)}{​P(Y=y_j​)}=\frac{p_{ij}}{p_{⋅j}},​​​i,j=1,2,...$

$P(X<x∣Y<y)=\frac{P(X<x,Y<y)}{P(Y<y)}​$，然后根据联合分布律和边际分布律读表计算；