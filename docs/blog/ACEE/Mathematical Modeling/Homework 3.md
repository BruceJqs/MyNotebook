---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
--- 
## Homework 03

### Question 01

![](../../../assets/Pasted%20image%2020241106203613.png)

（1）我们用 0,1 来表示开关的状态，0 表示开，1 表示关。

此时所有的开关状态可以被表示为一个长度为 $n$ 的 01 串，对于这个串一共有 $2^n$ 种可能，其中 $\underbrace{11...1}_{n个1}$ 表示开启电灯的状态。

每按一次开关能使状态对应一个新的字符串，故至少需要 $2^n-1$ 次才能确保开启电灯。 

（2）即我们需要一个长度为 $n$ 的 01 串的排列，使得每两个 01 串之间只有一位不同，这便是格雷码，因此 $n$ 位格雷码便是答案。

例如当 $n=4$ 时，我们有：

$$
\begin{aligned}
\text{0000}&\Leftrightarrow\text{0001}\Leftrightarrow\text{0011}\Leftrightarrow\text{0010}\Leftrightarrow\text{0110}\Leftrightarrow\text{0111}\Leftrightarrow\text{0101}\Leftrightarrow\text{0100}\\
&\Leftrightarrow\text{1100}\Leftrightarrow\text{1101}\Leftrightarrow\text{1111}\Leftrightarrow\text{1110}\Leftrightarrow\text{1010}\Leftrightarrow\text{1011}\Leftrightarrow\text{1001}\Leftrightarrow\text{1000}\Leftrightarrow\text{0000}
\end{aligned}
$$
***
### Question 02

![](../../../assets/Pasted%20image%2020241106210734.png)

对 $i=1,2,3,4,5,6$，从第 $i$ 堆硬币中取 $2^i-1$ 枚，合在一起称重。由于集合 $S=\{1, 2, 4, 8, 16, 32\}$ 任意两个子集的元素之和均不相同，由子集元素之和即可唯一确定子集。因此根据取出的 $63$ 枚硬币质量与 $6300$ 克的差即可判断出伪币所在的堆。

若每堆仅有 $24$ 枚硬币，取 $S = \{11, 17, 20, 22, 23, 24\}$ 。不难验证，$S$ 中任意含 $i + 1$ 个元素的子集元素之和大于含 $i$ 个元素的子集之和。含相同个数元素的子集元素之和也不相等。因此，由子集元素之和仍可唯一确定子集。称量方案仍存在。