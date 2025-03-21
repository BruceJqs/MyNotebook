---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
--- 

# Homework 05

## 7.2.3

![](../../../assets/Pasted%20image%2020250321110456.png)

![](../../../assets/Pasted%20image%2020250321110515.png)

（a）$|\lambda\mathbf{E}-\mathbf{A}|=|\begin{pmatrix}\lambda-2 & 1\\1 & \lambda-2\end{pmatrix}|=(\lambda-2)^2-1=0\Rightarrow\lambda_1=3,\lambda_2=1$

$\therefore\rho(\mathbf{A})=3>1$，不收敛

（b）$|\lambda\mathbf{E}-\mathbf{A}|=|\begin{pmatrix}\lambda & -1\\-1 & \lambda-1\end{pmatrix}|=\lambda(\lambda-1)-1=0\Rightarrow\lambda_1=\frac{1+\sqrt{5}}{2},\lambda_2=\frac{1-\sqrt{5}}{2}$

$\therefore\rho(\mathbf{A})=\frac{1+\sqrt{5}}{2}>1$，不收敛

（c）$|\lambda\mathbf{E}-\mathbf{A}|=|\begin{pmatrix}\lambda & -\frac{1}{2}\\-\frac{1}{2} & \lambda\end{pmatrix}|=\lambda^2-\frac{1}{4}=0\Rightarrow\lambda_1=\frac{1}{2},\lambda_2=-\frac{1}{2}$

$\therefore\rho(\mathbf{A})=\frac{1}{2}<1$，收敛

（d）$|\lambda\mathbf{E}-\mathbf{A}|=|\begin{pmatrix}\lambda-1 & -1\\2 & \lambda+2\end{pmatrix}|=\lambda^2+\lambda=0\Rightarrow\lambda_1=0,\lambda_2=-1$

$\therefore\rho(\mathbf{A})=1$，不收敛

（e）$|\lambda\mathbf{E}-\mathbf{A}|=|\begin{pmatrix}\lambda-2 & -1 & 0\\-1 & \lambda-2 & 0\\0 & 0 & \lambda-3\end{pmatrix}|=0\Rightarrow\lambda_1=\lambda_2=3,\lambda_3=1$

$\therefore\rho(\mathbf{A})=3>1$，不收敛

（f）$|\lambda\mathbf{E}-\mathbf{A}|=|\begin{pmatrix}\lambda+1 & -2 & 0\\0 & \lambda-3 & -4\\0 & 0 & \lambda-7\end{pmatrix}|=0\Rightarrow\lambda_1=7,\lambda_2=3,\lambda_3=-1$

$\therefore\rho(\mathbf{A})=7>1$，不收敛

（g）$|\lambda\mathbf{E}-\mathbf{A}|=|\begin{pmatrix}\lambda-1 & -1 & -1\\-2 & \lambda-3 & -2\\-1 & -1 & \lambda-2\end{pmatrix}|=0\Rightarrow\lambda_1=\lambda_2=1,\lambda_3=5$

$\therefore\rho(\mathbf{A})=5>1$，不收敛

（h）$|\lambda\mathbf{E}-\mathbf{A}|=|\begin{pmatrix}\lambda-3 & -2 & 1\\-1 & \lambda+2 & -3\\-2 & 0 & \lambda-4\end{pmatrix}|=0\Rightarrow\lambda_1=3,\lambda_2=4,\lambda_3=-2$

$\therefore\rho(\mathbf{A})=4>1$，不收敛
***
## 7.3.13

![](../../../assets/Pasted%20image%2020250321110607.png)

![](../../../assets/Pasted%20image%2020250321110640.png)

$$
\begin{aligned}
\text{det}(T_w)&=\text{det}(D-wL)^{-1}\text{det}((1-w)D+wU)\\
&=\text{det}(D^{-1})\text{det}((1-w)D+wU)\\
&=\text{det}((1-w)I+wD^{-1}U)=(1-w)^n\\
\therefore\rho(T_w)^n&>>|(1-w)^n|=|(1-w)|^n\\
&\Rightarrow\rho(T_w)>>|1-w|
\end{aligned}
$$


