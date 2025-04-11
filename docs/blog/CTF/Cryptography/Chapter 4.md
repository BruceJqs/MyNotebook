---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
--- 

# Chapter 04 : 分组密码工作模式与流密码

## 分组密码工作模式

### ECB

ECB（Electronic Code Book）模式是最简单的分组密码工作模式。它将明文分成固定大小的块，然后对每个块独立进行加密：

![](../../../assets/Pasted%20image%2020250411004232.png)

ECB 模式的优点是简单易实现，且加解密过程均可以并行处理，但缺点也很明显：相同的明文块会被加密成相同的密文块，这使得攻击者可以通过分析密文来推测明文的结构和内容
***
### CBC

CBC（Cipher Block Chaining）模式在加密每个块之前，将当前块与前一个块的密文进行异或操作。这种方式使得相同的明文块在不同的上下文中会产生不同的密文，从而提高了安全性：

![](../../../assets/Pasted%20image%2020250411004957.png)

CBC 模式的优点是相同的明文块会产生不同的密文块，从而提高了安全性，但缺点是加密过程不能并行处理，因为每个块都依赖于前一个块的结果；解密过程可以并行处理
***
### CFB

CFB（Cipher Feedback）将明文分成小块，然后将前一个密文块与当前明文块进行异或操作。CFB 模式允许对明文进行流式加密：

![](../../../assets/Pasted%20image%2020250411151717.png)

!!! example "Example"

	假设明文 P 共有 8 字节，设一个种子 S 也为 8 字节。加密过程如下：
	
	1. 现将 S 进行加密得到 X，$c[0]=p[0]\oplus x[0]$ 得到密文的首字节 $c[0]$
	2. 接下去改变种子 S，用 $s[1],s[2],\cdots,s[7],c[0]$ 拼接成一个新的 S
	3. 将新的 S 进行加密得到 X，$c[1]=p[1]\oplus x[0]$ 得到密文的第二个字节 $c[1]$
	4. 接下去改变种子 S，用 $s[2],\cdots,s[7],c[0],c[1]$ 拼接成一个新的 S
	5. 将新的 S 进行加密得到 X，$c[2]=p[2]\oplus x[0]$ 得到密文的第三个字节 $c[2]$
	6. 如此类推，直到最后一个字节 $c[7]$ 得到密文的最后一个字节 $c[7]$

CFB 模式的优点是可以从密文传输的错误中恢复，比如我们需要传输密文 $c_1,c_2,c_3,\cdots,c_k$，我们假定 $c_1$ 传输错误，记作 $c_1'$，那么解密还原的 $p_1$ 有错，若 $x_1$ 记作 $(*,*,*,*,*,*,*,*)$，那么有 $x_2=(*,*,*,*,*,*,*,c_1')$，$x_3=(*,*,*,*,*,*,c_1',c_2)$，$x_4=(*,*,*,*,c_1',c_2,c_3)$，...，$x_9=(c_1',c_2,c_3,\cdots,c_9)$，$x_{10}=(c_2,c_3,\cdots,c_{10})$，使用密钥 $x_1,x_2,x_3,\cdots,x_9$ 解密 $c_1'c_2c_3c_4c_5c_6c_7c_8c_9$ 还原得到的 $p_1,p_2,p_3,\cdots,p_9$ 全部有错，但是从 $p_{10}$ 开始的解密还原是正确的
***
### RC4

RC4 是一种对称流密码加密算法，它使用一个可变长度的密钥来生成一个伪随机的密钥流，然后将这个密钥流与明文进行异或操作来生成密文

RC4 算法加密的流程包括密钥调度算法 KSA 和伪随机子密码生成算法 PRGA 两大部分

!!! note "RC4"

	=== "KSA"
	
		1. 初始化一个长度为 256 的数组 S，S[i]=i
		2. 用密钥 K 对 S 进行置换，得到 S'
		
		```c
		state = &key->state[0];
		for(counter = 0; counter < 256; counter++)
			state[counter] = counter; /* 初始化256个密钥 */
		index1 = 0;
		index2 = 0;
		for(counter = 0; counter < 256; counter++)
		{    /* key_data_ptr 为种子密钥, 里面可以包含 [1,256] 个字节, 超过 256 字节的部分无用 */
			/* 以下循环利用 key_data_ptr 打乱 state, 注意 256 个 state只交换, 不赋值 */
			index2 = (key_data_ptr[index1] + state[counter] + index2) % 256;
			swap_byte(&state[counter], &state[index2]);
			index1 = (index1 + 1) % key_data_len;
		}
		```
	
	=== "PRGA"
	
		![](../../../assets/Pasted%20image%2020250411204706.png)
		
		```c
		state = &key->state[0];
		for(counter = 0; counter < buffer_len; counter ++)
		{
			x = (x + 1) % 256;
			y = (state[x] + y) % 256;
			swap_byte(&state[x], &state[y]); /* 加密/解密前, 交换一对state */
		
			xorIndex = (state[x] + state[y]) % 256; /* 计算密钥的index */
			buffer_ptr[counter] ^= state[xorIndex]; /* state[xorIndex]为当前密钥 */
		}
		```