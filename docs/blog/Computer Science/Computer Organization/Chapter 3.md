---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
---  
# Chapter 3 : Arithmetic for Computer

## Introduction

### Signed and Unsigned Numbers Possible Representations

- Sign-magnitude（原码）
	- 二进制（开头第一个表示符号，0 正 1 负）
- 1's Complement Code（反码）
	- 在原码的基础上，符号位不动，其它位取反
- 2's Complement Code（补码）
	- 在反码的基础上，运算+1
	- 任何正数的原码=反码=补码，而负数都是通过补码表示的
- Biased Notation（移码）
	- 在补码的基础上，符号位取反
***
## Arithmetic

### Addition & Subtraction

- 加法即二进制竖式加法

![](../../../assets/Pasted%20image%2020240918110327.png)

- 减法有两种方式，一种是直接竖式减法，但在计算机中**不存在减法**，可以通过加补码的形式实现减法

![](../../../assets/Pasted%20image%2020240918110524.png)
***
### Overflow

- 在进行加减法时，由于硬件规模是有限的，我们可能遇到数据溢出的情况：

![](../../../assets/Pasted%20image%2020240918110719.png)

![](../../../assets/Pasted%20image%2020240918110742.png)

- 对于有符号加法，当正数和正数相加得到负数，或者负数和负数相加得到正数时，就可以判定溢出：

![](../../../assets/Pasted%20image%2020240918110851.png)

- 对于无符号加法，如果结果小于二者中任意一个，也可以判定溢出
- 当出现溢出情况时，硬件层面检测出溢出情况，并生成一个异常/中断指令，将这个指令的地址存储到一个特别的寄存器 EPC 里，然后跳转到 OS 中专门的程序中来处理这个溢出（异常处理）
***
### Constructing an ALU

- 两个建立 ALU（Arithmetic Logic Unit）的方法：
	- 逐渐扩展加法器的功能
	- 并行冗余选择

!!! notes "逐渐扩展加法器功能"

	=== "半加器"
	
		![](../../../assets/Pasted image 20240918111944.png)
	
	=== "多个数相加"
	
		![](../../../assets/Pasted image 20240918112139.png)
	
	=== "进位情况"
	
		![](../../../assets/Pasted image 20240918112252.png)
	
	=== "全加器"
	
		![](../../../assets/Pasted image 20240918112431.png)
	
		![](../../../assets/Pasted image 20240918112507.png)

		- n 位加法，需要 n 个全加器
		
		![](../../../assets/Pasted image 20240918112832.png)
	
	=== "添加与、或运算"

		- 结合一个选择器，我们就可以构造一个支持与、或以及加法运算的 1 bit ALU：
		
		![](../../../assets/Pasted image 20240918113017.png)
	
	=== "添加减法运算"
	
		- 结合之前所讲，减法即为加补码，对于一位的情况，反转 b 并将 CarryIn 设置为 1（即实现 b 的补码转换，如果有多位就将第一位加法器的 CarryIn 设置为 1）
	
		![](../../../assets/Pasted image 20240918133122.png)
		
	=== "添加比较功能"
	
		为了实现 `slt rd, rs1, rs2` 这个操作（即实现比较操作）（SLT 即 Set Less Than），如果 `rs1 < rs2` ，那么将 `rd` 置为 `1` ，否则置为 `0` 。如何进行这一判断呢？很简单，`rs1 < rs2` 即 `rs1 - rs2 < 0`，也就是说如果 `rs1 - rs2` 结果的最高位是 `1` ，那么就说明 `rs1 < rs2` 。
		
		![](../../../assets/Pasted image 20240918134045.png)
	
	=== "添加检测溢出功能"
	
		![](../../../assets/Pasted image 20240918134234.png)
	
		注：图中的 Overflow Detection 被复杂化了，实际上可以通过 `CarryIn` 和 `CarryOut` 的异或完成

最终封装模块，可以得到完整的 32 位的 ALU 模块：

![](../../../assets/Pasted%20image%2020240918134416.png)

我们还可以添加一个检测 0 的模块，添加进 ALU 模块当中：

![](../../../assets/Pasted%20image%2020240923134808.png)

对于这样的一个 ALU，我们需要 4 bits 的 control lines，分别是 `Ainvert` , `Bnegate` 和 `Operation` (2 bits)。ALU 的符号和 control lines 的含义如下：

![](../../../assets/Pasted%20image%2020240923135342.png)
***
### Fast Adders

上面的 64 位加法的实现方式是通过 1 位加法器串联实现的，这种方式势必需要等待前一个加法器算出结果后才能算后一个的。这种多位加法器的实现称为行波加法器 **Ripple Carry Adder, RCA**。显然，这种实现方式比较慢。

#### Carry Look-ahead Adder, CLA

课本指出，RCA 缓慢的重要原因是后一个 adder 需要等前一个 adder 的 carry 结果；但我们不妨讨论出现 carry 的可能。第一种可能是，如果 a 和 b 都是 1，那么一定会 **生成** 一个 carry；另一种可能是，如果 a 和 b 中有且仅有一个是 1，那么如果传入的 carry 是 1，则这里也会 carry，即 carry 被 **传播** 了。

也就是说，$c_{out}=a⋅b+(a+b)⋅c_{in}$。我们记 **generate** $g=a⋅b$，**propagate** $p=a+b$，则有 $c_{out}=g+p⋅c_{in}$。所以，我们可以这样构造一个全加器：

![](../../../assets/Pasted%20image%2020240923140200.png)

所以，我们可以推导出如下关系：

$$
\begin{aligned}
c_1 &= g_0+(p_0·c_0)\\
c_2 &= g_1+(p_1·g_0)+(p_1·p_0·c_0)\\
c_3 &= g_2+(p_2·g_1)+(p_2·p_1·g_0)+(p_2·p_1·p_0·c_0)\\
c_4 &= g_3+(p_3·g_2)+(p_3·p_2·g_1)+(p_3·p_2·p_1·g_0)+(p_3·p_2·p_1·p_0·c_0)
\end{aligned}
$$

利用这个关系，我们可以构造这样一个四位加法器：

![](../../../assets/Pasted%20image%2020240923140246.png)

其实 CLA 的本质即为将可能的进位提前算出来，不需要等待前一位算出结果后再进位（这也是 Look-ahead 的来源），实现每位的加法器由串行转为并行，从而提高时间效率。

上面的 PFA, Partial Fully Adder，就是前面我们构造的新全加器的一部分。可以看到，通过这样的方式，我们可以加速加法的运算；但是注意到越到高位，门的 fan-in 就越大，因此不能一直增加的。所以对于更多位数的加法器，我们将上面这样构成的 4-bit CLA 再通过类似的方式串起来！

![](../../../assets/Pasted%20image%2020240923140526.png)

