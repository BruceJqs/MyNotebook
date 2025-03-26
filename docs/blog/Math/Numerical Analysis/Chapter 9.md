---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
--- 

# Chapter 09 : Approximating Eigenvalues

## The Power Method

### The Original Method

假设：$\mathbf{A}$ 是一个 $n\times n$ 的矩阵，且恰有一个特征值 $\lambda_1$ 的绝对值最大，有 $n$ 个特征值 $\lambda_1,\lambda_2,\cdots,\lambda_n$（$|\lambda_1|>|\lambda_2|\geq\cdots\geq|\lambda_n|$），对应为 $n$ 个线性独立的特征向量 $\mathbf{v}_1,\mathbf{v}_2,\cdots,\mathbf{v}_n$

