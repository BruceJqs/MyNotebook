---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
# comments: true
--- 

# Chapter 01 : 数学基础

!!! abstract "Abstract"

	基本上都是一些数论基础，在[离散](https://note.eternity1005.top/blog/Math/Discrete%20mathmatics/Discrete%20mathmatics%20notes-Ch04/)中大部分都有涉及

## 补充内容

> 本质上，补码/异或运算实际上就是模运算（加法逆元）

### 补码

对于一个八位十进制数 2，它的二进制为 `00000010`，而 -2 的补码为 `11111110`，我们可以得到：

![](../../../assets/Pasted%20image%2020250224190601.png)
***
### 异或

对于一位异或操作来说，我们有：

- $1\oplus 1=0\Leftrightarrow 1+1\equiv 0(\text{mod }2)$
- $1\oplus 0=1\Leftrightarrow 1+0\equiv 1(\text{mod }2)$
- $0\oplus 1=0\Leftrightarrow 0+1\equiv 1(\text{mod }2)$
- $0\oplus 0=0\Leftrightarrow 0+0\equiv 0(\text{mod }2)$

