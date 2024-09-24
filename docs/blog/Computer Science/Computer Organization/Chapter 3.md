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
***
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

#### Carry Skip Adder

老师没讲，应该不考（x）
***
#### Carry Select Adder, CSA

老师还是没讲，应该还是不考（x）
***
## Multiplication

二进制乘法与十进制相同，都可以用竖式解决，我们需要看的是硬件方面如何实现。
***
### Multiplier V1

换句话来说，所谓的乘法实际上是根据 Multiplier（乘数） 的 0/1 来选择是否要将 Multiplicand（被乘数） 的对应位移结果加到 Product（乘积） 上。

64 bits 乘法器的硬件实现大致如下：

![](../../../assets/Pasted%20image%2020240923143352.png)

其流程如下：

1. 判断 Multiplier 寄存器的最低位是否是 1：
2. 如果是，则将 Multiplicand 寄存器的值加到 Product 寄存器里；
3. 如果否，进入下一步；
4. 将 Multiplier 寄存器的值右移一位（这是为了不断拿出每一位，相当于在枚举 Multiplier 的每一位），将 Multiplicand 寄存器的值左移一位（对应于和 Multiplier 的第几位乘得到的位移，类似在做竖式乘法）；
5. 判断是否做满 64 次，决定是否终止；
***
### Multiplier V2

可以发现，V1 中做了大量的 128 位加法，但是实际上被加过去的 Multiplicand 有效内容只有 64 位。V2 正是解决了这个问题。

![](../../../assets/Pasted%20image%2020240923145124.png)

- 和之前课件有所不同的是，这里的乘积变成了 129 位，是为了保留进位

它将 Multiplicand 寄存器换为了 64 位，而将位移操作转移到了 Product 寄存器中进行。这里最重要的一点就是，64 位加法只影响 Product 寄存器左侧的 64 位，而之后的右移操作则是 128 位。这样，虽然最低位的结果一开始会被放在 Product 寄存器的第 65 位里，但是在经过 64 次右移之后，它就出现在第一位了。于是，所有的 128 位加法都被 64 位加法替代，实现了加速。

其流程如下：

1. 判断 Multiplier 寄存器的最低位是否是 1：
2. 如果是，则将 Multiplicand 寄存器的值加到 Product 寄存器的左半部分里；
3. 如果否，进入下一步；
4. 将 Multiplier 寄存器的值右移一位，将 Product 寄存器的值右移一位；
5. 判断是否做满 64 次，决定是否终止；
***
### Multiplier V3

我们还发现，我们对 Multiplier 的右移是为了枚举最低位，但是为了实现这个枚举，我们每次都要做 64 位的右移；除此之外，在一开始的几次中，Product 的右半部分大部分没有意义，但是仍然在 128 位的右移中影响效率。仔细一看，我们能发现，我们每右移一次 Multiplier 寄存器，就会右移一次 Product 寄存器，而前者将导致 Multiplier 寄存器中出现一个没意义的 bit，后者将导致 Product 寄存器中消失一个没意义的 bit。

V3 正是抓住了这个点，直接将 Multiplier 存在了 Product 的低 64 位中。当我们从中取出最低位并经过一次判断后，这一位就不重要了，而恰好 Product 需要右移，就将这一位消除，方便我们下一次从最低位拿出下一个比特！

那么这么做的好处在哪里呢？首先，少了一个寄存器，节省了空间；其次，原本需要 Multiplier 寄存器和 Product 寄存器都做右移，现在只需要 Product 寄存器右移即可，减少了一个 64 位右移操作。

![](../../../assets/Pasted%20image%2020240923150036.png)

其流程如下：

1. 判断 Product 寄存器的最低位是否是 1：
2. 如果是，则将 Multiplicand 寄存器的值加到 Product 寄存器的左半部分里；
3. 如果否，进入下一步；
4. 将 Product 寄存器的值右移一位；
5. 判断是否做满 64 次，决定是否终止；
***
### Signed Multiplication

有符号数乘法主要是转化为无符号数乘法来做。首先存储两个数的符号，然后将它们转化为无符号数。接下来对两个无符号数做无符号乘法，最后根据之前存储的符号决定结果的符号并转化为有符号数。
***
#### Booth's Algorithm

Booth's Algorithm 是一个优化乘法的算法。

![](../../../assets/Pasted%20image%2020240923152059.png)

Booth's Algorithm 的主要思想在于，减少乘数中“`1`”的数量。具体来说，在我们原先的乘法策略中，每当乘数中有一位 `1` 时，都会需要一个加法（将位移后的被乘数累加到结果中）。但是，如果乘数中有较长的一串 `1` 时，我们可以将它转化为一个大数字减一个小数，如：`00111100 = 01000000 - 00000100`，此时 4 个 `1` 变为 2 个 `1`，我们就可以减少做加法的次数。

![](../../../assets/Pasted%20image%2020240923152150.png)

在实际执行过程中，Booth's Algorithm 主要遵循两位比特的模式进行操作。

![](../../../assets/Pasted%20image%2020240923152241.png)

![](../../../assets/Pasted%20image%2020240923152406.png)

>上面这张图实际上的表示是挪用了 V3 的乘法器。product 一列代表的是 product 寄存器，左一半一开始置 0，右一半一开始存放的是乘数，而上面提到的将被乘数加减累计到结果中的操作，也是对于左半部分来说的（**换句话来说就是用 V3 做 Booth's**）。需要提醒的是，在 Booth's Algorithm 中，两位识别是从第一位开始的，此时第一位作为两位中的高位，低位为 0，而后在下一轮中第一位作为低位，第二位作为高位，以此类推。

Booth's Algorithm 也能应用于负数。

![](../../../assets/Pasted%20image%2020240923152728.png)

仔细想想就会发现其实很合理，对于正数，其最高位一定是 `0`，因此不管怎么样它最终都会匹配到一个 `01` 的模式，来给一个 `1111..` 收尾。但是负数不然，负数的最高位是 `1`，这也意味着它最终不会执行所谓的 `01` 对应的加法操作来给 `111...` 收尾。
***
### Faster Multiplication

![](../../../assets/Pasted%20image%2020240923153034.png)
***
### RISC-V Multiplication

- `mul`：低 64 位乘法
	- 给出乘积的低 64 位
- `mulh`：高 64 位乘法
	- 给出乘积的高 64 位（假设所有运算数是有符号数）
- `mulhu`：无符号高 64 位乘法
	- 给出乘积的高 64 位（假设所有运算数是无符号数）
- `mulhsu`：有符号与无符号高 64 位乘法
	- 给出乘积的高 64 位（假设一个运算数是无符号数一个运算数是有符号数）
- 我们可以用 `mulh` 的结果来检查有没有 64 位的溢出
***
## Division

二进制除法与十进制相同，都可以用竖式解决。

![](../../../assets/Pasted%20image%2020240923154525.png)
***
### Division V1

