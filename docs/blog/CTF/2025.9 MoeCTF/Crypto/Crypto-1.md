# Crypto-1｜ez_DES

## Tag

对称加密 DES，爆破
***
## Writeup

知道 DES 是一个对称加密算法就完事了，且 key 只有三位未知，那还说啥了，开爆！

```python
from Crypto.Cipher import DES
import string
import itertools

c = b'\xe6\x8b0\xc8m\t?\x1d\xf6\x99sA>\xce \rN\x83z\xa0\xdc{\xbc\xb8X\xb2\xe2q\xa4"\xfc\x07'
characters = string.ascii_letters + string.digits + string.punctuation
l = 8

def decrypt(ciphertext, key):
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted = cipher.decrypt(ciphertext)
    try:
        text = decrypted.decode('utf-8', errors='ignore')
        return text
    except:
        return ""

count = 0
for iter in itertools.product(characters, repeat=3):
    key = b'ezdes' + ''.join(iter).encode('utf-8')
    
    plaintext = decrypt(c, key)
    if 'moectf{' in plaintext:
        print(f"\n[+] Key: {key}")
        print(f"[+] Flag: {plaintext}")
        break
```

得到最终 flag：`moectf{_Ju5t envmEra+e.!}`