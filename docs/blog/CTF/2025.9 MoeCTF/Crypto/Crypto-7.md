# Crypto-7｜ezlegendre

## Tag

Legendre 符号，详见 [2024.9 MoeCTF ezlegendre](https://note.eternity1005.top/blog/CTF/2024.9%20MoeCTF/Crypto/Crypto-8/)
***
## Writeup

题目所给的 a 和 p 满足 a 是 p 的二次剩余，且 $a+i(i=1,\dots,10)$ 均是 p 的非二次剩余，那么就可以写 payload：

```python
from Crypto.Util.number import *

p = 258669765135238783146000574794031096183
a = 144901483389896508632771215712413815934
ciphertext = [...]

msg_binary = ''
for i in range(len(ciphertext)):
    if pow(ciphertext[i], (p - 1) // 2, p) == 1:
        msg_binary += '0'
    else:
        msg_binary += '1'

flag = long_to_bytes(int(msg_binary,2))
print(flag)
```

最终得到 flag：`moectf{Y0u_h@v3_ju5t_s01v3d_7h1s_pr0b13m!}`