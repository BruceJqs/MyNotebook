---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
--- 

# Chapter 09 : 常微分方程模型

## 追逐问题

??? question "问题描述"

	两艘船在平静的海面上相向而行，海盗船的速度为 $v_p$，商船的速度为 $v_m$
	
	- 两船速度不变。
	- 海盗船的航向始终指向商船。
	
	问：海盗船是否能追上商船？追上时，两船的位置分别在哪里？

### 两船速度不变

![](../../../assets/Pasted%20image%2020241221211450.png)

若在某一时刻，海盗船与商船位于同一地点 $A(x,y)$，则 $\frac{|AO|}{|MO|}=k$，即 $\frac{\sqrt{x^2+y^2}}{(x−m)^2+y^2}=k$

所以 A 的轨迹为圆（阿波罗尼斯圆）：$(x-\frac{k^2m}{k^2-1})^2+y^2=(\frac{km}{k^2-1})^2$
***
### 两船速度不变，一船方向改变

**商船沿直线**航行，航向垂直于连接商船与海盗船初始位置的直线。在任意时刻，**海盗船的航行方向**为连接商船与海盗船此时位置的直线的方向。

以海盗船初始位置为原点，商船初始位置为 $M(m,0)$，建立直角坐标系，记 $\frac{v_m}{v_p}=r$。设海盗船在与商船相遇前的轨迹为函数 $y=f(x)$，则

![](../../../assets/Pasted%20image%2020241221213654.png)

在 $t$ 时刻

- 商船位置 $M_t(m,v_mt)$，海盗船位置 $P_t(x(t),y(t))$
- 连接海盗船与商船当前位置的直线斜率为 $\frac{y−v_mt}{x−m}=f'(x)$
    - 直线方程为 $y−v_mt=f'(x)(x−m)$
- 海盗船的轨迹自原点至 $P_t$ 的弧长为 $v_pt=\int_0^x\sqrt{1+f'^2(z)}dz$

所以，我们可以得到：

$$
\frac{1}{v_p}\int_0^x\sqrt{1+f'^2(z)}dz=t=\frac{1}{v_m}(y-(x-m)f'(x))
$$

对两边求导，我们有：

$$
\begin{aligned}
\frac{1}{v_p}\sqrt{1+f'^2(x)}&=\frac{1}{v_m}(f'(x)-f'(x)-(x-m)f''(x))\\
-\frac{v_m}{v_p}\sqrt{1+f'^2(x)}&=(x-m)f''(x)\\
\frac{df'(x)}{\sqrt{1+f'^2(x)}}&=-\frac{r}{x-m}dx\\
\ln|f'(x)+\sqrt{1+f'^2(x)}||_0^x&=-r\ln|x-m||_0^x\\
\Rightarrow\ln|f'(x)+\sqrt{1+f'^2(x)}|&=-r\ln|1-\frac{x}{m}|\\
\Rightarrow f'(x)+\sqrt{1+f'^2(x)}&=(1-\frac{x}{m})^{-r}
\end{aligned}
$$

对两边取倒数，我们有：

$$
\begin{cases}
f'(x)+\sqrt{1+f'^2(x)}=(1-\frac{x}{m})^{-r}\\
f'(x)-\sqrt{1+f'^2(x)}=(1-\frac{x}{m})^r
\end{cases}
$$

因此 $f'(x)=\frac{1}{2}((1-\frac{x}{m})^{-r}-(1-\frac{x}{m})^r)$

再对两边积分，有 $f(x)=\frac{rm}{1-r^2}+\frac{m-x}{2}(\frac{1}{1+r}(1-\frac{x}{m})^r-\frac{1}{1-r}(1-\frac{x}{m})^{-r})$

所以追上时的纵坐标为 $f(m)=\frac{rm}{1-r^2}$

!!! example "Example-Putnam 1959 A-5"

	=== "Question"
	
		A sparrow, flying horizontal in a straight line, is 50 feet directly below an eagle and 100 feet directly above a hawk. Both hawk and eagle fly directly toward the sparrow, reaching it simultaneously. The hawk flies twice as fast as the sparrow. How far does each bird fly? At what rate does the eagle fly?
	
	=== "Answer"
	
		- $v_h=2v_s,m_h=2m_e$
		- 鹰与鹫同时抓到麻雀，故 $f_h(m_h)=f_e(m_e)$，即：
		
		$$
		\frac{r_hm_h}{1-r_h^2}=\frac{r_em_e}{1-r_e^2}\Rightarrow\frac{2m_h}{3}=\frac{r_em_e}{1-r_e^2}\Rightarrow\frac{4}{3}=\frac{r_e}{1-r_e^2}\Rightarrow r_e=\frac{\sqrt{73}-3}{8}
		$$
		
		- 飞行距离 $l_s=f_h(m_h)=\frac{2}{3}m_h=\frac{200}{3},l_h=\frac{l_s}{r_h}=\frac{400}{3},l_e=\frac{l_s}{r_e}=\frac{400}{3}·\frac{\sqrt{73}+3}{16}$
***
## 最速降线问题

??? question "问题描述"

	给定垂直平面上两点 A,B，一质点以何路径从 A 运动到 B，可使运动时间最短？

### 直线下降

- 给定垂直平面上两点 A,B，一质点沿连接 A,B 的直线轨道从 A 运动到 B，求该质点的运动时间 $T$（不计阻力）
	- 以 $A$ 为坐标原点，水平方向为 $x$ 轴，垂直方向为 $y$ 轴，建立直角坐标系。B 点坐标为 $(x_B,y_B),x_B\geq 0,y_B>0$。线段 $AB$ 与 $y$ 轴正向夹角为 $\theta$

![](../../../assets/Pasted%20image%2020241221215728.png)

即斜坡下滑问题，有 $\frac{1}{2}g\cos\theta T^2=l$，因此 $T=\sqrt{\frac{2l}{g\cos\theta}}=\sqrt{\frac{2\sqrt{x_B^2+y_B^2}}{g\frac{y_B}{\sqrt{x_B^2+y_B^2}}}}=\sqrt{\frac{2(x_B^2+y_B^2)}{gy_B}}$

!!! note "常微分方程解法"

	设质点开始运动时刻为 0 时刻。$t$ 时刻质点位于 $(x(t),y(t))$，速率为 $v(t)$，方向与 AB 平行。垂直方向速度分量大小为 $v(t)\cos\theta$
	
	质点在下降过程中，势能全部转化为动能，$\frac{1}{2}mv^2(t)=mgy(t)$，即有 $v(t)=\sqrt{2gy(t)}$
	
	由质点在垂直方向的速度与距离关系 $y(t)=\int_0^tv(z)\cos\theta dz=\int_0^t\sqrt{2gy(z)}\cos\theta dz$
	
	那么有：
	
	$$
	\begin{aligned}
	y'(t)=\sqrt{2gy(t)}\cos\theta&\Rightarrow\frac{y'(t)}{\sqrt{y(t)}}=\sqrt{2g}\cos\theta\Rightarrow 2\sqrt{y(t)}|_0^T=\sqrt{2g}\cos\theta|_0^T\\
	&\Rightarrow 2y_B=T\sqrt{2g}\cos\theta\Rightarrow T=\sqrt{\frac{2(x_B^2+y_B^2)}{gy_B}}
	\end{aligned}
	$$
	
***
### 圆弧下降

- 一质点沿圆心为 $C(0,R)$，半径为 $R$ 的圆弧轨道从 $A(0,0)$ 运动到 $B(R,R)$，求该质点的运动时间 $T$（不计阻力）

![](../../../assets/Pasted%20image%2020241221221045.png)

- 设质点开始运动时刻为 0 时刻。$t$ 时刻质点所在位置与圆心的连线与 $x$ 轴的夹角为 $\theta(t)$，速率为 $v(t)$
- $t$ 时刻，质点纵坐标为 $R\sin\theta(t)$，质点运动过的距离为 $R\theta$
- 由能量守恒，$\frac{1}{2}mv^2(t)=mgR\sin\theta(t)$

那么有：

$$
\begin{aligned}
R\theta'(t)&=v(t)=\sqrt{2gR\sin\theta(t)}\Rightarrow\frac{\theta'(t)}{\sqrt{\sin\theta(t)}}=\sqrt{\frac{2g}{R}}\\
\int_0^{\frac{\pi}{2}}\frac{d\varphi}{\sqrt{\sin\varphi}}&=\int_0^T\frac{\theta'(t)}{\sqrt{\sin\theta(t)}}=\int_0^T\sqrt{\frac{2g}{R}}dt=\sqrt{\frac{2g}{R}}T\\
\therefore T&=\sqrt{\frac{R}{2g}}\int_0^{\frac{\pi}{2}}\frac{d\varphi}{\sqrt{\sin\varphi}}\approx 1.8541\sqrt{\frac{R}{g}}
\end{aligned}
$$

- 最后一个约等于用到了椭圆积分
***
### 最速降线

#### Fermat 原理

- 光线在两点之间传播的路径是使得两点之间的传播时间最短的路径
***
#### Snell 定律

设光在点 $A,B$ 所在介质中的传播速度分别为 $v_1,v_2$，$A,B$ 与两介质交界面的垂直距离分别为 $h_1,h_2$，$A,B$ 间的水平距离为 $d$

设光经过交界面上与 $A$ 水平距离为 $x$ 的点，光传播所需时间为 $T(x)=\frac{\sqrt{h_1^2+x^2}}{v_1}+\frac{\sqrt{h_2^2+(d-x)^2}}{v_2}$，那么有：

$$
\begin{aligned}
T'(x)=\frac{1}{v_1}\frac{x}{\sqrt{h_1^2+x^2}}&+\frac{1}{v_2}\frac{-(d-x)}{\sqrt{h_2^2+(d-x)^2}}=0\\
\Rightarrow\frac{1}{v_1}\frac{x}{\sqrt{h_1^2+x^2}}&=\frac{1}{v_2}\frac{d-x}{\sqrt{h_2^2+(d-x)^2}}\\
\Rightarrow\frac{\sin\theta_1}{\sin\theta_2}&=\frac{\frac{x}{\sqrt{h_1^2+x^2}}}{\frac{d-x}{\sqrt{h_2^2+(d-x)^2}}}=\frac{v_1}{v_2}
\end{aligned}
$$

![](../../../assets/Pasted%20image%2020241221222951.png)
***
#### 推导最速降线

将平行于 x 轴的直线视作折射率逐渐减小的不同介质的分界面

![](../../../assets/Pasted%20image%2020241221222929.png)

由 Snell 定律，可知 $\frac{\sin\theta}{v}$ 为常数，记 $\frac{\sin\theta}{v}=C$，我们有：

$$
\begin{aligned}
\sin\theta=\cos\varphi&=\frac{1}{\sqrt{1+\tan^2\varphi}}=\frac{1}{\sqrt{1+y'^2}}\\
\frac{1}{2}mv^2=mgy&\Rightarrow v=\sqrt{2gy}
\end{aligned}
$$

所以：

$$
\begin{aligned}
\frac{\sin\theta}{v}&=\frac{1}{\sqrt{1+y'^2}}\frac{1}{\sqrt{2gy}}=C\\
\Rightarrow y'&=\sqrt{\frac{1-2gCy}{2gCy}}\triangleq\sqrt{\frac{C_2-y}{y}}\\
&\Rightarrow \sqrt{\frac{y}{C_2-y}}dy=dx
\end{aligned}
$$

令 $y=C_2\sin^2\beta$，有 $2C_2\sin^2\beta d\beta=dx\Rightarrow dx=C_2(1-\cos 2\beta)d\beta$

因此 $\begin{cases}x=R(\gamma-\sin\gamma)\\y=R(1-\cos\gamma)\end{cases}$，或者 $x=R\arccos(1-\frac{y}{R})-\sqrt{y(2R-y)}$
***
### 摆线

> 实际上，最速降线就是摆线

- 摆线即为平面上的一个圆沿一条直线（准线）作无滑动的滚动时，圆上一点的轨迹
	- 以准线为 $x$ 轴，起始位置的圆与准线的切点为原点，建立直角坐标系
	- 圆滚动角度为 $\beta$ 时，圆与准线的切点坐标为 $(R\beta,0)$
	- $x=R(\beta-\sin\beta),y=R(1-\cos\beta)$
- 圆滚过一周时旋轮线的弧长与围成的面积
	
	$$
	\begin{aligned}
	L&=\int_0^{2\pi}\sqrt{x'^2(\beta)+y'^2(\beta)}d\beta=R\int_0^{2\pi}\sqrt{(1-\cos\beta)^2+(\sin\beta)^2}d\beta\\
	&=R\int_0^{2\pi}\sqrt{2-2\cos\beta}d\beta=2R\int_0^{2\pi}\sin\frac{\beta}{2}d\beta=4R\cos\frac{\beta}{2}|_0^{2\pi}=8R
	\end{aligned}
	$$
	
	$$
	S=\int_0^{2\pi R}y(x)dx=R^2\int_0^{2\pi}(1-\cos\beta)^2d\beta=3\pi R^2
	$$
	
***
### 变分法

> 变分法是研究泛函的极值的方法，也是求出最速降线的严格做法

对于最速降线来说，有：

$$
\begin{aligned}
v(t)&=\frac{\sqrt{(dx)^2+(dy)^2}}{dt}=\frac{dx\sqrt{1+y'^2(x)}}{dt}\\
\Rightarrow dt&=\frac{\sqrt{(dx)^2+(dy)^2}}{v(t)}=\frac{\sqrt{1+y'^2(x)}}{\sqrt{2gy}}dx\\
\Rightarrow T&=\int_0^{x_B}\sqrt{\frac{1+y'^2(x)}{2gy}}dx
\end{aligned}
$$

> 可以用 Euler-Lagrange 方程求解
***
## 生物数学模型

### 种群数量变化模型

#### 指数增长模型

我们给出假设：

- 环境承载容量无限，所有个体独立生活，彼此间不存在竞争
- 种群处于封闭（Closed）状态，不存在迁入（Immigration）和迁出（Emigration）
- 记人均出生/死亡/增长率为：$b,\mu,r=b−\mu$
    - 存在常数 $b$ 和 $\mu$，对任意 $t$ ，在自 $t$ 至 $t+\Delta t$ 内，出生的个体数量为 $bx(t)\Delta t$，死亡的个体数量为 $\mu x(t)\Delta t$

所以有 $x(t+\Delta t)-x(t)=(b-\mu)x(t)\Delta t$，即 $\frac{x(t+\Delta t)-x(t)}{\Delta t}=rx(t)\Rightarrow\frac{dx}{dt}=rx$

解微分方程我们有 $x(t)=x_0e^{rt}$，当 $r>0$ 时，$x(t)\rightarrow\infty(t\rightarrow\infty)$；当 $r<0$ 时，$x(t)\rightarrow 0(t\rightarrow\infty)$

- 指数增长模型不适于描述较长时期的人口演变过程，但某地一个较短时间内的人口统计数据可能符合指数增长模型
***
#### Logistic 模型

种群人均增长率仅与种群数量有关，且是种群数量的递减函数：$\frac{dx}{dt}=rx(1−\frac{x}{K})$

其中 $K$ 为环境承载量，$r$ 为内禀增长率，$x$ 为种群数量，解方程有 $x(t)=\frac{Kx_0}{x_0+(K-x_0)e^{-rt}}$

![](../../../assets/Pasted%20image%2020241221230630.png)

Logistic 模型有如下性质：

- 当 $0<x_0<K$ 时，种群数量随时间单调递增；当 $x_0>K$ 时，种群数量随时间单调递减；当 $x_0=K$ 时，种群数量保持不变
- $x(t)$ 在 $t=\frac{1}{2}K$ 时有拐点
- 当 $r<0$ 时，种群数量随时间单调递减至 $0$；当 $r>0$ 时，种群数量随时间单调递增至 $K$；当 $r=0$ 时，种群数量保持不变

!!! tip "Tips"

	多数情况下，指数模型与 Logistic 模型并不是基于生物学机理，而是一种经验模型模型及其参数应根据实际数据进行估计和检验
	
	除此之外，还有很多别的模型，如：
	
	$$
	\begin{aligned}
	\frac{dx}{dt}&=rx\ln\frac{K}{x}\\
	\frac{dx}{dt}&=rx\frac{K-x}{K+ax}\\
	\frac{dx}{dt}&=rx(1-(\frac{x}{k})^{\theta})\\
	\frac{dx}{dt}&=(re^{1-\frac{x}{K}}-d)x
	\end{aligned}
	$$
	
***
#### 自洽系统

- 对一阶常微分方程 $x'(t)=f(x)$，若 $f(x)$ 不显含变量 $t$，则称该方程为**自洽系统（Autonomous System）**
- 满足 $f(x_{\infty})=0$ 的 $x_{\infty}$ 称为**平衡点（Equilibrium Point）**
- 对一阶常微分方程 $x'(t)=f(x)$，或者 $x(t)$ 无界，或者 $\lim_{t\rightarrow\infty}x(t)=x_{\infty}$。但不是所有平衡点均为某个非零解的极限
- 可用线性化（Linearization）方法研究平衡点附近解的性态
***
#### 随机模型

记 $x(t)$ 为 $t$ 时刻一种群个体数量

- $x(t)$ 是一个取非负整数值的随机变量，$\{x(t),t\geq 0\}$ 为一随机过程
- $x(t)$ 为连续时间齐次 Markov 链
    - $P\{x(t+s)=j|x(s)=i,x(u)=x_u,0\leq u<s\}=P\{x(t+s)=j|x(s)=i\}$
    - $P\{x(t+s)=j|x(s)=i\}$ 值与 $s$ 无关，记其为 $p_{ij}(t)$
- 设 $x(t)=n$, 种群在 $(t,t+\Delta t)$ 时段内
    - 出生 1 人的概率为 $\lambda_n\Delta t+o(\Delta t)$
    - 死亡 1 人的概率为 $\mu_n\Delta t+o(\Delta t)$
    - 出生和死亡事件总发生两次或以上的概率很小，忽略不计

!!! note "生灭过程"

	离散状态空间连续时间齐次 Markov 链称为生灭过程（Birth–Death Process），若对充分小的 $\Delta t$，有：
	
	$$
	\begin{cases}
	p_{i,i+1}(\Delta t)=\lambda_i\Delta t+o(\Delta t),\lambda_i\geq 0,i\geq 0\\
	p_{i,i-1}(\Delta t)=\mu_i\Delta t+o(\Delta t),\mu_i\geq 0,i\geq 1\\
	p_{i,i}(\Delta t)=1-(\lambda_i+\mu_i)\Delta t+o(\Delta t),i\geq 0
	\end{cases}
	\Rightarrow\sum\limits_{|j-i|\geq 2}p_{ij}(\Delta t)=o(\Delta t)
	$$
	
	- 其中 $p_{i,j}$ 表示在 $\Delta t$ 时间内，从状态 $i$ 转移到状态 $j$ 的概率
	- 纯生过程（Pure Birth Process）：$\mu_i=0,i\geq 0$
	- 纯灭过程（Pure Death Process）：$\lambda_i=0,i\geq 0$
	- Poisson 过程：$\mu_i=0,i\geq 0$
***
#### 家族消亡模型

- 分支过程（Branching Process）是用于描述与某一群体繁殖和转换相关的现象的随机过程，其基本假定是个体的繁殖是相互独立的
- 分支过程可用于描述传染病从极少感染者经过逐级传播到爆发的过程
- Fisher 和 Haldane 曾用分支过程研究基因变异后的形成的不利基因通过自然选择在后代中的保留问题

??? question "问题描述"

	设每位家族成员之多有 $k$ 个后代，有 $i$ 个后代的概率为 $p_i$，什么情况下家族会消亡？


