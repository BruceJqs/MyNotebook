---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
# comments: true
--- 
## Homework 01
### 学在浙大

#### Question 1

![](../../../assets/Pasted%20image%2020240920194252.png)

（1）由题意可得 $\sum\limits_{i=1}^kL_1(\mu,\sigma_i)=\sum\limits_{i=1}^k\sum\limits_{j=1}^n|\mu_j-\sigma_j^i|=\sum\limits_{j=1}^n\sum\limits_{i=1}^k|\mu_j-\sigma_j^i|$
考虑其中的一项 $\sum\limits_{i=1}^k|\mu_j-\sigma_j^i|$，这时 $\mu_j$ 为变量，而 $\sigma_j^i$ 为既定常量
将 $\sigma_j^1,\sigma_j^2,...,\sigma_j^k$ $k$ 个元素进行排序，假设排序后为 $\sigma_j^{1'},\sigma_j^{2'} ,...,\sigma_j^{k'}$，考虑以下两种情况：

- $k$ 为偶数，那么取 $\mu_j=\frac{\sigma_j^{\frac{k}{2}'}+\sigma_j^{\frac{k}{2}+1'}}{2}$，$\sum\limits_{i=1}^k|\mu_j-\sigma_j^i|$ 可取到最小值
- $k$ 为奇数，那么取 $\mu_j=\sigma_j^{\frac{k}{2}'}$，$\sum\limits_{i=1}^k|\mu_j-\sigma_j^i|$ 可取到最小值

按照以上取法可以得到 $\mu$，即 $\mu_j$​ 应该是第 $j$ 个物品在所有专家中的排名的中位数。将 $\mu$ 中元素排序过后每个元素对应的排名（相同排名顺序可任意确定）即为综合排序 $\sigma'$，但是 $\sigma^*$ 无法从 $\mu$ 得到，因为 $\mu$ 中的元素可能存在相同的情况

（2）这个题目等价于证明对数据 $a_1,a_2,...,a_k$，中位数为 $\mu$，平均值为 $\beta$，$2\sum\limits_{i=1}^k|a_i-\mu|\geq\sum\limits_{i=1}^k|a_i-\beta|$
将 $a_1,a_2,...,a_k$ 平均分为两部分，设 $x_1\leq x_2\leq ...\leq x_n\leq \mu \leq y_1\leq y_2\leq ... \leq y_n$，当 $k$ 为偶数时 $\mu = \frac{x_n+y_1}{2}$，$k$ 为奇数时 $\mu$ 即为中间那个数，我们分两种情况来看：

- $\beta\leq\mu$，不妨设 $x_m\leq\beta\leq x_{m+1}$，令 $\mu=x_{n+1}$，此时：

$$
\begin{aligned}
RHS&=\sum\limits_{i=1}^m|x_i-\beta|+\sum\limits_{i=m+1}^{n+1}|x_i-\beta|+\sum\limits_{i=1}^n|y_i-\beta|=\sum\limits_{i=1}^m(\beta-x_i)+\sum\limits_{i=m+1}^{n+1}(x_i-\beta)+\sum\limits_{i=1}^n(y_i-\beta)\\
&=\sum\limits_{i=1}^k a_i-2\sum\limits_{i=1}^m x_i+m\beta-(k-m)\beta=2m\beta-2\sum\limits_{i=1}^m x_i=2\sum\limits_{i=1}^m(\beta-x_i)\\
&\leq 2\sum\limits_{i=1}^m(\mu-x_i)\leq 2\sum\limits_{i=1}^k|a_i-\mu|
\end{aligned}
$$

- $\beta\geq\mu$，同理，设 $y_m\leq\beta\leq y_{m+1}$，令 $\mu = y_0$

（3）

***
#### Question 2

![](../../../assets/Pasted%20image%2020240920214129.png)

（1）$s_1=5-10+57-45=7,s_2=10-5+10-7=8$

$s_3=7-10+3-10=-10,s_4=45-57+10-3=-5$

$\therefore \pmb{S}=\{7,8,-10,-5\}^T$

（2）$s_1^{(2)}=0(AAA)-5(AAB)+12(AAD)-5(ABB)+12(ADD)-5+3(ABC)+0(ADA)+12+7(ADC)+0(ABA)=31$

$s_2^{(2)}=0(BBB)+5(BAA)+5(BBA)+3(BBC)+3(BCC)+0(BAB)+0(BCB)+5+12(BAD)+3-7(BCD)=29$

$s_3^{(2)}=0(CCC)-3(CCB)-3(CBB)-7(CCD)-7(CDD)+0(CBC)+0(CDC)-3+5(CBA)-7-12(CDA)=-37$


$s_4^{(2)}=0(DDD)+7(DDC)+7(DCC)-12(DDA)-12(DAA)+0(DCD)+0(DAD)+7-3(DCB)-12-5(DAB)=-23$

$\therefore S^{(2)}=\{31,29,-37,-23\}^T$

（3）$S^{(2)}=M·S+l·S$

设 $M^2=(m^2_{ij})_{n\times n}$，其中 $m_{ij}^2$ 表示队 $i$ 与队 $j$ 之间进行了 $m_{ij}^2$ 场”二级比赛“

（4）$S^{(r)}=M^{(r-1)}·S+l·S^{(r-1)}$
***
### MOOC

![](../../../assets/Pasted%20image%2020241006225824.png)

![](../../../assets/Pasted%20image%2020241006230048.png)
