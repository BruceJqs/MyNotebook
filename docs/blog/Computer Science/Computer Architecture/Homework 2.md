---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
--- 

# Homework 02

## 2.17

![](../../../assets/Pasted%20image%2020250415132238.png)

![](../../../assets/Pasted%20image%2020250415132250.png)

（a）直接映射的访问时间为 0.86ns，2 路组相联的访问时间为 1.12ns，4 路组相联的访问时间为 1.37ns

那么 2 路组相联相对直接映射的比例为 $1.12/0.86=1.30$，4 路组相联相对直接映射的比例为 $1.37/0.86=1.59$

（b）16KB 缓存的访问时间为 1.27ns，32KB 缓存的访问时间为 1.35ns，64KB 缓存的访问时间为 1.37ns

那么 32KB 缓存相对 16KB 缓存的比例为 $1.35/1.27=1.06$，64KB 缓存相对 16KB 缓存的比例为 $1.37/1.27=1.08$

（c）我们有：

$$
\begin{aligned}
\text{Average Access Time} &= \text{Hit Rate} \times \text{Hit Time} + \text{Miss Rate} \times \text{Miss Penalty}\\
\text{Miss Rate} &= \frac{\text{Misses per Instruction}}{\text{References per Instruction}}
\end{aligned}
$$

使用 CACTI 查得直接映射的时钟周期为 0.5ns，2 路组相联的时钟周期为 0.5ns，4 路组相联的时钟周期为 0.83ns，8 路组相联的时钟周期为 0.79ns

综上我们可以得到：

$$
\begin{aligned}
\text{Hit Time}_{\text{Direct Mapped}} &= \frac{0.86}{0.5}=2\text{ cycles}\\
\text{Hit Time}_{\text{2-Way}} &= \frac{1.12}{0.5}=3\text{ cycles}\\
\text{Hit Time}_{\text{4-Way}} &= \frac{1.37}{0.83}=2\text{ cycles}\\
\text{Hit Time}_{\text{8-Way}} &= \frac{2.03}{0.79}=3\text{ cycles}\\
\text{Miss Penalty}_{\text{Direct Mapped}} &= \frac{10}{0.5}=20\text{ cycles}\\
\text{Miss Penalty}_{\text{2-Way}} &= \frac{10}{0.5}=20\text{ cycles}\\
\text{Miss Penalty}_{\text{4-Way}} &= \frac{10}{0.83}=13\text{ cycles}\\
\text{Miss Penalty}_{\text{8-Way}} &= \frac{10}{0.79}=13\text{ cycles}\\
\text{Miss Rate}_{\text{Direct Mapped}} &=  2.2\%\\
\text{Miss Rate}_{\text{2-Way}} &=  1.2\%\\
\text{Miss Rate}_{\text{4-Way}} &=  0.33\%\\
\text{Miss Rate}_{\text{8-Way}} &=  0.09\%\\
\end{aligned}
$$

所以：

$$
\begin{aligned}
\text{Average Access Time}_{\text{Direct Mapped}} &= (1-0.022)\times 2 + 0.022 \times 20 = 2.396\text{ cycles}=1.198\text{ ns}\\
\text{Average Access Time}_{\text{2-Way}} &= (1-0.012)\times 3 + 0.012 \times 20 = 3.24\text{ cycles}=1.62\text{ ns}\\
\text{Average Access Time}_{\text{4-Way}} &= (1-0.0033)\times 2 + 0.0033 \times 13 = 2.06\text{ cycles}=1.69\text{ ns}\\
\text{Average Access Time}_{\text{8-Way}} &= (1-0.0009)\times 3 + 0.0009 \times 13 = 3.01\text{ cycles}=2.37\text{ ns}\\
\end{aligned}
$$

所以直接映射最好
***
## 2.18

![](../../../assets/Pasted%20image%2020250415163456.png)

（a）当前缓存的访问时间为 $1.69\text{ ns}=3\text{ cycles}$

对于路预测缓存来说，访问时间为 $(1-0.022)\times (0.8\times 2+(1-0.8)\times 3)+0.022\times 20=2.59\text{ cycles}$

（b）加速比为 $(0.83-0.5)/0.5=66\%$

（c）原来的访问时间为 $2.59\text{ cycles}$，如果是 15 个时钟周期的错误预测损失，访问时间为 $(1-0.022)\times (0.8\times 2+(1-0.8)\times 15)+0.022\times 20=4.94\text{ cycles}$，增加了 $2.35\text{ cycles}$

（d）加速比为 $\frac{2.4\text{ ns}-1.59\text{ ns}}{1.59\text{ ns}}=51\%$
***
## 2.26

![](../../../assets/Pasted%20image%2020250415213036.png)

（a）LRU 策略新拿到的块会放到优先队列的头部，当块被再次访问时会被放到优先队列的头部，当块被替换时会将优先队列的尾部的块替换掉

（b）将新拿到的块放到队列的倒数第二位，当块被再次访问时放到优先队列的头部，当块被替换时会将优先队列的尾部的块替换掉
***
## 2.27

![](../../../assets/Pasted%20image%2020250415220328.png)

![](../../../assets/Pasted%20image%2020250415220638.png)

根据每个程序的行为和服务给它们动态地提供缓存当中的一部分路，但是在提供隐私信息的时候，事先确定路的分配且运行时不能改变
***
## 2.28

![](../../../assets/Pasted%20image%2020250415221716.png)

将经常需要使用的块放在靠近处理器核心的 Bank 当中，一些不常用的块放在远离处理器核心的 Bank 当中，如果离处理器核心近的 Bank 能处理更多的请求就能实现更高的性能
***
## 2.32

![](../../../assets/Pasted%20image%2020250415222254.png)

$$
\begin{aligned}
\text{Instructions per Second} &= 8\text{ cores}\times 3\text{ GHz}/2.0\text{ CPI}=1.2\times 10^{10}\\
\text{L2 Misses per Second} &= 1.2\times 10^{10}\times 0.00667= 8\times 10^{7}\\
\text{Bandwidth} &= 8\times 10^{7}\times 32\text{ bytes}\times 2=5120\text{MB/s}\\
\end{aligned}
$$

所以只需要一个就够了
***
## 2.33

![](../../../assets/Pasted%20image%2020250415223306.png)

应该放在不同的通道上，因为如果位于同一个 bank 当中，如果它们命中，需要按顺序取出访问，如果位于不同的 bank 当中，可以并行访问，这样能提高效率
***
## 2.36

![](../../../assets/Pasted%20image%2020250416204501.png)

$\text{Time} = \frac{8\times 10^9\times 2\times 2.56}{64\times 1.6}=4\times 10^8\text{ seconds}$（这真的对吗）
***
## 2.37

![](../../../assets/Pasted%20image%2020250416224042.png)

（a）可以，用于在 VM 上安装应用和开发环境

（b）可以，用于在 VM 上启动应用服务作为临时服务

（c）不可以，因为 VM 的性能较差所以不可能会有更高的性能

（d）可以，不同 VM 之间相互独立，可以将应用安装在不同的 VM

（e）可以，VM 是完全独立的，可以独立运行应用
***
## 2.38

![](../../../assets/Pasted%20image%2020250416230331.png)

![](../../../assets/Pasted%20image%2020250416230351.png)

（a）执行非常多计算，但是数据集比较小，也很少进行 I/O 或系统函数调用的程序

（b）120%

（c）用 Pure Virtualization 是 10.3，用 Paravirtualization 是 3.76

（d）空调用或者空 I/O 调用。这是因为它们没有实际需要做的工作来超过更改保护级别的开销
***
## 2.41

![](../../../assets/Pasted%20image%2020250416230709.png)

![](../../../assets/Pasted%20image%2020250416230719.png)

移除 Alpha 21264 中支持乱序执行的硬件（发射队列、重命名映射器）后，其释放的面积可将数据缓存从 ​**64 KB 扩大至约 80 KB**​（假设OOO硬件面积占原数据缓存的25%）







