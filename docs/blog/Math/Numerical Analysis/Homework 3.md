---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
--- 

# Homework 03

## 2.4.11

![](../../../assets/Pasted%20image%2020250309131745.png)

假设我们有 $\frac{|p_{n+1}-p|}{|p_n-p|^3}=0.75$ 和 $|p_0-p|=0.5$，那么我们可以得到：

$$
|p_n-p|=0.75\times |p_{n-1}-p|^3=0.75^2\times |p_{n-2}-p|^9=\cdots=(0.75)^{\frac{3^n-1}{2}}|p_0-p|^{3^n}
$$

如果要有 $|p_n-p|\leq 10^{-8}$，那么我们需要 $n\geq 3$
***
## 6.1.8

![](../../../assets/Pasted%20image%2020250309132041.png)

![](../../../assets/Pasted%20image%2020250309132134.png)

- 将 Step 4 当中的下标 $j=i+1,...,n$ 改为 $j=1,2,...,n$，如果 $j\not=i$ 时执行 Step 5 和 6
- 将 Step 8 和 9 去除，$x_i$ 即为 $\frac{a_{i,n+1}^{(i)}}{a_{ii}^{(i)}}$
***
## 6.1.11

![](../../../assets/Pasted%20image%2020250309132117.png)

(a) 对于乘除法，我们有总次数：

$$
\underbrace{\sum\limits_{k=1}^n(n-1)}_{\text{Division to Compute m}}+\underbrace{\sum\limits_{k=1}^n(n+1-k)(n-1)}_{\text{Multiplication of Elimination}}+\underbrace{n}_{\text{Division to Compute x}}=\frac{n^3}{2}+n^2-\frac{n}{2}
$$

对于加减法，我们有总次数：

$$
\sum\limits_{k=1}^n(n+1-k)(n-1)=\frac{n^3}{2}-\frac{n}{2}
$$

(b) 

| $n$                  |                           | 3   | 10   | 50     | 100     |
| -------------------- | ------------------------- | --- | ---- | ------ | ------- |
| Gauss-Jordan         | Multiplications/Divisions | 21  | 595  | 64975  | 509950  |
| Gauss-Jordan         | Additions/Subtractions    | 12  | 495  | 62475  | 499950  |
| Gauss-Jordan         | Sum                       | 33  | 1090 | 127450 | 1009900 |
| Gaussian Elimination | Multiplications/Divisions | 17  | 430  | 44150  | 343300  |
| Gaussian Elimination | Additions/Subtractions    | 11  | 375  | 42875  | 338250  |
| Gaussian Elimination | Sum                       | 28  | 805  | 87025  | 681550  |

所以 Gaussian Elimination 需要更少的计算次数

