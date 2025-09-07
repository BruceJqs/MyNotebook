---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
# comments: true
--- 

# Final Review

## 机器学习基本概念

### 机器学习：概念与分类

机器学习定义：通过对数据的优化学习，**建立能够刻画数据中所蕴含语义概念或分布结构等信息的模型**

从数据利用的角度分类：

- 监督学习（Supervised Learning）
- 无监督学习（Unsupervised Learning）
- 半监督学习（Semi-supervised Learning）
***
### 有监督学习

目标：给定带有标签信息数据的训练集 $\mathcal{D}=\{(x_i,y_i)\}_{i=1}^n$ ，学习一个从输入 $x_i$ 到输出 $y_i$ 的<font color="red">最优映射函数 f（又称决策函数</font>，将输入数据映射到语义标注空间，实现数据分类和识别）

- $x_i$：数据/数据的特征表达
- $y_i$：语义内容
- $n$：训练样例数量

无监督学习直接从**无标签数据** $\mathcal{D}=\{x_i,i=1,\cdots,n\}$ 出发学习映射函数；半监督学习在学习映射函数过程中使用的**一部分数据有标签，一部分数据没有标签**

验证集：一般从训练集中取一部分数据，对模型进行评估

测试集：测试结果作为模型性能最终结果

- 训练集、验证集和测试集所包含数据之间没有任何交叉
***
### 模型评估与参数估计手段：损失函数

泛化能力（Generalization）：保证模型在训练集上所取得性能与在测试集上所取得性能保持一致

损失函数（Loss Function）：将映射函数记为 $f$、第 $i$ 个训练数据记为 $(x_i,y_i)$ 以及 $f$ 对 $x_i$ 的预测结果记为 $\hat{y_i}$（即 $\hat{y_i}=f(x_i)$），定义损失函数 $\text{Loss}(f(x_i),y_i)$ 来估量预测值 $\hat{y_i}$ 与真实值 $y_i$ 之间的差距

训练过程中希望映射函数在训练集上累加差异最小，即 $\min\sum\limits_{i=1}^n\text{Loss}(f(x_i),y_i)$，常见损失函数：

| 损失函数名称        | 损失函数定义                                                                           |
| ------------- | -------------------------------------------------------------------------------- |
| 0-1 损失函数      | $\text{Loss}(y_i,f(x_i))=\begin{cases}1,f(x_i)\neq y_i\\0,f(x_i)=y_i\end{cases}$ |
| 平方损失函数        | $\text{Loss}(y_i,f(x_i))=(y_i-f(x_i))^2$                                         |
| 绝对损失函数        | $\text{Loss}(y_i,f(x_i))=\vert y_i-f(x_i)\vert$                                  |
| 对数损失函数/对数似然函数 | $\text{Loss}(y_i,P(y_i\vert x_i))=-\log P((y_i\vert x_i))$                       |

***
### 经验风险与期望风险

经验风险（Empirical Risk）： $\mathcal{R}_{\text{emp}}=\frac{1}{n}\sum\limits_{i=1}^n\text{Loss}(y_i,f(x_i))$，越小代表模型对训练集数据拟合程度越好

期望风险（Expected Risk）：设任务中所有数据联合分布为 $P(x,y)$， $\mathcal{R}=\int_{x\times y}\text{Loss}(y,f(x))P(x,y)dxdy$，也称真实风险/真实误差

- 经验风险与期望风险不同，机器学习中模型优化目标一般为**经验风险最小化**，实际更追求的是期望风险最小化
	- 两者关系：$\mathcal{R}\leq\mathcal{R}_{\text{emp}}+\text{err}$，其中 err 取值与机器学习模型的复杂程度和训练集样本数目有关，如果使⽤同⼀批训练数据反复训练，模型会变得越复杂，虽然经验⻛险会降低，但是 err 取值会越⼤，导致期望⻛险增加，这⼀现象被称为过学习（Overfitting）

模型泛化能力与经验风险、期望风险关系如下：

| 经验风险（训练集表现） | 期望风险（所有数据表现） | 模型泛化能力 |
| ----------- | ------------ | ------ |
| 小           | 小            | 强      |
| 小           | 大            | 过学习    |
| 大           | 大            | 欠学习    |
| 大           | 小            | 不可能    |

为了防止过学习，结构风险最小化（Structural Risk Minimization）引入正则化（Regularizer）或惩罚项（Penalty Term）来降低模型复杂度，在经验风险和模型复杂度寻找平衡：

$$
\frac{1}{n}\sum\limits_{i=1}^n\text{Loss}(y_i,f(x_i))+\lambda J(f)
$$

- $J(f)$ 是正则化因子或惩罚项因子
- $\lambda$ 是用来调整惩罚强度的系数
***
### 模型度量方法

以二分类问题为例，设 $n$ 为训练样例的总数，正例总数和负例总数分别为 $P$ 和 $N$，机器模型预测类别分为四类：真实例（TP）、假正例（FP）、真反例（TN）、假反例（FN），则：

- 准确率（Accuracy）：$\text{ACC}=\frac{TP+TN}{P+N}$，如果正负样例比例不平衡，准确率不是一个好的方法
- 错误率（Error Rate）：$\text{errorRate}=\frac{FP+FN}{P+N}=1-\text{ACC}$
- 精确率（Precision）：$\text{precision}=\frac{TP}{TP+FP}$，也叫查准率
- 召回率（Recall）：$\text{recall}=\frac{TP}{TP+FN}$，也叫查全率

实际应用中精确率和召回率是相互矛盾的，可采用 F1-score（综合分类率）来综合考虑两者（即两者调和平均数）：

$$
\text{F1-score}=\frac{2}{\frac{1}{\text{precision}}+\frac{1}{\text{recall}}}=\frac{2\times\text{precision}\times\text{recall}}{\text{precision}+\text{recall}}
$$
***
### 有关大模型

- 大模型最大的贡献是将预训练+微调变成了预训练，把微调去掉了，改变了使用的范式（趋势之一）
- 趋势：
	- 从二维到三维思维
	- 从小模型变成大模型（更通用）
	- 宏观到微观
	- 识别到生成
	- 具身智能
- 用少量数据（如 10 条）故意让模型过拟合是验证代码是否正确的一个非常有效的技巧，如果 10 条数据都不能过拟合，那么代码一定有问题
***
## 回归分析

### 一元线性回归模型

最小二乘法：误差总和 $L(a,b)=\sum\limits_{i=1}^n(y_i-ax_i-b)^2$，分别对 $a$ 和 $b$ 求偏导数并令其为 0，得到参数估计公式：

$$
\begin{aligned}
a &= \frac{\sum\limits_{i=1}^n x_iy_i-n\overline{x}\overline{y}}{\sum\limits_{i=1}^n x_i^2-n\overline{x}^2}\\
b &= \overline{y} - a\overline{x}
\end{aligned}
$$

***
### 多元线性回归模型

多元线性回归模型：设总共有 $m$ 个训练数据 $\{(\pmb{x_i},y_i)\}_{i=1}^m$，其中 $\pmb{x_i}=[x_{i,1},x_{i,2},\cdots,x_{i,D}]\in\mathbb{R}^D$，$D$ 为数据特征的维度，找到一组参数 $\pmb{a}=[a_0,a_1,\cdots,a_D]$，使得线性函数 $f(\pmb{x_i})=a_0+\sum\limits_{j=1}^Da_jx_{i,j}=a_0+\pmb{a}^T\pmb{x_i}$ 最小化均方误差函数 $J_m=\frac{1}{m}\sum\limits_{i=1}^m(y_i-f(\pmb{x_i}))^2$

!!! note "Note"

	用矩阵来表示所有训练数据和数据标签：$X=[x_1,\cdots,x_m],\mathbf{y}=[y_1,\cdots,y_m]$
	
	其中每个数据 $x_i$ 扩展一个维度，值为 1，对应参数 $a_0$，则均方误差函数可以表示为 $J_m(\mathbf{a})=(\mathbf{y}-X^T\mathbf{a})^T(\mathbf{y}-X^T\mathbf{a})$
	
	对所有参数 $\pmb{a}$ 可得 $\nabla J(\mathbf{a})=-2X(y-X^T\mathbf{a})$
	
	令 $\nabla J(\mathbf{a})=0$，得到 $\mathbf{a}=(XX^T)^{-1}X\mathbf{y}$
***
### 非线性回归

Logistic 回归模型：$y=\frac{1}{1+e^{-z}}=\frac{1}{1+e^{-w^Tx+b}},y\in (0,1),z=\mathbf{w}^T\mathbf{x}+b$，其中 $\mathbf{x}\in\mathbb{R}^d$ 是输入数据，$\mathbf{w}\in\mathbb{R}^d$ 和 $b\in\mathbb{R}$ 是回归函数的参数

- Logistic 回归只能用于解决二分类问题，将它推广为多项逻辑斯蒂回归模型（Multi-Nominal Logistic Model，也即 Softmax 函数），用于处理多类分类问题，可以得到处理多类分类问题的Softmax 回归
***
## 前馈神经网络与参数优化

### 人工神经网络概述

!!! abstract "Abstract"

	一些背书内容，我也不知道有没有用先放着了

- MCP 神经元：于 1943 年由 Warren McCulloch 和 Walter Pitts 提出
	- 对生物神经元的简化抽象，试图用数学和逻辑的方式来模拟神经元的工作原理
	- 基于核心假设：二值输出、线性加权和、阈值函数（输出由输入是否达到某个固定阈值确定）
- 赫布理论：于 1949 年由 Donald Hebb 提出
	- 神经元之间持续重复经验刺激可导致突触传递效能增加
- 感知机：于 20 世纪 50 年代由 Fank Rosenblatt 提出
	- 仅包含输入层和输出层的两层神经网络，可完成两类问题的线性分类
	- 其基本概念包括输入和输出、权重、激活函数、学习规则
- 误差后向传播：于 1974 年由 Werbos 提出，后由 Rumelhart 和 Hinton 等人完善
	- 解决了多层感知机中参数优化这一难题
- 深度学习：与 2006 年由 Hinton 提出
***
#### 神经元

> 在生物学中，神经元细胞有**兴奋与抑制**两种状态

给定 $n$ 个二值化（0 或 1）的输入数据 $x_i(1\leq i\leq n)$ 与连接参数 $w_i(1\leq i\leq n)$，MCP 神经元模型对输入数据线性加权求和，使用函数 $\Phi$ 将加权累加结果映射为 0 或 1，以完成两类分类任务

![](../../../assets/Pasted%20image%2020250611145936.png)
***
#### 感知机

单层感知机：一个输入层+一个输出层，可作为一种两类线性分类模型，相对神经元多加一个偏置项 $b$

![](../../../assets/Pasted%20image%2020250611150348.png)

- 感知机中的连接权重参数并不是预先设定好的，而是通过多次迭代训练得到的
- 感知机可模拟逻辑与、与非和或等线性可分函数，但是无法完成逻辑异或这一非线性可分逻辑函数
***
### 前馈神经网络

在感知机模型中增加若干隐藏层，增强神经网络的非线性表达能力，就会让神经网络具有更强的拟合能力，这样由多个隐藏层构成的多层感知机被称为前馈神经网络

![](../../../assets/Pasted%20image%2020250611150721.png)

- 前馈神经网络中相邻层所包含的神经元之间通常使用**全连接**方式进行连接
- 前馈神经网络可以**模拟复杂非线性函数**功能，所模拟函数的复杂性取决于网络隐藏层数目和各层中神经元数目

前馈神经网络常用的非线性映射函数（激活函数）有：

- Sigmoid 函数：$f(x)=\frac{1}{1+e^{-x}}$
	- 优点：概率形式输出、单调递增、非线性变化
	- $f'(x)=f(x)(1-f(x))$
	- 缺点：由于导数小于 1，在使用反向传播算法更新参数过程中易出现导数过于接近于 0 的情况，即梯度消失（Vanishing Gradient）问题，并且这个问题会随着网络的深度增加而变得愈发严重
- ReLU 函数：$f(x)=\max(0,x)$
	- $f'(x)=\begin{cases}0,\text{for }x<0\\1,\text{for }x\geq 0\end{cases}$
	- 当输入 $x\geq 0$ 时，导数恒为 1，避免了梯度消失问题
	- 当输入 $x<0$ 时，导数恒为 0，导致神经网络中若干参数激活值为 0，即参与分类等任务神经元数目稀缺，在一定程度上克服过拟合现象，但也导致了神经元死亡（可以使用其他函数例如 Leaky ReLU/Parametric ReLU 等来解决，它们在 $x<0$ 时梯度取值非零）
	
	![](../../../assets/Pasted%20image%2020250611151846.png)
	
- Softmax 函数：$y_i=\text{softmax}(x_i)=\frac{e^{x_i}}{\sum\limits_{j=1}^k e^{x_j}}$
	- Softmax 函数通常用于多分类问题的输出层，能够将神经网络输出的实数值转换为概率分布
	- 由于 Softmax 输出结果的值累加起来为 1，因此可将输出概率最大的作为分类目标
	
	![](../../../assets/Pasted%20image%2020250611152122.png)
	
- 激活函数必须是<font color="red">单调递增的</font>
***
### 神经网络参数优化

> 神经网络参数优化是一个监督学习的过程，利用损失函数结果来优化模型参数，即让神经网络对数据进行拟合（Data Fitting），具体而言，模型会利用反向传播算法将损失函数计算所得误差从输出端出发、由后向前传递给神经网络中每个单元，然后通过梯度下降算法对神经网络中参数进行更新

#### 损失函数

神经网络参数优化一般常用的损失函数（又称为代价函数）有均方误差损失函数（$\text{MSE}=\frac{1}{n}\sum\limits_{i=1}^n(y_i-\hat{y_i})^2$）和交叉熵损失函数（$H(y_i,\hat{y_i})=-y_i\log\hat{y_i}$）
***
#### 梯度下降

> 梯度下降是一种使损失函数最小化的方法

一元变量所构成函数 $f$ 在 $x$ 处梯度为 $\frac{df(x)}{dx}=\lim\limits_{h\rightarrow 0}\frac{f(x+h)-f(x)}{h}$

- 在多元函数中，梯度是对每一变量所求导数组成的向量
- 梯度的反方向是函数值下降最快的方向，因此是损失函数求解的方向

!!! note "Note"

	假设损失函数 $f(x)$ 是连续可微的多元变量函数，泰勒展开如下：
	
	$$
	f(\pmb{x}+\Delta\pmb{x})=f(\pmb{x})+f'(\pmb{x})\Delta\pmb{x}+\frac{1}{2}f''(\pmb{x})(\Delta\pmb{x})^2+\cdots+\frac{1}{n!}f^{(n)}(\pmb{x})(\Delta\pmb{x})^n
	$$
	
	可以得到 $f(\pmb{x}+\Delta\pmb{x})-f(\pmb{x})\approx(\nabla f(\pmb{x}))^T\Delta\pmb{x}$
	
	由于 $f(x)$ 是损失函数，所以我们希望 $f(\pmb{x}+\Delta\pmb{x})$ 小于 $f(\pmb{x})$，那么有 $(\nabla f(\pmb{x}))^T\Delta\pmb{x}<0$
	
	而我们有 $(\nabla f(\pmb{x}))^T\Delta\pmb{x}=\|\nabla f(\pmb{x})\|\|\Delta\pmb{x}\|\cos\theta$，因此我们只需要取 $\theta=\pi$，梯度能下降地最快，因为我们忽略了损失函数泰勒展开的二阶及以上项，因此在实际中用 $\pmb{x}-\eta\nabla f(\pmb{x})$ 来更新 $\pmb{x}$（具体实现中 $\eta$ 可取一定值，其实就是<font color="red">学习率</font>）

梯度下降算法可以分为批量梯度下降算法（Batch Gradient Descent）、随机梯度下降算法（Stochastic Gradient Descent）和小批量梯度下降算法（Mini-batch Gradient Descent）等类型：

- 批量梯度下降：在整个训练集上计算损失误差，如果数据集较大，则会因内存容量不足无法完成梯度计算
- 随机梯度下降：每次从训练集中随机选取一个样本进行梯度计算，更新参数。梯度方向具有很大波动，收敛速度通常较慢，但是随机性有助于跳出局部最优解
- 小批量梯度下降：每次从训练集中随机选取一小部分样本进行梯度计算，更新参数。可保证训练过程更稳定，采用批量训练方法也可利用矩阵计算优势，是目前最常用的梯度下降算法
***
#### 误差反向传播

求损失函数梯度时需要对各个变量求偏导，需要用到链式法则

![](../../../assets/Pasted%20image%2020250611154817.png)

例如，要对 $w_1$ 更新，因为 $w_1$ 与加权累加函数 $\mathcal{X}$ 和 sigmoid 函数均有关，因此 $\frac{\partial\mathcal{L}}{\partial w_1}=\frac{\partial\mathcal{L}}{\partial\mathcal{O}}\frac{\partial\mathcal{O}}{\partial\mathcal{X}}\frac{\partial\mathcal{X}}{\partial w_1}$
***
## 卷积神经网络

> 对于图像这样的数据，<font color="red">不能直接将所构成的像素点向量与前馈神经网络中的每个神经元相连</font>

- 卷积这一思想利用了图像中像素点存在“空间依赖度”的特点，即相邻像素点之间具有很强的相关性、而彼此远离像素点之间的相关性很弱
- 卷积算子的特点有：
	- 选择性感受野：每个输出点的取值仅依赖于其在输入图像中该点及其邻域区域点 的取值，而与这个区域之外的其他点取值均无关，该区域被称为感受野（Receptive Field）
	- 局部感知、参数共享：卷积操作的权重参数可学习、可被重复使用，减少了参数总数，一定程度防止过拟合
	- 下采样约减抽象：假设被卷积图像大小为 $w\times w$，卷积核大小为 $F\times F$，上下左右四个边缘填充像素行/列数为 $P=\lfloor\frac{F}{2}\rfloor$，步长为 $S$，则被卷积结果的分辨率是 $\frac{w+2P-F}{S}+1$

卷积神经网络的组成和操作如下：

- 卷积核：以当前像素为中心，在大小为 $[h,w]$ 局部区域内，为每个方向和距离 $(i,j)$ 安排一参数 $W^{(i,j)}$
	
	![](../../../assets/Pasted%20image%2020250611171231.png)
	
	![](../../../assets/Pasted%20image%2020250611172109.png)
	
	$$
	I'^{(x,y)}=\sum\limits_{i=-\lfloor\frac{h}{2}\rfloor}^{\lfloor\frac{h}{2}\rfloor}\sum\limits_{j=-\lfloor\frac{w}{2}\rfloor}^{\lfloor\frac{w}{2}\rfloor}I^{(x+i,y+j)}W^{(i,j)}
	$$
	
	- 卷积神经网络是可以感受到方向和距离的
- Padding：卷积神经网络中为了保证卷积操作后图像大小不变，通常会在图像边缘添加一些额外的像素，这个过程称为 Padding，一般填充 0
	
	![](../../../assets/Pasted%20image%2020250611171547.png)
	
- Stride：卷积神经网络中卷积核在图像上滑动的步长，通常为 1 或 2

	
	![](../../../assets/Pasted%20image%2020250611171630.png)
	
- Dilation：卷积神经网络中卷积核的扩张率，通常为 1 或 2
	
	![](../../../assets/Pasted%20image%2020250611171715.png)
	
- Pooling：池化操作是卷积神经网络中常用的下采样方法，主要有最大池化（Max Pooling）、平均池化（Average Pooling）、 k-max 池化（K-Max Pooling）等
	
	![](../../../assets/Pasted%20image%2020250611172623.png)
	

全貌图如下：

![](../../../assets/Pasted%20image%2020250611173902.png)

***
## 循环神经网络

> 循环神经网络（Recurrent Neural Network, RNN）是一类处理序列数据（如文本句子、视频帧等）时所采用的网络结构，前馈神经网络或卷积神经网络所需要处理的输入数据一次性给定，难以处理存在前后依赖关系的数据

![](../../../assets/Pasted%20image%2020250611174506.png)

在时刻 $t$，输入数据为 $x_t$，循环神经网络会结合前一时刻 $t-1$ 得到的隐式编码 $h_{t-1}$，根据 $h_t=\Phi(U\times x_t+W\times h_{t-1})$ 产生当前时刻隐式编码 $h_t$，其中 $\Phi$ 是激活函数，一般可为 Sigmoid 或 Tanh 激活函数，$U$ 和 $W$ 为模型参数
***
### 自然语言

对自然语言来说，一旦得到了每个单词的隐式编码后，通常可以通过如下方法得到一个句子的向量编码：

1. 考虑到句子中所有单词的信息均被后向传递，因此将最后一个单词的输出作为整个句子向量编码表示；
2. 将每个单词的隐式编码进行加权平均，将加权平均结果作为句子的向量编码表示

这样，一旦得到了句子的向量编码表示，就可以利用某个分类器，对句子的类别进行判断
***
### 应用模式

在循环神经网络中，根据输入序列数据与输出序列数据中所包含“单元”的多寡，循环神经网络可以实现如下三种模式：

- “多对多”（即输入和输出序列数据中包含多个单元，常用于机器翻译）
- “多对一”（即输入序列数据包含多个单元，输出序列数据只包含一个单元，常用于文本的情感分类）
- “一对多”（即输入序列数据包含一个单元，输出序列数据包含多个单元，常用于图像描述生成）

![](../../../assets/Pasted%20image%2020250611175045.png)
***
### 梯度传递

循环神经网络虽然具有一定的记忆能力，但当彼此相关信息在序列中相距较远时，循环神经网络无法捕捉到数据之中的时序依赖关系。除此之外，当输入序列过长时，循环神经网络也容易出现梯度消失（Gradient Vanishing）或者梯度爆炸（Gradient Exploding）的问题

例如下图，时刻 $t$ 输入数据 $x_t$（文本中的单词）的隐式编码为 $h_t$、其真实输出为 $y_t$（单词词性）、模型预测 $x_t$ 的词性是 $O_t$。参数 $W_x$ 将 $x_t$ 映射为隐式编码 $h_t$、参数 $W_O$ 将 $h_t$ 映射为预测输出 $O_t$、$h_{t-1}$ 通过参数 $W_h$ 参与 $h_t$ 的生成。其中 $W_x$、$W_o$ 和 $W_h$ 是复用参数

![](../../../assets/Pasted%20image%2020250611175747.png)

假设时刻 $t$ 隐式编码根据 $h_t=\text{tanh}(W_xx_t+W_hh_{t-1}+b)$ 得到，使用交叉熵计算时刻 $t$ 预测输出与实际输出的误差 $E_t$，显然，整个序列产生的误差为 $E=\frac{1}{2}\sum\limits_{t=1}^TE_t$

因为在时刻 $t$ 计算 $O_t$ 时不仅涉及到时刻 $t$ 的 $W_x$，也涉及到了前面所有时刻的 $W_x$，按照链式求导法则，需要对前面所有时刻的 $W_x$ 依次求导，再将求导结果进行累加，即：

$$
\frac{\partial E_t}{\partial W_x}=\sum\limits_{i=1}^t\frac{\partial E_t}{\partial O_t}\frac{\partial O_t}{\partial h_t}(\prod\limits_{j=i+1}^t\frac{\partial h_j}{\partial h_{j-1}})\frac{\partial h_i}{\partial W_x}
$$

其中 $\prod\limits_{j=i+1}^t\frac{\partial h_j}{\partial h_{j-1}}=\prod\limits_{j=i+1}^t\text{tanh}'\times W_h$
***
### 长短时记忆模型

> 可以看到对于简单的循环神经网络，由于 tanh 的导数位于 0 到 1，对于长序列而言，多个小数相乘会导致参数求导结果很小，引发梯度消失问题，为了缓解这个问题，长短时记忆模型（Long Short-Term Memory, LSTM）被提出

LSTM 通过引入内部记忆单元（对“历史信息”的累积）和门结构来对当前时刻输入信息以及前序时刻所生成信息进行整合和传递

常见的 LSTM 模型中有输入门（Input Gate）、遗忘门（Forget Gate）和输出门（Output Gate）三种门结构，对于给定的当前时刻输入数据 $x_t$ 和前一时刻隐式编码 $h_{t-1}$ ，输入门、遗忘门和输出门通过各自参数对其编码，分别得到三种门结构的输出 $i_t,f_t$ 和 $o_t$

在此基础上，再进一步结合前一时刻内部记忆单元信息 $c_{t-1}$ 来更新当前时刻内部记忆单元信息 $c_t$ ，最终得到当前时刻的隐式编码 $h_t$

- 输入门：$i_t=\text{sigmoid}(W_{xi}x_t+W_{hi}h_{t-1}+b_i)$
- 遗忘门：$f_t=\text{sigmoid}(W_{xf}x_t+W_{hf}h_{t-1}+b_f)$
- 输出门：$o_t=\text{sigmoid}(W_{xo}x_t+W_{ho}h_{t-1}+b_o)$
- 内部记忆单元：$c_t=f_tc_{t-1}+i_t\text{tanh}(W_{xc}x_t+W_{hc}h_{t-1}+b_c)$
- 隐式编码：$h_t=o_t\text{tanh}(c_t)$

![](../../../assets/Pasted%20image%2020250611181240.png)

对于梯度来说，求导 $c_t=f_tc_{t-1}+i_t\text{tanh}(W_{xc}x_t+W_{hc}h_{t-1}+b_c)$ :

$$
\frac{\partial c_t}{\partial c_{t-1}}=f_t+\frac{\partial f_t}{\partial c_{t-1}}\times c_{t-1}+\cdots
$$

可见，求导结果至少大于等于 $f_t$，即以往们的输出结果，如果遗忘门选择保留旧状态，则这一求导结果就接近 1（或者接近向量 1），使得梯度是存在的，从而避免了梯度消失问题
***
### GRU

> 门控循环单元（Gated Recurrent Unit, GRU）是 LSTM 的一种变体，GRU 通过合并输入门和遗忘门来简化 LSTM 模型

GRU 模型中有更新门（Update Gate）和重置门（Reset Gate）两种门结构，对于给定的当前时刻输入数据 $x_t$ 和前一时刻隐式编码 $h_{t-1}$ ，更新门和重置门通过各自参数对其编码，分别得到两种门结构的输出 $z_t$ 和 $r_t$

设 $x_t$ 为输入向量，$h_t$ 为输出向量，$\hat{h_t}$ 为当前时刻的候选隐式编码，$z_t$ 为更新门输出，$r_t$ 为重置门输出，则 GRU 的计算过程如下：

- 更新门：$z_t=\sigma(W_{z}\cdot[h_{t-1},x_t])$
- 重置门：$r_t=\sigma(W_{r}\cdot[h_{t-1},x_t])$
- 候选隐式编码：$\hat{h_t}=\tanh(W_{h}\cdot[r_t\odot h_{t-1},x_t])$
- 隐式编码：$h_t=(1-z_t)\odot h_{t-1}+z_t\odot \hat{h_t}$


![](../../../assets/Pasted%20image%2020250611181736.png)
***
### Padding

> 在循环神经网络中，输入序列的长度通常是不一致的，因此需要对输入序列进行 Padding 操作，将所有输入序列填充到相同长度

![](../../../assets/Pasted%20image%2020250611182335.png)


- Padding 放后面不好，放前面好，这是因为循环神经网络是按时间序列处理数据的，<font color="red">越往后的信息对最终状态的影响越大</font>
	- 也正因如此，循环神经网络不适合处理无序集（Set）问题，可以通过引入双向循环神经网络十前文和后文的影响差不多 
***
### 双向循环神经网络

> 双向循环神经网络（Bidirectional Recurrent Neural Network, BiRNN）是一种特殊的循环神经网络结构，它通过在时间序列的正向和反向两个方向上同时进行信息处理，从而更好地捕捉序列数据中的上下文信息

![](../../../assets/Pasted%20image%2020250611182446.png)
***
## 图神经网络

- 节点表示：在图神经网络中，每个节点都会有一个向量表示，该向量捕获了与节点相关的特征信息（包括固有属性和结构性特征）
- 边表示：在图神经网络中，边的表示通常是一个向量，捕获了连接两个节点之间的关系信息（例如边的权重、类型、方向等）
- 消息传递：图神经网络的核心是消息传递机制，节点通过边向其邻居发送消息（通常是特征信息的某种变换），并基于收到的消息更新自己的状态。这 个过程通常包括聚合（Aggregation）和更新（Update）两个步骤
	- 聚合函数：聚合函数负责合并多个输入（来自邻居节点的消息）成一个单一的输出，以便更新当前节点的表示。常见的聚合函数包括求和（sum）、均值 （mean）、最大值（max）等
	- 更新函数：更新函数则用于结合节点当前的状态和聚合得到的新信息来生成节点 的新状态。这通常是通过一个神经网络层来实现的，如全连接层或非线性转换层
***
## 注意力与正则化

### 注意力机制

- 首先生成每个单词的内嵌向量（包含了单词在句子中位置编码向量信息），记为 $w_i(1\leq i\leq 4)$，计算每个单词 $w_i$ 的查询向量（Query）、键向量（Key）和值向量（Value）：
	- 查询向量：$q_i=W^q\times w_i$
	- 键向量：$k_i=W^k\times w_i$
	- 值向量：$v_i=W^v\times w_i$
- 对每个单词 $w_i$ 而言，$W^q,W^k$ 和 $W^v$ 三个映射矩阵都是一样的，也是自注意力模型需要训练的全部参数
- 自注意力模型就是要挖掘单词 $w_i$ 与其他单词在句子中因为上下文（context）关联而具有的自注意力取值大小

![](../../../assets/Pasted%20image%2020250611201653.png)

- 也可引入“多头”注意力（Multi-Headed Attention）机制从更多角度来挖掘某个单词与其他单词之间概率关联，但是每个单词自注意力关联可以并行计算
	- 一旦计算得到单词和其他单词所形成的自注意力关联后，Transformer 再将这些自注意力关联通过前向神经网络（feed-forward）进行非线性映射。非线性变换的引入能帮助模型捕捉到更丰富的特征和语义信息，有助于提高模型的表达能力（如更好捕获单词和单词之间复杂的共现概率）
	- 多头注意力机制是由于两个 Token 之间可能存在多种不同类型的关系（如语法关系、语义关系等）
***
### Transformer

不同于传统卷积神经网络使用固定的卷积核（感受野），Transformer 模型使用自注意力来自适应计算感受野

- 原始 Transformer 使用绝对位置编码，这将会与物体本身无关的位置信息“污染”到特征中，但由于数据是海量的，所以仍然有效

Transformer 涉及的主要参数如下：

- Image：$\mathbf{I}\in\mathbb{R}^{C\times N}(N=H\times W)$
	- 绝对位置编码：$\mathbf{I}^{(x,y)}=\mathbf{F}^{(x,y)}+\text{Emb}(x,y)$
- Query：$\mathbf{Q}=\mathbf{W_q}\cdot\mathbf{I}\in\mathbb{R}^{C'\times N},\mathbf{W_q}\in\mathbb{R}^{C'\times C}$
- Key：$\mathbf{K}=\mathbf{W_k}\cdot\mathbf{I}\in\mathbb{R}^{C'\times N},\mathbf{W_k}\in\mathbb{R}^{C'\times C}$
- Scaled Dot Product：$\mathbf{P}=\frac{\mathbf{Q}^T\cdot\mathbf{K}}{\sqrt{C'}}\in\mathbb{R}^{N\times N}$
- Attention：$\mathbf{A}=\text{softmax}(\mathbf{P})\in\mathbb{R}^{N\times N}$
- Value：$\mathbf{V}=\mathbf{W_v}\cdot\mathbf{I}\in\mathbb{R}^{C'\times N},\mathbf{W_v}\in\mathbb{R}^{C'\times C}$
	- Value 没有对方向、距离信息编码
- $\mathbf{F}_a=\sum\limits_{b=1}^N\mathbf{A}_{ab}\times\mathbf{V}_b$，其中 $\mathbf{A}_{ab}$ 表示 patch $a$ 对 patch $b$ 之间的相关性，$\mathbf{V}_b$ 表示 patch $b$ 的表征，最终求和得到以 patch $a$ 为中心的相关区域的表征

![](../../../assets/Pasted%20image%2020250611191107.png)

- 多头注意力：将 Query、Key 和 Value 分别映射到 $h$ 个不同的子空间，得到 $h$ 个不同的注意力矩阵 $\mathbf{A}_i$，然后将这些矩阵拼接起来，得到最终的注意力矩阵 $\mathbf{A}$

![](../../../assets/Pasted%20image%2020250611191312.png)

事实上，Transformer 和卷积区别在于 Transformer 引入了注意力的参数：

![](../../../assets/Pasted%20image%2020250611191814.png)
***
### 神经网络正则化

> 为了缓解神经网络在训练过程中出现的过拟合现象（通常发生在模型参数量过多、数据量不足的时候），需要采取一些正则化技术来提升神经网络的泛化能力

- Dropout：指在训练神经网络的过程中随机丢掉一部分神经元来降低神经网络的复杂度，从而防止过拟合。在实现上，每次迭代训练以一定概率随机屏蔽每一层中的若干神经元，用余下神经元构成的网络继续训练
	
	![](../../../assets/Pasted%20image%2020250611202822.png)
	
- L1 和 L2 正则化：对于具有 $n$ 个训练数据 $\{(x_1,y_1),\cdots,(x_n,y_n)\}$ 的神经网络，加入正则化项后，神经网络的损失函数一般可如下表示：
	
	$$
	\min\frac{1}{n}\sum\limits_{i=1}^n\text{Loss}(y_i,f(\mathbf{W},x_i))+\lambda\times\Phi(\mathbf{W})
	$$
	
	- $f(\mathbf{W},x_i)$ 表示参数为 $\mathbf{W}$ 的神经网络对输入 $x_i$ 的预测
	- $\Phi(\mathbf{W})$ 为正则化项（又称惩罚项），一般用模型参数 $\mathbf{W}$ 的范数形式来表示，假设神经网络模型中参数数目为 $\mathbb{N}$，则参数的范数形式主要有：
		- L0 范数：数学表示为 $\|\mathbf{W}\|_0=\sum\limits_{i=1}^{\mathbb{N}}\mathbb{I}(w_i\neq 0)$，其中 $\mathbb{I}$ 为指示函数，若括号内表达式为真则函数值为 1，否则为 0。$L_0$ 可实现模型参数的稀疏化，但由于 $L_0$ 范数正则化是一个 NPH 问题，难以求解，因此一般不用 $L_0$ 范数
		- L1 范数：数学表示为 $\|\mathbf{W}\|_1=\sum\limits_{i=1}^{\mathbb{N}}|w_i|$，也被称为“稀疏规则算子”（Lasso Regularization）
		- L2 范数：数学表示为 $\|\mathbf{W}\|_2=\sqrt{\sum\limits_{i=1}^{\mathbb{N}}w_i^2}$
	- $\lambda$ 为正则化权重
- 批归一化（Batch Normalization）：通过规范化手段，把神经网络每层中任意神经元的输入值分布改变成均值为 0、方差为 1 的标准正态分布，把偏移较大的分布强制映射为标准正态分布。经过批归一化处理，激活函数的输入值被映射到非线性函数梯度较大的区域，使得梯度变大从而克服梯度消失问题，进而加快收敛速度，其步骤如下：
	1. 计算批次均值：对于给定的一个批次的数据，计算每个特征维度的均值
	2. 计算批次方差：计算每个特征的方差
	3. 规范化：对每个特征进行规范化处理，使得输出的均值接近 0 而方差接近 1，规范化的 $k$ 个特征值 $\hat{x_{ik}}=\frac{x_{ik}-\mu_k}{\sqrt{\sigma_k^2+\epsilon}}$，其中 $\epsilon$ 是一个很小的数，防止分母为 0
	4. 缩放与偏移：对规范化后的数据进行缩放和偏移处理 $y_{ik}=\gamma_k\hat{x_{ik}}+\beta_k$，其中 $\gamma_k$ 和 $\beta_k$ 是可学习的参数，分别代表缩放（Scale）和偏移（Shift）
	5. 反向传播更新参数：在更新网络的权重和偏置时还要更新 $\gamma_k$ 和 $\beta_k$