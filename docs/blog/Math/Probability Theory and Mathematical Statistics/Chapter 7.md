---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
---  

# Chapter 07 :  参数估计

> 参数：反映总体某方面特征的量

## 点估计

设总体 $X$ 的分布函数为 $F(x;\theta)$，$\theta=(\theta_1,\theta_2,...,\theta_k)$ 是未知的待估参数，$X_1,X_2,...,X_n$ 是 $X$ 的一个样本。点估计就是要对每一个未知参数 $\theta_i$ 构造一个适当的统计量 $\hat{\theta_i}=\hat{\theta_i}(X_1,X_2,...,X_n)$，用作对未知参数 $\theta_i$ 的估计，称为 $\theta_i$ 的**点估计量**。

若已知样本的观察值为 $x_1,x_2,...,x_n$，则称 $\hat{\theta_i}=\hat{\theta_i}(X_1,X_2,...,X_n)$ 为 $\theta_i$ 的一个**点估计值**。
***
### 矩法

思想：用样本矩去估计相应的总体矩，换言之，用原点矩 $A_k=\frac{1}{n}\sum\limits_{i=1}^nX_i^k$ 去估计 $\mu_k$，用中心矩$B_k=\frac{1}{n}\sum\limits_{i=1}^n(X_i-\overline{X})^k$ 去估计 $\nu_k$。

用原点矩估计 $\mu_k$ 具体步骤如下（假设有 $k$ 个待求未知参数，用中心矩同理）：

- 列出总体的前 $k$ 阶矩 $\mu_i=E(X^i)=h_i(\theta_1,\theta_2,...,\theta_k),i=1,2,...,k$
- 从方程组中解出这 $k$ 个参数 $\theta_i=g_i(\mu_1,\mu_2,...,\mu_k),i=1,2,...,k$
- 将上一步解出的参数的表达式中出现的总体矩用相应的样本矩替换$\hat{\theta_i}=g_i(A_1,A_2,...,A_k),i=1,2,...,k$

值得注意的是：

- 如果方程中存在恒等式，则可以顺延求 $\mu_{k+1},\mu_{k+2},...$
- 理论上任意 $k$ 个关于 $\mu_i$ 的方程组都可以，但考试要求前 $k$ 个才算对
***
### 极大似然法

思想：用“最像” $\theta$ 真值的值去估计 $\theta$，换言之，在参数空间中找一个 $\theta$，使得 $L(\theta)$ 达到最大。

具体步骤如下（若待估参数不止一个，则对每个待估参数 $\theta_i$ 均执行如下操作）：

- 构造似然函数 $L(\theta)=L(\theta;x_1,x_2,...,x_n)=\prod\limits_{i=1}^nf(x_i;\theta)$（对离散型变量则右侧为 $\prod\limits_{i=1}^np(x_i;\theta)$）
- 求解 $\theta$，使得 $L(\theta)$ 达到最大值，称这个 $\theta$ 为极大似然估计量，记作 $\hat{\theta}$

**求解似然函数最大值点**的常用方法：

- 解似然方程 $\frac{\partial L(\theta)}{\partial\theta_i}=0$，检验极大值点
- 或者也可以解对数似然方程 $\frac{\partial\ln⁡L(\theta)}{\partial\theta_i}=0$，检验极大值点
- 若 $L(\theta)$ 关于某个 $\theta_i$ 是单调的，则最大值在边界取得

极大似然估计法的性质：

- 不变原则：设参数 $\theta$ 的极大似然估计为 $\hat{\theta}$，若 $g(⋅)$ 为连续函数，则 $g(\theta)$ 的极大似然估计为 $g(\hat{\theta})$
***
## 估计量的评价准则

### 无偏性准则

若参数 $\theta$ 估计量 $\hat{\theta}=\theta(X_1,X_2,...,X_n)$ 的数学期望存在，且满足 $E(\hat{\theta})=\theta$，则称 $\hat{\theta}$ 是 $\theta$ 的一个**无偏估计量**或**无偏估计（Unbiased Estimation）**。

- 若 $E(\hat{\theta})\not=\theta$，则称 $|E(\hat{\theta})−\theta|$ 为估计量 $\hat{\theta}$ 的**偏差**
- 若 $\lim\limits_{n\rightarrow+\infty}E(\hat{\theta})=0$，则称 $\hat{\theta}$ 是 $\theta$ 的**渐进无偏估计（Asymptotic Unbiased Estimation）**
***
### 有效性准则

设 $\theta_1$ 和 $\theta_2$ 是参数 $\theta$ 的两个无偏估计，如果对于 $\forall\theta\in\Theta$，$Var(\theta_1)\leq Var(\theta_2)$，且不恒取等，则称 $\theta_1$ 比 $\theta_2$ **有效**。
***
### 均方误差准则

$E[(\hat{\theta}−\theta)^2]$ 是估计量 $\hat{\theta}$ 的**均方误差（Mean Square Error）**，记为 $Mse(\hat{\theta})$。

在均方误差准则下，估计量的均方误差越小越好。若 $Mse(\hat{\theta}_1)\leq Mse(\hat{\theta}_2)$ 且不恒取等，则称 $\hat{\theta}_1$ 优于 $\hat{\theta}_2$。

- 若 $\hat{\theta}$ 是参数 $\theta$ 的无偏估计量，则有 $Mse(\hat{\theta})=Var(\hat{\theta})$
- 均方误差有分解式 $E[(\hat{\theta}−\theta)^2]=Var(\hat{\theta})+(E(\hat{\theta})−\theta)^2$
- 均方误差准则常用于有偏估计量之间，或有偏估计量与无偏估计量之间的比较；实际应用中，有时均方误差准则比无偏性准则更加重要
***
### 相合性准则

若对于 $\forall\epsilon>0$，有 $\lim\limits_{n\rightarrow+\infty}P{|\hat{\theta}_n−\theta|<\epsilon}=1$，即 $\hat{\theta}_n\stackrel{P}{\rightarrow}\theta$，则称 $\hat{\theta}_n$ 是 $\theta$ 的相合估计量（Consistent Estimation）或一致估计量。

有如下定理：

- 设 $\hat{\theta}_n$ 是 $\theta$ 的一个估计量，若 $\lim\limits_{n\rightarrow+\infty}E(\hat{\theta})=\theta$，$\lim\limits_{n\rightarrow+\infty}Var(\hat{\theta}_n)=0$，则 $\hat{\theta}_n$ 是 $θ$ 的相合估计。
***
## 区间估计

**点估计**是由样本求出未知参数 $\theta$ 的一个估计值 $\hat{\theta}$，而**区间估计**则要由样本给出参数 $\theta$ 的一个估计范围，并指出该区间包含 $\theta$ 的可靠程度。

下面给出区间估计的一些基本概念：

- 置信区间：设总体 $X$ 的分布函数 $F(x;\theta)$ 含有一个未知参数 $\theta$，对于给定的值 $\alpha$，如果有两个统计量 $\theta_L=\theta_L(X_1,X_2,...,X_n)$，$\theta_U=\theta_U(X_1,X_2,...,X_n)$，$\theta_L<\theta_U$，使得 $P\{\theta_L(X_1,X_2,...,X_n)<\theta<\theta_U(X_1,X_2,...,X_n)\}\geq 1−\alpha,\forall\theta\in\Theta$，则称随机区间 $[\theta_L,\theta_U]$ 是 $\theta$ 的置信水平为 $1−\alpha$ 的**双侧置信区间**，简称**置信区间**
- 置信下限和置信上限：分别是 $\theta_L$ 和 $\theta_U$
- 置信度（置信水平）：$1−\alpha$
- 单侧置信区间：在置信区间的定义中，如果修改为 $P\{\theta_L(X1,X2,...,Xn)<θ\}\geq 1−\,\forall\theta\in\Theta$，则称随机区间 $[\theta_L,+\infty]$ 是 $\theta$ 的置信水平为 $1−\alpha$ 的**单侧置信区间**
    - 相应地，我们还可以定义单侧置信下限，以及具有单侧置信上限的单侧置信区间 $(−\infty,\theta_U)$

双侧置信区间和单侧置信区间的关系：

设 $\theta_L=\theta_L(X_1,X_2,...,X_n)$，$\theta_U=\theta_U(X_1,X_2,...,X_n)$ 分别是 $\theta$ 的置信水平为 $1−\alpha_1$ 和 $1−\alpha_2$ 的单侧置信下限及上限，且对于任何样本都满足 $\theta_L<\theta_U$，则 $(\theta_L,\theta_U)$ 是 $\theta$ 的置信水平为 $1−\alpha_1−\alpha_2$ 的双侧置信区间。