# Crypto-3｜ezBSGS

## Tag

求解离散对数，Baby-Step Giant-Step 算法
***
## Writeup

题目很简单，即求解 $g^x\equiv y(\mod p)$，我们有 Baby-Step Giant-Step 算法：

将指数分解为 $x = im + j$，其中 $m = \lceil \sqrt{p-1} \rceil$

步骤：

1. Baby step：预计算并存储 $g^j \mod p$，其中 $j = 0, 1, ..., m-1$，构建哈希表：$\text{table}[g^j] = j$
2. Giant step：计算 $h · (g^{-m})^i$，其中 $i = 0, 1, ..., m-1$，检查结果是否在哈希表中，如果找到匹配，则 $x = im + j$

这样就可以将时间复杂度控制在 $O(\sqrt{p})$，Payload 如下：

```python
import math

g = 13
y = 114514
p = 100000000000099

m = math.isqrt(p - 1) + 1

table = {}
power = 1
for j in range(m):
    if power not in table:
        table[power] = j
    power = (power * g) % p

g_inv_m = pow(g, -m, p)
gamma = y
for i in range(m):
    if gamma in table:
        x = i * m + table[gamma]
        print(f"\n[*] Flag: moectf{{{x}}}")
        break
    gamma = (gamma * g_inv_m) % p
```

事实上，python 的 sympy 库内置了离散对数函数，可以直接调用开挂：

```python
from sympy.ntheory import discrete_log

base = 13
target = 114514
modulus = 100000000000099

x = discrete_log(modulus, target, base)

print(f"\n[+] Flag: moectf{{{x}}}")
```

运行即可得到 flag：`moectf{18272162371285}`