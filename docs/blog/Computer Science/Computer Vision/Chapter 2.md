# Chapter 2: Image Formation

## Camera and lens

 ### Image Formation

成像的第一步就是理解相机的原理，一种最简单的方法就是直接把一片薄膜（Film）放在物体面前，但是，由于我们没法做到物体上一点和薄膜上的点一一映射，因此这样的方法是不可行的。

![image-20251230231042511](../../../assets/image-20251230231042511.png)

***

### Pinhole Camera

由于直接把一片薄膜放在物体面前的方法不可行，我们在物体和薄膜之间加一块挡板，以阻挡大多数的光线，由此得到了一台简陋的**针孔相机**（Pinhole Camera），中间的开口被称为**光圈**（Aperture）。

![image-20251230231212441](../../../assets/image-20251230231212441.png)

***

### Shrinking the Aperture

由物理常识可得，**光圈越小，成像就越清晰**。但这并不代表着光圈越小越好，这是因为：

- 光圈越小，通过的光也就越少，成像就会变得很暗
- **衍射**（Diffraction）效应：当光圈尺寸和光的波长相当甚至更小时，通过光圈后会偏离直线传播路径并发生弯曲扩散，自然难以形成清晰的像

![image-20260102105822185](../../../assets/image-20260102105822185.png)

***

### Lens

**透镜**（Lens）（或镜头）有着和针孔相同的投影原理，但是它能让更多的光进来，并让这些光汇聚起来。

成像公式：$\frac{1}{i}+\frac{1}{o}=\frac{1}{f}$，其中 $i,o,f$ 分别为像距、物距和**焦距**（Focal Length）

![image-20260102110516015](../../../assets/image-20260102110516015.png)

- 当 $o\rightarrow\infty,f=i$

  ![image-20260102110559574](../../../assets/image-20260102110559574.png)

- 透镜可用于**图像放大**（Image Magnification），放大率为 $m=\frac{h_i}{h_0}=\frac{i}{o}$

  ![[image-20260102110723288]](../../../assets/image-20260102110723288.png)

- 相机通过改变焦距来实现图像放大，因为 $\frac{1}{i}+\frac{1}{o}=\frac{1}{f}\Rightarrow i=\frac{of}{o-f}\Rightarrow m=\frac{i}{o}=\frac{f}{o-f}$，因此 $f$ 越大，分子越大，分母越小，$m$ 显然会变大

  ![image-20260102111241461](../../../assets/image-20260102111241461.png)

	- 从另一个角度看，调整焦距的同时也改变了**视场**（Field of View, **FOV**)：焦距越长，视角更窄；焦距越短，视角越宽。当然，除焦距外，FOV 还取决于传感器的大小
	
		![image-20260102111447095](../../../assets/image-20260102111447095.png)

- 在相机中，**光圈**是指镜头的受光区域，一般用**镜头直径**区分。可通过增减光圈大小来控制图像亮度。一种更方便的表示光圈的方法是使用一个关于焦距的分数，即 $D=\frac{f}{N}$，其中 $N$ 为**焦比**（F-number）。比如对于 50mm 的焦距，当光圈完全打开时，焦比为 1.8（此时光圈直径为 27.8mm）。

	![image-20260102112229435](../../../assets/image-20260102112229435.png)

***

#### Lens Defocus

- 假设物体位于黄色虚线处时，物体的光线进入透镜后正好在底片处汇聚成一点，因此成像很清晰

	![image-20260102112614976](../../../assets/image-20260102112614976.png)

- 但如果稍微改变物体的位置，比如靠近些，那么对应的像就会远离镜头（同时也远离底片，符合高斯成像公式的约束），来自物体的光在底片处就会形成一片光斑（**模糊圈**（Blue Circle）或**弥散圈**（Circle of Confusion）），如图中加粗的橙色实线部分所示

	![image-20260102112720675](../../../assets/image-20260102112720675.png)
	
	- 利用相似三角形能解出 $b$：$\dfrac{b}{D} = \dfrac{|i' - i|}{i'} \Rightarrow b = \dfrac{D}{i'}|i' - i|, b \propto D \propto \dfrac{1}{N}$

当物体位置不动时，要想对好焦，可以从以下几方面考虑：

- 只移动底片（右上）
- 只移动镜头位置（左下）
- 两者也可同时移动（右下）

![image-20260102112959110](../../../assets/image-20260102112959110.png)

**景深**（Depth of Field, **DoF**）：一种物体距离范围，在范围内（即模糊度 b 小于像素尺寸的范围）的图像能够对好焦。其原理图如下：

![image-20260102113100382](../../../assets/image-20260102113100382.png)

- $c = \dfrac{f^2(o - o_1)}{No_1(o - f)} = \dfrac{f^2(o_2 - o)}{No_2(o - f)}$
- DoF = $o_2 - o_1 = \dfrac{2of^2cN(o - f)}{f^4 - c^2N^2(o - f)^2}$
- **减小光圈直径（增大焦比）会增加 DoF**

??? question "How to blur the background?"

	- 更大的光圈
	- 更长的焦距
	- 前景要近
	- 背景要远

***

## Geometric Image Formation

相机模型描述了三维世界和二维图像之间的几何关系。

![image-20260102113448881](../../../assets/image-20260102113448881.png)

两类投影模型：

- **正射投影**（Orthographic Projection）
- **透视投影**（Perspective Projection）

***

### Perspective Projection

**透视投影**（Perspective Projection）：三维世界坐标 $\rightarrow$ 二维图像坐标

![image-20260102113714370](../../../assets/image-20260102113714370.png)
$$
p = \begin{bmatrix}u \\ v\end{bmatrix} = \begin{bmatrix}\dfrac{fx}{z} \\ \dfrac{fy}{z}\end{bmatrix}
$$
!!! note "Homogeneous Coordinates"

	- 非齐次坐标 $\mathbf{x}$ $\rightarrow$ 齐次坐标 $\tilde{\mathbf{x}}$
	
		$$
		\begin{aligned}
		\tilde{\mathbf{x}} = \begin{pmatrix}\tilde{x} \\ \tilde{y} \\ \tilde{w}\end{pmatrix} = \begin{pmatrix}x \\ y \\ 1\end{pmatrix} = \begin{pmatrix}\mathbf{x} \\ 1\end{pmatrix} = \bar{\mathbf{x}} \\
		\tilde{\mathbf{x}} = \begin{pmatrix}\tilde{x} \\ \tilde{y} \\ \tilde{z} \\ \tilde{w}\end{pmatrix} = \begin{pmatrix}x \\ y \\ z \\ 1\end{pmatrix} = \begin{pmatrix}\mathbf{x} \\ 1\end{pmatrix} = \bar{\mathbf{x}}
		\end{aligned}
		$$
	
		- 其中 $\bar{\mathbf{x}}$ 为**增广向量**（Augmented Vector）
	
	- 齐次坐标 $\rightarrow$ 非齐次坐标
	
		$$
		\begin{aligned}
		\bar{\mathbf{x}} = \begin{pmatrix}\mathbf{x} \\ 1\end{pmatrix} = \begin{pmatrix}x \\ y \\ 1\end{pmatrix} = \dfrac{1}{\tilde{w}} \tilde{\mathbf{x}} = \dfrac{1}{\tilde{w}} \begin{pmatrix}\tilde{x} \\ \tilde{y} \\ \tilde{w}\end{pmatrix} = \begin{pmatrix}\tilde{x} / \tilde{w}\\ \tilde{y} / \tilde{w}\\ 1\end{pmatrix} \\
		\bar{\mathbf{x}} = \begin{pmatrix}\mathbf{x} \\ 1\end{pmatrix} = \begin{pmatrix}x \\ y \\ z \\1\end{pmatrix} = \dfrac{1}{\tilde{w}} \tilde{\mathbf{x}} = \dfrac{1}{\tilde{w}} \begin{pmatrix}\tilde{x} \\ \tilde{y} \\ \tilde{z} \\ \tilde{w}\end{pmatrix} = \begin{pmatrix}\tilde{x} / \tilde{w}\\ \tilde{y} / \tilde{w}\\ \tilde{z} / \tilde{w} \\ 1\end{pmatrix}
		\end{aligned}
		$$

在齐次坐标表示中，透视投影就是一个简单的线性变换（矩阵乘法）：

$$
\begin{bmatrix}f & 0 & 0 & 0 \\ 0 & f & 0 & 0 \\ 0 & 0 & 1 & 0\end{bmatrix} \begin{bmatrix}x \\ y \\ z \\ 1\end{bmatrix} = \begin{bmatrix}fx \\ fy \\ z\end{bmatrix} \cong \begin{bmatrix}\frac{fx}{z} \\ \frac{fy}{z} \\ 1\end{bmatrix}
$$
物体上两点在像平面上的透视投影：

![image-20260102115040857](../../../assets/image-20260102115040857.png)

!!! example "Example"

	=== "投影"
	
		![image-20260102115251121](../../../assets/image-20260102115251121.png)
	
	=== "从另一个角度看"
	
		![image-20260102115334572](../../../assets/image-20260102115334572.png)

一个投影可能对应无数种不同的物体形状：

![image-20260102115405437](../../../assets/image-20260102115405437.png)

透视投影的性质：

- 保留了直线“**直**”的性质

![image-20260102115501104](../../../assets/image-20260102115501104.png)

- 但是**长度**和**角度**关系却被丢失了

  - 长度

		![image-20260102115513497](../../../assets/image-20260102115513497.png)

  - 角度
  
		![image-20260102115532367](../../../assets/image-20260102115532367.png)

由于角度变化，两条在物理世界平行的线会在图像中汇聚于一点（即**消失点**，Vanishing Point）

![image-20260102115634848](../../../assets/image-20260102115634848.png)

![image-20260102115642204](../../../assets/image-20260102115642204.png)

性质：

- 任意两条平行线之间都有一个共同的消失点 v
- 来自相机上一点 C 的通过 v 的射线与直线平行
  - 因此 v 能够反映**直线的方向**
  - v 可能在图像外，甚至无穷远处

由于平面上任意两条平行线定义了一个消失点，这些消失点的并集就构成了一条**消失线**（Vanishing Line）

![image-20260102115815487](../../../assets/image-20260102115815487.png)

不同的平面会产生不同的消失线，因此消失线包含了**平面朝向**的信息：

![image-20260102120221897](../../../assets/image-20260102120221897.png)

!!! example "Example"

	=== "地平线"
	
		![image-20260102120416806](../../../assets/image-20260102120416806.png)
	
	=== "透视效应"
	
		![image-20260102120440622](../../../assets/image-20260102120440622.png)

***

### Perspective distortion

