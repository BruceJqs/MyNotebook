---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
# comments: true
---
## Homework 02

### 2.4

![](../../../assets/Pasted%20image%2020241025102935.png)

$\text{B[g] = A[f] + A[f + 1]}$
***
### 2.8

![](../../../assets/Pasted%20image%2020241025102905.png)

f = &A + &A
***
### 2.12

![](../../../assets/Pasted%20image%2020241025102840.png)

`0000000 00001 00001 000 00001 0110011`

由 opcode 可知为 R 型指令，为 `add x1,x1,x1`
***
### 2.14

![](../../../assets/Pasted%20image%2020241025102809.png)

R 型指令，`sub x6,x7,x5`，`0100000 00101 00111 000 00110 0110011`
***
### 2.17

![](../../../assets/Pasted%20image%2020241025102743.png)

#### 2.17.1

`x7 = (x7 << 4) | x6 = 0x0000000AAAAAAAA0 | 0x1234567812345678 = 0x1234567ABABEFEF8`

#### 2.17.2

`x7 = x6 << 4 = 0x2345678123456780`

#### 2.17.3

`x7 = (x5 >> 3) & 0xFEF = 0x0000000015555555 & 0xFEF = 0x545`
***
### 2.22

![](../../../assets/Pasted%20image%2020241025102703.png)

#### 2.22.1

从 0x1FF00000 到 0x200FFFFE

#### 2.22.2

从 0x1FFFF000 到 0x20000FFE
***
### 2.24

![](../../../assets/Pasted%20image%2020241025102623.png)

#### 2.24.1

20

#### 2.24.2

```c
acc = 0;
i = 10;
while (i != 0){
	acc += 2;
	i -= 1;
}
```

#### 2.24.3

$4\times N+1$

#### 2.24.4

```c
acc = 0;
i = 10;
while (i >= 0){
	acc += 2;
	i -= 1;
}
```
***
### 2.29

![](../../../assets/Pasted%20image%2020241025103005.png)


```asm
fib:
	beq x10,x0,done
	addi x5,x0,1
	beq x10,x5,done
	addi x2,x2,-16
	sd x1,0(x2)
	sd x10,8(x2)
	addi x10,x10,-1
	jal x1,fib
	ld x5,8(x2)
	sd x10,8(x2)
	addi x10,x5,-2
	jal x1,fib
	ld x5,8(x2)
	add x10,x10,x5
	ld x1,0(x2)
	addi x2,x2,16
done:
	jalr x0,x1
```

