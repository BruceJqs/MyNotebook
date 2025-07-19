---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
---  

# Return-to-libc

## 任务 1：找出 libc 函数的地址

使用批处理的方法，我们可以得到 system 函数和 exit 函数的地址：

![](../../../../../assets/Pasted%20image%2020250719084237.png)
***
## 任务 2：将 Shell 字符串放入内存

编译代码并运行：

![](../../../../../assets/Pasted%20image%2020250719085713.png)

可以看到，我们得到了 `/bin/sh` 字符串的地址
***
## 任务 3：发起攻击

运行代码我们可以得知 ebp 和 buffer 的地址：

![](../../../../../assets/Pasted%20image%2020250719103937.png)

因为跳转后 ebp 变为 ebp + 4，由此我们可以知道 Y 的值（即跳转地址）为 `0xffffce68 - 0xffffce50 + 4`，X 的值（即参数地址）为 `Y + 8`，Z 的值（即跳转后的跳转地址）为 `Y + 4`，那么我们可以设计 Payload：

![](../../../../../assets/Pasted%20image%2020250719110000.png)

运行并验证：

![](../../../../../assets/Pasted%20image%2020250719110037.png)

可以看到我们成功获得了 Root Shell

- 如果我们不包括 exit 函数的地址，运行代码在退出时会出现段错误：
	
	![](../../../../../assets/Pasted%20image%2020250719110846.png)
	
	- 这是因为当 system 函数退出时返回地址是我们填充的 `0xaaaaaaaa`，这是一个无效地址，那么就会出现段错误
- 如果我们将可执行文件名改为 `newretlib`，无法获得 Root Shell：

	![](../../../../../assets/Pasted%20image%2020250719111231.png)
	
	这是因为环境变量在内存中的地址会因为程序路径长度的改变而发生偏移。在任务 2 中找到的字符串将不再准确，导致 `system()` 收到一个错误的参数地址，攻击失败。
***
## 任务 4：击败 Shell 的对策

我们需要利用 `execv()` 函数来进行攻击，首先利用 gdb 我们可以获得 `execv()` 函数的地址：

![](../../../../../assets/Pasted%20image%2020250719114342.png)

为了让 0 的影响最小化，我们先将一些必要的覆盖地址放在前面，将需要的地址放在后面：

- 首先 X，Y，Z 的值不变，在 Y 的地方放上 execv 函数的地址作为返回地址
- 在 Z 的地方放上 exit 函数的地址作为 execv 函数执行完毕的返回地址
- 在 X 的地方放上 `/bin/bash` 字符串的地址作为 execv 函数的第一个参数，在后面放上 argv 数组的地址作为第二个参数
- 在后面（这里我设置 offset 为 100）构造 argv 数组，argv 数组的第一个元素是 `/bin/bash` 字符串的地址，第二个元素是 `-p` 字符串地址，最后一个元素是 NULL
	- 同时我们需要保存 `/bin/bash` 和 `-p` 字符串

然后我们可以设计 Payload 如下：

![](../../../../../assets/Pasted%20image%2020250719120446.png)

运行即可获得 Root Shell：

![](../../../../../assets/Pasted%20image%2020250719120332.png)
***
## 任务 5：返回导向编程

首先我们用 gdb 获取 foo 函数的地址：

![](../../../../../assets/Pasted%20image%2020250719122227.png)

与上一个任务类似地，我们只需要在调用 execv 函数之前调用 10 次 foo 函数即可，Payload 的前半部分不变，后半部分如下：

![](../../../../../assets/Pasted%20image%2020250719122702.png)

运行即可运行 10 次 foo 并获得 Root Shell：

![](../../../../../assets/Pasted%20image%2020250719122620.png)
***
## Bonus：使用 ROP 进行任务 4

我们仍然使用 system 函数来获取 shell，但是在这之前添加上 setuid(0) 指令使得进程变为 Root 进程，同时为了传递参数 0，我们首先要通过占位符进行输入，再用 4 个 sprintf 函数来将 0 写入内存中，首先我们获取 libc 函数的地址和 bof 的返回指令地址：

![](../../../../../assets/Pasted%20image%2020250719130358.png)

然后我们可以设计 Payload 如下：

![](../../../../../assets/Pasted%20image%2020250719180957.png)

运行同样地可以获得 Root Shell：

![](../../../../../assets/Pasted%20image%2020250719180751.png)

