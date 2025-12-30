# Lab05-ZJU-I型机械臂逆运动学仿真

## 解析解推导

假设 $T_{06}=\begin{bmatrix}nx & ox & ax & dx\\ny & oy & ay & dy\\nz & oz & az & dz\\0 & 0 & 0 & 1\end{bmatrix}$

由于 $T_{06}=T_{01}T_{12}T_{23}T_{34}T_{45}T_{56}$，变换 $T_{01}^{-1}T_{06}= T_{12}T_{23}T_{34}T_{45}T_{56}$：

![](../../../assets/Pasted%20image%2020251102211728.png)

解二元一次方程：

$$
\begin{cases}
ay\cos(q_{1})-ax\sin(q_{1})=\sin(q_{5}) \\
dy\cos(q_{1})-dx\sin(q_{1})=\frac{171\sin(q_{5})}{2000}+\frac{23}{1000}
\end{cases}
$$

消去 $\sin(q_{5})$ 得 $(2000dy-171ay)\cos(q_{1})-(2000dx-171ax)\sin(q_{1})=46$，即可编写代码解得 $q_{1}$：

```matlab
py = 2000 * dy - 171 * ay;
px = 2000 * dx - 171 * ax;
d = 46;
q1_1 = atan2(py, px) - atan2(d, sqrt(py^2 + px^2 - d^2))
q1_2 = atan2(py, px) - atan2(d, - sqrt(py^2 + px^2 - d^2))
```

同时根据：

$$
\begin{cases}
ny\cos(q_{1})-nx\sin(q_{1})=\cos(q_{5})\cos(q_{6}) \\
oy\cos(q_{1})-ox\sin(q_{1})=-\cos(q_{5})\sin(q_{6})
\end{cases}
$$

两式相除可以得到 $\tan(q_{6})=-\frac{oy\cos(q_{1})-ox\sin(q_{1})}{ny\cos(q_{1})-nx\sin(q_{1})}$，从而解得 $q_{6}$：

```matlab
q6_1 = atan2(ox * sin(q1_1) - oy * cos(q1_1), ny * cos(q1_1) - nx * sin(q1_1))
q6_2 = atan2(ox * sin(q1_2) - oy * cos(q1_2), ny * cos(q1_2) - nx * sin(q1_2))
```

再根据：

$$
\begin{cases}
ay\cos(q_{1})-ax\sin(q_{1})=\sin(q_{5}) \\
ny\cos(q_{1})-nx\sin(q_{1})=\cos(q_{5})\cos(q_{6})
\end{cases}
$$

两式相除可以得到 $\tan(q_{5})=\frac{ay\cos(q_{1})-ax\sin(q_{1})}{ny\cos(q_{1})-nx\sin(q_{1})\cos(q_{6})}$，从而解得 $q_{5}$：

```matlab
q5_1 = atan2(cos(q6_1) * (ay * cos(q1_1) - ax * sin(q1_1)), ny * cos(q1_1) ...
    - nx * sin(q1_1))
q5_2 = atan2(cos(q6_2) * (ay * cos(q1_2) - ax * sin(q1_2)), ny * cos(q1_2) ...
    - nx * sin(q1_2))
```

然后变换 $T_{01}^{-1}T_{06}T_{56}^{-1}T_{45}^{-1}=T_{12}T_{23}T_{34}$：

![](../../../assets/Pasted%20image%2020251102213116.png)

![](../../../assets/Pasted%20image%2020251102213141.png)

![](../../../assets/Pasted%20image%2020251102213152.png)

![](../../../assets/Pasted%20image%2020251102213158.png)

根据 $ans[1][4]^2+ans[3][4]^2$ 两式恒等，可解到 $q_{3}$：

```matlab
m1_1 = dx * cos(q1_1) - (171/2000) * ax * cos(q1_1) - (171/2000) * ay * sin(q1_1) ...
    + dy * sin(q1_1) - (77/1000) * ox * cos(q1_1) * cos(q6_1) ...
    - (77/1000) * nx * cos(q1_1) * sin(q6_1) - (77/1000) * oy * cos(q6_1) * sin(q1_1) ...
    - (77/1000) * ny * sin(q1_1) * sin(q6_1);
n1_1 = dz - (171/2000) * az - (77/1000) * oz * cos(q6_1) - (77/1000) * nz * sin(q6_1) ...
    - 23/100;

m1_2 = dx * cos(q1_2) - (171/2000) * ax * cos(q1_2) - (171/2000) * ay * sin(q1_2) ...
    + dy * sin(q1_2) - (77/1000) * ox * cos(q1_2) * cos(q6_2) ...
    - (77/1000) * nx * cos(q1_2) * sin(q6_2) - (77/1000) * oy * cos(q6_2) * sin(q1_2) ...
    - (77/1000) * ny * sin(q1_2) * sin(q6_2);
n1_2 = dz - (171/2000) * az - (77/1000) * oz * cos(q6_2) - (77/1000) * nz * sin(q6_2) ...
    - 23/100;

q3_1 = acos((40000 * m1_1^2 + 40000 * n1_1^2 - 4 * 17^2 - 37^2) / (4 * 17 * 37))
q3_2 = - acos((40000 * m1_1^2 + 40000 * n1_1^2 - 4 * 17^2 - 37^2) / (4 * 17 * 37))
q3_3 = acos((40000 * m1_2^2 + 40000 * n1_2^2 - 4 * 17^2 - 37^2) / (4 * 17 * 37))
q3_4 = - acos((40000 * m1_2^2 + 40000 * n1_2^2 - 4 * 17^2 - 37^2) / (4 * 17 * 37))
```

再将 $ans[1][4]$ 和 $ans[3][4]$ 分别展开联立，解得 $q_{2}$：

```matlab
m2_1 = 34 * m1_1 * cos(q3_1) + 37 * m1_1 - 34 * n1_1 * sin(q3_1)
n2_1 = 34 * n1_1 * cos(q3_1) + 37 * n1_1 + 34 * m1_1 * sin(q3_1)

m2_2 = 34 * m1_1 * cos(q3_2) + 37 * m1_1 - 34 * n1_1 * sin(q3_2)
n2_2 = 34 * n1_1 * cos(q3_2) + 37 * n1_1 + 34 * m1_1 * sin(q3_2)

m2_3 = 34 * m1_2 * cos(q3_3) + 37 * m1_2 - 34 * n1_2 * sin(q3_3)
n2_3 = 34 * n1_2 * cos(q3_3) + 37 * n1_2 + 34 * m1_2 * sin(q3_3)

m2_4 = 34 * m1_2 * cos(q3_4) + 37 * m1_2 - 34 * n1_2 * sin(q3_4)
n2_4 = 34 * n1_2 * cos(q3_4) + 37 * n1_2 + 34 * m1_2 * sin(q3_4)

q2_1 = atan2(m2_1, n2_1)
q2_2 = atan2(m2_2, n2_2)
q2_3 = atan2(m2_3, n2_3)
q2_4 = atan2(m2_4, n2_4)
```

最后根据 $ans[3][1]/ans[3][2]$ 可以解得 $q_{4}$：

```matlab
m3_1 = az * cos(q5_1) - nz * cos(q6_1) * sin(q5_1) + oz * sin(q5_1) * sin(q6_1)
n3_1 = - oz * cos(q6_1) - nz * sin(q6_1)

m3_2 = az * cos(q5_2) - nz * cos(q6_2) * sin(q5_2) + oz * sin(q5_2) * sin(q6_2)
n3_2 = - oz * cos(q6_2) - nz * sin(q6_2)

q4_1 = atan2(-m3_1, -n3_1) - q2_1 - q3_1
q4_2 = atan2(-m3_1, -n3_1) - q2_2 - q3_2
q4_3 = atan2(-m3_2, -n3_2) - q2_3 - q3_3
q4_4 = atan2(-m3_2, -n3_2) - q2_4 - q3_4
```
***
## 仿真验证

### 第一组

代入解得：

![](../../../assets/Pasted%20image%2020251102214804.png)

仿真验证：

![](../../../assets/Pasted%20image%2020251102214842.png)

![](../../../assets/Pasted%20image%2020251102214905.png)

符合计算结果
***
### 第二组

代入解得：

![](../../../assets/Pasted%20image%2020251102215117.png)

仿真验证：

![](../../../assets/Pasted%20image%2020251102215323.png)

![](../../../assets/Pasted%20image%2020251102215341.png)

符合计算结果
***
### 第三组

代入解得：

![](../../../assets/Pasted%20image%2020251102215433.png)

仿真验证：

![](../../../assets/Pasted%20image%2020251102215542.png)

![](../../../assets/Pasted%20image%2020251102215554.png)

符合计算结果
***
### 第四组

代入解得：

![](../../../assets/Pasted%20image%2020251102215617.png)

仿真验证：

![](../../../assets/Pasted%20image%2020251102215820.png)

![](../../../assets/Pasted%20image%2020251102215840.png)

符合计算结果
***
### 第五组

代入解得：

![](../../../assets/Pasted%20image%2020251102215941.png)

仿真验证：

![](../../../assets/Pasted%20image%2020251102220058.png)

![](../../../assets/Pasted%20image%2020251102220129.png)

符合计算结果

