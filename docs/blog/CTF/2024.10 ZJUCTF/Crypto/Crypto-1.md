---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
---  

# Crypto｜ezxor

## 做题历程 & 感想

好神奇一题 hhh，题还没做完呢 flag 就能猜出来了(bushi)

充分证明 Bruce Crypto 还是玩不明白……
***
## Writeup

根据给出的 ezxor.py：

```python
plain = 'Romance in the mundane world is like a starry sky admired from a bustling city.'
flag  = r'ZJUCTF{***************************}'

plain += flag

assert  100 < len(plain) < 128

import random
random.seed(flag)

cipher = ''
for i in range(len(plain)):
    cipher += bin(ord(plain[i]))[2:].zfill(8)

for i in range(len(cipher)):
    tmp = int(cipher[i])
    for j in range(i, len(cipher)):
        tmp ^= int(cipher[j])
    cipher = cipher[:i] + str(tmp) + cipher[i+1:]

for _ in range(20):
    random_index = random.randint(0, len(cipher)-1)

    cipher = cipher[:random_index] + ('1' if cipher[random_index] == '0' else '0') + cipher[random_index+1:]

print(cipher)
# 01100011101101011011011000000011101101000101001001000110001111101011000110010100001111111010011110110000010001100011111110110110010110011011010001000111101111100100101110111001110000000101101001001010010111000100100011000111110000000000111001011101111000000100100001001110010011011011100111000000010000011100000001011101101001111011111001011100010111100101000111000000010111011011001001010001110000000100000110111000010010011011000110100011101110011011100010111111101110111010001110110101101101100011111110111110001110111011110001011001101000100101100001001000010011100100101110111010001111111011110110110001101001111010111000110100011011010111001110011001100000101110011110000100010100100110011110111001101101111011011110010101101110000100101000101011101110011100000110010101100110100100011001001000110000101100101001001001101110011001010110100111101101011001010110010001100011000110011001111101100110000111101110010101110111000010100000100011110110000011111001010110
```

可以首先看出加密过程分为三个板块：

- cipher = plain + flag 转换为二进制
- 将 cipher 的每一位异或从自己开始到最后的每一位
- 随机挑选 20 个幸运位反转

这个随机真是要了命啊诶哟～

Bruce 怀着试试的心态先不管反转这回事把密文逆回去：

很容易想到这个密文必须从后往前一位一位逆出来，首先发现第二板块异或操作连自己都异或了，这点很重要，相当于是默认 0 在和后面的所有位异或，这就导致事实上我们仅仅通过自己和后面这些位是无法得到当前位到底是什么东西的（因为 `1 ^ 1 = 0 ^ 0 = 0`），所以我们需要看前一位，前一位的默认 0 和自己和后面这些位异或得到了前一位的密文，因为后面这些位我们是从后往前一位一位推出来的（意思就是这些位已经已知），这样我们就可以得到当前位是什么，用数学语言来描述就是：

$$
\begin{gather}
\because 0\oplus ans[i]\oplus ans[i+1]\oplus ...\oplus ans[len(cipher)-1]=cipher[i-1]\\
\therefore ans[i]=0\oplus cipher[i-1]\oplus ans[i+1]\oplus ...\oplus ans[len(cipher)-1]
\end{gather}
$$

编写 python 程序如下：

```python
cipher = "01100011101101011011011000000011101101000101001001000110001111101011000110010100001111111010011110110000010001100011111110110110010110011011010001000111101111100100101110111001110000000101101001001010010111000100100011000111110000000000111001011101111000000100100001001110010011011011100111000000010000011100000001011101101001111011111001011100010111100101000111000000010111011011001001010001110000000100000110111000010010011011000110100011101110011011100010111111101110111010001110110101101101100011111110111110001110111011110001011001101000100101100001001000010011100100101110111010001111111011110110110001101001111010111000110100011011010111001110011001100000101110011110000100010100100110011110111001101101111011011110010101101110000100101000101011101110011100000110010101100110100100011001001000110000101100101001001001101110011001010110100111101101011001010110010001100011000110011001111101100110000111101110010101110111000010100000100011110110000011111001010110"
plain = 'Romance in the mundane world is like a starry sky admired from a bustling city.'
ans = cipher

for i in range(len(cipher) - 1, 0, -1):
    temp = 0
    for j in range(i + 1, len(cipher)):
        temp ^= int(ans[j])
    temp ^= int(cipher[i-1])
    ans = ans[:i] + str(temp) + ans[i+1:]
    
binary_values = [ans[i:i+8] for i in range(0, len(ans), 8)]
ascii_characters = [chr(int(bv, 2)) for bv in binary_values]
ascii_string = ''.join(ascii_characters)
print(ascii_string)
```

运行得到结果：

![](../../../../assets/Pasted%20image%2020241017002532.png)

 根据给出的不带 flag 的 plain 可以看到有很多字符已经对了，无非就是那几个幸运位反转导致奇怪的字符诞生了。我们关注后面属于 flag 的这一部分，根据题目描述完全就是英文单词，大胆猜测 flag 为 `ZJUCTF{Well_done!_Welcome_to_ZJUCTF_2024!}` 提交，过了！

![](../../../../assets/Pasted%20image%2020241017002916.png)

玄学～