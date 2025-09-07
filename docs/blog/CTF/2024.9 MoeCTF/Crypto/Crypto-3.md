---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
# comments: true
---  

# Crypto-3｜ez-hash

## 做题历程 & 感想

看到这题让 Bruce 想起短学期 TA 给过的某个强大工具（当时作为 PoW(Power of Work) TA 并没有解释只是让 Bruce 直接贴上代码直接跳过进入正题）

在这里能派上用场啦！

但还是因为 Bruce 不好好看题导致还是耗了不少时间 qwq
***
## Writeup

阅读题目所给程序：

``` python
from hashlib import sha256
from secret import flag, secrets

assert flag == b'moectf{' + secrets + b'}'
assert secrets[:4] == b'2100' and len(secrets) == 10
hash_value = sha256(secrets).hexdigest()
print(f"{hash_value = }")
# hash_value = '3a5137149f705e4da1bf6742e62c018e3f7a1784ceebcb0030656a2b42f50b6a'
```

可以看出这是一道让我们算出 secrets 的后六位从而使得 secrets 经过 sha256 加密后为 hash_value，我们有一个非常强大的解题器：python mbruteforce！它能帮助我们直接进行爆破（虽然这道题强行枚举问题也不是很大）

值得注意的是，题目描述为：

![](../../../../assets/Pasted%20image%2020240926104022.png)

这是一个联系方式！也就意味着 secrets 全是数字（Bruce 就是没看清这个导致爆破了好久才发现

编写 python 程序如下：

```python
from pwn import *
from pwnlib.util.iters import mbruteforce
from hashlib import *

hash_value = '3a5137149f705e4da1bf6742e62c018e3f7a1784ceebcb0030656a2b42f50b6a'
ans = mbruteforce(lambda x: sha256(b'2100'+ x.encode()).hexdigest() == hash_value, string.digits, length = 6)
print(ans)
```

运行即得 secrets 后六位，拼接即可得到 flag：`moectf{2100360168}`
