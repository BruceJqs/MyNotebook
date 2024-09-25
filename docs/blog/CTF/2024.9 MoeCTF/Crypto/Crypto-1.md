---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
---  

# Crypto-1｜现代密码学入门指北

## 做题历程 & 感想

这道题与[短学期 lab0 Crypto Challenge-2](https://brucejqs.github.io/MyNotebook/blog/CTF/2023-2024%E6%9A%91%E7%9F%AD%E5%AD%A6%E6%9C%9F/Lab0%20Report/#challenge-2_3) 完全相同，是一个非常基本的 RSA，公钥加密私钥解密。

所以 Bruce 毫不费力地把它秒啦～
***
## Writeup

![](../../../../assets/Pasted%20image%2020240925144532.png)

编写 python 程序如下：

``` python
from Crypto.Util.number import long_to_bytes

n = 40600296529065757616876034307502386207424439675894291036278463517602256790833
p = 197380555956482914197022424175976066223
q = 205695522197318297682903544013139543071
c = 36450632910287169149899281952743051320560762944710752155402435752196566406306
e = 65537

phi = (p - 1) * (q - 1)
d = pow(e, -1, phi)
m = pow(c, d, n)
print(long_to_bytes(m))
```

运行即可得到 flag：`moectf{the_way_to_crypto}`