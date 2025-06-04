---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
--- 

# Homework 05

## 5.1

![](../../../assets/Pasted%20image%2020250604214640.png)

![](../../../assets/Pasted%20image%2020250604214650.png)

（a）C0.L0:(S, AC20, 0020)，返回 0020

（b）C0.L0:(M, AC20, 0080)，C3.L0:(I, AC20, 0020)

（c）C3.L0:(M, AC20, 0080)

（d）C1.L2:(S, AC10, 0010)，返回 0010

（e）C0.L1:(M, AC08, 0048)，C3.L1:(I, AC08, 0008)

（f）C0.L2:(M, AC30, 0078)，M:AC10 $\leftarrow$ 0030（Write-Back）

（g）C3.L2:(M, AC30, 0078)
***
## 5.2

![](../../../assets/Pasted%20image%2020250604214748.png)

![](../../../assets/Pasted%20image%2020250604214808.png)

![](../../../assets/Pasted%20image%2020250604214823.png)

（a）第一条指令是满足 C3 的缓存，第二条指令是满足 C1 的缓存（带 Write-Back），第三条指令是满足内存的，所以实现 1 需要 200 个周期，实现 2 需要 380 个周期

（b）第一条指令是满足内存的，第二条指令是写命中，第三条指令是满足内存的（带 Write-Back），所以实现 1 和实现 2 都需要 225 个周期

（c）第一条指令是满足 C3 的缓存，第二条指令是读命中，第三条指令是满足内存的，所以实现 1 需要 140 个周期，实现 2 需要 230 个周期

（d）第一条指令是满足内存的，第二条指令是满足 C0 和 C3 的（带 Write-Back），第三条指令是满足内存的，所以实现 1 需要 250 个周期，实现 2 需要 340 个周期
***
## 5.9

![](../../../assets/Pasted%20image%2020250604214841.png)

![](../../../assets/Pasted%20image%2020250604214850.png)


（a）

第一条指令：

信息：

- 从 C3 到 Dir4 的读失效请求信息（011 $\rightarrow$ 010 $\rightarrow$ 000 $\rightarrow$ 100）
- 从 M4 到 C3 的读响应信息（100 $\rightarrow$ 101 $\rightarrow$ 111 $\rightarrow$ 011）

C3 高速缓存第 0 行从 <I, x, x, ...> 到 <S, 4, 4, ...>

Dir 4 从 <I, 00000000> 到 <S, 00001000>，M4 = 4444...

第二条指令：

信息：

- 从 C3 到 Dir2 的读失效请求信息（011 $\rightarrow$ 010）
- 从 M2 到 C3 的读响应信息（010 $\rightarrow$ 011）

C3 高速缓存第 0 行从 <S, 4, 4, ...> 到 <S, 2, 2, ...>

Dir2 从 <I, 00000000> 到 <S, 00001000>，M2 = 2222...

第三条指令：

信息：

- 从 C7 到 M4 的写失效请求信息（111 $\rightarrow$ 110 $\rightarrow$ 100）
- 从 Dir4 到 C3 的失效信息（100 $\rightarrow$ 101 $\rightarrow$ 111 $\rightarrow$ 011）
- 从 C3 到 Dir4 的信息（011 $\rightarrow$ 010 $\rightarrow$ 000 $\rightarrow$ 100）
- 从 Dir4 到 C7 的信息（100 $\rightarrow$ 101 $\rightarrow$ 111）

C3 高速缓存第 0 行从 <S, 2, 2, ...> 到 <I, x, x, ...>，C7 高速缓存第 0 行从 <I, x, x, ...> 到 <M, aaaa, ...>

Dir 4 从 <S, 00001000> 到 <M, 10000000>，M4 = 4444...

第四条指令：

信息：

- 从 C1 到 M4 的写失效请求信息（001 $\rightarrow$ 000 $\rightarrow$ 100）
- 从 Dir4 到 C7 的失效信息（100 $\rightarrow$ 101 $\rightarrow$ 111）
- 从 C7 到 Dir4 的信息（带 Write-Back）（111 $\rightarrow$ 110 $\rightarrow$ 100）
- 从 Dir4 到 C1 的写响应信息（100 $\rightarrow$ 101 $\rightarrow$ 001）

C7 高速缓存第 0 行从 <M, aaaa, ...> 到 <I, x, x, ...>，C1 高速缓存第 0 行从 <I, x, x, ...> 到 <M, bbbb, ...>

Dir 4 从 <M, 10000000> 到 <M, 00000010>，M4 = aaaa...

（b）

第一条指令：

信息：

- 从 C3 到 M0 的读失效请求信息（011 $\rightarrow$ 010 $\rightarrow$ 000）
- 从 M0 到 C3 的读响应信息（000 $\rightarrow$ 001 $\rightarrow$ 011）

C3 高速缓存第 0 行从 <I, x, x, ...> 到 <S, 0, 0, ...>

Dir 0 从 <I, 00000000> 到 <S, 00000100>，M0 = 0000...

第二条指令：

信息：

- 从 C3 到 M2 的读失效请求信息（011 $\rightarrow$ 010）
- 从 M2 到 C3 的读响应信息（010 $\rightarrow$ 011）

C3 高速缓存第 0 行从 <S, 0, 0, ...> 到 <S, 2, 2, ...>

Dir2 从 <I, 00000000> 到 <S, 00000100>，M2 = 2222...

第三条指令：

信息：

- 从 C6 到 M4 的写失效请求信息（110 $\rightarrow$ 100）
- 从 M4 到 C6 的写响应信息（100 $\rightarrow$ 110）

C6 高速缓存第 0 行从 <I, x, x, ...> 到 <M, aaaa, ...>

Dir 4 从 <I, 00000000> 到 <M, 01000000>，M4 = aaaa...

第四条指令：

信息：

- 从 C3 到 M4 的写失效请求信息（011 $\rightarrow$ 010 $\rightarrow$ 000 $\rightarrow$ 100）
- 从 M4 到 C3 的写响应信息（100 $\rightarrow$ 101 $\rightarrow$ 111 $\rightarrow$ 011）

C3 高速缓存第 0 行从 <S, 2, 2, ...> 到 <M, aaaa, ...>

Dir 4 从 <M, 01000000> 到 <M, 00001000>，M4 = bbbb...

（c）

第一条指令：

信息：

- 从 C0 到 M7 的读失效请求信息（000 $\rightarrow$ 001 $\rightarrow$ 011 $\rightarrow$ 111）
- 从 M7 到 C0 的读响应信息（111 $\rightarrow$ 110 $\rightarrow$ 100 $\rightarrow$ 000）

C0 高速缓存第 0 行从 <I, x, x, ...> 到 <S, 7, 7, ...>

Dir 7 从 <I, 00000000> 到 <S, 00000001>，M7 = 7777...

第二条指令：

信息：

- 从 C3 到 M4 的读失效请求信息（011 $\rightarrow$ 010 $\rightarrow$ 000 $\rightarrow$ 100）
- 从 M4 到 C3 的读响应信息（100 $\rightarrow$ 101 $\rightarrow$ 111 $\rightarrow$ 011）

C3 高速缓存第 0 行从 <I, x, x, ...> 到 <S, 4, 4, ...>

Dir 4 从 <I, 00000000> 到 <S, 00001000>，M4 = 4444...

第三条指令：

信息：

- 从 C6 到 M2 的写失效请求信息（110 $\rightarrow$ 010）
- 从 M2 到 C6 的写响应信息（010 $\rightarrow$ 110）

C6 高速缓存第 0 行从 <I, x, x, ...> 到 <M, 2, 2, ...>

Dir2 从 <I, 00000000> 到 <M, 01000000>，M2 = aaaa...

第四条指令：

信息：

- 从 C2 到 M2 的写命中

C2 高速缓存第 0 行从 <I, x, x, ...> 到 <M, 2, 2, ...>

Dir2 从 <M, 00000100> 到 <M, 00000100>，M2 = bbbb...














