---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
# comments: true
--- 

# Homework 09

## 8.1.5

![](../../../assets/Pasted%20image%2020250416150222.png)

（a）我们有 $b_0=\sum\limits_{i=1}^m 1=10,b_1=\sum\limits_{i=1}^mx_i=54.1,b_2=\sum\limits_{i=1}^mx_i^2=303.39,c_0=\sum\limits_{i=1}^my_i=1958.39,c_1=\sum\limits_{i=1}^my_ix_i=11366.843$

$$
\begin{bmatrix}
10 & 54.1\\
54.1 & 303.39
\end{bmatrix}\begin{bmatrix}
a_0\\
a_1
\end{bmatrix}=\begin{bmatrix}
1958.39\\
11366.843
\end{bmatrix}
$$

解得 $a_0=-194.138,a_1=72.0845$，即 $P(x)=72.0845x-194.138,\text{error}=329$

（b）$b_3=1759.831,b_4=10523.1207,c_2=68006.6811$

$$
\begin{bmatrix}
10 & 54.1 & 303.39\\
54.1 & 303.39 & 1759.831\\
303.39 & 1759.831 & 10523.1207
\end{bmatrix}\begin{bmatrix}
a_0\\
a_1\\
a_2
\end{bmatrix}=\begin{bmatrix}
1958.39\\
11366.843\\
68006.6811
\end{bmatrix}
$$

解得 $a_0=1.23556,a_1=-1.14352,a_2=6.61821$，即 $P(x)=6.61821x^2-1.14352x+1.23556,\text{error}=1.44\times 10^{-3}$

（c）$b_5=64607.97751,b_6=405616.743519,c_3=417730.09823$

$$
\begin{bmatrix}
10 & 54.1 & 303.39 & 1759.831\\
54.1 & 303.39 & 1759.831 & 10523.1207\\
303.39 & 1759.831 & 10523.1207 & 64607.97751\\
1759.831 & 10523.1207 & 64607.97751 & 405616.743519
\end{bmatrix}\begin{bmatrix}
a_0\\
a_1\\
a_2\\
a_3
\end{bmatrix}=\begin{bmatrix}
1958.39\\
11366.843\\
68006.6811\\
417730.09823
\end{bmatrix}
$$

解得 $a_0=3.42904,a_1=-2.37919,a_2=6.84557,a_3=-0.0136742$，即 $P(x)=-0.0136742x^3+6.84557x^2-2.37919x+3.42904,\text{error}=5.27\times 10^{-4}$

（d）$\ln y=\ln b+ax$，$c_0=52.0336,c_1=285.4898$

$$
\begin{bmatrix}
10 & 54.1\\
54.1 & 303.39
\end{bmatrix}\begin{bmatrix}
a_0\\
a_1
\end{bmatrix}=\begin{bmatrix}
52.0336\\
285.4898
\end{bmatrix}
$$

解得 $a_0=3.1888,a_1=0.372382$，即 $P(x)=24.2588e^{0.372382x},\text{error}=418$

（e）$\ln y=\ln b+a\ln x$，$b_0=10, b_1=16.6995,b_2=28.2537,c_0=52.0336,c_1=87.6334$

$$
\begin{bmatrix}
10 & 16.6995\\
16.6995 & 28.2537
\end{bmatrix}\begin{bmatrix}
a_0\\
a_1
\end{bmatrix}=\begin{bmatrix}
52.0336\\
87.6334
\end{bmatrix}
$$

解得 $a_0=1.8308,a_1=2.01954$，即 $P(x)=6.23903x^{2.01954},\text{error}=0.00703$
***
## 8.2.3

![](../../../assets/Pasted%20image%2020250416182226.png)

（a）$\int_{-1}^1 1dx=2,\int_{-1}^1 x^2dx=\frac{2}{3},\int_{-1}^1(x^2-2x+3)dx=\frac{20}{3},\int_{-1}^1(x^2-2x+3)xdx=-\frac{4}{3}$

$\therefore f(x)\approx \frac{10}{3}-2x=3.33333-2x$

（b）$\int_{-1}^1x^3dx=0,\int_{-1}^1x^4dx=\frac{2}{5}$

$\therefore f(x)\approx 0.6x$

（c）$\int_{-1}^1\frac{1}{x+2}dx=\ln 3,\int_{-1}^1\frac{x}{x+2}dx=2-2\ln 3$

$\therefore f(x)\approx \frac{\ln 3}{2}+(3-3\ln 3)x=0.54931-0.29584x$

（d）$\int_{-1}^1e^xdx=e-\frac{1}{e},\int_{-1}^1xe^xdx=\frac{2}{e}$

$\therefore f(x)\approx 1.17520+1.10364x$

（e）$\int_{-1}^1(\frac{1}{2}\cos x+\frac{1}{3}\sin 2x)dx=\sin 1,\int_{-1}^1(\frac{1}{2}x\cos x+\frac{1}{3}x\sin 2x)dx=-\frac{1}{6}(2\cos 2-\sin 2)$

$\therefore f(x)\approx 0.42074+0.42540x$

（f）$\int_{-1}^1\ln(x+2)dx=3\ln 3-2,\int_{-1}^1x\ln(x+2)dx=\frac{1}{2}(4-3\ln 3)$

$\therefore f(x)=0.64792+0.52812x$
***
## 8.2.11

![](../../../assets/Pasted%20image%2020250416182247.png)

$$
\begin{aligned}
B_1&=\frac{\int_0^{\infty}xe^{-x}dx}{\int_0^{\infty}e^{-x}dx}=1\quad L_1(x)=(x-B_1)L_0(x)=x-1\\
B_2&=\frac{\int_0^{\infty}(x-1)^2xe^{-x}dx}{\int_0^{\infty}(x-1)^2e^{-x}dx}=3\quad C_2=\frac{\int_0^{\infty}x(x-1)e^{-x}dx}{\int_0^{\infty}e^{-x}dx}=1\\
L_2(x)&=(x-B_2)L_1(x)-C_2L_0(x)=x^2-4x+2\\
B_3&=\frac{\int_0^{\infty}x(x^2-4x+2)^2e^{-x}dx}{\int_0^{\infty}(x^2-4x+2)^2e^{-x}dx}=5\quad C_3=\frac{\int_0^{\infty}x(x^2-4x+2)(x-1)e^{-x}dx}{\int_0^{\infty}(x-1)^2e^{-x}dx}=4\\
L_3(x)&=(x-B_3)L_2(x)-C_3L_1(x)=(x-5)(x^2-4x+2)-4(x-1)=x^3-9x^2+18x-6\\
\end{aligned}
$$
