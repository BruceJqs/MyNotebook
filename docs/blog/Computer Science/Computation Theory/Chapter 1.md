# Chapter 1 : Sets, Relations and Languages

## Sets & Relations & Functions

基本和离散内容一致，详情请见[离散笔记-集合&函数](https://note.eternity1005.top/blog/Math/Discrete%20mathmatics/Discrete%20mathmatics%20notes-Ch02/#sets)和[离散笔记-关系](https://note.eternity1005.top/blog/Math/Discrete%20mathmatics/Discrete%20mathmatics%20notes-Ch09/#relations-and-their-properties)，补充点如下：

1. $A$ 的幂集可以用 $2^A$ 来表示
2. 逆关系：$R\subseteq A\times B\Leftrightarrow R^{-1}\subseteq B\times A$
***
## Alphabet and Language

数据在计算机的内存中被编码为比特串或其他适合操作的符号，计算理论的数学研究必须要从理解符号字符串的数学原理开始。
***
### Alphabet

定义：任何有限集都被称为字母表，字母表的元素被称为字母表的符号（Symbol），我们 $\Sigma$ 来表示字母表。

其中，有限集 $\{0,1\}$ 被称为二进制字母表，一般认为空集不能为字母表
***
### Strings

定义： 我们称字母表 $\Sigma$ 中符号的有限序列为 $\Sigma$ 的字符串（String）或单词（Word）

- 字母表 $\Sigma$ 不包含任何符号的空字符串，记为 $e$，长度为 0
- 字母表 $\Sigma$ 组成的所有字符串的集合记为 $\Sigma^*$
- 字符串 $w$ 的长度（Length）即序列长度，记作 $|w|$

字符串有如下操作：

1. 拼接（Concatenation）：对于字符串 $w_1$ 和 $w_2$，它们的拼接记作 $w_1w_2$ 或 $w_{1}\circ w_{2}$，表示将 $w_2$ 附加到 $w_1$ 的末尾形成的新字符串
	- 当且仅当 $|w|=|x|+|y|,w(j)=x(j)(j=1,\cdots,|x|)$ 且 $w(|x|+j)=y(j) (j=1,\cdots,|y|)$时，$w=x\circ y$
	- $\forall w,we=ew=w$
	- 满足结合律，即 $(wx)y=w(xy)$
	- 当且仅当存在字符串 $x,y$，满足 $w=xvy$，称字符串 $v$ 为 $w$ 的子串（Substring）
	    - $w=xv\rightarrow v$ 是 $w$ 的后缀（Suffix）
	    - $w=vy\rightarrow v$ 是 $w$ 的前缀（Prefix）
2. 幂（Exponentiation）：字符串 $w$ 的 $n$ 次幂记作 $w^n$，满足 $w^{i+1}=w^n\circ w,i\geq 0,w^0=e$
3. 反转（Reversal）：字符串 $w$ 的反转记作 $w^R$，满足 $e^R=e,(aw)^R=w^Ra,a\in \Sigma$
***
### Language

定义：字母表 $\Sigma$ 上的语言（Language）是 $\Sigma^*$ 的任意子集，记作 $L\subseteq \Sigma^*$

- $\Sigma,\Sigma^*,\phi$ 都是语言
- 有限语言（Finite Language）：包含有限个字符串的语言
- 无限语言（Infinite Language）：包含无限个字符串的语言，可以被表示为 $L=\{w\in\Sigma^*:w\text{ has property P}\}$，e.g. $L=\{\text{ab},\text{aabb},\text{aaabbb},\cdots\}=\{a^nb^n|n\geq 1\}$






