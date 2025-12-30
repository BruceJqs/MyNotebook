# Crypto-6｜ez_det

## Tag

线性代数，行列式
***
## Writeup

我们有如下等式：

$$
\begin{cases}
\text{Noise1}\cdot \text{Mask}=C \\
\text{det}(\text{Mask})=1 \\
\text{Noise1}=\begin{pmatrix}
x_{11} &  x_{12} & x_{13} & x_{14} & x_{15}\\
x_{21} &  x_{22} & x_{23} & x_{24} & x_{25}\\
x_{31} &  x_{32} & x_{33} & x_{34} & x_{35}\\
x_{41} &  x_{42} & x_{43} & x_{44} & x_{45}\\
\text{flag} & 0 & 0 & 0 & 0
\end{pmatrix}
\end{cases}
$$

令 $X=\text{Noise1}[1..4][2..5]$ 根据行列式定义我们可以得到 $\text{det}(\text{Noise1})=\text{flag}\times\text{det}(X)$，因此可以算出 flag 的值，Payload 如下：

```python
from Crypto.Util.number import *
from sage.all import *

Noise1 = [...]
C = [...]
X = [[Noise1[i][j] for j in range(1, 5)] for i in range(4)]
C = matrix(ZZ, C)
X = matrix(ZZ, X)

flag = det(C) // det(X)
print(long_to_bytes(flag))
```

得到最终 flag：`moectf{D0_Y0u_kn0w_wh@7_4_de7erm1n@n7_1s!}`