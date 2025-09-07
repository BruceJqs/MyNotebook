---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
# comments: true
---  
# Crypto-8｜ezlegendre

## 复盘心得

hhh 又是一个新的数学知识，Crypto 就是天天学数学（bushi
***
## Writeup

观察所给代码：

```python
from sympy import *
from Crypto.Util.number import *

p = getPrime(128)
a = randprime(2, p)

FLAG = b'moectf{xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx}'


def encrypt_flag(flag):
    ciphertext = []
    plaintext = ''.join([bin(i)[2:].zfill(8) for i in flag])
    for bit in plaintext:
        e = randprime(2, p)
        n = pow(int(bit) + a, e , p)
        ciphertext.append(n)
    return ciphertext

print(encrypt_flag(FLAG))
```

可以看出这是一个根据 flag 转为二进制一位一位地进行加密操作，将该位 $i$ 执行 $(a+i)^e\text{ mod }p$ 获得加密信息。

我们需要学一个船新的数学知识（也正是题目所指的 Legendre）：[Legendre 符号](https://oi-wiki.org/math/number-theory/quad-residue/#legendre-%E7%AC%A6%E5%8F%B7)

在知道 Legendre 符号之前我们先来说说什么是[二次剩余](https://oi-wiki.org/math/number-theory/quad-residue/#%E5%AE%9A%E4%B9%89)：

!!! note "二次剩余"

	令整数 $a,p$ 满足 $(a,p)=1$，若存在整数 $x$ 使得 $x^2\equiv a(\text{mod }p)$，则称 $a$ 为模 $p$ 的二次剩余，否则称 $a$ 为模 $p$ 的二次非剩余。

以及判断二次剩余的方法：Euler 判别法

对奇素数 $p$ 和满足 $(p,a)=1$ 的整数 $a$：

- $a$ 是 $p$ 的二次剩余当且仅当 $a^{\frac{p-1}{2}}\equiv 1(\text{ mod } p)$
- $a$ 是 $p$ 的二次非剩余当且仅当 $a^{\frac{p-1}{2}}\equiv -1(\text{ mod } p)$

证明见 [OI Wiki](https://oi-wiki.org/math/number-theory/quad-residue/#euler-%E5%88%A4%E5%88%AB%E6%B3%95)～

!!! note "Legendre Symbol"

	对于奇素数 $p$ 和整数 $a$，定义 Legendre 符号如下：
	
	$$
	\Big(\frac{a}{p}\Big)=\begin{cases}
	0,p|a\\
	1,(p\nmid a)\land((\exists x\in\mathbb{Z}),a\equiv x^2(\text{mod }p))\\
	-1,\text{otherwise}
	\end{cases}
	$$
	

我们这里需要知道它的一个性质，即为[完全积性](https://oi-wiki.org/math/number-theory/basic/#%E7%A7%AF%E6%80%A7%E5%87%BD%E6%95%B0)：$\Big(\frac{a_1a_2}{p}\Big)=\Big(\frac{a_1}{p}\Big)\Big(\frac{a_2}{p}\Big)$

那么我们有 $\Big(\frac{a^e}{p}\Big)=\Big(\frac{a}{p}\Big)^e$

而由程序我们知道 $e$ 是一个奇素数，那么就有 $\text{sgn}(\Big(\frac{a^e}{p}\Big))=\text{sgn}(\Big(\frac{a}{p}\Big)^e)$

程序设置的 $a$ 和 $p$ 也很有来头，根据 Euler 判别法我们可以得知 $a$ 为 $p$ 的二次非剩余，$a+1$ 为 $p$ 的二次剩余，那么正好，只要加密结果的 Legendre 符号为 -1 用的底数就是 $a$，Legendre 符号为 1 用的底数就是 $a+1$，编写 Python 程序如下：

```python
from Crypto.Util.number import *

'''
p = 303597842163255391032954159827039706827
a = 34032839867482535877794289018590990371
ciphertext = [...]
'''

msg_binary = ''
for i in range(len(ciphertext)):
    if pow(ciphertext[i], (p - 1) // 2, p) == 1:
        msg_binary += '1'
    else:
        msg_binary += '0'
        
flag = long_to_bytes(int(msg_binary,2))
print(flag)
```

运行即可得到 flag：`moectf{minus_one_1s_n0t_qu4dr4tic_r4sidu4_when_p_mod_f0ur_equ41_to_thr33}`
