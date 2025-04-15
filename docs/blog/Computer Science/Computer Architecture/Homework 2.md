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

（b）




