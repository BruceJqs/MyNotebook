---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
---

# Homework 04

## 4.1

![](../../../assets/Pasted%20image%2020241116210756.png)
***
### 4.1.1

$\text{Regwrite} = 1$
$\text{ALUSrc} = 0$
$\text{ALU Operation} = 10$
$\text{MemWrite} = 0$
$\text{MemRead} = 0$
$\text{MemtoReg} = 0$
***
### 4.1.2

寄存器组，ALUSrc 选择器，ALU，MemtoReg 选择器
***
### 4.1.3

Data Memory 和 ImmGen 不产生输出，且不会被用到
***
## 4.4

![](../../../assets/Pasted%20image%2020241116213719.png)
***
### 4.4.1

Load 类型和 Jal 指令会发生执行错误
***
### 4.4.2

Load 类型和 Store 类型指令会发生执行错误
***
## 4.6

![](../../../assets/Pasted%20image%2020241116214224.png)
***
### 4.6.1

不需要额外的逻辑单元
***
### 4.6.2

$\text{RegWrite} = 1$
$\text{ALUSrc} = 1$
$\text{MemtoReg} = 0$
$\text{MemWrite} = 0$
$\text{MemRead} = 0$
$\text{ALU Operation} = 10$
$\text{Branch} = 0$
$\text{Jump} = 0$
***
## 4.7

![](../../../assets/Pasted%20image%2020241116220059.png)

![](../../../assets/Pasted%20image%2020241116220124.png)
***
### 4.7.1

$$
\begin{aligned}
\text{Delay} &= 250(\text{I-Mem}) + 150(\text{Register File}) + 30(\text{Register Read}) + 25(\text{ALUMux}) \\
&+ 200(\text{ALU})  + 25(\text{MemoryMux}) + 20(\text{Register Setup}) = 700 \text{ps}
\end{aligned}
$$

***
### 4.7.2

$$
\begin{aligned}
\text{Delay} &= 250(\text{I-Mem}) + 150(\text{Register File}) + 30(\text{Register Read}) + 25(\text{ALUMux}) \\
&+ 200(\text{ALU}) +  250(\text{D-Mem}) + 25(\text{MemoryMux}) + 20(\text{Register Setup}) = 950\text{ps}
\end{aligned}
$$

***
### 4.7.3

$$
\begin{aligned}
\text{Delay} &= 250(\text{I-Mem}) + 150(\text{Register File}) + 30(\text{Register Read}) + 25(\text{ALUMux}) \\
&+ 200(\text{ALU}) +  250(\text{D-Mem}) = 905\text{ps}
\end{aligned}
$$

***
### 4.7.4

$$
\begin{aligned}
\text{Delay} &= 250(\text{I-Mem}) + 150(\text{Register File}) + 30(\text{Register Read}) + 25(\text{ALUMux}) \\
&+ 200(\text{ALU}) + 5(\text{Single Gate}) + 25(\text{AddrMux}) + 20(\text{Register Setup}) = 705\text{ps}
\end{aligned}
$$

***
### 4.7.5

$$
\begin{aligned}
\text{Delay} &= 250(\text{I-Mem}) + 150(\text{Register File}) + 30(\text{Register Read}) + 25(\text{ALUMux}) \\
&+ 200(\text{ALU}) + 25(\text{MemoryMux}) + 20(\text{Register Setup}) = 700\text{ps}
\end{aligned}
$$

***
### 4.7.6

$\text{Minimum Clock Cycle} = 950\text{ps}$
***
## 4.9

![](../../../assets/Pasted%20image%2020241116223952.png)
***
### 4.9.1

改动前：$\text{Clock Cycle} = 950\text{ps}$

改动后：$\text{Clock Cycle} = 1250\text{ps}$
***
### 4.9.2

加速比为 $\frac{950\times n}{1250\times n\times 0.95} = 0.8$
***
### 4.9.3

最低频率为 $\frac{1}{1250\text{ps}}=800\text{MHz}$
***
## 4.11

![](../../../assets/Pasted%20image%2020241116225227.png)
***
### 4.11.1

不需要添加新功能部件
***
### 4.11.2

控制单元需要改造
***
### 4.11.3

不需要添加新的数据通路
***
### 4.11.4

不需要添加新的控制信号
***
## 4.16

![](../../../assets/Pasted%20image%2020241116230136.png)
***
### 4.16.1

非流水化时钟周期 $= 250 + 350 + 150 + 300 + 200=1250\text{ps}$
流水化时钟周期 $= 350\text{ps}$
***
### 4.16.2

流水化和非流水化延迟均为 $1250\text{ps}$
***
### 4.16.3

拆分 ID 级，新处理器的始终周期为 $300\text{ps}$
***
### 4.16.4

数据存储利用率为 $20\%(\text{Load}) + 15\%(\text{Store})=35\%$ 
***
### 4.16.5

寄存器堆的写口利用率为 $45\%(\text{ALU/Logic}) + 20\%(\text{Load}) = 65\%$
***
## 4.18

![](../../../assets/Pasted%20image%2020241116231828.png)

$x13=33,x14=26$
***
## 4.20

![](../../../assets/Pasted%20image%2020241116233025.png)

```asm
addi x11, x12, 5
NOP
NOP
add x13, x11, x12
addi x14, x11, 15
NOP
add x15, x13, x12
```
***
## 4.21

![](../../../assets/Pasted%20image%2020241116233519.png)
***
### 4.21.1

加速比为 $\frac{1.4n\times 250}{1.05n\times 300}=1.11$
***
### 4.21.2

由 $300\times(1+\alpha)\times n\leq 250\times 1.4\times n$，最后解得 $\alpha\leq\frac{1}{6}$

所以指令比例应当小于 $16.7\%$
***
### 4.21.3

由 $300\times(1+\alpha)\times n\leq 250\times(1+x)\times n$

解得 $\alpha\leq\frac{5}{6}(1+x)-1$
***
### 4.21.4

不会，因为 $300\times n\leq 250\times 1.075\times  n$
***
### 4.21.5

最少插入 NOP 指令为 $(\frac{6}{5}-1)n=0.2n$
***
## 4.25

![](../../../assets/Pasted%20image%2020241116235822.png)
***
### 4.25.1

![](../../../assets/Pasted%20image%2020241117002552.png)
***
### 4.25.2

![](../../../assets/Pasted%20image%2020241117002936.png)

永远不会出现
