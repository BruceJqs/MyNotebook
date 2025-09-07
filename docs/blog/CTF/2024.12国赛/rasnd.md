---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
# comments: true
--- 

# Crypto｜rasnd

## 做题感想

其实前半部分很快就搞定了，后半部分还是靠 wsgg 的提醒解决的 www

又因为想囤 flag 被动态 flag 制裁了……（这个故事告诉我们不要囤 flag）
***
## Writeup

观察题给程序，flag 被分成两部分输出

对于第一个问题，我们有以下等式：

$$
\begin{cases}
x_1*p+y_1*q=\text{hint}_1+\text{0x114}\\
x_2*p+y_2*q=\text{hint}_2+\text{0x514}\\
\end{cases}
$$

注意到 $x_1$ 和 $x_2$ 量级都比较小，我们考虑直接枚举爆破，消元 $p$ 我们有 $x_2(\text{hint}_1+\text{0x114})-x_1(\text{hint}_2+\text{0x514})=(y_1x_2-y_2x_1)q$

左边在枚举爆破时都是已知的，而我们还有 $n=pq$，那么我们取两者最大公约数即可得 $q$ 的值

```python title="Solution1.py"
hint1 = hint1 + 0x114
hint2 = hint2 + 0x514
e = 0x10001
for x1 in range(2 ** 11 + 1):
    for x2 in range(2 ** 11 + 1):
        temp = x2 * hint1 - x1 * hint2
        if temp <= 0:
            temp = - temp
        q = math.gcd(n, temp)
        if(q == 1):
            continue
        if isprime(q):
            p = n // q
            print("q = ", q)
            print("p = ", p)
            phi = (p - 1) * (q - 1)
            d = pow(e, -1, phi)
            m = pow(c, d, n)
            print(long_to_bytes(m))
            print("\n")
```
***
对于第二个问题，我们有 $(514p-114q)^{n-p-q}=(514p-114q)^{\phi(n)-1}\equiv\text{hint}(\text{mod }N)$

而对此我们有 $(514p-114q)^{\phi(n)}=1(\text{mod }N)$，所以就有 $\text{hint}\equiv(514p-114q)^{-1}(\text{mod }N)$，即可求得 $514p-114q$ 的值，设 $\text{temp}=514p-114q$

然后我们两边同时乘 $q$，有 $\text{temp}\times q=514pq-114q^2=514n-114q^2$，这便是关于 $q$ 的一个一元二次方程，解这个方程就可以得到 $q$ 的值

```python title="Solution2.py"
temp = pow(hint, -1, n)
q = (- temp + math.isqrt(temp ** 2 + 4 * 114 * 514 * n)) // 2 // 114
p = n // q
phi = (p - 1) * (q - 1)
d = pow(e, -1, phi)
m = pow(c, d, n)
print(long_to_bytes(m))
```