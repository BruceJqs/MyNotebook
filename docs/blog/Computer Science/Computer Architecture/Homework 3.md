---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
--- 

# Homework 03

## 3.7

![](../../../assets/Pasted%20image%2020250601121816.png)

![](../../../assets/Pasted%20image%2020250601121825.png)

![](../../../assets/Pasted%20image%2020250601121841.png)

```asm
Loop:    fld      T9, 0(Rx)
I0:      fmul.d   T10, f0, T9
I1:      fdiv.d   T11, f0, T9
I2:      fld      T12, 0(Ry)
I3:      fadd.d   T13, f0, T12
I4:      fadd.d   T14, T11, T9
I5:      sd       T12, 0(Ry)
```
***
## 3.8

![](../../../assets/Pasted%20image%2020250601122905.png)

![](../../../assets/Pasted%20image%2020250601122935.png)

初始状态：

| $F_i$ | $RT[F_i]$ |
| ----- | --------- |
| $F_0$ | 0         |
| $F_2$ | 2         |
| $F_4$ | 4         |
| $F_5$ | 5         |
| $F_9$ | 9         |

第一个周期：

| $F_i$ | $RT[F_i]$ |
| ----- | --------- |
| $F_0$ | 0         |
| $F_2$ | 2         |
| $F_4$ | 4         |
| $F_5$ | 9         |
| $F_9$ | 10        |

第二个周期：

| $F_i$ | $RT[F_i]$ |
| ----- | --------- |
| $F_0$ | 0         |
| $F_2$ | 12        |
| $F_4$ | 4         |
| $F_5$ | 11        |
| $F_9$ | 10        |
***
## 3.11

![](../../../assets/Pasted%20image%2020250601134256.png)

![](../../../assets/Pasted%20image%2020250601134311.png)

（a）各指令每个周期情况如下：

| Cycle | $I_0$ | $I_1$ | $I_2$ | $I_3$ | $I_4$ | $I_5$ |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| 1     | IF    |       |       |       |       |       |
| 2     | ID    | IF    |       |       |       |       |
| 3     | EX    | ID    | IF    |       |       |       |
| 4     | MEM1  | stall | ID    | IF    |       |       |
| 5     | MEM2  | stall | stall | ID    | IF    |       |
| 6     | MEM3  | stall | stall | EX    | ID    | IF    |
| 7     | WB    | EX    | stall | MEM   | stall | ID    |
| 8     |       | MEM   | stall | WB    | EX    | stall |
| 9     |       | WB    | EX    |       | MEM   | stall |
| 10    |       |       | MEM1  |       | WB    | EX1   |
| 11    |       |       | MEM2  |       |       | EX2   |
| 12    |       |       | MEM3  |       |       | MEM   |
| 13    |       |       | WB    |       |       | WB    |

所以一次循环因为分支开销损失 4 个周期

（b）如果分支预测正确就不损失，错误就损失 2 个周期

（c）正确预测损失的时钟周期数为 0
***
## 3.13

![](../../../assets/Pasted%20image%2020250601142621.png)

![](../../../assets/Pasted%20image%2020250601142913.png)

A 处理器：

| Cycle | Slot 1               | Slot 2               |
| ----- | -------------------- | -------------------- |
| 1     | lw x1(thread 1)      | lw x1(thread 2)      |
| 2     | stall                | stall                |
| 3     | stall                | stall                |
| 4     | stall                | stall                |
| 5     | lw x2(thread 1)      | lw x2(thread 2)      |
| ...   |                      |                      |
| 33    | beq x9, x1(thread 1) | beq x9, x1(thread 2) |
| 34    | stall                | stall                |
| 35    | stall                | stall                |
| 36    | stall                | stall                |
| ...   |                      |                      |
| 65    | DADDIU(thread 1)     | DADDIU(thread 2)     |
| 66    | blt(thread 1)        | blt(thread 2)        |
| 67    | stall                | stall                |
| 68    | stall                | stall                |
| 69    | stall                | stall                |
| 70    | second iteration     |                      |

一共用 138 个周期

B 处理器：

| Cycle | Slot 1     | Slot 2     | Slot 3     | Slot 4     |
| ----- | ---------- | ---------- | ---------- | ---------- |
| 1     | lw x1      |            |            |            |
| 2     | stall      | lw x2      |            |            |
| 3     | stall      | stall      | lw x3      |            |
| 4     | stall      | stall      | stall      | lw x4      |
| 5     | lw x5      | stall      | stall      | stall      |
| 6     | stall      | lw x6      | stall      | stall      |
| 7     | stall      | stall      | lw x7      | stall      |
| 8     | stall      | stall      | stall      | lw x8      |
| 9     | beq x9, x1 | stall      | stall      | stall      |
| 10    | stall      | beq x9, x2 | stall      | stall      |
| 11    | stall      | stall      | beq x9, x3 | stall      |
| 12    | stall      | stall      | stall      | beq x9, x4 |
| 13    | beq x9, x5 | stall      | stall      | stall      |
| 14    | stall      | beq x9, x6 | stall      | stall      |
| 15    | stall      | stall      | beq x9, x7 | stall      |
| 16    | stall      | stall      | stall      | beq x9, x8 |
| 17    | DADDIU     | stall      | stall      | stall      |
| 18    | blt        |            | stall      | stall      |
| 19    | stall      | lw x1      |            | stall      |
| 20    | stall      | stall      | lw x2      |            |
| 21    | stall      | stall      | stall      | lw x3      |
| 22    | lw x4      | stall      | stall      | stall      |
| 23    | stall      | lw x5      | stall      | stall      |
| 24    | stall      | stall      | lw x6      | stall      |
| 25    | stall      | stall      | stall      | lw x7      |
| 26    | lw x8      | stall      | stall      | stall      |
| 27    | stall      | beq x9, x1 | stall      | stall      |
| 28    | stall      | stall      | beq x9, x2 | stall      |
| 29    | stall      | stall      | stall      | beq x9, x3 |
| 30    | beq x9, x4 | stall      | stall      | stall      |
| 31    | stall      | beq x9, x5 | stall      | stall      |
| 32    | stall      | stall      | beq x9, x6 | stall      |
| 33    | stall      | stall      | stall      | beq x9, x7 |
| 34    | beq x9, x8 | stall      | stall      | stall      |
| 35    | stall      | DADDIU     | stall      | stall      |
| 36    | stall      | blt        |            | stall      |
| 37    | stall      | stall      |            |            |
| 38    |            | stall      |            |            |
| 39    |            | stall      |            |            |

一共用 39 个周期

C 处理器：

与 B 相似，用 39 个周期
***
## 3.16

![](../../../assets/Pasted%20image%2020250601143225.png)

构造指令如下：

```asm
I1: ADD R3, R1, R2
I2: ADD R6, R4, R5
I3: SUB R9, R3, R6
```

第一周期，I1 在 ALU1 中执行，I2 在 ALU2 中执行

第二周期，I1 计算完成，结果准备好写入 CDB；I2 也计算完成

第三周期，两者都要写入 CDB，发生竞争