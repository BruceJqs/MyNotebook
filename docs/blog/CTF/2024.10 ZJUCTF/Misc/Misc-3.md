---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
---  

# Misc｜小 A 口算

## 做题历程 & 感想

紧跟潮流 hhh，其实说白了还是一个对 websocket, pwntools 还有 py 程序编写的基本功，本质不难 Bruce 一把代码就过了～凌晨一点收工睡觉明天再战！（瞬间有信心了）
***
## Writeup

其实很简单，连一下 websocket 就会发现是前不久刚火的小猿口算（CTF 版）

编程序的时候对牢行数把题目扒下来 if 一下再传回去就好了～EZ～程序如下：

```python
from pwn import *
from wstube import websocket

context.log_level = 'debug'

p = websocket("wss://ctf.zjusec.com/api/proxy/ad8571c7-0b06-413e-b642-bce4169f40a1")

p.recvuntil("Input your choice: ")
p.sendline("1")

p.recvline()
p.recvline()

i = 0
while(i <= 10000):
    p.recvline()
    text = p.recvline()
    text = text.decode()
    p.recvuntil("input '>', '<' or '=' : ")
    index = text.find("?")
    a = int(text[:index-1])
    b = int(text[index+2:])
    if (a > b):
        p.sendline(">")
    elif (a < b):
        p.sendline("<")
    else:
        p.sendline("=")
    p.recvline()
    i += 1
```

这里不知道到底要做对几道题才能给 flag 就把上限设置的高了点然后让它强行报错（所以这是个大漏洞危险程序 hhh） debug 翻一翻就能看到 flag：`ZJUCTF{WoW_K1n6_0F_5h0-g4Ku-s31_4r1thm3t1c}`

![](../../../../assets/Pasted%20image%2020241016011122.png)