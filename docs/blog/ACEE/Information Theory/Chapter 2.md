---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
--- 

# Chapter 2 : 随机变量的熵和互信息

## 概率论基础

随机变量的概率空间 $\{X,\mathcal{X},q(x)\}$

- $\mathcal{X}$：$X$ 的取值空间，$\mathcal{X}=\{x_k;k=1,2,...,K\}$
- $q(x)$：事件 $\{X=x\}$ 发生的概率，$q(x)\geq 0$，$\sum_{x\in\mathcal{X}}q(x)=1$

联合变量对 $(X,Y)$，二维随机变量 $\{(X,Y),\mathcal{X}\times\mathcal{Y},p(x,y)\}$

- $p(x,y)=P\{X=x,Y=y\}$
- $\mathcal{X}=\{x_k;k=1,2,...,K\}$，$\mathcal{Y}=\{y_j;j=1,2,...,J\}$
- $p(x_k,y_j)\geq 0$，$\sum_k\sum_j(x_k,y_j)=1$
- $\sum_k p(x_k,y_j)=\omega(y_j)$，$\sum_j p(x_k,y_j)=q(x_k)$

!!! note "条件概率"

	$$
	p(x|y)=\frac{p(x,y)}{\omega(y)},\quad p(y|x)=\frac{p(x,y)}{q(x)}
	$$
	
***
## 事件的自信息

!!! note ""

	自信息：事件发生后提供的信息量

> 信息量是信息论的重要概念，事件的信息量基于该事件发生的概率

定义：对于概率空间 $\{X,\mathcal{X},q(x)\}$，事件 $\{X=x_k\}$ 的自信息定义为 $I(x_k)=-\log_a q(x_k)$

- 当 $a=2$ 时，信息量的单位是比特（bit）；当 $a=e$ 时，信息量的单位是纳特（nat）
	- 这便是信息所谓比特的来源

定义为概率的负对数的优点：

- 符合**概率越小，信息量越大**的要求
- 对数函数是比较简单的函数，**容易进行数学处理**，
- **对数函数的可加性**符合生活中关于**信息可叠加性**的经验

!!! note "事件自信息的本质"

	- 事件发生后对外界（观察者）所提供的信息量
	- 事件发生前外界（观察者）为确证该事件的发生所需要的信息量，也是外界为确证该事件所需要付出的代价
	- 事件的自信息并不代表事件的不确定性，事件本身没有不确定性可言，它要么是观察的假设和前提，要么是观察的结果

事件自信息的性质：

- $q(x_k)$ 越大，$I(x_k)$ 越小，概率越小的事件其自信息越大
	- e.g. 某一个城市的天气经常下雨，即下雨天的概率比较大，那么当该城市气象台预报第二天将要降雨的时候，此时信息量比较小；相反，如果预报第二天是个晴天的时候，此时这个信息的信息量是比较大的
- $q(x_k)=1,I(x_k)=0$，确定事件的自信息为 0
	- e.g. “明天的最低气温低于100度”这句话的信息量几乎为 0，因为该事件发生的概率基本为 1
- $q(x_k)\rightarrow 0,I(x_k)=\infty$
	- “张三买彩票中了 500 万”，这句话的信息量是巨大的，因为中彩票头的概率基本上趋向于 0
***
### 事件的条件自信息

对于二维随机变量 $\{(X,Y),\mathcal{X}\times\mathcal{Y},p(x,y)\}$，事件 $Y=y_j$ 发生后，事件 $X=x_k$ 的条件自信息为$I(x_k|y_j)=-\log p(x_k|y_j)$

!!! note "事件条件自信息的本质"

    - 事件 $Y=y_j$ 发生后，事件 $X=x_k$ 再发生需要新的信息量
    - 事件 $Y=y_j$ 发生后，事件 $X=x_k$ 再发生提供给观察者的信息量

!!! example "Example"

	=== "Example 01"
	
		- $x_k$：杭州下雨，$y_j$：上海下雨
		- $I(x_k)$：杭州下雨需要的信息量，$I(x_k|y_j)$：上海下雨后杭州下雨需要的信息量
		- $q(x_k)=0.5,p(x_k|y_j)=0.75$，则 $I(x_k)=1\text{bit},I(x_k|y_j)=\log_2(\frac{4}{3})\text{bit},I(x_k)>I(x_k|y_j)$
	
	=== "Example 02"
	
		- $x_k$：杭州下雨，$y_j$：上海晴天
		- $I(x_k)$：杭州下雨需要的信息量，$I(x_k|y_j)$：上海晴天时杭州下雨需要的信息量
		- $q(x_k)=0.5,p(x_k|y_j)=0.25$，则 $I(x_k)=1\text{bit},I(x_k|y_j)=2\text{bit},I(x_k)<I(x_k|y_j)$
	
	=== "Example 03"
	
		- （无关事件）$x_k$：杭州下雨，$y_j$：北京下雨
		- $I(x_k)=I(x_k|y_j)$
***
### 事件的联合自信息

对于二维随机变量 $\{(X,Y),\mathcal{X}\times\mathcal{Y},p(x,y)\}$，事件 $(X,Y)=(x_k,y_j)$ 的联合自信息为：$I(x_k,y_j)=-\log p(x_k,y_j)$，表示事件 $\{X=x_k\}$ 和 $\{Y=y_j\}$ 同时发生需要的信息量，或者同时发生后对外界提供的信息量
***
## 事件的互信息

!!! note ""

	互信息：相互之间提供的信息量

**互信息**是衡量两个随机变量之间的相关性的重要指标，定义为：

$$
I(x_k;y_j)=I(x_k)-I(x_k|y_j)=-\log q(x_k)-\{-\log p(x_k,y_j)\}=\log\frac{p(x_k,y_j)}{q(x_k)\omega(y_j)}
$$

显然可以看出，互信息有对称性 $I(x_k;y_j)=I(y_j;x_k)$

- 事件的互信息的本质：事件 $\{Y=y_j\}$ 发生后对事件 $\{X=x_k\}$ 不确定性的降低，大于 0 表示不确定性降低；小于 0 表示不确定性增加

!!! example "Example"

	=== "Example"
	
		- $x_k$：杭州下雨，$y_j$：上海下雨
		- $I(x_k)$：杭州下雨需要的信息量，$I(x_k|y_j)$：上海下雨后杭州下雨需要的信息量
		- $q(x_k)=0.5,p(x_k|y_j)=0.75$，则 $I(x_k)=1\text{bit},I(x_k|y_j)=\log_2(\frac{4}{3})\text{bit},I(x_k;y_j)>0$
	
	=== "Example 02"
	
		- $x_k$：杭州下雨，$y_j$：上海晴天
		- $I(x_k)$：杭州下雨需要的信息量，$I(x_k|y_j)$：上海晴天时杭州下雨需要的信息量
		- $q(x_k)=0.5,p(x_k|y_j)=0.25$，则 $I(x_k)=1\text{bit},I(x_k|y_j)=2\text{bit},I(x_k;y_j)<0$
	
	=== "Example 03"
	
		- （无关事件）$x_k$：杭州下雨，$y_j$：北京下雨
		- $I(x_k)=I(x_k|y_j),I(x_k;y_j)=0$
***
### 事件的条件互信息

在给定事件 $Z=z$ 的条件下，事件 $X=x$ 和事件 $Y=y$ 的条件互信息为：

$$
I((x;y)|z)=I(x|z)-I(x|(y,z))=\log\frac{p(x|(y,z))}{q(x|z)}=\log\frac{p(x,y|z)}{q(x|z)\omega(y|z)}
$$

表示 $Z=z$ 发生时，事件 $X=x$ 和事件 $Y=y$ 相互之间提供的信息量

!!! example "Example"

	- $x$：杭州下雨，$y$：上海下雨，$z$：宁波下雨
	- $q(x)=q(y)=q(z)=0.125$
	- $p(x|y)=p(x|z)=p(y|z)=0.25$
	- $p(x|y,z)=0.5$
	- $I(x)=3\text{bit},I(x|y)=2\text{bit},I(x;y)=1\text{bit},I(x;y|z)=1\text{bit}$
***
### 事件的联合互信息

联合事件 $\{Y=y,Z=z\}$ 与事件 $\{X=x\}$ 之间的互信息为:

$$I(x;(y,z))=\log\frac{p(x|y,z)}{q(x)}=\log\frac{p(x,y,z)}{q(x)\omega(y,z)}$$

表示事件 $\{Y=y,Z=z\}$ 联合提供给事件 $\{X=x\}$ 的信息量

!!! example "Example"

	- $x$：杭州下雨，$y$：上海下雨，$z$：宁波下雨
	- $I(x)$：杭州下雨需要的信息量，$I(x;y,z)$：上海下雨和宁波下雨这两个事件同时给杭州下雨这个事件的信息量
	- $q(x)=0.125;p(x|y)=0.25$，则 $I(x;y)=I(x)-I(x|y)=1$
	- $p(x|y,z)=0.5$，则 $I(x;y,z)=I(x)-I(x|y,z)=2>I(x;y)$

!!! note "链式法则"
	
	$$
	I(x;(y,z))=I(x;y)+I(x;z|y)
	$$
	
	事件 $\{Y=y,Z=z\}$ 联合发生后对事件 $\{X=x\}$ 的信息量等于事件 $\{Y=y\}$ 对事件 $\{X=x\}$ 的信息量加上事件 $\{Y=y\}$ 已知的前提下，事件 $\{Z=z\}$ 提供给事件 $\{X=x\}$ 的信息量
	
	??? note "Proof"
	
		$$
		\begin{aligned}
		I(x;y,z)&=\log\frac{p(x|y,z)}{p(x)}=\log\frac{p(x|y)p(x|y,z)}{p(x)p(x|y)}\\
		&=\log\frac{p(x|y)}{p(x)}+\log\frac{p(x|y,z)}{p(x|y)}\\
		&=I(x;y)+I(x;z|y)
		\end{aligned}
		$$
		
***
## 随机变量的熵

> 熵：变量的不确定性

**熵**是衡量随机变量不确定性的重要指标，定义为随机变量各个事件的平均自信息：

$$
H(X)=E[I(X)]=\sum_{x\in\mathcal{X}}q(x)I(x)=-\sum_{x\in\mathcal{X}}q(x)\log q(x)
$$

- 熵与自信息的区别：熵针对的是随机变量，自信息针对具体的事件

!!! example "Example"

    二元随机变量 $X$ 的概率分布 $q(x_1)=p,q(x_2)=1-p$，则 $X$ 的熵为：
	
    $$
    H(X)=-p\log p-(1-p)\log(1-p)
    $$
	
    当 $p=0.5$ 时，$H(X)=1$，表示 $X$ 的不确定性最大，即等概率变量的随机性最大，所以熵最大；当 $p=0$ 或 $p=1$ 时，$H(X)=0$，表示 $X$ 的不确定性最小，即确定性变量的熵为 0。
***
### 联合熵

对于二维随机变量 $\{(X,Y),\mathcal{X}\times\mathcal{Y},p(x,y)\}$，事件 $(X,Y)$ 的联合熵为：

$$H(X,Y)=-\sum_{x\in\mathcal{X}}\sum_{y\in\mathcal{Y}}p(x,y)\log p(x,y)$$

表示随机变量 $X$ 和 $Y$ 联合发生后的不确定性

!!! note "链式法则"

	$$
	H(X,Y)=H(X)+H(Y|X)=H(Y)+H(X|Y)
	$$
	
	随机变量 $X$ 和 $Y$ 联合发生后的不确定性等于随机变量 $X$ 的不确定性加上在给定 $X$ 的条件下随机变量 $Y$ 的不确定性。
	
	当 $X$ 和 $Y$ 统计独立时，$H(X,Y)=H(X)+H(Y)$
	
	- 在三元情况下，$H(X,Y,Z)=H(X)+H(Y,Z|X)=H(X)+H(Y|X)+H(Z|X,Y)$
	
	??? note "Proof"
	
		$$
		\begin{aligned}
		H(X,Y)&=E[I(X,Y)]=-\sum\limits_{x\in\mathcal{X}}\sum\limits_{y\in\mathcal{Y}}p(x,y)\log p(x,y)\\
		&=-\sum\limits_{x\in\mathcal{X}}\sum\limits_{y\in\mathcal{Y}}p(x,y)\log p(x)-\sum\limits_{x\in\mathcal{X}}\sum\limits_{y\in\mathcal{Y}}p(x,y)\log p(y|x)\\
		&=H(X)+H(Y|X)
		\end{aligned}
		$$
		
***
### 条件熵

在给定事件 $Y=y$ 的条件下，事件 $X$ 的条件熵为：

$$
H(X|Y=y)=-\sum_{x\in\mathcal{X}}p(x|y)\log p(x|y)
$$

或者也可定义为：

$$
H(X|Y)=E\{H(X|y)\}=-\sum\limits_{x\in\mathcal{X}}\sum\limits_{y\in\mathcal{Y}}p(x,y)\log p(x|y)
$$

- 从第二个定义我们可以看出，当 $X$ 和 $Y$ 统计独立时，$H(X|Y)=H(X)$

!!! example "Example"

	随机变量 $X=1$ 表示杭州下雨，$X=0$ 表示杭州不下雨；$Y=1$ 表示上海下雨，$Y=0$ 表示上海不下雨
	
	设 $p(x=1)=0.5;p(x=0)=0.5;p(1|1)=0.75,p(0|1)=0.25$，则 $H(X|Y=1)<H(X)$
	
	$p(X=1)=0.25; p(X=0)=0.75; p(1|1)=0.5, p(0|1)=0.5$，则 $H(X|Y=1)>H(X)$
***
### 熵的性质

对于随机变量 $X$ ，如果

$$\mathbb{X}=\begin{pmatrix}x_1&x_2&\cdots&x_K\\p_1&p_2&\cdots&p_K\end{pmatrix}$$

则有：

$$
H(X)\triangleq H_K({p_1,p_2,\cdots,p_K})\triangleq H_K(P)=-\sum_{k=1}^Kp_k\log p_k
$$

- $H_K(P)$ 对概率矢量 $P$ 的分量是**对称的**，即 $H_K(P)$ 对 $p_1,p_2,\cdots,p_K$ 的排列是不变的——$p_1,p_2,\cdots,p_K$ 的排列不同，$H_K(P)$ 的值不变
- **非负性**：$H(X)\geq 0$
- **确定性**：$H(X)=0$ 当且仅当 $X$ 是**确定性**的随机变量，即 $X$ 的取值只有一个
- **可扩展性**：$\lim\limits_{\epsilon\to 0}H_{K+1}(P_1,P_2,\cdots,P_K-\epsilon,\epsilon)=H_K(P_1,P_2,\cdots,P_K)$ —— 在增加一个概率接近于零的事件时，总熵几乎不变
- **可加性**：$H(X_2)|_{X_2\in\mathcal{X}_2}=H(X_1)|_{X_1\in\mathcal{X}_1}+H(X_2|X_1)|_{X_2\in\mathcal{X}_2}^{X_1\in\mathcal{X}_1}$

!!! note "可加性"

	- $H(X_1)|_{X_1\in\mathcal{X}_1} = H(P(A), P(B))$
	- $H(X_2)|_{X_2\in\mathcal{X}_2} = H(P(A)P_{A_1}, P(A)P_{A_2}, P(A)P_{A_3}, P(B)P_{B_1}, P(B)P_{B_2})$
	- $H(X_2 | X_1)|_{X_2\in\mathcal{X}_2}^{X_1\in\mathcal{X}_1}=\sum\limits_{x_1\in\mathcal{X}_1}P(x_1)H(X_2|x_1)=P(A) H(P_{A_1}, P_{A_2}, P_{A_3}) + P(B) H(P_{B_1}, P_{B_2})$
	
	对变量 X 可以进行多步分层的观察，每一步都可从上一步的观察结果中得到更为细致的结果，变量 X 在最后的观察结果集合中的不确定性等于第一次观察结果的不确定性，加上其后每次观察结果在前一次观察结果已知的前提下的条件不确定性
	
	多元形式：
	
	$$
    \begin{aligned}
    H_M &= -\sum_{k=1}^K \sum_{j=1}^{m_k} p_k q_{jk} \log (p_k q_{jk}) \\
    &= -\sum_{k=1}^K \sum_{j=1}^{m_k} p_k q_{jk} \log p_k - \sum_{k=1}^K \sum_{j=1}^{m_k} p_k q_{jk} \log q_{jk} \\
    &= -\sum_{k=1}^K p_k \log p_k \sum_{j=1}^{m_k} q_{jk} - \sum_{k=1}^K p_k \sum_{j=1}^{m_k} q_{jk} \log q_{jk} \\
    &= -\sum_{k=1}^K p_k \log p_k - \sum_{k=1}^K p_k \sum_{j=1}^{m_k} q_{jk} \log q_{jk} \\
    &= H_K(p_1, p_2, \cdots, p_K) + \sum_{k=1}^K p_k H_{m_k}(q_{1k}, q_{2k}, \cdots, q_{m_k k})
    \end{aligned}
    $$
    

- **极值性**：$H_K(p_1,p_2,\cdots,p_k)\leq H_K(\frac1K,\frac1K,\cdots,\frac1K) =  \log K$，当且仅当 $X$ 是**均匀分布**时取等号。

??? note "Proof"

	$H_K(p_1,p_2,...,p_K)\leq -\sum\limits_{k=1}^Kp_k\log q_k$ 对任何概率矢量 $\pmb{q}$ 均成立。因为：
	
	$$
	\begin{aligned}
	H_K(p_1,p_2,...,p_K)+\sum\limits_{k=1}^Kp_k\log q_k&=\sum\limits_{k=1}^Kp_k\log\frac{q_k}{p_k}\\
	&\leq\log e·\sum\limits_{k=1}^Kp_k(\frac{q_k}{p_k}-1)(\text{由}\ln x\leq x-1)\\
	&=0(q_k=\frac{1}{K},k=1,2,...,K)
	\end{aligned}
	$$
	

- **条件熵小于等于熵**：$H(X|Y)\leq H(X)$——增加条件，减少不确定性。当且仅当 X 和 Y 独立时取等号

??? note "Proof"

	$$
    \begin{aligned}
    H(p_1,p_2,...,p_K)&\leq -\sum\limits_{k=1}^Kp_k\log q_k\\
    H(X|Y) &= E \{H(X|y)\} = -\sum_{x \in \mathcal{X}} \sum_{y \in \mathcal{Y}} P(x, y) \log P(x|y) \\
    &= -\sum_{y \in \mathcal{Y}} \omega(y) \left\{\sum_{x \in \mathcal{X}} P(x|y) \log P(x|y)\right\} \\
    &\leq -\sum_{y \in \mathcal{Y}} \omega(y) \left\{\sum_{x \in \mathcal{X}} P(x|y) \log P(x)\right\} \\
    &= -\sum_{x \in \mathcal{X}} \left\{\sum_{y \in \mathcal{Y}} P(x|y) w(y)\right\} \log P(x) \\
    &= -\sum_{x \in \mathcal{X}} \left\{\sum_{y \in \mathcal{Y}} P(x,y)\right\} \log P(x) \\
    &= -\sum_{x \in \mathcal{X}} P(x) \log P(x) \\
    &= H(X)
    \end{aligned}
    $$
	

- **凸性**：$H(X)$是严格上凸函数， $H(\lambda \vec{P_1}+(1-\lambda)\vec{P_2})\geq \lambda H(\vec{P_1})+(1-\lambda)H(\vec{P_2}),\quad 0\leq \lambda\leq 1$

!!! note "取极大值的充要条件"

	Jensen不等式：
	
	$$
	\begin{aligned}
		&\text{令 } (\alpha_1, \alpha_2, \cdots, \alpha_L) \text{ 是凸集中的一组矢量，} f(\alpha) \text{ 是该凸集上的一个上凸函数，} \\
		&(\theta_1, \theta_2, \cdots, \theta_L) \text{ 是一组概率分布，则有} \\
		&\sum_{l=1}^L \theta_l f(\alpha_l) \leq f \left( \sum_{l=1}^L \theta_l \alpha_l \right)
	\end{aligned}
	$$

	首先我们有
	
	![](../../../assets/Pasted image 20250302205411.png)
	
	!!! note "怎么理解？"
		注意到，此时每个分量为非负。我们要找到极值，就是让这个函数在邻域内的值都比它小。
		
		如果 $\alpha_k$ 大于零，那么这个偏导数一定要为零，否则必定在这个方向或反方向上有增大的空间。-->如果我们增大或减小 $\alpha_k$，那么这个函数的值会增大。
		
		如果 $\alpha_k$ 等于零，那么这个偏导数需要小于或等于零。如果大于零，必定在这个方向上有增大的空间。-->如果我们增大 $\alpha_k$，那么这个函数的值会增大。
		
	把这个移作概率空间。除了要求非负，还要求和为1。所以我们用拉式乘子法，构造函数：
	
	$$
	L(P,\lambda)=H(P)+\lambda(1-\sum_{k=1}^Kp_k)
	$$
	
	求偏导，有：
	
	$$
	\begin{cases}
	\frac{\partial L}{\partial p_k}=\frac{\partial f(P)}{\partial p_k}-\lambda=0\\
	\frac{\partial L}{\partial \lambda}=1-\sum\limits_{k=1}^Kp_k=0
	\end{cases}
	$$
	
	根据前文的解释，我们有：
	
	$$
	\begin{cases}
	\frac{\partial f(P)}{\partial p_k}=\lambda\qquad p_k > 0\\
	\frac{\partial f(P)}{\partial p_k}\leq \lambda\qquad p_k = 0
	\end{cases}
	$$
	
***




