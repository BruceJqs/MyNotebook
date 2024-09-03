## Divisibility and Modular Arithmetic

### Division

定义：如果 $a$ 和 $b$ 都为整数且 $a\not =0$ ，如果存在一个整数 $c$ 使得 $b=ac$ （或者 $b/a$ 是一个整数），那么称 $a$ 整除 $b$ （用<font color="red"> $a|b$ </font>表示），$a$ 是 $b$ 的一个因子或除数，而 $b$ 是 $a$ 的一个倍数，用<font color="red"> $a\nmid b$ </font>表示 $a$ 不整除 $b$ 。

定理：令 $a,b,c$ 为整数，其中 $a\not= 0$

- 如果 $a|b$ 和 $a|c$ ，那么对任意整数 $m$ 和 $n$ 都有 $a|(mb+nc)$
- 如果 $a|b$ ，那么对所有整数 $c$ 都有 $a|bc$
- 如果 $a|b$，$b|c$，则 $a|c$

### Division Algorithm

除法算法（Division Algorithm）：令 $a$ 为整数，$d$ 为正整数。则存在唯一的整数 $q$ 和 $r$ ，满足 $0\leq r<d$，使得 $a=dq+r$ ，其中 $d$ 称为<font color="red">除数（Divisor）</font>，$a$ 称为<font color="red">被除数（Dividend）</font>，$q$ 称为<font color="red">商（Quotient）（记为 $q=a\space div\space d$）</font>，$r$ 称为<font color="red">余数（Remainder）（记为 $r=a\space mod \space d$）</font>。

### Congruence Relation

定义：如果 $a$ 和 $b$ 为整数而 $m$ 为正整数，则当 $m$ 整除 $a-b$ 时称 $a$ 模 $m$ <font color="red">同余（Congruent）</font> $b$，用式子<font color="red"> $a\equiv b(mod\space m)$ </font>表示，该式子被称为<font color="red">同余式（Congruence）</font>，$m$ 被称为它的<font color="red">模（Modulus）</font>，用<font color="red"> $a\not \equiv b(mod\space m)$ </font>表示 $a$ 和 $b$ 不是模 $m$ 同余的。

定理：令 $a$ 和 $b$ 为整数，$m$ 为正整数

- $a\equiv b(mod\space m) \Leftrightarrow a\space mod\space m=b\space mod \space m \Leftrightarrow \exists k \in \Z,a=b+km$
- 如果 $a\equiv b(mod\space m),c\equiv d(mod\space m)$，则 $a+c\equiv b+d(mod\space m),ac\equiv bd(mod\space m)$（一般地，当 $d=c$ 时，<font color="red">$a+c\equiv b+c(mod\space m),ac\equiv bc(mod\space m)$</font>）
- <font color="red">$(a+b)\space mod \space m=((a\space mod\space m)+(b\space mod \space m))mod\space m$</font>
- <font color="red">$ab\space mod\space m=((a\space mod\space m)(b\space mod \space m))mod\space m$</font>

### Arithmetic Modulo

在 $\Z_m$ 上，即小于 $m$ 的非负整数的集合 $\{0,1,...,m-1\}$ 上定义算术运算，定义这些整数的加法（用<font color="red"> $+_m$ </font>表示）：<font color="red">$a+_mb=(a+b)mod\space m$</font>；定义这些整数的乘法（用<font color="red"> $·_m$ </font>表示）：<font color="red">$a·_mb=(a·b)mod\space m$</font>。这些运算被称为模 $m$ 算术。

模 $m$ 算术满足如下性质：

- 封闭性：如果 $a$ 和 $b$ 属于 $\Z_m$，则 $a+_mb$ 和 $a·_mb$ 也属于 $\Z_m$
- 结合律：如果 $a$ 和 $b$ 属于 $\Z_m$，则 $(a+_mb)+_mc=a+_m(b+_mc),(a·_mb)·_mc=a·_m(b·_mc)$
- 交换律：如果 $a$ 和 $b$ 属于 $\Z_m$，则 $a+_mb=b+_ma,a·_mb=b·_ma$
- 单位元：元素 0 和 1 分别是模 $m$ 加法和乘法的单位元。即如果 $a$ 属于 $\Z_m$，则 $a+_m0=0+_ma=a,a·_m1=1·_ma=a$
- 加法逆元：如果 $a\not =0$ 属于 $\Z_m$，则 $m-a$ 是 $a$ 的模 $m$ 加法逆元，而 0 是其自身的加法逆元。即 $a+_m(m-a)=0,0+_m0=0$
- 分配律：如果 $a,b$ 和 $c$ 属于 $\Z_m$，则 $a·_m(b+_mc)=(a·_mb)+_m(a·_mc),(a+_mb)·_mc=(a·_mc)+_m(b·_mc)$

## Integer Representations and Algorithms

## Primes and Greatest Common Divisors

### Primes

定义：如果一个大于 1 的整数 $p$ 的正因子只是 1 和 $p$，那么这个整数被称为<font color="red">素数（Prime）</font>；大于 1 但又不是素数的正整数被称为<font color="red">合数（Composite）</font>

### The Fundamental Theorem of Arithmetic

算术基本定理（The Fundamental Theorem of Arithmetic）：每一个大于 1 的整数都可以唯一地写为两个或多个素数的乘积，其中素数因子以非递减序排列。（即质因子分解）

### Trial Division

定理：<font color="red">如果 $n$ 是一个合数，那么 $n$ 必有一个素因子小于等于 $\sqrt{n}$</font>

![image-20240407081313449](../../assets/image-20240407081313449.png)

### Infinitude of Primes

定理：<font color="red">存在无穷多个素数</font>

![image-20240407081523338](../../assets/image-20240407081523338.png)

### Mersenne Primes

定义：如果一个素数被表示为 $2^p-1$，其中 $p$ 为素数，那么这个素数被称为<font color="red">梅森素数（Mersenne Primes）</font>

### Distribution of Primes

素数定理（Prime Number Theorem）：<font color="red">当 $x$ 无限增长时，不超过 $x$ 的素数个数（记为 $\pi(x)$）与 $\frac{x}{\ln x}$ 之比趋近于 1。</font>

### Greatest Common Divisor

定义：令 $a$ 和 $b$ 是两个整数，不全为 0。 能使 $d|a$ 和 $d|b$ 的最大整数 $d$ 称为 $a$ 和 $b$ 的<font color="red">最大公约数（Greatest Common Divisor）</font>，记作 <font color="red">$\gcd(a,b)$</font>。

如果整数 $a$ 和 $b$ 的最大公约数是 1，那么称它们是<font color="red">互素的（Relatively Prime）</font>。

更一般地，当 $1\leq i<j\leq n$ 时都有 $\gcd(a_i,a_j)=1$ ，那么称整数 $a_1,a_2,...,a_n$ 是<font color="red">两两互素的（Pairwise Relatively Prime）</font>。

### Least Common Multiple

定义：正整数 $a$ 和 $b$ 的<font color="red">最小公倍数（Least Common Multiple）</font>是能被 $a$ 和 $b$ 整除的最小正整数，记作<font color="red"> $lcm(a,b)$ </font>。

### Prime Factorizations

假设 $a$ 和 $b$ 的质因数分解式（Prime Factorizations）为：

$a=p_1^{a_1}p_2^{a_2}...p_n^{a_n},b=p_1^{b_1}p_2^{b_2}...p_n^{b_n}$

那么 $a$ 和 $b$ 的最大公约数可被表示为：<font color="red">$\gcd(a,b)=p_1^{\min(a_1,b_1)}p_2^{\min(a_2,b_2)}...p_n^{\min(a_n,b_n)}$</font>

最小公倍数可被表示为：<font color="red">$lcm(a,b)=p_1^{\max(a_1,b_1)}p_2^{\max(a_2,b_2)}...p_n^{\max(a_n,b_n)}$</font>

<font color="red">$ab=\gcd(a,b)\times lcm(a,b)$</font>

### Euclidean Algorithm

令 $a=bq+r$，其中 $a,b,q$ 和 $r$ 均为整数。则<font color="red"> $\gcd(a,b)=\gcd(b,r)$</font>

![image-20240409081016436](../../assets/image-20240409081016436.png)

欧几里得算法（Euclidean Algorithm）：辗转相除法求最大公约数。（当 $a\geq b$ 时时间复杂度为 $O(\log\space b)$

### gcds as Linear Combinations

贝祖定理（Bézout’s Theorem）：如果 $a$ 和 $b$ 为正整数，则存在整数 $s$ 和 $t$ 使得 <font color="red">$\gcd(a,b)=sa+tb$</font>，其中 $s$ 和 $t$ 被称为 $a$ 和 $b$ 的<font color="red">贝祖系数（Bézout’s Coefficients）</font>，等式被称为贝祖恒等式。

**e.g. 将 $\gcd(252,198)=18$ 表达为贝祖恒等式。**

![image-20240409085036349](../../assets/image-20240409085036349.png)

由贝祖定理可以推导出如下定理：

- 如果 $a,b$ 和 $c$ 为正整数，使得 $\gcd(a,b)=1$ 且 $a|bc$，则 $a|c$

![image-20240409081243033](../../assets/image-20240409081243033.png)

- 如果 $p$ 是素数，且 $p|a_1a_2...a_n$，其中 $a_i$ 为整数，则对于某个 $i$，$p|a_i$

- 令 $m$ 为正整数，$a,b$ 和 $c$ 为整数。如果 $ac\equiv bc(mod\space m)$ 且 $\gcd(c,m)=1$，则 $a\equiv b(mod\space m)$

![image-20240409081642694](../../assets/image-20240409081642694.png)

## Solving Congruences

### Linear Congruences

定义：具有形式<font color="red"> $ax\equiv b(mod\space m)$</font> 的同余方程（其中 $m$ 为正整数，$a$ 和 $b$ 为整数，$x$ 为变量）被称为<font color="red">线性同余方程（Linear Congruences）</font>

### Inverse of a modulo m

如果存在一个整数 $\overline{a}$，使得 $\overline{a}a\equiv 1(mod\space m)$，那么称整数 $\overline{a}$ 为 $a$ 模 $m$ 的<font color="red">逆（Inverse of $a$ modulo $m$）</font>

定理：如果 $a$ 和 $m$ 为互素的整数且 $m>1$，则 $a$ 模 $m$ 的逆存在。更进一步地，这个模 $m$ 的逆是<font color="red">唯一的</font>。（即存在<font color="red">唯一小于 $m$ </font>的正整数 $\overline{a}$ 是 $a$ 模 $m$ 的逆，并且 $a$ 模 $m$ 的其他每个逆均和 $\overline{a}$ 模 $m$ 同余）

证明：由 $\gcd(a,m)=1$ 及贝祖定理得存在整数 $s$ 和 $t$ 使得 $sa+tm=1$，即 $sa+tm\equiv 1(mod\space m)$，由 $tm\equiv 0(mod\space m)$，则 $sa\equiv 1(mod\space m)$，即 $s$ 为 $a$ 模 $m$ 的逆。

**e.g.1. 找到 3 模 7 的逆。**

![image-20240409084700618](../../assets/image-20240409084700618.png)

**e.g.2. 找到 101 模 4620 的逆。**

![image-20240409084804922](../../assets/image-20240409084804922.png)

### Using Inverses to Solve Congruences

**e.g. 解同余方程 $3x\equiv 4(mod\space 7)$**

由 4.4.2 e.g.1. 得 -2 是 3 模 7 的逆，在同余式两边同乘 -2 得 $-2\times3x\equiv -2\times4(mod\space 7)$，因为 $-6\equiv 1(mod\space 7)$ 且 $-8\equiv 6(mod\space 7)$，所以如果 $x$ 是解，则有 $x\equiv -8\equiv 6(mod\space 7)$

### The Chinese Remainder Theorem

<font color="red">中国剩余定理（The Chinese Remainder Theorem）</font>：令 $m_1,m_2,...,m_n$ 为大于 1 的两两互素的正整数，而 $a_1,a_2,...,a_n$ 是任意整数。则同余方程组
$$
\begin{cases}
x\equiv a_1(mod\space m_1)\\
x\equiv a_2(mod\space m_2)\\
\cdots\\
x\equiv a_n(mod\space m_n)
\end{cases}
$$
有唯一的模 $m=m_1m_2...m_n$ 的解（即存在一个满足 $0\leq x\leq m$ 的解 $x$，而所有其他的解均与此解模 $m$ 同余）

![image-20240409090913357](../../assets/image-20240409090913357.png)

**e.g. 求解同余方程组**
$$
\begin{cases}
x\equiv 2(mod\space 3)\\
x\equiv 3(mod\space 5)\\
x\equiv 2(mod\space 7)
\end{cases}
$$
![image-20240409091141991](../../assets/image-20240409091141991.png)

### Back Substitution

回代方法是另一种求解同余方程组的方法。

**e.g. 求解同余方程组**
$$
\begin{cases}
x\equiv 1(mod\space 5)\\
x\equiv 2(mod\space 6)\\
x\equiv 3(mod\space 7)
\end{cases}
$$
![image-20240409091434369](../../assets/image-20240409091434369.png)

### Computer Arithmetic with Large Integers

假定 $m_1,m_2,...m_n$ 是两两互素的模数，并令 $m$ 为其乘积。根据中国剩余定理可以证明满足 $0\leq a<m$ 的整数 $a$ 可唯一地表示为一个 $n$ 元组，其元素由 $a$ 除以 $m_i$ 的余数组成（$i=1,2,..n$）。即 $a$ 可以唯一地表示为 $(a\space mod\space m_1,a\space mod\space m_2,...,a\space mod\space m_n)$（<font color="blue">被用于处理大整数</font>）

**e.g. 利用模数为 $99,98,97,95$ 来寻找 $123684$ 和 $413456$ 的和。**

![image-20240409092458896](../../assets/image-20240409092458896.png)

### Fermat's Little Theorem

<font color="red">费马小定理（Fermat's Little Theorem）</font>：如果 $p$ 为素数，$a$ 是一个不能被 $p$ 整除的整数，则 $a^{p-1}\equiv 1(mod\space p)$。更一般地，对每个整数 $a$ 都有 $a^p\equiv a(mod\space p)$。

**e.g. 求 $7^{222}\space mod \space 11$**

![image-20240409092924616](../../assets/image-20240409092924616.png)

### Pseudoprimes

定义：令 $b$ 是一个正整数。如果 $n$ 是一个正合数且 $b^{n-1}\equiv 1(mod\space n)$，则 $n$ 称为以 $b$ 为基数的<font color="red">伪素数（Pseudoprimes）</font>

卡米切尔数（Carmichael Numbers）：一个正合数 $n$ 如果对于所有满足 $\gcd(b,n)=1$ 的正整数 $b$ 都有同余式 $b^{n-1}\equiv 1(mod\space n)$ 成立，则被称为卡米切尔数。

**e.g. 561 是一个卡米切尔数。**

![image-20240409093536284](../../assets/image-20240409093536284.png)