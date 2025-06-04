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

![](../../../assets/Pasted%20image%2020250603122951.png)

![](../../../assets/Pasted%20image%2020250603121428.png)

![](../../../assets/Pasted%20image%2020250603121441.png)

假设 `seq_length` 保存在 `x3` 寄存器当中，RISC-V 代码如下：

```asm
li x1, 0
Loop:
	flw f0, 0(RtipL)
	flw f1, 0(RclL)
	flw f2, 4(RtipL)
	flw f3, 4(RclL)
	flw f4, 8(RtipL)
	flw f5, 8(RclL)
	flw f6, 12(RtipL)
	flw f7, 12(RclL)
	flw f8, 0(RtipR)
	flw f9, 0(RclR)
	flw f10, 4(RtipR)
	flw f11, 4(RclR)
	flw f12, 8(RtipR)
	flw f13, 8(RclR)
	flw f14, 12(RtipR)
	flw f15, 12(RclR)
	fmul.s f16, f0, f1
	fmul.s f17, f2, f3
	fmul.s f18, f4, f5
	fmul.s f19, f6, f7
	fadd.s f20, f16, f17
	fadd.s f20, f20, 18
	fadd.s f20, f20, f19
	fmul.s f16, f8, f9
	fmul.s f17, f10, f11
	fmul.s f18, f12, f13
	fmul.s f19, f14, f15
	fadd.s f21, f16, f17
	fadd.s f21, f21, 18
	fadd.s f21, f21, f19
	fmul.s f20, f20, f21
	fsw f20, 0(RclP)
	add RclP, RclP, 4
	addi x1, x1, 1
	and x2, x2, 3
	bne x2, Skip
Skip:
	blt x1, x3, Loop
```

RV64V 代码如下：

```asm
li x1, 0
vcfgd 10 * FP32
Loop:
	vld v0, 0(RclL)
	vld v1, 0(RclR)
	vld v2, 0(RtipL)
	vld v3, 16(RtipL)
	vld v4, 32(RtipL)
	vld v5, 48(RtipL)
	vld v6, 0(RtipR)
	vld v7, 16(RtipR)
	vld v8, 32(RtipR)
	vld v9, 48(RtipR)
	vmul v2, v2, v0
	vmul v3, v3, v0
	vmul v4, v4, v0
	vmul v5, v5, v0
	vmul v6, v6, v1
	vmul v7, v7, v1
	vmul v8, v8, v1
	vmul v9, v9, v1
	vsum f0, v2
	vsum f1, v3
	vsum f2, v4
	vsum f3, v5
	vsum f4, v6
	vsum f5, v7
	vsum f6, v8
	vsum f7, v9
	fmul.s f0, f0, f4
	fmul.s f1, f1, f5
	fmul.s f2, f2, f6
	fmul.s f3, f3, f7
	fsw f0, 0(RclP)
	fsw f1, 4(RclP)
	fsw f2, 8(RclP)
	fsw f3, 12(RclP)
	add RclP, RclP, 16
	add RclL, RclL, 16
	add RclR, RclR, 16
	addi x1, x1, 1
	blt, x1, x3, Loop
```
***
## 4.3

![](../../../assets/Pasted%20image%2020250603130512.png)

| chime | inst1             | inst2           |
| ----- | ----------------- | --------------- |
| 1     | vld v0, 0(RclL)   |                 |
| 2     | vld v1, 0(RclR)   |                 |
| 3     | vld v2, 0(RtipL)  | vmul v2, v2, v0 |
| 4     | vld v3, 16(RtipL) | vmul v3, v3, v0 |
| 5     | vld v4, 32(RtipL) | vmul v4, v4, v0 |
| 6     | vld v5, 48(RtipL) | vmul v5, v5, v0 |
| 7     | vld v6, 0(RtipR)  | vmul v6, v6, v1 |
| 8     | vld v7, 16(RtipR) | vmul v7, v7, v1 |
| 9     | vld v8, 32(RtipR) | vmul v8, v8, v1 |
| 10    | vld v9, 48(RtipR) | vmul v9, v9, v1 |
| 11    | vsum f0, v2       |                 |
| 12    | vsum f1, v3       |                 |
| 13    | vsum f2, v4       |                 |
| 14    | vsum f3, v5       |                 |
| 15    | vsum f4, v6       |                 |
| 16    | vsum f5, v7       |                 |
| 17    | vsum f6, v8       |                 |
| 18    | vsum f7, v9       |                 |

共需要 18 个时钟间隔，每次运算出一个结果需要 15 FLOPs，所以每个 FLOP 需要 $18/(15*4)=0.3$ 个时钟周期
***
## 4.5

![](../../../assets/Pasted%20image%2020250603141839.png)

```c
__global__ void compute(float * clL, float *clR, float *clP, float *tiPL, float * tiPR){
	int i, k = threadIdx.x;
	__shared__ float clL_s[4], clR_s[4];
	for(i = 0; i < 4; i++){
		clL_s[i] = clL[k * 4 + i];
		clR_s[i] = clR[k * 4 + i];
	}
	clP[k * 4] = (tiPL[k + AA] * clL_s[A] + tiPL[k + AC] * clL_s[C] + tiPL[k + AG] * clL_s[G] + tiPL[k + AT] * clL_s[T]) * (tiPR[k + AA] * clR_s[A] + tiPR[k + AC] * clR_s[C] + tiPR[k + AG] * clR_s[G] + tiPR[k + AT] * clR_s[T]);
	clP[k * 4 + 1] = (tiPL[k + CA] * clL_s[A] + tiPL[k + CC] * clL_s[C] + tiPL[k + CG] * clL_s[G] + tiPL[k + CT] * clL_s[T]) * (tiPR[k + CA] * clR_s[A] + tiPR[k + CC] * clR_s[C] + tiPR[k + CG] * clR_s[G] + tiPR[k + CT] * clR_s[T]);
	clP[k * 4 + 2] = (tiPL[k + GA] * clL_s[A] + tiPL[k + GC] * clL_s[C] + tiPL[k + GG] * clL_s[G] + tiPL[k + GT] * clL_s[T]) * (tiPR[k + GA] * clR_s[A] + tiPR[k + GC] * clR_s[C] + tiPR[k + GG] * clR_s[G] + tiPR[k + GT] * clR_s[T]);
	clP[k * 4 + 3] = (tiPL[k + TA] * clL_s[A] + tiPL[k + TC] * clL_s[C] + tiPL[k + TG] * clL_s[G] + tiPL[k + TT] * clL_s[T]) * (tiPR[k + TA] * clR_s[A] + tiPR[k + TC] * clR_s[C] + tiPR[k + TG] * clR_s[G] + tiPR[k + TT] * clR_s[T]);
}
```
***
## 4.7

![](../../../assets/Pasted%20image%2020250603142119.png)

![](../../../assets/Pasted%20image%2020250603142132.png)

![](../../../assets/Pasted%20image%2020250603142100.png)

```asm
mul.u64 %r1, %ctaid.x, 4000
mul.u64 %r2, %tid.x, 4
add.u64 %r1, %r1, %r2
ld.param.u64 %r2, [clL]
add.u64 %r1, %r1, %r2

mul.u64 %r2, %ctaid.x, 2
add.u64 %r2, %r2, 1
mul.u64 %r2, %r2, 2000
mul.u64 %r3, %tid.x, 4
add.u64 %r2, %r2, %r3
ld.param.u64 %r3, [clR]
add.u64 %r2, %r2, %r3
ld.global.f32 %f1, [%r1+0]
st.shared.f32 [clL_s+0], %f1
ld.global.f32 %f1, [%r2+0]
st.shared.f32 [clR_s+0], %f1
ld.global.f32 %f1, [%r1+4]
st.shared.f32 [clL_s+4], %f1
ld.global.f32 %f1, [%r2+4]
st.shared.f32 [clR_s+4], %f1
ld.global.f32 %f1, [%r1+8]
st.shared.f32 [clL_s+8], %f1
ld.global.f32 %f1, [%r2+8]
st.shared.f32 [clR_s+8], %f1
ld.global.f32 %f1, [%r1+12]
st.shared.f32 [clL_s+12], %f1
ld.global.f32 %f1, [%r2+12]
st.shared.f32 [clR_s+12], %f1

mul.u64 %r1, %ctaid.x, 16000
mul.u64 %r2, %tid.x, 64
add.u64 %r1, %r1, %r2
ld.param.u64 %r2, [tiPL]
add.u64 %r1, %r1, %r2

mul.u64 %r2, %ctaid.x, 2
add.u64 %r2, %r2, 1
mul.u64 %r2, %r2, 8000
mul.u64 %r3, %tid.x, 64
add.u64 %r2, %r2, %r3
ld.param.u64 %r3, [tiPR]
add.u64 %r2, %r2, %r3

mul.u64 %r3, %ctaid.x, 24000
mul.u64 %r4, %tid.x, 16
add.u64 %r3, %r3, %r4
ld.param.u64 %r4, [clP]
add.u64 %r3, %r3, %r4
ld.global.f32 %f1, [%r1]
ld.global.f32 %f2, [%r1+4]
...
ld.global.f32 %f16, [%r1+60]
ld.global.f32 %f17, [%r2]
ld.global.f32 %f18, [%r2+4]
...
ld.global.f32 %f32, [%r2+60]
ld.shared.f32 %f33, [clL_s+0]
ld.shared.f32 %f34, [clL_s+4]
ld.shared.f32 %f35, [clL_s+8]
ld.shared.f32 %f36, [clL_s+12]
ld.shared.f32 %f37, [clR_s+0]
ld.shared.f32 %f38, [clR_s+4]
ld.shared.f32 %f39, [clR_s+8]
ld.shared.f32 %f40, [clR_s+12]

mul.f32 %f1, %f1, %f33
mul.f32 %f2, %f2, %f34
mul.f32 %f3, %f3, %f35
mul.f32 %f4, %f4, %f36
add.f32 %f1, %f1, %f2
add.f32 %f1, %f1, %f3
add.f32 %f1, %f1, %f4
mul.f32 %f17, %f17, %f37
mul.f32 %f18, %f18, %f38
mul.f32 %f19, %f19, %f39
mul.f32 %f20, %f20, %f40
add.f32 %f17, %f17, %f18
add.f32 %f17, %f17, %f19
add.f32 %f17, %f17, %f20
st.shared.f32 [%r3], %f17

mul.f32 %f5, %f5, %f33
mul.f32 %f6, %f6, %f34
mul.f32 %f7, %f7, %f35
mul.f32 %f8, %f8, %f36
add.f32 %f5, %f5, %f6
add.f32 %f5, %f5, %f7
add.f32 %f5, %f5, %f8
mul.f32 %f21, %f21, %f37
mul.f32 %f22, %f22, %f38
mul.f32 %f23, %f23, %f39
mul.f32 %f24, %f24, %f40
add.f32 %f21, %f21, %f22
add.f32 %f21, %f21, %f23
add.f32 %f21, %f21, %f24
st.shared.f32 [%r3+4], %f21

mul.f32 %f9, %f9, %f33
mul.f32 %f10, %f10, %f34
mul.f32 %f11, %f11, %f35
mul.f32 %f12, %f12, %f36
add.f32 %f9, %f9, %f10
add.f32 %f9, %f9, %f11
add.f32 %f9, %f9, %f12
mul.f32 %f25, %f25, %f37
mul.f32 %f26, %f26, %f38
mul.f32 %f27, %f27, %f39
mul.f32 %f28, %f28, %f40
add.f32 %f25, %f25, %f26
add.f32 %f25, %f25, %f27
add.f32 %f25, %f25, %f28
st.shared.f32 [%r3+8], %f25

mul.f32 %f13, %f13, %f33
mul.f32 %f14, %f14, %f34
mul.f32 %f15, %f15, %f35
mul.f32 %f16, %f16, %f36
add.f32 %f13, %f13, %f14
add.f32 %f13, %f13, %f15
add.f32 %f13, %f13, %f16
mul.f32 %f29, %f29, %f37
mul.f32 %f30, %f30, %f38
mul.f32 %f31, %f31, %f39
mul.f32 %f32, %f32, %f40
add.f32 %f29, %f29, %f30
add.f32 %f29, %f29, %f31
add.f32 %f29, %f29, %f32
st.shared.f32 [%r3+12], %f29
```
***
## 4.11

![](../../../assets/Pasted%20image%2020250603142151.png)

![](../../../assets/Pasted%20image%2020250603142217.png)

（a）

```c
for(i = 0; i < 32; i += 2)
	dot[i] = dot[i] + dot[i + 1];
for(i = 0; i < 16; i += 4)
	dot[i] = dot[i] + dot[i + 2];
for(i = 0; i < 8; i += 8)
	dot[i] = dot[i] + dot[i + 4];
for(i = 0; i < 4; i += 16)
	dot[i] = dot[i] + dot[i + 8];
for(i = 0; i < 2; i += 32)
	dot[i] = dot[i] + dot[i + 16];
dot[0] += dot[32];
```

（b）

```asm
vadd v0(0), v0(4)
vadd v0(8), v0(12)
vadd v0(16), v0(20)
vadd v0(24), v0(28)
vadd v0(32), v0(36)
vadd v0(40), v0(44)
vadd v0(48), v0(52)
vadd v0(56), v0(60)
```
***
## 4.14

![](../../../assets/Pasted%20image%2020250603142229.png)

![](../../../assets/Pasted%20image%2020250603142237.png)

（a）因为 A 的下标都是 i，不可能存在依赖，所以我们只考虑 B：

- RAW 冒险，在迭代 $i_1$ 写入 $B[4*i_1+5]$，在迭代 $i_2$ 读取 $B[2*i_2+4]$，那么有 $4*i_1+5=2*i_2+4,i_1<i_2$，分析奇偶性即可看出不可能
- WAR 冒险，在迭代 $i_1$ 写入 $B[2*i_1+4]$，在迭代 $i_2$ 读取 $B[4*i_2+5]$，那么有 $2*i_1+4=4*i_2+5,i_1<i_2$，分析奇偶性即可看出不可能
- WAW 冒险，在迭代 $i_1$ 写入 $B[4*i_1+5]$，在迭代 $i_2$ 写入 $B[4*i_2+5]$，不可能

综上并没有依赖

（b）输出依赖：$S_1$ 和 $S_3$（$A[i]$）

反依赖：$S_4$ 和 $S_3$（$C[i]$）

重写代码如下：

```c
for(i = 0; i < 100; i++)
	T[i] = A[i] * B[i];
	B[i] = T[i] + c;
	A1[i] = C[i] * c;
	C1[i] = D[i] * A1[i];
```

真依赖：$S_4$ 和 $S_3$（$A[i]$），$S_2$ 和 $S_1$（$T[i]$）

（c）对于数组 B 的迭代 i 和迭代 i+1 有反依赖，可以通过在 S2 对 B 的重命名来避免