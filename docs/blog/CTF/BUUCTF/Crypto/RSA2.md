# RSA2

## Tag

RSA 已知 n, e, dp, c

***

## Writeup

已知条件为 $dp\equiv d(\text{mod }p-1)$，那么有 $e*dp\equiv ed(\text{mod }p-1)$，即 $ed=k_1(p-1)+e*dp$，再由 $ed\equiv 1(\text{mod }(p-1)(q-1))$ 可以得到 $ed=k_2(p-1)(q-1)+1$，两式相减得到 $(p-1)[k_2(q-1)-k_1]+1-e*dp=0$

令 $x=k_2(q-1)-k_1$，那么有 $(p-1)x+1-e*dp=0$，由 $dp<p-1$，则有 $e>x$，即 $x\in(1,e)$，遍历枚举即可：

