---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
---  

# Chapter 08 : 假设检验

统计推断的另一类重要问题是假设检验问题。它包括：

- 参数检验：已知总体分布的形式，需对其中的未知参数给出假设检验
- 非参数检验：总体的分布形式完全未知的情况下，对总体的分布或数字特征进行假设检验

!!! example "Example"

	接下来的所有概念都会围绕着一个例子进行说明，方便理解。
	
	设某种清漆的9个样品，其干燥时间（以小时计）分别为：
	
    6.0  6.7  6.5  6.5  7.0  6.8  6.2  6.1  5.8
    
    根据以往经验，干燥时间的总体服从正态分布 $N(6.0, 0.36)$，现根据样本检验均值是否与以往有显著差异？
***
## 假设

- 原假设（零假设）：$H_0$
- 备择假设（对立假设）：$H_1$

关于总体参数 $\theta$ 的假设：

- 左边检验：$H_0:\theta\geq\theta_0,H_1:\theta<\theta_0$
- 右边检验：$H_0:\theta\leq\theta_0,H_1:\theta>\theta_0$
- 双边检验：$H_0:\theta=\theta_0,H_1:\theta\not=\theta_0$
***
## 检验统计量和拒绝域

如果统计量 $T=T(X_1,...,X_n)$ 的取值大小和原假设 $H_0$ 是否成立有密切关系，可将之称为对应假设问题的检验统计量，对应于拒绝原假设 $H_0$ 时，样本值的范围称为拒绝域，即为 $W$，其补集 $\overline{W}$ 称为接受域

!!! example "Example"

	对于上面的例子来说，考虑有关参数 $\mu$ 的假设：$H_0:\mu=6.0,H_1:\mu\not=6.0$（双边检验）
	
	因样本均值 $\overline{X}$ 是 $\mu$ 的无偏估计，$\overline{X}$ 的取值大小反映了 $\mu$ 的取值大小，当原假设成立时，$|\overline{X}-6.0|$ 取值应偏小。
	
	检验规则：
	
	- 当 $|\overline{X}-6.0|\geq C$ 时，拒绝原假设 $H_0$
	- 当 $|\overline{X}-6.0|<C$ 时，接受原假设 $H_0$
	
	其中 $C$ 是待定的常数，那么可取检验统计量为 $\overline{X}$（或 $\overline{X}-6.0$），拒绝域为 $W=\{(X_1,...,X_n):|\overline{X}-6.0|\geq C\}$
***
## 两类错误

> 由于样本的随机性，任一检验规则在应用时，都有可能发生错误的判断

|           | 原假设为真   | 原假设不真    |
| --------- | ------- | -------- |
| 根据样本拒绝原假设 | 第 I 类错误 | 正确       |
| 根据样本接受原假设 | 正确      | 第 II 类错误 |

- 第 I 类错误：拒绝真实的原假设（弃真），犯错概率 $\alpha=P\{\text{第 I 类错误}\}=P\{\text{拒绝}H_0|H_0\text{是真的}\}=P_{H_0}\{\text{拒绝}H_0\}$
- 第 II 类错误：接受错误的原假设（取伪），犯错概率 $\beta=P\{\text{第 II 类错误}\}=P\{\text{接受}H_0|H_0\text{是假的}\}=P_{H_1}\{\text{接受}H_0\}$

!!! example "Example"

	在上面的例子中，犯第 I 类错误的概率：
	
	$$
	\begin{aligned}
	\alpha(C)&=P\{\text{拒绝}H_0|H_0\text{是真的}\}\\
	&=P\{|\overline{X}-6.0|\geq C|\mu=6.0\}\\
	&=P\{\frac{\overline{X}-6.0}{\sigma/\sqrt{n}}\geq\frac{C}{\sigma/\sqrt{n}}|\mu=6.0\}
	\end{aligned}
	$$
	
	由于当 $H_0$ 成立时，即 $\mu=6.0$ 时，$\frac{\overline{X}-6.0}{\sigma/\sqrt{n}}∼N(0,1)$，因此 $\alpha(C)=2-2\Phi(\frac{C}{\sigma/\sqrt{n}})$
	
	犯第 II 类错误的概率：
	
	$$
	\begin{aligned}
	\beta(C)&=P\{\text{接受}H_0|H_0\text{是假的}\}\\
	&=P\{|\overline{X}-6.0|<C|\mu\not=6.0\}\\
	&=P\{6.0-C<\overline{X}<6.0+C|\mu\not=6.0\}\\
	&=P\{\frac{6.0-C-\mu}{\sigma/\sqrt{n}}<\frac{\overline{X}-\mu}{\sigma/\sqrt{n}}<\frac{6.0+C-\mu}{\sigma/\sqrt{n}}|\mu\not=6.0\}\\
	&=\Phi\{\frac{6.0+C-\mu}{\sigma/\sqrt{n}}\}-\Phi\{\frac{6.0-C-\mu}{\sigma/\sqrt{n}}\},\mu\not=6.0
	\end{aligned}
	$$
	
	显然，犯第 I 类错误的概率 $\alpha(C)$ 关于 $C$ 是单调减函数，而犯第 II 类错误的概率 $\beta(C)$ 关于 C 是单调增函数
	
	因此，在给定的样本量 $n$ 下，不可能找界值 $C$，使得 $\alpha(C)$ 和 $\beta(C)$ 都非常小，即，犯两类错误的概率相互制约！

根据上面的分析，我们发现两类错误的概率相互制约，因此我们需要找到一个平衡值，我们有 Neyman-Pearson 原则：首先控制犯第 I 类错误的概率不超过某个常数 $\alpha\in(0,1)$，再寻找检验，使得犯第 II 类错误的概率尽可能小。其中的常数 $\alpha$ 称为显著水平，常取 $\alpha=0.01,0.05,0.1$ 等。

!!! example "Example"

	在上面的例子中，根据若 Neyman-Pearson 原则，取显著水平 $\alpha=0.05$，则有 $\alpha(C)=2-2\Phi(\frac{C}{\sigma/\sqrt{n}})\leq 0.05$，计算得 $C\geq z_{0.025}\sigma/\sqrt{n}=0.392$，此时拒绝域为 $W=\{(X_1,...,X_9):|\overline{X}-6.0|\geq 0.392\}$
	
	根据实际样本资料，得 $\overline{x}=6.4$，有 $|\overline{x}-6.0|=0.4>0.392$，样本落入拒绝域
	
	我们有 95% 的把握拒绝原假设 $H_0$，即认为油漆干燥时间与以往有显著差异
	
	根据上述检验规则，犯第 I 类错误的概率 $\alpha(0.392)=0.05=\alpha$
	
	犯第 II 类错误的概率
	
	$$
	\begin{aligned}
	\beta(0.392)&=\Phi\{\frac{6.0+0.392-\mu}{0.6/\sqrt{9}}\}-\Phi\{\frac{6.0-0.392-\mu}{0.6/\sqrt{9}}\}\\
	&=\Phi\{\frac{6.392-\mu}{0.2}\}-\Phi\{\frac{5.608-\mu}{0.2}\},\mu\not=6.0
	\end{aligned}
	$$
	
***
## P_值与统计显著性

- P_值：当原假设成立时，检验统计量取比观察到的结果更为极端的数值的概率

P_ 值与显著水平 $\alpha$ 的关系：

- 若 $P\_\leq\alpha$，等价于样本落在拒绝域内，因此，拒绝原假设，此时称检验结果在水平 $\alpha$ 下是统计显著的
- 若 $P\_>\alpha$，等价于样本不落在拒绝域内，因此，不拒绝（接受）原假设，此时称检验结果在水平 $\alpha$ 下是统计不显著

!!! example "Example"

	对于上面这个例子，有:
	
	$$
	P\_=P_{H_0}(|\overline{X}-6.0|\geq|6.4-6.0|)=P_{H_0}(|\frac{\overline{X}-6.0}{0.2}|\geq 2)=2-2\Phi(2)=0.046
	$$
	
	$|\overline{X}-6.0|\geq 0.4$ 是小概率事件，因此拒绝原假设

> 用 P_ 值计算来判断拒绝还是接受原假设相对更为简单，而且能知道概率大小
***
## 处理假设检验问题的基本步骤

- 根据实际问题提出原假设和备择假设
- 提出检验统计量和拒绝域的形式
- 在给定的显著水平 $\alpha$ 下，根据 Neyman-Pearson 原则求出拒绝域的临界值/计算检验统计量的观测值与 $P\_$ 值
- 根据实际样本观测值做出判断/根据给定的显著水平 $\alpha$，做出判断
***
## 单个正态总体参数的假设检验

![](../../../assets/Pasted%20image%2020241219162659.png)