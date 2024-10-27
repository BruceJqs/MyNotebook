# Project : 农作物的种植策略

## 参考

- [B 站视频](https://www.bilibili.com/video/BV1M9tpeVEXR?spm_id_from=333.788.videopod.sections&vd_source=ba4755ddf929bb319c3f5ca1d6fe2582)
- [Gitee 源码](https://gitee.com/binbinqi/cumcum_2024_c)

## 题目描述

来源：2024 年高教杯全国大学生数学建模竞赛 C 题第一小题

![](../../../assets/Pasted%20image%2020241027013943.png)

## 问题分析

该问题为一个优化决策类问题，优化决策类问题有三要素，在本题表现如下：

- 决策变量
	- 在每一年的每一季在每个地块上是否种植某作物（0-1 变量）
	- 种多少亩该作物（连续变量）
- 目标函数
	- 利润最大（收益=销售额-成本=种植亩数$\times$(亩产$\times$价格-成本)）
- 约束条件
	- 种植面积约束
		- 在每个地块上种植的作物总面积不能超过该地块的面积
		- 每种作物在单个地块种植的面积不宜太小（可以设置百分比阈值，也可设置绝对阈值）
	- 重茬约束
		- 对于单季制作物，两年之间不能重复种植在某个地块上
		- 对于两季制作物，同一年两季之间不能重复种植在某个地块上；第一年的第二季和第二年的第一季也不能重复种植在某个地块上
	- 豆类种植约束
		- 所有土地三年内至少种植一次豆类作物
	- 分散约束
		- 每种作物每季的种植地不能太分散
	- 水浇地约束
		- 水浇地适宜每年种植一季水稻或两季蔬菜，即一旦种植了水稻，那么就不能种植其他作物，并且第二季也不能种植其他作物

对于第一小问，是一种价格、销量、成本和产能<font color="red">不随时间变化</font>的理想情况（即 2024-2030 的所有数据都以 2023 年的为准）。
***
## 模型假设

- 2023年的销售量按照地块类型、作物类型和季节三个维度来统计，不同地块类型的同一种作物，因为价格不同，不会算作同一种作物来同一统计销量。
- 2023年没有种植的作物，2024年如果种植的话，默认其销量是无穷大,或者为其他类型地块该类作物的平均销量
***
## 模型建模

### 集合定义

#### 耕地

- 平旱地：$A=\{A_1,A_2,...,A_6\}$
- 梯田：$B=\{B_1,B_2,...,B_{14}\}$
- 山坡地：$C=\{C_1,C_2,...,C_6\}$
- 水浇地：$D=\{D_1,D_2,...,D_8\}$
- 普通大棚：$E=\{E_1,E_2,...,E_{16}\}$
- 智慧大棚：$F=\{F_1,F_2,...,F_4\}$

总的来说，耕地 $G=A\bigcup B\bigcup C\bigcup D\bigcup E\bigcup F$
 ***
#### 作物

- 粮食（豆类）：$H=\{1,2,3,4,5\}$
- 粮食：$I=\{6,7,8,...,15\}$
- 粮食水浇地：$J=\{16\}$
- 蔬菜（豆类）：$K=\{17,18,19\}$
- 蔬菜（水浇地第一季）：$L=\{20,21,...,34\}$
- 蔬菜（水浇地第二季）：$M=\{35,36,37\}$
- 食用菌（普通大棚第二季）：$N=\{38,39,40,41\}$

总的来说，作物 $O=H\bigcup I\bigcup J\bigcup K\bigcup L\bigcup M\bigcup N$
***
#### 其他

- 季度：$S=\{1,2\}=S_1\bigcup S_2$
- 年份：$Y=\{2024,2025,...,2030\}$
- 地块：$R=\{A,B,C,D,E,F\}$

![](../../../assets/Pasted%20image%2020241027133727.png)

- 平旱地、梯田、山坡地：$V_1=(A\bigcup B\bigcup C)\times(H\bigcup I)\times S_1$
- 水浇地：$V_2=D\times J\times S_1$
- 水浇地、普通大棚、智慧大棚第一季：$V_3=(D\bigcup E\bigcup F)\times (K\bigcup L)\times S_1$
- 智慧大棚第二季：$V_4=F\times(K\bigcup L)\times S_2$
- 水浇地第二季：$V_5=D\times M\times S_2$
- 普通大棚第二季：$V_6=E\times N\times S_2$

总的来说，所有作物种植的可能性组合 $V=V_1\bigcup V_2\bigcup ...\bigcup V_6$

![](../../../assets/Screenshot%202024-10-27%20at%2013.48.06.png)

- 第一季地块：$W_1=(A\bigcup B\bigcup C\bigcup D\bigcup E\bigcup F)\times S_1$
- 第二季地块：$W_2=(D\bigcup E\bigcup F)\times S_2$

总的来说，地块情况 $W=W_1\bigcup W_2$
***
### 输入参数

![](../../../assets/Pasted%20image%2020241027135805.png)

![](../../../assets/Pasted%20image%2020241027135741.png)

- 地块 $g$ 的面积：$a_g,\forall g \in G$
- 地块类型 $r$ 作物 $o$ 季节 $s$ 年 $t$ 的销售单价：$p_{r,o,s,t},r\in R$
- 地块类型 $r$ 作物 $o$ 季节 $s$ 年 $t$ 的种植成本：$c_{r,o,s,t},r\in R$
- 地块类型 $r$ 作物 $o$ 季节 $s$ 年 $t$ 的销量：$q_{r,o,s,t},r\in R$
- 地块类型 $r$ 作物 $o$ 季节 $s$ 年 $t$ 的亩产量：$w_{r,o,s,t},r\in R$
- 同一种作物最多种植的地块数：$\theta$
- 作物面积占地块面积的最小比例：$\delta$
***
### 决策变量

- 种植亩数（连续变量）：$x_{g,o,s,t},\forall(g,o,s)\in V,t\in Y$
- 是否种植作物（0-1 变量）：$y_{g,o,s,t},\forall(g,o,s)\in V,t\in Y$
***
### 约束条件

#### 种植面积约束

- 地块总面积约束：$\sum\limits_{o\in O}x_{g,o,s,t}\leq a_g,\forall(g,s)\in W,t\in Y$
- 种植面积不能太小：$x_{g,o,s,t}\geq a_gy_{g,o,s,t}\delta,\forall(g,o,s)\in V,t\in Y$
- 不种植该作物，那么种植面积为 0：$x_{g,o,s,t}\leq a_gy_{g,o,s,t},\forall(g,o,s)\in V,t\in Y$

***
#### 水浇地约束

- 如果水浇地种植水稻，则第一季不能种植任何其他作物：$y_{g,o,s,t}+y_{g,o',s,t}\leq 1,\forall g\in G,o\in J,s\in S_1,o'\in K\bigcup L,t\in Y$
- 如果水浇地种植水稻，则第二季不能种植任何其他作物：$y_{g,o,s,t}+y_{g,o',s',t}\leq 1,\forall g\in G,o\in J,s\in S_1,o'\in M,s'\in S_2,t\in Y$
***
#### 重茬约束

- 粮食重茬约束：$y_{g,o,s,t}+y_{g,o,s,t+1}\leq 1,\forall (g,o,s)\in V_1\bigcup V_2,t\in Y$
- 智慧大棚第一季与第二季重茬约束：$y_{g,o,s,t}+y_{g,o,s',t}\leq 1,\forall g\in F,o\in K\bigcup L,s\in S_1,s'\in S_2,t\in Y$
- 智慧大棚第二季与第二年第一季重茬约束：$y_{g,o,s,t}+y_{g,o,s',t+1}\leq 1,\forall g\in F,o\in K\bigcup L,s\in S_2,s'\in S_1,t\in Y$
***
#### 豆类种植约束

- 平旱地、梯田、山坡地豆类种植约束：$\sum\limits_{t'=t}^{t+2}\sum\limits_{o\in H}y_{g,o,s,t'}\geq 1,\forall g\in A\bigcup B\bigcup C,s\in S_1,t\in Y$
- 水浇地、普通大棚豆类种植约束：$\sum\limits_{t'=t}^{t+2}\sum\limits_{o\in K}y_{g,o,s,t'}\geq 1,\forall g\in D\bigcup E,s\in S_1,t\in Y$
- 智慧大棚豆类种植约束：$\sum\limits_{t'=t}^{t+2}\sum\limits_{o\in K}\sum\limits_{s\in S}y_{g,o,s,t'}\geq 1,\forall g\in F,t\in Y$
***
#### 分散约束

$\sum\limits_{g\in G}y_{g,o,s,t}\leq\theta,\forall G\in R,o\in O,s\in S,t\in Y$
***
### 目标函数

$$
\max\sum\limits_{o,s,t}\sum\limits_{G\in R}f(w_{G,o,s,t}\sum\limits_{g\in G}x_{g,o,s,t},q_{G,o,s,t},p_{G,o,s,t})-\sum\limits_{g\in G}x_{g,o,s,t}c_{g,o,s,t}
$$

其中 $f(x,y,z)=\begin{cases}xz,x\leq y\\yz,x>y\end{cases}$

引入 0-1 变量 $\lambda$，$\lambda=0\Leftrightarrow x>y,\lambda=1\Leftrightarrow x\leq y$，那么有 $f(x,y,z)=(\lambda x+(1-\lambda)y)z$
