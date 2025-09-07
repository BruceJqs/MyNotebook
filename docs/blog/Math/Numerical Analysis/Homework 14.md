---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
# comments: true
--- 

# Homework 14

## 4.7.1

![](../../../assets/Pasted%20image%2020250619162547.png)

![](../../../assets/Pasted%20image%2020250619171013.png)

![](../../../assets/Pasted%20image%2020250619170330.png)

（a） 利用勒让德多项式来构造，四阶多项式为：$P_0=1,P_1=x,P_2=\frac{3}{2}x^2-\frac{1}{2},P_3=\frac{5}{2}x^3-\frac{3}{2}x$

使用 $P_3$ 的根为 $0,\pm\sqrt{\frac{3}{5}}$，有：

$$
\begin{aligned}
\int_1^{1.5}x^2\ln xdx&=\frac{1}{4}\int_{-1}^1(\frac{t+5}{4})^2\ln(\frac{t+5}{4})dt\\
&\approx\frac{1}{4}[0.5556*(\frac{5-0.7746}{4})^2\ln\frac{5-0.7746}{4}+0.8889*(\frac{5}{4})^2\ln\frac{5}{4}\\
&+0.5556*(\frac{5+0.7746}{4})^2\ln\frac{5+0.7746}{4}]\approx 0.1923
\end{aligned}
$$

（b）

$$
\begin{aligned}
\int_0^1 x^2e^{-x}dx&=\frac{1}{2}\int_{-1}^1(\frac{t+1}{2})^2e^{-\frac{t+1}{2}}dt\\
&\approx\frac{1}{2}[0.5556*(\frac{1-0.7746}{2})^2e^{-\frac{1-0.7746}{2}}+0.8889*(\frac{1}{2})^2e^{-\frac{1}{2}}\\
&+0.5556*(\frac{1+0.7746}{2})^2e^{-\frac{1+0.7746}{2}}]\approx 0.1594
\end{aligned}
$$

同理可得

![](../../../assets/Pasted%20image%2020250619171817.png)
***
## 4.7.5

![](../../../assets/Pasted%20image%2020250619162616.png)

要求精度为 3，那么要求对 $f(x)=1,x,x^2,x^3$ 均成立，有方程组：

$$
\begin{cases}
2=a+b\\
0=-a+b+c+d\\
\frac{2}{3}=a+b-2c+2d\\
0=-a+b+3c+3d
\end{cases}
$$

解得 $a=1,b=1,c=\frac{1}{3},d=\frac{1}{3}$
***
## 5.3.5(a)(b)

![](../../../assets/Pasted%20image%2020250619172241.png)

（a）$y''=\frac{2}{t}y'-\frac{2}{t^2}y+2te^t+t^2e^t=\frac{2}{t^2}y+4te^4+t^2e^t$

二阶泰勒方法为 $w_{i+1}=w_i+hy'+\frac{h^2}{2}y''$

| $t$ | $w_i$    | $y(t)$   |
| --- | -------- | -------- |
| 1   | 0        | 0        |
| 1.1 | 0.339785 | 0.345920 |
| 1.5 | 3.910985 | 3.967666 |
| 1.6 | 5.643081 | 5.720962 |
| 1.9 | 14.15268 | 14.32308 |
| 2.0 | 18.46999 | 18.68310 |

（b）插值法即可

![](../../../assets/Pasted%20image%2020250619174617.png)