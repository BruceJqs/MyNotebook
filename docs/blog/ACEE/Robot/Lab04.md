# Lab04-ZJU-I 型机械臂正运动学仿真

## DH 参数

DH 参数表如下：

| i   | $\theta$         | $d$    | $a_{i-1}$ | $\alpha_{i-1}$   |
| --- | ---------------- | ------ | --------- | ---------------- |
| 1   | 0                | 0.23   | 0         | 0                |
| 2   | $-\frac{\pi}{2}$ | -0.054 | 0         | $-\frac{\pi}{2}$ |
| 3   | 0                | 0      | 0.185     | 0                |
| 4   | $\frac{\pi}{2}$  | 0.077  | 0.17      | 0                |
| 5   | $\frac{\pi}{2}$  | 0.077  | 0         | $\frac{\pi}{2}$  |
| 6   | 0                | 0.0255 | 0         | $\frac{\pi}{2}$  |

***
## 正运动学推导

根据 DH 参数，我们利用 Matlab 代码：

```matlab
syms q1 q2 q3 q4 q5 q6
q_syms = [q1, q2, q3, q4, q5, q6]
t01 = mdh_transform(0,     0,     0.23,   0,     q1)
t12 = mdh_transform(0,     -pi/2, -0.054, -pi/2, q2)
t23 = mdh_transform(0.185, 0,     0,      0,     q3)
t34 = mdh_transform(0.17,  0,     0.077,  pi/2,  q4)
t45 = mdh_transform(0,     pi/2,  0.077,  pi/2,  q5)
t56 = mdh_transform(0,     pi/2,  0.0255, 0,     q6)

function T = mdh_transform(a, alpha, d, q0, q)
    q0 = sym(q0);
    cq = cos(q0 + q);
    sq = sin(q0 + q);
    ca = cos(alpha);
    sa = sin(alpha);
    T = [ cq,     -sq,       0,     a;
          sq*ca,  cq*ca,    -sa,  -sa*d;
          sq*sa,  cq*sa,     ca,   ca*d;
          0,       0,        0,     1];
    T = simplify(T, 'Steps', 100);
    T = vpa(T, 8); 
end
```

得到六个关节的变换矩阵：

![](../../../assets/Pasted%20image%2020251019203827.png)

进行相关处理后，得到末端执行器相对于基座的齐次变换矩阵：

![](../../../assets/Pasted%20image%2020251019211208.png)

其中：

$$
\begin{aligned}
&\sigma_1 = \cos(q_4)\sigma_8 + \sin(q_4)\sigma_7 \\
&\sigma_2 = \cos(q_4)\sigma_{14} - \sin(q_4)\sigma_{13} \\
&\sigma_3 = \cos(q_4)\sigma_{12} + \sin(q_4)\sigma_{11} \\
&\sigma_4 = \cos(q_4)\sigma_7 - \sin(q_4)\sigma_8 \\
&\sigma_5 = \cos(q_5)\sin(q_1) + \sin(q_5)\sigma_9 \\
&\sigma_6 = \cos(q_1)\cos(q_5) + \sin(q_5)\sigma_{10} \\
&\sigma_7 = \cos(q_2)\cos(q_3) - \sin(q_2)\sin(q_3) \\
&\sigma_8 = \cos(q_2)\sin(q_3) + \cos(q_3)\sin(q_2) \\
&\sigma_9 = \cos(q_4)\sigma_{11} - \sin(q_4)\sigma_{12} \\
&\sigma_{10} = \cos(q_4)\sigma_{13} + \sin(q_4)\sigma_{14} \\
&\sigma_{11} = \cos(q_1)\cos(q_2)\cos(q_3) - \cos(q_1)\sin(q_2)\sin(q_3) \\
&\sigma_{12} = \cos(q_1)\cos(q_2)\sin(q_3) + \cos(q_1)\cos(q_3)\sin(q_2) \\
&\sigma_{13} = \sin(q_1)\sin(q_2)\sin(q_3) - \cos(q_2)\cos(q_3)\sin(q_1) \\
&\sigma_{14} = \cos(q_2)\sin(q_1)\sin(q_3) + \cos(q_3)\sin(q_1)\sin(q_2)
\end{aligned}
$$
***
## 仿真验证

代入五组参数值：

```matlab
test1  = [pi/6,  0,     pi/6,  0,     pi/3,  0];
test2  = [pi/6,  pi/6,  pi/3,  0,     pi/3,  pi/6];
test3  = [pi/2,  0,     pi/2,  -pi/3, pi/3,  pi/6];
test4  = [-pi/6, -pi/6, -pi/3, 0,     pi/12, pi/2];
test5  = [pi/12, pi/12, pi/12, pi/12, pi/12, pi/12];
```
***
### 第一组

第一组参数值对应的末端执行器位置计算得到：

![](../../../assets/Pasted%20image%2020251019204708.png)

Coppeliasim 中进行仿真如下图所示：

![](../../../assets/Pasted%20image%2020251019204633.png)

![](../../../assets/Pasted%20image%2020251019204647.png)

结果是对应的
***
### 第二组

第二组参数值对应的末端执行器位置计算得到：

![](../../../assets/Pasted%20image%2020251019204751.png)

Coppeliasim 中进行仿真如下图所示：

![](../../../assets/Pasted%20image%2020251019204943.png)

![](../../../assets/Pasted%20image%2020251019204957.png)

结果是对应的
***
### 第三组

第三组参数值对应的末端执行器位置计算得到：

![](../../../assets/Pasted%20image%2020251019204803.png)

Coppeliasim 中进行仿真如下图所示：

![](../../../assets/Pasted%20image%2020251019205132.png)

![](../../../assets/Pasted%20image%2020251019205150.png)

结果是对应的
***
### 第四组

第四组参数值对应的末端执行器位置计算得到：

![](../../../assets/Pasted%20image%2020251019204812.png)

Coppeliasim 中进行仿真如下图所示：

![](../../../assets/Pasted%20image%2020251019205332.png)

![](../../../assets/Pasted%20image%2020251019205348.png)

结果是对应的
***
### 第五组

第五组参数值对应的末端执行器位置计算得到：

![](../../../assets/Pasted%20image%2020251019204819.png)

Coppeliasim 中进行仿真如下图所示：

![](../../../assets/Pasted%20image%2020251019205447.png)

![](../../../assets/Pasted%20image%2020251019205512.png)

结果是对应的



