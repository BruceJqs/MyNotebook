# Lab06-几何雅可比矩阵

因为 PPT 所叙述的是标准 DH 参数，而我们所使用的是非标准 DH 参数，因此公式需要修正一下：

$$
J = \begin{bmatrix}
z_{1} \times (P_{n}-P_{1}) & z_{2} \times (P_{n}-P_{2}) & \cdots &  z_{n} \times (P_{n}-P_{n}) \\
z_{1} & z_{2} & \cdots & z_{n}
\end{bmatrix}
$$

其中 $z_{i}=R_{i-1}^{i}\begin{bmatrix}0 \\ 0 \\ 1\end{bmatrix},\begin{bmatrix}P_{i} \\ 1\end{bmatrix}=T_{i-1}^{i}\begin{bmatrix}0 \\ 0 \\ 0 \\ 1\end{bmatrix}$，编写 matlab 代码如下：

```matlab
syms q1 q2 q3 q4 q5 q6
c1=cos(q1); s1=sin(q1);
c2=cos(q2); s2=sin(q2);
c3=cos(q3); s3=sin(q3);
c4=cos(q4); s4=sin(q4);
c5=cos(q5); s5=sin(q5);
c6=cos(q6); s6=sin(q6);
% 关节参数
d1 = 0.23;
d2 = -0.054;
d3 = 0.185;
d4 = 0.17;
d34 = 0.077;
d45 = -0.077;
d56 = -0.0855;
% 各变换矩阵
T01 = [ c1, -s1,  0,    0;
        s1,  c1,  0,    0;
         0,   0,  1, d1;
         0,   0,  0,   1]
T12 = [ s2,  c2,  0,    0;
        0,   0,  1,  d2;
        c2, -s2,  0,    0;
        0,   0,  0,   1]
T23 = [ c3, -s3,  0, d3;
        s3,  c3,  0,  0;
         0,   0,  1,  0;
         0,   0,  0,  1]
T34 = [ -s4, -c4,  0, d4;
         c4, -s4,  0, 0;
          0,   0,  1, d34;
          0,   0,  0,   1]
T45 = [ -s5, -c5,  0, 0;
          0,   0, -1, d45;
         c5, -s5,  0, 0;
          0,   0,  0, 1]
T56 = [ c6, -s6,  0, 0;
         0,   0, -1, d56;
         s6,  c6,  0, 0;
         0,   0,  0, 1]
T02 = T01 * T12
T03 = T02 * T23
T04 = T03 * T34
T05 = T04 * T45
T06 = T05 * T56
Z0 = [0; 0; 1]
Z1 = T01(1:3, 3)
Z2 = T02(1:3, 3)
Z3 = T03(1:3, 3)
Z4 = T04(1:3, 3)
Z5 = T05(1:3, 3)
Z6 = T06(1:3, 3)
P0 = [0; 0; 0]
P1 = T01(1:3, 4)
P2 = T02(1:3, 4)
P3 = T03(1:3, 4)
P4 = T04(1:3, 4)
P5 = T05(1:3, 4)
P6 = T06(1:3, 4)
J = [cross(Z1, (P6 - P1)), cross(Z2, (P6 - P2)), cross(Z3, (P6 - P3)), cross(Z4, (P6 - P4)), cross(Z5, (P6 - P5)), cross(Z6, (P6 - P6));
    Z1, Z2, Z3, Z4, Z5, Z6]
```

最后算得雅可比矩阵如下：

![](../../../assets/PixPin_2025-11-09_20-44-24.png)

![](../../../assets/PixPin_2025-11-09_20-44-41.png)

$$
\begin{array}{l}
\mathrm{}\\
\textrm{where}\\
\mathrm{}\\
\;\;\sigma_1 =\frac{171\,\sin \left(q_1 \right)\,\sin \left(q_5 \right)}{2000}\\
\mathrm{}\\
\;\;\sigma_2 =\frac{171\,\cos \left(q_1 \right)\,\sin \left(q_5 \right)}{2000}\\
\mathrm{}\\
\;\;\sigma_3 =\frac{17\,\cos \left(q_3 \right)\,\sin \left(q_1 \right)\,\sin \left(q_2 \right)}{100}\\
\mathrm{}\\
\;\;\sigma_4 =\frac{17\,\cos \left(q_2 \right)\,\sin \left(q_1 \right)\,\sin \left(q_3 \right)}{100}\\
\mathrm{}\\
\;\;\sigma_5 =\frac{17\,\cos \left(q_1 \right)\,\cos \left(q_3 \right)\,\sin \left(q_2 \right)}{100}\\
\mathrm{}\\
\;\;\sigma_6 =\frac{17\,\cos \left(q_1 \right)\,\cos \left(q_2 \right)\,\sin \left(q_3 \right)}{100}\\
\mathrm{}\\
\;\;\sigma_7 =\frac{37\,\sin \left(q_1 \right)\,\sin \left(q_2 \right)}{200}\\
\mathrm{}\\
\;\;\sigma_8 =\frac{37\,\cos \left(q_1 \right)\,\sin \left(q_2 \right)}{200}\\
\mathrm{}\\
\;\;\sigma_9 =\frac{77\,\sin \left(q_1 \right)}{1000}\\
\mathrm{}\\
\;\;\sigma_{10} =\frac{77\,\cos \left(q_1 \right)}{1000}\\
\mathrm{}\\
\;\;\sigma_{11} =\frac{171\,\cos \left(q_5 \right)\,\sigma_{22} }{2000}\\
\mathrm{}\\
\;\;\sigma_{12} =\frac{171\,\cos \left(q_5 \right)\,\sigma_{23} }{2000}\\
\mathrm{}\\
\;\;\sigma_{13} =\frac{37\,\cos \left(q_2 \right)}{200}+\sigma_{28} -\sigma_{27} -\sigma_{24} +\sigma_{26} -\sigma_{25} \\
\mathrm{}\\
\;\;\sigma_{14} =\sigma_{27} -\sigma_{28} +\sigma_{24} -\sigma_{26} +\sigma_{25} \\
\mathrm{}\\
\;\;\sigma_{15} =\cos \left(q_4 \right)\,\sigma_{30} -\sin \left(q_4 \right)\,\sigma_{29} \\
\mathrm{}\\
\;\;\sigma_{16} =\cos \left(q_4 \right)\,\sigma_{32} +\sin \left(q_4 \right)\,\sigma_{31} \\
\mathrm{}\\
\;\;\sigma_{17} =\cos \left(q_4 \right)\,\sigma_{34} -\sin \left(q_4 \right)\,\sigma_{35} \\
\mathrm{}\\
\;\;\sigma_{18} =\frac{77\,\sin \left(q_4 \right)\,\sigma_{29} }{1000}\\
\mathrm{}\\
\;\;\sigma_{19} =\frac{77\,\cos \left(q_4 \right)\,\sigma_{30} }{1000}\\
\mathrm{}\\
\;\;\sigma_{20} =\frac{77\,\sin \left(q_4 \right)\,\sigma_{31} }{1000}\\
\mathrm{}\\
\;\;\sigma_{21} =\frac{77\,\cos \left(q_4 \right)\,\sigma_{32} }{1000}\\
\mathrm{}\\
\;\;\sigma_{22} =\cos \left(q_4 \right)\,\sigma_{29} +\sin \left(q_4 \right)\,\sigma_{30} \\
\mathrm{}\\
\;\;\sigma_{23} =\cos \left(q_4 \right)\,\sigma_{31} -\sin \left(q_4 \right)\,\sigma_{32} \\
\mathrm{}\\
\;\;\sigma_{24} =\frac{171\,\cos \left(q_5 \right)\,\sigma_{33} }{2000}\\
\mathrm{}\\
\;\;\sigma_{25} =\frac{77\,\sin \left(q_4 \right)\,\sigma_{35} }{1000}\\
\mathrm{}\\
\;\;\sigma_{26} =\frac{77\,\cos \left(q_4 \right)\,\sigma_{34} }{1000}\\
\mathrm{}\\
\;\;\sigma_{27} =\frac{17\,\sin \left(q_2 \right)\,\sin \left(q_3 \right)}{100}\\
\mathrm{}\\
\;\;\sigma_{28} =\frac{17\,\cos \left(q_2 \right)\,\cos \left(q_3 \right)}{100}\\
\mathrm{}\\
\;\;\sigma_{29} =\sin \left(q_1 \right)\,\sin \left(q_2 \right)\,\sin \left(q_3 \right)-\cos \left(q_2 \right)\,\cos \left(q_3 \right)\,\sin \left(q_1 \right)\\
\mathrm{}\\
\;\;\sigma_{30} =\cos \left(q_2 \right)\,\sin \left(q_1 \right)\,\sin \left(q_3 \right)+\cos \left(q_3 \right)\,\sin \left(q_1 \right)\,\sin \left(q_2 \right)\\
\mathrm{}\\
\;\;\sigma_{31} =\cos \left(q_1 \right)\,\cos \left(q_2 \right)\,\cos \left(q_3 \right)-\cos \left(q_1 \right)\,\sin \left(q_2 \right)\,\sin \left(q_3 \right)\\
\mathrm{}\\
\;\;\sigma_{32} =\cos \left(q_1 \right)\,\cos \left(q_2 \right)\,\sin \left(q_3 \right)+\cos \left(q_1 \right)\,\cos \left(q_3 \right)\,\sin \left(q_2 \right)\\
\mathrm{}\\
\;\;\sigma_{33} =\cos \left(q_4 \right)\,\sigma_{35} +\sin \left(q_4 \right)\,\sigma_{34} \\
\mathrm{}\\
\;\;\sigma_{34} =\cos \left(q_2 \right)\,\cos \left(q_3 \right)-\sin \left(q_2 \right)\,\sin \left(q_3 \right)\\
\mathrm{}\\
\;\;\sigma_{35} =\cos \left(q_2 \right)\,\sin \left(q_3 \right)+\cos \left(q_3 \right)\,\sin \left(q_2 \right)
\end{array}
$$
