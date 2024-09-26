---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
---  
# Crypto-5｜baby_equation

## 做题历程 & 感想

初高中学的因式分解忘得一干二净……还好还有 ~~残存的强大数感~~ （bushi

dfs 忘得一干二净（调了半天才调出来
***
## Writeup

阅读所给的程序：

```python
from Crypto.Util.number import *
from secret import flag


l = len(flag)
m1, m2 = flag[:l//2], flag[l//2:]
a = bytes_to_long(m1)
b = bytes_to_long(m2)
k = 0x2227e398fc6ffcf5159863a345df85ba50d6845f8c06747769fee78f598e7cb1bcf875fb9e5a69ddd39da950f21cb49581c3487c29b7c61da0f584c32ea21ce1edda7f09a6e4c3ae3b4c8c12002bb2dfd0951037d3773a216e209900e51c7d78a0066aa9a387b068acbd4fb3168e915f306ba40
assert ((a**2 + 1)*(b**2 + 1) - 2*(a - b)*(a*b - 1)) == 4*(k + a*b)
```

下意识我们把下面那丑陋的式子改写一下（因式分解全靠数感：

$$
\begin{aligned}
(a^2+1)(b^2+1)-2(a-b)(ab-1)&=4(k+ab)\\
\Leftrightarrow a^2b^2+a^2+b^2+1-2a^2b+2ab^2+2a-2b&=4k+4ab\\
\Leftrightarrow a^2b^2+a^2+b^2+1-2a^2b+2ab^2+2a-2b-4ab&=4k\\
\Leftrightarrow (a^2+2a+1)(b^2-2b+1)&=4k\\
\Leftrightarrow (a+1)^2(b-1)^2&=4k
\end{aligned}
$$

看着舒服多了～

那么这道题就比较明朗了，我们把 $4k$ 分解质因数，然后拼出两个完全平方数的乘积，$a,b$ 也就迎刃而解了～

我们用短学期 TA 给的质因数分解网站 [Integer factorization calculator](https://www.alpertron.com.ar/ECM.HTM) （有的时候在大数分解比题目提示的 yafu 更好）可以得到如下信息：

![](../../../../assets/Pasted%20image%2020240926115740.png)

因为 $a,b$ 是源于 flag 的，代表着至少 $a$ 是有一定限制的（在这道题里面 flag 前六位是 `moectf`）根据这样的信息我们可以编写 python 程序（这里我们多猜了一个 `flag`）：

```python
root = 8699621268124163273600280057569065643071518478496234908779966583664908604557271908267773859706827828901385412151814796018448555312901260592
factor = [2, 2, 2, 2, 3, 3, 31, 61, 223, 4013, 281317, 4151351, 339386329, 370523737, 5404604441993, 26798471753993, 25866088332911027256931479223, 64889106213996537255229963986303510188999911]
visit = [False for i in range(len(factor))]

def trans(num):
    hexnum = hex(num)[2:]
    if(len(hexnum) % 2 == 1):
        hexnum = '0' + hexnum
    ascii = bytes.fromhex(hexnum).decode('ascii')
    return ascii

def check(num):
    hexnum = hex(num)[2:]
    if(len(hexnum) % 2 == 1):
        hexnum = '0' + hexnum
    for i in range(len(hexnum)-2, -1, -2):
        if int(hexnum[i:i+2], 16) > 127:
            return False
    ascii = bytes.fromhex(hexnum).decode('ascii')
    if(ascii[:7] == 'moectf{' or ascii[:5] == 'flag{'):
        return True

def dfs(cur, index):
    if(check(cur - 1)):
        print(trans(cur - 1) + trans(root // cur + 1))
        exit()
    for i in range(index + 1, len(factor)):
        if(not visit[i]):
            visit[i] = True
            cur = cur * factor[i]
            dfs(cur, i)
            visit[i] = False
            cur = cur // factor[i]

dfs(2, 0)
```

运行即可得到 flag：`moectf{7he_Fund4m3nt4l_th30r3m_0f_4rithm3tic_i5_p0w4rful!}`
