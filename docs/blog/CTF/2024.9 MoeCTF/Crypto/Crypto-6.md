---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
---  
# Crypto-6｜大白兔

## 复盘感想

好硬核一道 Crypto，看的时候就感觉这一道大数论题所以死活也做不出来（数学太菜了 www）
***
## Writeup

根据题给代码：

```python
from Crypto.Util.number import *

flag = b'moectf{xxxxxxxxxx}'
m = bytes_to_long(flag)

e1 = 12886657667389660800780796462970504910193928992888518978200029826975978624718627799215564700096007849924866627154987365059524315097631111242449314835868137
e2 = 12110586673991788415780355139635579057920926864887110308343229256046868242179445444897790171351302575188607117081580121488253540215781625598048021161675697

def encrypt(m , e1 , e2):
    p = getPrime(512)
    q = getPrime(512)
    N = p*q
    c1 = pow((3*p + 7*q),e1,N)
    c2 = pow((2*p + 5*q),e2,N)
    e = 65537
    c = pow(m , e , N)
    return c
    

print(encrypt(m ,e1 , e2))

'''
N = 107840121617107284699019090755767399009554361670188656102287857367092313896799727185137951450003247965287300048132826912467422962758914809476564079425779097585271563973653308788065070590668934509937791637166407147571226702362485442679293305752947015356987589781998813882776841558543311396327103000285832158267
c1 = 15278844009298149463236710060119404122281203585460351155794211733716186259289419248721909282013233358914974167205731639272302971369075321450669419689268407608888816060862821686659088366316321953682936422067632021137937376646898475874811704685412676289281874194427175778134400538795937306359483779509843470045
c2 = 21094604591001258468822028459854756976693597859353651781642590543104398882448014423389799438692388258400734914492082531343013931478752601777032815369293749155925484130072691903725072096643826915317436719353858305966176758359761523170683475946913692317028587403027415142211886317152812178943344234591487108474
c = 21770231043448943684137443679409353766384859347908158264676803189707943062309013723698099073818477179441395009450511276043831958306355425252049047563947202180509717848175083113955255931885159933086221453965914552773593606054520151827862155643433544585058451821992566091775233163599161774796561236063625305050
```

从 RSA 的角度来说，我们只需要 $p,q$ 即可求出答案，但这道题 $N$ 非常大根本分解不开，很多常见的 RSA 攻击手段（小指数、同模 etc）都用不上……

注意到题目还多给了两个信息：$c_1,c_2$，并且给出了他们的得到方法：

$$
\begin{aligned}
c_1=(3p+7q)^{e_1}\text{ mod } N\\
c_2=(2p+5q)^{e_2}\text{ mod } N
\end{aligned}
$$

明显是一个跟同余有关的数学题，对于形如 $c=(ap+bq)^e\text{ mod }N$ 的方程，我们考虑二项式定理，将其展开，得到：

$$
c=\sum\limits_{i=0}^eC_e^i(ap)^{e-i}(bq)^i\text{ mod } N
$$

我们还有条件：$N=pq$，化简得到 $c=(ap)^e+(bq)^e\text{ mod }N$（因为当 $i=1,2,...,e-1$ 时乘积项均为 $pq$ 的倍数，即为 $N$ 的倍数）

我们因此可以现将两个式子调整为齐次：

$$
\begin{aligned}
c_1^{e_2}=(3p+7q)^{e_1e_2}\text{ mod } N\\
c_2^{e_1}=(2p+5q)^{e_1e_2}\text{ mod } N
\end{aligned}
$$

并化简如下：

$$
\begin{aligned}
c_1^{e_2}=(3p)^{e_1e_2}+(7q)^{e_1e_2}\text{ mod }N\\
c_2^{e_1}=(2p)^{e_1e_2}+(5q)^{e_1e_2}\text{ mod }N
\end{aligned}
$$

两式消去 $p^{e_1e_2}$，我们有：$2^{e_1e_2}c_1^{e_2}-3^{e_1e_2}c_2^{e_1}=(14q)^{e_1e_2}-(15q)^{e_1e_2}\text{ mod }N=(14^{e_1e_2}-15^{e_1e_2})q^{e_1e_2}\text{ mod }N$

通过逆元，一般化来说，我们就可以已知 $q^x\text{ mod }N$ 的值，假设 $q_0=q^x\text{ mod }N=q^x-kN$，对方程两边分别模 $p,q$，我们可以得到：

$$
\begin{aligned}
q_0\equiv 0(\text{mod }q)\\
q_0\not\equiv 0(\text{mod }p)
\end{aligned}
$$

因此可以得知 $q_0$ 是 $q$ 的倍数，那么求 $\gcd(q_0,N)$ 即可得到 $q$ 的值，$p$ 也就迎刃而解了！

Payload 如下：

```python
from Crypto.Util.number import *

N = 107840121617107284699019090755767399009554361670188656102287857367092313896799727185137951450003247965287300048132826912467422962758914809476564079425779097585271563973653308788065070590668934509937791637166407147571226702362485442679293305752947015356987589781998813882776841558543311396327103000285832158267
c1 = 15278844009298149463236710060119404122281203585460351155794211733716186259289419248721909282013233358914974167205731639272302971369075321450669419689268407608888816060862821686659088366316321953682936422067632021137937376646898475874811704685412676289281874194427175778134400538795937306359483779509843470045
c2 = 21094604591001258468822028459854756976693597859353651781642590543104398882448014423389799438692388258400734914492082531343013931478752601777032815369293749155925484130072691903725072096643826915317436719353858305966176758359761523170683475946913692317028587403027415142211886317152812178943344234591487108474
c = 21770231043448943684137443679409353766384859347908158264676803189707943062309013723698099073818477179441395009450511276043831958306355425252049047563947202180509717848175083113955255931885159933086221453965914552773593606054520151827862155643433544585058451821992566091775233163599161774796561236063625305050
e1 = 12886657667389660800780796462970504910193928992888518978200029826975978624718627799215564700096007849924866627154987365059524315097631111242449314835868137
e2 = 12110586673991788415780355139635579057920926864887110308343229256046868242179445444897790171351302575188607117081580121488253540215781625598048021161675697
e = 65537

b = pow(2, e1*e2, N) * pow(c1, e2, N) - pow(3, e1*e2, N) * pow(c2, e1, N)
a = pow(14, e1*e2, N) - pow(15, e1*e2, N)
x = pow(a, -1, N) * b % N

q = GCD(x, N)
p = N // q

phi = (p - 1) * (q - 1)
d = pow(e, -1, phi)
m = pow(c, d, N)
print(long_to_bytes(m))
```

运行即可得到 flag : `moectf{Sh4!!0w_deeb4t0_P01arnova}`