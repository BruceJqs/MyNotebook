---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
---  

# Chapter 06 : 数理统计的基本概念

## 随机样本与统计量

### 随机样本

- 总体与个体：一个统计问题总有它明确的研究对象，研究对象的全体称为**总体（母体）**，总体中的每个成员称为**个体**；
- 总体容量：总体中包含的个体数；
    - 有限总体是容量有限的总体；
    - 无限总体是容量无限的总体，通常将容量非常大的总体也按无限总体处理；
- 随机样本：为推测总体的分布及其各种特征，按一定规则从总体中抽取若干个体进行观察试验，以获得关于总体的信息，这一过程称为抽样，所抽取的部分个体称为**样本**，通常记为 $X=(X_1,X_2,...,X_n)$；
- 样本容量：样本中所包含的个体数目 $n$；
    - 注意，每一个样本 $X_i$ 都是随机变量，维数与总体一致；
- 简单随机样本：满足**代表性**和**独立性**的样本称为**简单随机样本(Simple Random Sample)**，获得简单随机样本的抽样方法称为简单随机抽样；
    - 代表性：$X_1,X_2,...,X_n$​ 中的每一个与所考察的总体 $X$ 都有相同的分布；
    - 独立性：$X_1,X_2,...,X_n$ 是相互独立的随机变量；

后面提到的所有样本，指的都是简单随机样本。

- 若总体有分布函数 $F(x)$，则样本具有联合分布函数 $F_n(x_1,x_2,...,x_n)=\prod\limits_{i=1}^nF(x_i)$；
- 若总体为连续型（或离散型）随机变量，其概率密度函数（或分布律）为 $f(x)$，则样本具有联合密度函数（或联合分布律）$f_n(x_1,x_2,...,x_n)=\prod\limits_{i=1}^nf(x_i)$
***
### 统计量

设 $(X_1,X_2,...,X_n)$ 是来自总体 $X$ 的一个样本，$g(X_1,X_2,...,X_n)$ 是 $X_1,X_2,...,X_n$​ 的函数，若 $g$ 中**不含任何未知参数**，则称 $g(X_1,X_2,...,X_n)$ 为一**统计量**。换言之，统计量是样本的不含任何未知参数的函数。

- 统计量仍然为随机变量；
- 统计量的分布（称为抽样分布）一般与总体分布有关，**可以依赖未知参数**；
- 当样本的观察值确定时，统计量的值也就随之确定了；

> 常用的统计量有样本均值、样本方差和样本 $k$ 阶矩
***
#### 样本均值

$$
\overline{X}=\frac{1}{n}\sum\limits_{i=1}^nX_i
$$

样本均值反映了总体的期望（均值）。

样本均值的性质：

- $E(\overline{X})=\mu,Var(\overline{X})=\frac{\sigma^2}{n}$；
- $\sum\limits_{i=1}^n(X_i−\overline{X})=0$；
- 数据观测值与样本均值的偏差平方和最小，即在形如 $\sum(X_i−c)^2$ 的函数中，$∑(X_i−\overline{X})^2$ 最小；
- 若总体服从 $N(\mu,\sigma^2)$，则 $\overline{X}$ 的**精确分布**为 $N(\mu,\frac{\sigma^2}{n})$；
- 若总体分布未知或不是正态分布，则当 $n$ 较大时，$\overline{X}$ **近似服从** $N(\mu,\frac{\sigma^2}{n})$；
***
#### 样本方差

$$
S^2=\frac{1}{n−1}\sum\limits_{i=1}^n​(X_i​−X)^2
$$

样本方差反映了总体的方差，常作为总体方差 $\sigma^2$ 的无偏估计。

样本方差的性质：

- $E(S^2)=\sigma^2$；
- $\sum(X_i−\overline{X})^2=\sum X_i^2−\frac{1}{n}(\sum X_i)^2=\sum X_i^2−n\overline{X}^2$；

此外，$S=\sqrt{S^2}=\sqrt{\frac{1}{n−1}\sum\limits_{i=1}^n(X_i−\overline{X})^2}$  称为样本标准差
***
#### 样本 k 阶矩

样本 $k$ 阶（原点）矩，常作为总体 $j=k$ 阶原点矩 $\mu_k$ 的估计：

$$
A_k=\frac{1}{n}\sum\limits_{i=1}^nX_i^k,k=1,2,...
$$

样本 $k$ 阶中心距，常作为总体 $j=k$ 阶中心矩 $\nu_k$​ 的估计，$B_2$ 可作为总体方差 $\sigma_2$ 的有偏估计：

$$
B_k=\frac{1}{n}\sum\limits_{i=1}^n(X_i−\overline{X})^k,k=2,3,...
$$

样本 $k$ 阶矩的性质：

- 假设 $X_1,X_2,...,X_n$​ 是 $X$ 中抽取的样本，$\mu_k=E(X_k)$ 存在，由辛钦大数定律可知：  $A_k=\frac{1}{n}\sum\limits_{i=1}^nX_i^k\stackrel{P}{\rightarrow}\mu_k,k=1,2,...$
***
样本与总体的各阶矩对比表：

|          |                       **样本的矩（随机变量）**                       |    **总体 X 的矩（常数）**     |
| :------: | :--------------------------------------------------------: | :--------------------: |
|    均值    |      $\overline{X}=\frac{1}{n}\sum\limits_{i=1}^nX_i$      |         $E(X)$         |
|    方差    | $S^2=\frac{1}{n-1}\sum\limits_{i=1}^n(X_i-\overline{X})^2$ |  $Var(X)=E(X-E(X))^2$  |
| 均方差/标准差  |                       $S=\sqrt{S^2}$                       | $\sigma=\sqrt{Var(X)}$ |
| $k$ 阶原点矩 |         $A_k=\frac{1}{n}\sum\limits_{i=1}^nX_i^k$          |     $\mu_k=E(X^k)$     |
| $k$ 阶中心矩 |  $B_k=\frac{1}{n}\sum\limits_{i=1}^n(X_i-\overline{X})^k$  |  $\nu_k=E(X-E(X))^k$   |

***
## 三大抽样分布

> 统计量的分布称为**抽样分布（Sampling Distribution）**

|                                 **统计量的构造**                                  |                                                                             **抽样分布密度函数**                                                                             |           **期望**           |                     **方差**                     |
| :-------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :------------------------: | :--------------------------------------------: |
|                       $\chi^2=x_1^2+x_2^2+...+x_n^2$                        |                                      $p(y)=\frac{1}{\Gamma(\frac{n}{2})2^{\frac{n}{2}}}y^{\frac{n}{2}-1}e^{-\frac{y}{2}}(y>0)$                                       |            $n$             |                      $2n$                      |
| $F=\frac{\frac{y_1^2+y_2^2+...+y_m^2}{m}}{\frac{x_1^2+x_2^2+...+x_n^2}{n}}$ | $p(y)=\frac{\Gamma(\frac{m+n}{2})(\frac{m}{n})^{\frac{m}{2}}}{\Gamma(\frac{m}{2})\Gamma(\frac{n}{2})}y^{\frac{m}{2}-1}·(1+\frac{m}{n}y)^{-\frac{m+n}{2}}$<br>$(y>0)$ | $\frac{n}{n-2}$<br>$(n>2)$ | $\frac{2n^2(m+n-2)}{m(n-2)^2(n-4)}$<br>$(n>4)$ |
|           $t=\frac{y_1}{\sqrt{\frac{x_1^2+x_2^2+...+x_n^2}{n}}}$            |                    $p(y)=\frac{\Gamma(\frac{n+1}{2})}{\sqrt{n\pi}\Gamma(\frac{n}{2})}(1+\frac{y^2}{n})^{-\frac{n+1}{2}}$<br>$(-\infty<y<+\infty)$                    |       $0$<br>$(n>1)$       |           $\frac{n}{n-2}$<br>$(n>2)$           |

***
### 卡方分布

设 $X_1,X_2,...,X_n$​ 为独立同分布，服从 $N(0,1)$。则称 $\chi_n^2=\sum\limits_{i=1}^nX_i^2$​ 服从自由度（即等式右端包含的独立变量的个数）为 $n$ 的 $\chi^2$ 分布，记 $\chi_n^2∼\chi^2(n)$。

$\chi^2$ 分布的密度函数（不要求）：

$$
f_{\chi^2}(x)=\frac{1}{\Gamma(\frac{n}{2})2^{\frac{n}{2}}}x^{\frac{n}{2}-1}e^{-\frac{x}{2}},x>0
$$

其中，$\Gamma(\alpha)=\int_0^{+\infty}x^{\alpha-1}e^{-x}dx$

!!! note "Gamma 函数的性质"

	其实是 vjf 就讲过的东西，但几乎全忘了（bushi
	
	- $\Gamma(\alpha+1)=\alpha\Gamma(\alpha)$
	- $\Gamma(n+1)=n!,\Gamma(\frac{1}{2})=\sqrt{\pi}$
	
	!!! tip "$\Gamma(\frac{1}{2})=\sqrt{\pi}$"
	
		$$
		\begin{aligned}
		\Gamma(\frac{1}{2})&=\int_0^{+\infty}x^{-\frac{1}{2}}e^{-x}dx=\int_{-\infty}^{+\infty}e^{-x^2}dx=I\\
		I^2&=\int_{-\infty}^{+\infty}e^{-x^2}dx\times\int_{-\infty}^{+\infty}e^{-y^2}dy=\int_{-\infty}^{+\infty}\int_{-\infty}^{+\infty}e^{-(x^2+y^2)}dxdy\\
		&=\int_0^{2\pi}d\theta\int_0^{+\infty}e^{-r^2}rdr=\pi
		\end{aligned}
		$$
		

![](../../../assets/Pasted%20image%2020241128103641.png)

$\chi^2$ 分布有如下性质：

- 设 $X∼\chi^2(n)$，则有 $E(X)=n$，$Var(X)=2n$；

	!!! note
		$$
		\begin{aligned}
		E(X^4)&=\int_{-\infty}^{+\infty}x^4\frac{1}{\sqrt{2\pi}}e^{-\frac{x^2}{2}}dx=2\int_0^{+\infty}x^4\frac{1}{\sqrt{2\pi}}e^{-\frac{x^2}{2}}dx\\
		&\stackrel{\frac{x^2}{2}=t}{\rightarrow}2\int_0^{+\infty}4t^2\frac{1}{\sqrt{2\pi}}e^{-t}\sqrt{2}\frac{1}{2\sqrt{t}}dt=\frac{4}{\sqrt{\pi}}\int_0^{+\infty}t^{\frac{3}{2}}e^{-t}dt\\
		&=\frac{4}{\sqrt{\pi}}\Gamma(\frac{5}{2})=\frac{4}{\sqrt{\pi}}\frac{3}{2}\Gamma(\frac{3}{2})=\frac{4}{\sqrt{\pi}}\frac{3}{2}\frac{1}{2}\Gamma(\frac{1}{2})=3\\
		D(X^2)&=E(X^4)-(E(X^2))^2=3-1=2
		\end{aligned}
		$$
		
- 设 $Y_1∼\chi^2(m)$，$Y_2∼\chi^2(n)$，且两者互相独立，则 $Y_1+Y_2∼\chi^2(m+n)$；
    - 这一性质被称为 $\chi^2$ 分布的可加性，可以推广到有限个相加的情形：$Y_i∼\chi^2(n_i),i=1,2,...,m$，并假设 $Y_1,Y_2,...,Y_m$ 相互独立，则 $\sum\limits_{i=1}^mY_i∼\chi^2(\sum\limits_{i=1}^mn_i)$
- $\chi^2$ 分布的上 $\alpha$ 分位数：  
    对于给定的正数 $\alpha,0<\alpha<1$，称满足条件 $P\{\chi^2>\chi_{\alpha}^2(n)\}=\int_{\chi_{\alpha}^2}^{+\infty}(n)f_{\chi^2}(x)dx=\alpha$ 的点 $\chi_{\alpha}^2(n)$ 为 $\chi^2(n)$ 分布的上 $\alpha$ 分位数；

![](../../../assets/Pasted%20image%2020241128110059.png)
***
### t 分布

设 $X∼N(0,1)$，$Y∼\chi^2(n)$，且 $X,Y$ 相互独立，则称随机变量 $T=\frac{X}{\sqrt{\frac{Y}{n}}​}$ 服从自由度为 $n$ 的 $t$ 分布，记做 $T∼t(n)$。

$t$ 分布的密度函数（不要求）：

$$
f_t(x)=\frac{\Gamma(\frac{n+1}{2})}{\sqrt{n\pi}\Gamma(\frac{n}{2})}(1+\frac{x^2}{n})^{-\frac{n+1}{2}}(-\infty<x<+\infty)
$$

![](../../../assets/Pasted%20image%2020241128111751.png)

$t$ 分布有如下性质：

- 设 $T∼t(n)$，则当 $n\geq 2$ 时，有 $E(T)=0$；当 $n\geq 3$ 时，有 $Var(T)=\frac{n}{n−2}$；
- 当 $n$ 足够大时，$t$ 分布近似于标准正态分布 $N(0,1)$；
- 设 $T∼t(n)$，$N∼N(0,1)$，则对任意的 $n\geq 1$，都存在 $a_0>0$，使得 $P(|T|\geq a_0)\geq P(|N|\geq a_0)$；
- $t_{1−\alpha}(n)=−t_{\alpha}(n)$；

![](../../../assets/Pasted%20image%2020241128111825.png)

***
### F 分布

设 $U∼\chi^2(n_1)$，$V∼\chi^2(n_2)$，且 $U,V$ 相互独立，则称随机变量 $F=\frac{\frac{U}{n_1}}{\frac{V}{n_2}}$ 服从自由度为 $(n_1,n_2)$ 的 $F$ 分布，记 $F∼F(n_1,n_2)$，其中 $n_1$ 为第一自由度，$n_2$ 为第二自由度。

$F$ 分布的密度函数（不要求）：

$$
f_F(x)=\frac{\Gamma(\frac{n_1+n_2}{2})(\frac{n_1}{n_2})^{\frac{n_1}{2}}}{\Gamma(\frac{n_1}{2})\Gamma(\frac{n_2}{2})}x^{\frac{n_1}{2}-1}·(1+\frac{n_1}{n_2}x)^{-\frac{n_1+n_2}{2}},x>0
$$

![](../../../assets/Pasted%20image%2020241128113929.png)

F 分布有如下性质：

- 设 $F∼F(n_1,n_2)$，则 $F^{−1}∼F(n_2,n_1)$；
- 设 $X∼t(n)$，则 $X^2∼F(1,n)$；
- $F_{1−\alpha}(n_1,n_2)=\frac{1}{F_{\alpha}(n_2,n_1)}$；

![](../../../assets/Pasted%20image%2020241128114546.png)
***
### 三大抽样分布表

- [卡方分布](https://www.obhrm.net/index.php/%E5%8D%A1%E6%96%B9%E5%88%86%E5%B8%83%E8%A1%A8_Chi-Square_Probabilities)
- [t 分布](https://en.wikipedia.org/wiki/Student%27s_t-distribution#Table_of_selected_values)
- [F 分布](https://blog.csdn.net/sinat_34439107/article/details/78577412)
***
## 正态总体下的抽样分布

设 $X_1,X_2,...,X_n$ 是来自正态总体 $N(\mu,\sigma^2)$ 的样本，$\overline{X}$ 是样本均值，$S^2$ 是样本方差，则有：

1. $\overline{X}∼N(\mu,\frac{\sigma^2}{n})$；
2. $\frac{(n−1)S^2}{\sigma^2}∼\chi^2(n−1)$；
3. $\overline{X}$ 与 $S^2$ 相互独立；
4. $\frac{\overline{X}−\mu}{\frac{S}{\sqrt{n}}}∼t(n−1)$；
5. 这里注意区别一下：$\frac{\overline{X}−\mu}{\frac{\sigma}{\sqrt{n}}}∼N(0,1)$；

设 $X_1,X_2,...,X_n$​​ 和 $Y_1,Y_2,...,Y_n$ 是分别来自正态总体 $N(\mu_1,\sigma_1^2)$ 和 $N(\mu_2,\sigma_2^2)$，并且它们相互独立，$\overline{X},\overline{Y}$ 是样本均值，$S_1^2,S_2^2$​ 是样本方差，则有：

1. $\frac{\frac{S_1^2}{\sigma_1^2}}{\frac{S_2^2}{\sigma_2^2}}∼F(n_1−1,n_2−1)$；
2. $\frac{(\overline{X}−\overline{Y})−(\mu_1−\mu_2)}{\frac{\sigma_1^2}{n_1}+\frac{\sigma_2^2}{n_2}}∼N(0,1)$；
3. 当 $\sigma_1^2=\sigma_2^2=\sigma^2$ 时：$\frac{(\overline{X}−\overline{Y})−(\mu_1−\mu_2)}{S_{\omega}\sqrt{\frac{1}{n_1}+\frac{1}{n_2}}}∼t(n_1+n_2−2)$，其中 $S_{\omega}^2=\frac{(n_1−1)S_1^2+(n_2−1)S_2^2}{n_1+n_2−2}$；