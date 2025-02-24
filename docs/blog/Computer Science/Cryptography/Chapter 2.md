---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
--- 

# Chapter 02 : 古典密码

> 加密过程（Encryption）为明文经过密钥通过加密算法进行加密变为密文的过程
> 
> 解密过程（Decryption）为密文解密还原成明文的过程

## 单表密码

> 单表密码只使用一张密码字母表，且明文字母与密文字母有固定的对应关系，我们可以使用频率分析法可以解决单表密码

### 加法密码

典型例子：凯撒加密

- 加密：$c = (p-$'$A$'$+3)\text{ mod }26+$'$A$'
- 解密：$p = (c-$'$A$'$-3)\text{ mod }26+$'$A$' 或 $p = (c-$'$A$'$+23)\text{ mod }26+$'$A$'
***
### 乘法密码

- 加密：$c = p\times k\text{ mod }n$
- 解密：$p = c\times k^{-1}\text{ mod }n$，其中 $k^{-1}$ 为 $k$ 的乘法逆元
***
### 仿射密码

- 加密：$c = (p\times k_1+k_2)\text{ mod }n$
- 解密：$p = (c-k_2)\times k_1^{-1}\text{ mod }n$
***
## 多表密码

> 多表密码是对每个明文字母采用不同的单表代换，即同一明文字母对应多个密文字母

典型例子：[Playfair](https://en.wikipedia.org/wiki/Playfair_cipher)、[Vigenere](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher)、[Beaufort](https://en.wikipedia.org/wiki/Beaufort_cipher)、[Vernam](https://en.wikipedia.org/wiki/One-time_pad)、[Hill](https://en.wikipedia.org/wiki/Hill_cipher)、[Enigma](https://en.wikipedia.org/wiki/Enigma_machine)

