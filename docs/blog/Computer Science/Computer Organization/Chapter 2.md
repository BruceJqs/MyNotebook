---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
---  
# Chapter 2 : Instructions : Language of the Machine

## Introduction

![](../../../assets/Pasted%20image%2020241012150957.png)

![](../../../assets/Pasted%20image%2020241012151047.png)

![](../../../assets/Pasted%20image%2020241012151133.png)
***
## Operations of the Computer Hardware

- 设计原则 1：`Simplicity favors regularity`
	- 规律性使实现更简单
	- 简单性以更低的成本实现更高的性能
### Arithmetic

![](../../../assets/Pasted%20image%2020241012151827.png)
***
## Operands of the Computer Hardware

### RISC-V Registers

RISC-V architecture 提供 32 个数据寄存器，分别命名为 `x0` ~ `x31` ，每个寄存器的大小是 `64` 位。在 RISC-V architecture 中，一个 **word** 为 32 位，一个 **doubleword** 为 64 位。这些寄存器中的一部分有专门的用途。

RISC-V architecture 也提供一系列浮点数寄存器 `f0` ~ `f31` ，这不是我们讨论的重点。

- 设计原则 2：`Smaller is faster`

![](../../../assets/Pasted%20image%2020241012152104.png)

- 其中 "preserved on call" 的意思是，是否保证调用前后这些寄存器的值不变。

![](../../../assets/Pasted%20image%2020241012154329.png)
***
### Memory Operands

RISC-V architecture 的地址是 64 位的，地址为字节地址，因此总共可以寻址 264 个字节，即 261 个 dword (doubleword, 下同)，因为一个 dword 占 log2⁡648=3 位。

在一些 architecture 中，word 的起始地址必须是 word 大小的整倍数，dword 也一样，这种要求称为 **alignment restriction**。RISC-V 允许不对齐的寻址，但是效率会低。

RISC-V 使用 **little endian** 小端编址。也就是说，当我们从 0x1000 这个地址读出一个 dword 时，我们读到的实际上是 0x1000~0x1007 这 8 个字节，并将 0x1000 存入寄存器低位，0x1007 存入高位。

![](../../../assets/Pasted%20image%2020241012152019.png)

> 一个记忆方法是，如果你将地址横着写，即从左到右递增，那么对于大端来说是比较自然的，但是对于小端来说会比较不自然。以上面的 `0A0B0C0D` 为例子，大端为从低地址到高地址是 `0A` `0B` `0C` `0D`，而小端从低到高地址则是 `0D` `0C` `0B` `0A`。

RISC-V 支持 PC relative 寻址、立即数寻址 ( `lui` )、间接寻址 ( `jalr` )、基址寻址 ( `8(sp)` )：

![](../../../assets/Pasted%20image%2020241012152418.png)

![](../../../assets/Pasted%20image%2020241012154427.png)

![](../../../assets/Pasted%20image%2020241012154504.png)

- 寄存器和内存：

![](../../../assets/Pasted%20image%2020241012154651.png)

- 常数处理：

![](../../../assets/Pasted%20image%2020241012154748.png)

- 设计原则 3：`Make Common Case Fast`

![](../../../assets/Pasted%20image%2020241012154844.png)
***
## Signed and unsigned numbers

### 补码 2's complement

$x+\overline{x}=111…111_2=−1$，因此 $−x=\overline{x}+1$。前导 0 表示正数，前导 1 表示负数。

因此在将不足 64 位的数据载入寄存器时，如果数据是无符号数，只需要使用 0 将寄存器的其他部分填充 (**zero extension**)；而如果是符号数，则需要用最高位即符号位填充剩余部分，称为符号扩展 (**sign extension**)。

即，在指令中的 `lw` , `lh` , `lb` 使用 sign extension，而 `lwu` , `lhu` , `lbu` 使用 zero extension。
***
### 指令，指令格式

![](../../../assets/Pasted%20image%2020241012150310.png)

> 在 RISC 指令集中，只有 load 系列和 store 系列指令能够访问内存。

RISC-V 的跳转指令的 offset 是基于当前指令的地址的偏移；这不同于其他一些汇编是基于下一条指令的偏移的。即如果是跳转语句 `PC` 就不 +4 了，而是直接 +offset。

`lw` , `lwu` 等操作都会清零高位。

RISC-V 指令格式如下：

![](../../../assets/Pasted%20image%2020241012152951.png)

其中 `I` 型指令有两个条目；这是因为立即数移位操作 `slli` , `srli` , `srai` 并不可能对一个 64 位寄存器进行大于 63 位的移位操作，因此 12 位 imm 中只有后 6 位能实际被用到，因此前面 6 位被用来作为一个额外的操作码字段，如上图中第二个 `I` 条目那样。其他 `I` 型指令适用第一个 `I` 条目。

!!! Example

	![](../../../assets/Pasted image 20241012153516.png)