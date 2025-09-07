---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
# comments: true
---  

# Buffer Overflow SetUID

## 任务 1：调用 Shellcode

运用 Makefile 编译代码并运行：

![](../../../../../assets/Pasted%20image%2020250715132303.png)

可以看到，两个程序都成功获取了 seed 权限的 Shell，如果用 setuid 方式编译：

![](../../../../../assets/Pasted%20image%2020250715132218.png)

可以看到，我们成功获取了 root 权限的 Shell
***
## 任务 3：针对 32 位程序发起攻击

使用 `-g` 选项重新编译代码，并用 gdb 对二进制文件进行调试：

1. 在 bof() 函数设下端点：

![](../../../../../assets/Pasted%20image%2020250715133513.png)

2. 运行程序到断点处：

![](../../../../../assets/Pasted%20image%2020250715133545.png)

可以看到汇编部分，此时 esp 的值还没有赋给 ebp，所以此时我们获取的值是函数调用者的地址：

![](../../../../../assets/Pasted%20image%2020250715133858.png)

而我们想获得 `bof()` 函数的基址，需要先让程序执行到 `mov ebp,esp` 之后：

![](../../../../../assets/Pasted%20image%2020250715134216.png)

此时获得的就是 `bof()` 函数的基址，然后也可以获得 buffer 的起始地址：

![](../../../../../assets/Pasted%20image%2020250715134331.png)

因此，可以设计 Payload 如下：

![](../../../../../assets/Pasted%20image%2020250715150217.png)

其中因为 Shellcode 长度为 27，放在 320 处即可；返回地址放在 Shellcode 之前的任意一个 NOP 即可；偏移即为 buffer 大小加 4，而 buffer 大小即为 ebp 和 buffer 起始地址之差。运行即可获得 Root 权限的 Shell：

![](../../../../../assets/Pasted%20image%2020250715150020.png)
***
## 任务 4：在不知道缓冲区大小的情况下发起攻击

通过 gdb 我们可以获取缓冲区的起始地址：

![](../../../../../assets/Pasted%20image%2020250715151459.png)

如果我们不知道缓冲区大小，根据题目描述我们可以构造 Payload 如下：

![](../../../../../assets/Pasted%20image%2020250715151905.png)

既然我们不知道 Buffer 的大小，那么我们将所有可能性的地方都把返回地址填上，不管 Buffer 多大返回地址都会被覆盖，运行即可获得 Root 的 Shell：

![](../../../../../assets/Pasted%20image%2020250715151814.png)
***
## 任务 5：针对 64 位程序发起攻击

获得缓冲区的起始地址和 rbp 地址：

![](../../../../../assets/Pasted%20image%2020250715153456.png)

我们把 shellcode 移到前面来，后面的返回地址改为 buffer 的地址，这样即使出现 0x00 字节被截断了，栈上的 0x00 字节也会被我们复用，代码如下：

![](../../../../../assets/Pasted%20image%2020250715160151.png)

运行即可获得 Root 的 Shell：

![](../../../../../assets/Pasted%20image%2020250715160106.png)
***
## 任务 6：针对 64 位程序发起攻击

对比起任务 5，缓冲区的大小大大减小，放不下 Shellcode，但是函数当中的 str 地址我们还是知道的，所以我们用 gdb 获取 str 的偏移：

![](../../../../../assets/Pasted%20image%2020250715161923.png)

那么我们只要让返回地址来到 str 区域即可，构造 Payload 如下：

![](../../../../../assets/Pasted%20image%2020250715162452.png)

运行即可获得 Root 的 Shell：

![](../../../../../assets/Pasted%20image%2020250715162427.png)
***
## 任务 7：击败 dash 的防御措施

重新将 `/bin/sh` 指向 `/bin/bash`，重新用 `make setuid` 编译 shellcode，得到：

![](../../../../../assets/Pasted%20image%2020250715162947.png)

这和之前我们得到的结果不一样，说明 `/bin/dash` 的防御机制较为强大，但是我们只要在 shellcode 之前添加上 setuid(0) 的代码，即可攻破：

![](../../../../../assets/Pasted%20image%2020250715163326.png)
***
## 任务 8：击败地址随机化

我们开启地址随机化，重新进行任务 3 的攻击：

![](../../../../../assets/Pasted%20image%2020250715165204.png)

可以看到，我们的攻击失败了，我们利用脚本反复进行攻击：

![](../../../../../assets/Pasted%20image%2020250715175318.png)

一个小时后成功获得 root 的 Shell
***
## 任务 9：其他防御机制

### 任务 9.a：开启 StackGuard 防护

关闭地址随机化，编译时不使用 `-fno-stack-protector` 参数，重新编译运行 `stack-L1`：

![](../../../../../assets/Pasted%20image%2020250715184003.png)

可以看到，程序运行失败了，说明 StackGuard 检测到栈溢出成功地阻止了攻击
***
### 任务 9.b：开启不可执行栈防护

编译时使用 `-z noexecstack` 参数，重新编译运行 `stack-L1`：

![](../../../../../assets/Pasted%20image%2020250715184516.png)

可以看到，程序运行失败了，说明不可执行栈让代码不能在栈上执行，成功地阻止了攻击




