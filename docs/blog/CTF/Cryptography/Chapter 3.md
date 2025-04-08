---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
--- 

# Chapter 03 : Hash 函数

## MD5

MD5 函数是一种广泛使用的加密哈希函数，它对任意长度的报文产生一个128位（16字节）的哈希值，通常用 32 位十六进制数表示。MD5 函数常用于验证数据完整性，结合 RSA 等算法进行数字签名和数据加密

- MD5 是一种单向函数，将报文加密成摘要，中间不需要密钥，相当于有损压缩
- MD5 常用于用户名密码加密，在服务器数据库中仅保存 $m=\text{md5}(\text{password})$，在用户登录时，比较 $m$ 和 $m'=\text{md5}(\text{password'})$ 是否相等，若 $m'=m\Rightarrow\text{password}'=\text{password}$
	- 当 $\text{password}'\neq\text{password}$ 时，却有 $\text{md5}(\text{password}')=\text{md5}(\text{password})$，这种现象称为 MD5 碰撞（Collision），MD5 碰撞几乎不可能发生

!!! example "Example"

	假如 A 要发送一封邮件 L 给 B
	
	1. 用 B 的公钥对 L 进行加密：$L'=\text{RSA}(L,B\text{ 的公钥})$
	2. 用 MD5 对 L 进行哈希：$m=\text{md5}(L),s=\text{RSA}(m,A\text{ 的私钥})$
	3. 将 $L'$ 和 $s$ 一起发送给 B
	
	B 收到邮件后要对 $L'$ 进行解密，同时要检验这封信是否确实发自 A
	
	4. $L=\text{RSA}(L',B\text{ 的私钥})$
	5. $m=\text{md5}(L)$
	6. $m'=\text{RSA}(s,A\text{ 的公钥})$
	
	比较 $m$ 和 $m'$ 是否相等，若相等，则说明这封邮件确实是 A 发给 B 的
***
### 分块及填充

MD5 对文件进行分块计算，每块大小为 64 字节，设文件大小为 $n$ 字节，则最后那个块的长度为 $n\text{ mod } 64$

- 值得注意的是，当最后一块大小刚好为 64 字节时，该块只能算倒数第 2 块，即它的后面那块（大小为 0 字节）才算最后一块。故最后块的大小为 $[0,63]$ 字节, 该块需要按以下步骤补充数据凑成64 字节的一个块或者 128 字节的两个块：
	1. 假定该块大小 $n<56$ 字节，则在末尾补上 0x80 0x00 0x00 ... 0x00（共 55-n 个 0x00）
	2. 假定该块大小 $n$ 在 $[56,63]$ 范围内时，则应在末尾补上 $64-n+56$ 个字节
	3. 无论是什么情况，都要在后面补上 8 个字节（小端序保存，相当于一个 64 位整数），它的值为被加密信息总共的位数（不包含填充内容）

!!! example "Example"

	假设有一个文件的内容为 `'A'`，仅一个字节，那么填充为：
	
	A, 0x80, 0x00, ..., 0x00（共 54 个 0x00）, 0x08, 0x00, 0x00, ..., 0x00（共 8 字节，其类型为 64 位整数
***
### MD5 计算

MD5 计算分为以下几个步骤：

- 初始化：设定 4 个初始变量（32 位）$a_0=0x67452301,b_0=0xEFCDAB89,c_0=0x98BADCFE,d_0=0x10325476$，拼起来就是 128 位的摘要，以及设定已处理的报文的二进制位数为 0（方便填充）

```c
int Init_MD5(MD5_CTX *MD5_ctx)
{
   MD5_ctx->count[0] = 0;
   MD5_ctx->count[1] = 0;
   MD5_ctx->state[0] = 0x67452301; // a0
   MD5_ctx->state[1] = 0xEFCDAB89; // b0
   MD5_ctx->state[2] = 0x98BADCFE; // c0
   MD5_ctx->state[3] = 0x10325476; // d0
   return 0;
}
```

- 将输入数据分块处理并更新哈希状态：

```c
int Update_MD5(MD5_CTX *MD5_ctx, 
               unsigned char *buf, 
               ulong32 buf_len)
{
   ulong32 i, bytes_left, bytes_to_fill;
   bytes_left = (MD5_ctx->count[0] >> 3) & 0x3F; // 内部缓冲data中剩余未处理的字节数
                                                 // &0x3F 等价于 %64
   
   MD5_ctx->count[0] += buf_len<<3;
   if(MD5_ctx->count[0] < buf_len<<3 // 相加后结果变小，说明发生溢出，所以向高 32 位进位
      MD5_ctx->count[1]++;
   MD5_ctx->count[1] += buf_len>>29;
   bytes_to_fill = 64 - bytes_left; // data中需要补充的字节数
   if (buf_len >= bytes_to_fill) 
   {
      memcpy(&MD5_ctx->data[bytes_left], buf, bytes_to_fill); // 现在data中已充满64字节
      Process_One_Block_MD5 (MD5_ctx->state, MD5_ctx->data); // 对data中的64字节进行计算
      bytes_left = 0; // data中剩余未处理字节数变0
      for (i=bytes_to_fill; i+63 < buf_len; i+=64) // 从buf复制64字节到data
      {  // i=bytes_to_fill是为了跳过buf中已经补充给data的bytes_to_fill个字节的数据
         // i+63 < buf_len是为了保证buf中剩余数据至少还有64字节
         // i+63 >= 63是为了防止i+63发生溢出(注意i是ulong32, 当它接近2^32-1时, 
         // i+63会溢出), 若i+63<63即i+63溢出, 则意味着buf中剩余字节不足64字节
         Process_One_Block_MD5(MD5_ctx->state, &buf[i]);
      }
   }
   else
      i = 0;
   memcpy(&MD5_ctx->data[bytes_left], &buf[i], buf_len-i);
   return 0;
}
```

- 最后填充处理剩余数据：

```c
int Final_MD5(MD5_CTX *MD5_ctx)
{
   ulong32 bytes_left, pad_len;
   unsigned char total_bits[8];
   memcpy(total_bits, (unsigned char *)MD5_ctx->count, 8); // total_bits=
                                                           // 已处理的报文的二进制位数
                                                           // (含data中剩余的字节)
                                                           // 后面补充的pad_stuff及
                                                           // total_bits本身不计在内
   bytes_left = (MD5_ctx->count[0] >> 3) & 0x3F;
   pad_len = (bytes_left < 56) ? (56 - bytes_left) : 
               (64 - bytes_left + 56); // bytes_left==56时, 要补8+56=64字节
                                       // bytes_left==57时, 要补7+56=63字节
   Update_MD5(MD5_ctx, pad_stuff, pad_len); // 把pad_stuff加到data中计算
   Update_MD5(MD5_ctx, total_bits, 8); // 把total_bits加到data中计算
   return 0;
}
```
***
### MD5 碰撞

如果有 $A$ 把 letter 及 RSA+MD5 加密而成的数字签名发送给 B，B 在收到信后验证签名，假定有碰撞 $\text{md5}(m_1)=\text{md5}(m_2)$，其中如果计算 $\text{md5}(m_1)$ 及 $\text{md5}(m_2)$ 时所用的 4 个 state 种子值均等于 $\text{md5}(\text{letter})$ 完成 Final_MD5() 前的 4 个 state 值，则一定有：$\text{md5}(\text{letter}+m_1)=\text{md5}(\text{letter}+m_2)$，因此 $\text{letter}+m_1$ 的签名可以用于 $\text{letter}+m_2$
***
### 破解方法

MD5 可以用彩虹表（Rainbow Table）来破解，我们举个简单的例子，假定 M 是 某 4 个大写字母组合生成的 MD5 值，我们可以通过如下步骤建立一张包含 4 个大写英文字母的彩虹表：

1. 产生一个随机数 $n_0$，其中 $n_0\in [0,26^4-1]$，找出与 $n_0$ 对应的字母组合 $p_0$，计算 $m_0=\text{md5}(p_0)$
2. 迭代 100 次：
	1. 计算 $n_j=m_{j-1}\text{ mod } 26^4$（消减函数）
	2. 以 $n_j$ 为序号，找出与它对应的 4 个英文字母组合 $p_j$（例如 $n=0$ 时 $p=AAAA$，$n=1$ 时 $p=AAAB$，$n=25$ 时 $p=AAAZ$，$n=26$ 时 $p=AABA$
	3. 计算 $m_j=\text{md5}(p_j)$
3. 在数据库中记录步骤 1 所得的 $n_0$ 以及 $j=100$ 时步骤 4 所得的 $m_{100}$

重复大步骤 1-3，我们可以得到若干条链，每条链包含 101 个 MD5 值

得到彩虹表之后，我们在数据库中查找 $M$，如果能找到，说明 $M$ 是 $j=100$ 时算出来的，那么从数据库中取出 $n_0$，再执行一次大步骤 2，这时候得到的 $n_{100}$ 所对应的字母组合 $p_{100}$ 即为所求

如果数据库中找不到 $M$，则设 $m_j=M$，再执行小步骤 1-3 算出 $m_{j+1}$，然后再在数据库中查找 $m_{j+1}$ ，如果能找到，说明 $M$ 是 $j=99$ 时算出来的，那么同上面的道理执行大步骤 2（但是迭代 99 次）可以得到答案
***
## SHA

SHA-1 散列算法计算出来的哈希值达 160 位，即 20 字节，也需要像 MD5 一样分块处理，每块 64 字节，当最后一块不足 64 字节也按照 MD5 的方式进行填充，与 MD5 不同的是，最后补上报文总位数的 8 个字节时是按照大端序，而非 MD5 的小端序