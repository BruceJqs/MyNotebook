---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
---   

# Homework 05

## 5.3

![](../../../assets/Pasted%20image%2020241211190113.png)

### 5.3.1

一个块大小 $=64\text{ bit}/8*2=16\text{ Byte}$

块数 $=32*2^{10}/16=2^{11}$

$\text{Byte Offset}=2^1$

$\text{Tag Bit}=64-(11+1+3)=49$

$\text{Total Bits}=2^{11}\times(2\times 64+49+1)=356\text{K bits}$
***
### 5.3.2

一个块大小 $=64\text{ bit}/8*16=2^7\text{ Byte}$

块数 $=64*2^{10}/2^7=2^9$

$\text{Byte Offset}=2^4$

$\text{Tag Bit}=64-(9+4+3)=48$

$\text{Total Bits}=2^9\times(16\times 64+48+1)=536.5\text{K bits}$

所以比 5.3.1 的 Cache 大 180.5K bits
***
### 5.3.3

当块的大小变大时，Hit Time 和 Miss Penalty 也相应变长

当块数变少时，Miss Rate 就变高了

两者相结合就导致性能更慢
***
### 5.3.4

如果我们交替访问在同一个组里的两个 Block 而在直接映射中属于同一个 Block 的内存地址，那么在 2-相联当中在前两次访问 Miss 后，后面全部命中，但是在直接映射中则会每次都 Miss，举例来说，我们交替访问 0 和 2048 即可
***
## 5.4

![](../../../assets/Pasted%20image%2020241211200015.png)


可以使用这个索引函数来索引直接映射 Cache，只要生成的索引为 10 位即可，但是这样的映射可能会导致映射不均匀，从而导致更高的 Miss Rate，可能还需要更高的 Tag 位数
***
## 5.5

![](../../../assets/Pasted%20image%2020241211200645.png)

### 5.5.1

块大小 $=2^5/2^3=4$ 个字
***
### 5.5.2

块数 $=2^5=32$ 块
***
### 5.5.3

总位数 $=2^5\times(4\times 64+54+1)=9952\text{ bits}$
***
### 5.5.4

|  Hex  |     Binary     | Tag | Index | Offset | Hit/Miss | Replacement |
|:-----:|:--------------:|:---:|:-----:|:------:|:--------:|:-----------:|
| 0x00  | 0000_0000_0000 | 0x0 | 0x00  |  0x00  |   Miss   |             |
| 0x04  | 0000_0000_0100 | 0x0 | 0x00  |  0x04  |   Hit    |             |
| 0x10  | 0000_0001_0000 | 0x0 | 0x00  |  0x10  |   Hit    |             |
| 0x84  | 0000_1000_0100 | 0x0 | 0x04  |  0x04  |   Miss   |             |
| 0xe8  | 0000_1110_1000 | 0x0 | 0x07  |  0x08  |   Miss   |             |
| 0xa0  | 0000_1010_0000 | 0x0 | 0x05  |  0x00  |   Miss   |             |
| 0x400 | 0100_0000_0000 | 0x1 | 0x00  |  0x00  |   Miss   |  0x00-0x1f  |
| 0x1e  | 0000_0001_1110 | 0x0 | 0x00  |  0x1e  |   Miss   | 0x400-0x41f |
| 0x8c  | 0000_1000_1100 | 0x0 | 0x04  |  0x0c  |   Hit    |             |
| 0xc1c | 1100_0001_1100 | 0x3 | 0x00  |  0x1c  |   Miss   |  0x00-0x1f  |
| 0xb4  | 0000_1011_0100 | 0x0 | 0x05  |  0x14  |   Hit    |             |
| 0x884 | 1000_1000_0100 | 0x2 | 0x04  |  0x04  |   Miss   |  0x80-0x9f  |
***
### 5.5.5

$\text{Hit Rate}=\frac{4}{12}=\frac{1}{3}$
***
### 5.5.6

| Index | Tag |    Data     |
|:-----:|:---:|:-----------:|
|   0   |  3  | 0xc00-0xc1f |
|   4   |  2  | 0x880-0x89f |
|   5   |  0  |  0xa0-0xbf  |
|   7   |  0  |  0xe0-0xff  |
***
## 5.6

![](../../../assets/Pasted%20image%2020241211204549.png)

### 5.6.1

- 在 L1 和 L2 Cache 之间添加缓冲器可以有效减少 L1 在向 L2 Cache 写穿时的延迟
- 在 L2 Cache 与内存之间添加缓冲器可以有效减少 Dirty Block 写进内存时造成的延迟
***
### 5.6.2

当 L1 写入失效，读入的数据会直接写入 L2 而不会写入 L1

- 如果造成了 L2 写入也失效，那么考虑 L2 Cache 块是否为脏块
	- 如果是，那么将脏块写入内存，同时将 L2 写成当前数据；
	- 如果不是，那么直接从内存拿到缓存中再写成当前数据
- 如果没造成 L2 写入失效，那么直接写 L2 
***
### 5.6.3

- L1 写入失效时，块将会按照 5.6.2 的方式写到 L2 当中
- L1 读取失效时，将会读取 L2 中的块：
	- 如果 L2 也读取失效，那么会从内存读取并存到 L1
	- 如果 L2 读取命中，那么会将此存到 L1，但因为多级独占 Cache 配置，所以 L2 的块也将写到内存当中
***
## 5.10

![](../../../assets/Pasted%20image%2020241211210822.png)

### 5.10.1

$\text{Clock Rate}_{P1}=\frac{1}{0.66ns}=1.515GHz$

$\text{Clock Rate}_{P2}=\frac{1}{0.9ns}=1.111GHz$
***
### 5.10.2

$\text{AMAT}_{P1}=\frac{8\%\times 70.66ns+92\%\times 0.66ns}{0.66ns}=9.485\text{Cycles}$

$\text{AMAT}_{P2}=\frac{6\%\times 70.90ns+94\%\times 0.90ns}{0.90ns}=5.667\text{Cycles}$
***
### 5.10.3

$\text{CPI}_{P1}=1+8\%\times\frac{70ns}{0.66ns}+8\%\times 36\%\times\frac{70ns}{0.66ns}=12.54$

$\text{CPI}_{P2}=1+6\%\times\frac{70ns}{0.90ns}+6\%\times 36\%\times\frac{70ns}{0.90ns}=9.65$

P2 更快
***
### 5.10.4

$\text{AMAT}_{P1}'=1+8\%\times(\frac{5.62ns}{0.66ns}+95\%\times\frac{70ns}{0.66ns})=9.742$

变差了
***
### 5.10.5

$\text{CPI}_{P1}'=1+8\%\times(\frac{5.62ns}{0.66ns}+95\%\times\frac{70ns}{0.66ns})+8\%\times 36\%\times(\frac{5.62ns}{0.66ns}+95\%\times\frac{70ns}{0.66ns})=12.89$
***
### 5.10.6

$1+8\%\times(\frac{5.62ns}{0.66ns}+\alpha\times\frac{70ns}{0.66ns})<1+8\%\times\frac{70ns}{0.66ns}$

解得 $\alpha<92.0\%$
***
### 5.10.7

$1+8\%\times(\frac{5.62ns}{0.66ns}+\alpha\times\frac{70ns}{0.66ns})+8\%\times 36\%\times(\frac{5.62ns}{0.66ns}+\alpha\times\frac{70ns}{0.66ns})<9.65$

解得 $\alpha<67.0\%$
***
## 5.11

![](../../../assets/Pasted%20image%2020241211222230.png)

![](../../../assets/Pasted%20image%2020241211222307.png)

### 5.11.1

![](../../../assets/Pasted%20image%2020241211225524.png)
***
### 5.11.2

| Hex  |  Binary   | Tag | Index | Offset | Hit/Miss |                         Table 1                          |       Table 2        | Table 3  |
| :--: | :-------: | :-: | :---: | :----: | :------: | :------------------------------------------------------: | :------------------: | :------: |
| 0x03 | 0000_0011 | 0x0 |   1   |   1    |   Miss   |                         Tag(1)=0                         |                      |          |
| 0xb4 | 1011_0100 | 0xb |   2   |   0    |   Miss   |                   Tag(1)=0<br>Tag(2)=b                   |                      |          |
| 0x2b | 0010_1011 | 0x2 |   5   |   1    |   Miss   |             Tag(1)=0<br>Tag(2)=b<br>Tag(5)=2             |                      |          |
| 0x02 | 0000_0010 | 0x0 |   1   |   0    |   Hit    |             Tag(1)=0<br>Tag(2)=b<br>Tag(5)=2             |                      |          |
| 0xbe | 1011_1110 | 0xb |   7   |   0    |   Miss   |       Tag(1)=0<br>Tag(2)=b<br>Tag(5)=2<br>Tag(7)=b       |                      |          |
| 0x58 | 0101_1000 | 0x5 |   4   |   0    |   Miss   | Tag(1)=0<br>Tag(2)=b<br>Tag(4)=5<br>Tag(5)=2<br>Tag(7)=b |                      |          |
| 0xbf | 1011_1111 | 0xb |   7   |   1    |   Hit    | Tag(1)=0<br>Tag(2)=b<br>Tag(4)=5<br>Tag(5)=2<br>Tag(7)=b |                      |          |
| 0x0e | 0000_1110 | 0x0 |   7   |   0    |   Miss   | Tag(1)=0<br>Tag(2)=b<br>Tag(4)=5<br>Tag(5)=2<br>Tag(7)=b |       Tag(7)=0       |          |
| 0x1f | 0001_1111 | 0x1 |   7   |   1    |   Miss   | Tag(1)=0<br>Tag(2)=b<br>Tag(4)=5<br>Tag(5)=2<br>Tag(7)=b |       Tag(7)=0       | Tag(7)=1 |
| 0xb5 | 1011_0101 | 0xb |   2   |   1    |   Hit    | Tag(1)=0<br>Tag(2)=b<br>Tag(4)=5<br>Tag(5)=2<br>Tag(7)=b |       Tag(7)=0       | Tag(7)=1 |
| 0xbf | 1011_1111 | 0xb |   7   |   1    |   Hit    | Tag(1)=0<br>Tag(2)=b<br>Tag(4)=5<br>Tag(5)=2<br>Tag(7)=b |       Tag(7)=0       | Tag(7)=1 |
| 0xba | 1011_1010 | 0xb |   5   |   0    |   Miss   | Tag(1)=0<br>Tag(2)=b<br>Tag(4)=5<br>Tag(5)=2<br>Tag(7)=b | Tag(5)=b<br>Tag(7)=0 | Tag(7)=1 |
| 0x2e | 0010_1110 | 0x2 |   7   |   0    |   Miss   | Tag(1)=0<br>Tag(2)=b<br>Tag(4)=5<br>Tag(5)=2<br>Tag(7)=b | Tag(5)=b<br>Tag(7)=2 | Tag(7)=1 |
| 0xce | 1100_1110 | 0xc |   7   |   0    |   Miss   | Tag(1)=0<br>Tag(2)=b<br>Tag(4)=5<br>Tag(5)=2<br>Tag(7)=b | Tag(5)=b<br>Tag(7)=2 | Tag(7)=c |
***
### 5.11.3

![](../../../assets/Pasted%20image%2020241211231735.png)

***
### 5.11.4

| Hex  |  Binary   | Tag  | Hit/Miss |                    Content                     |
|:----:|:---------:|:----:|:--------:|:----------------------------------------------:|
| 0x03 | 0000_0011 | 0x03 |   Miss   |                      0x03                      |
| 0xb4 | 1011_0100 | 0xb4 |   Miss   |                   0x03, 0xb4                   |
| 0x2b | 0010_1011 | 0x2b |   Miss   |                0x03, 0xb4, 0x2b                |
| 0x02 | 0000_0010 | 0x02 |   Miss   |             0x03, 0xb4, 0x2b, 0x02             |
| 0xbe | 1011_1110 | 0xbe |   Miss   |          0x03, 0xb4, 0x2b, 0x02, 0xbe          |
| 0x58 | 0101_1000 | 0x58 |   Miss   |       0x03, 0xb4, 0x2b, 0x02, 0xbe, 0x58       |
| 0xbf | 1011_1111 | 0xbf |   Miss   |    0x03, 0xb4, 0x2b, 0x02, 0xbe, 0x58, 0xbf    |
| 0x0e | 0000_1110 | 0x0e |   Miss   | 0x03, 0xb4, 0x2b, 0x02, 0xbe, 0x58, 0xbf, 0x0e |
| 0x1f | 0001_1111 | 0x1f |   Miss   | 0x1f, 0xb4, 0x2b, 0x02, 0xbe, 0x58, 0xbf, 0x0e |
| 0xb5 | 1011_0101 | 0xb5 |   Miss   | 0x1f, 0xb5, 0x2b, 0x02, 0xbe, 0x58, 0xbf, 0x0e |
| 0xbf | 1011_1111 | 0xbf |   Hit    | 0x1f, 0xb5, 0x2b, 0x02, 0xbe, 0x58, 0xbf, 0x0e |
| 0xba | 1011_1010 | 0xba |   Miss   | 0x1f, 0xb5, 0xba, 0x02, 0xbe, 0x58, 0xbf, 0x0e |
| 0x2e | 0010_1110 | 0x2e |   Miss   | 0x1f, 0xb5, 0xba, 0x2e, 0xbe, 0x58, 0xbf, 0x0e |
| 0xce | 1100_1110 | 0xce |   Miss   | 0x1f, 0xb5, 0xba, 0x2e, 0xce, 0x58, 0xbf, 0x0e |
***
### 5.11.5

![](../../../assets/Pasted%20image%2020241211232744.png)
***
### 5.11.6
| Hex  |  Binary   | Tag  | Offset | Hit/Miss |                           Content                           |
| :--: | :-------: | :--: | :----: | :------: | :---------------------------------------------------------: |
| 0x03 | 0000_0011 | 0x01 |   1    |   Miss   |                        (0x02, 0x03)                         |
| 0xb4 | 1011_0100 | 0x5a |   0    |   Miss   |                 (0x02, 0x03), (0xb4, 0xb5)                  |
| 0x2b | 0010_1011 | 0x15 |   1    |   Miss   |          (0x02, 0x03), (0xb4, 0xb5), (0x2a, 0x2b)           |
| 0x02 | 0000_0010 | 0x01 |   0    |   Hit    |          (0xb4, 0xb5), (0x2a, 0x2b), (0x02, 0x03)           |
| 0xbe | 1011_1110 | 0x5f |   0    |   Miss   |  (0xb4, 0xb5), (0x2a, 0x2b),<br>(0x02, 0x03), (0xbe, 0xbf)  |
| 0x58 | 0101_1000 | 0x2c |   0    |   Miss   | (0x2a, 0x2b), (0x02, 0x03),<br> (0xbe, 0xbf), (0x58, 0x59)  |
| 0xbf | 1011_1111 | 0x5f |   1    |   Hit    | (0x2a, 0x2b), (0x02, 0x03),<br>  (0x58, 0x59), (0xbe, 0xbf) |
| 0x0e | 0000_1110 | 0x07 |   0    |   Miss   | (0x02, 0x03), (0x58, 0x59),<br> (0xbe, 0xbf), (0x0e, 0x0f)  |
| 0x1f | 0001_1111 | 0x0f |   1    |   Miss   | (0x58, 0x59), (0xbe, 0xbf), <br> (0x0e, 0x0f), (0x1e, 0x1f) |
| 0xb5 | 1011_0101 | 0x5a |   1    |   Miss   |  (0xbe, 0xbf), (0x0e, 0x0f),<br>(0x1e, 0x1f), (0xb4, 0xb5)  |
| 0xbf | 1011_1111 | 0x5f |   1    |   Hit    | (0x0e, 0x0f), (0x1e, 0x1f),<br> (0xb4, 0xb5), (0xbe, 0xbf)  |
| 0xba | 1011_1010 | 0x5d |   0    |   Miss   | (0x1e, 0x1f), (0xb4, 0xb5), <br>(0xbe, 0xbf), (0xba, 0xbb)  |
| 0x2e | 0010_1110 | 0x17 |   0    |   Miss   | (0xb4, 0xb5), (0xbe, 0xbf),<br> (0xba, 0xbb), (0x2e, 0x2f)  |
| 0xce | 1100_1110 | 0x67 |   0    |   Miss   | (0xbe, 0xbf), (0xba, 0xbb), <br>(0x2e, 0x2f), (0xce, 0xcf)  |
***
### 5.11.7

| Hex  |  Binary   | Tag  | Offset | Hit/Miss |                           Content                            |
| :--: | :-------: | :--: | :----: | :------: | :----------------------------------------------------------: |
| 0x03 | 0000_0011 | 0x01 |   1    |   Miss   |                         (0x02, 0x03)                         |
| 0xb4 | 1011_0100 | 0x5a |   0    |   Miss   |                  (0x02, 0x03), (0xb4, 0xb5)                  |
| 0x2b | 0010_1011 | 0x15 |   1    |   Miss   |           (0x02, 0x03), (0xb4, 0xb5), (0x2a, 0x2b)           |
| 0x02 | 0000_0010 | 0x01 |   0    |   Hit    |           (0xb4, 0xb5), (0x2a, 0x2b), (0x02, 0x03)           |
| 0xbe | 1011_1110 | 0x5f |   0    |   Miss   |  (0xb4, 0xb5), (0x2a, 0x2b),<br>(0x02, 0x03), (0xbe, 0xbf)   |
| 0x58 | 0101_1000 | 0x2c |   0    |   Miss   |  (0xb4, 0xb5), (0x02, 0x03),<br> (0x2a, 0x2b), (0x58, 0x59)  |
| 0xbf | 1011_1111 | 0x5f |   1    |   Miss   | (0x2a, 0x2b), (0x02, 0x03),<br>  (0xb4, 0xb5), (0xbe, 0xbf)  |
| 0x0e | 0000_1110 | 0x07 |   0    |   Miss   | (0x2a, 0x2b), (0x02, 0x03),<br>  (0xb4, 0xb5), (0x0e, 0x0f)  |
| 0x1f | 0001_1111 | 0x0f |   1    |   Miss   | (0x2a, 0x2b), (0x02, 0x03),<br>  (0xb4, 0xb5), (0x1e, 0x1f)  |
| 0xb5 | 1011_0101 | 0x5a |   1    |   Miss   | (0x2a, 0x2b), (0x02, 0x03),<br>   (0xbe, 0xbf), (0xb4, 0xb5) |
| 0xbf | 1011_1111 | 0x5f |   1    |   Hit    | (0x2a, 0x2b), (0x02, 0x03),<br>   (0xbe, 0xbf), (0xbe, 0xbf) |
| 0xba | 1011_1010 | 0x5d |   0    |   Miss   | (0x2a, 0x2b), (0x02, 0x03),<br>   (0xbe, 0xbf), (0xba, 0xbb) |
| 0x2e | 0010_1110 | 0x17 |   0    |   Miss   | (0x2a, 0x2b), (0x02, 0x03),<br>   (0xbe, 0xbf), (0x2e, 0xef) |
| 0xce | 1100_1110 | 0x67 |   0    |   Miss   | (0x2a, 0x2b), (0x02, 0x03),<br>   (0xbe, 0xbf), (0xce, 0xcf) |
***
### 5.11.8

| Hex  |  Binary   | Tag  | Offset | Hit/Miss |                          Content                           |
| :--: | :-------: | :--: | :----: | :------: | :--------------------------------------------------------: |
| 0x03 | 0000_0011 | 0x01 |   1    |   Miss   |                        (0x02, 0x03)                        |
| 0xb4 | 1011_0100 | 0x5a |   0    |   Miss   |                 (0x02, 0x03), (0xb4, 0xb5)                 |
| 0x2b | 0010_1011 | 0x15 |   1    |   Miss   |          (0x02, 0x03), (0xb4, 0xb5), (0x2a, 0x2b)          |
| 0x02 | 0000_0010 | 0x01 |   0    |   Hit    |          (0x02, 0x03), (0xb4, 0xb5), (0x2a, 0x2b)          |
| 0xbe | 1011_1110 | 0x5f |   0    |   Miss   | (0x02, 0x03), (0xb4, 0xb5), <br>(0x2a, 0x2b), (0xbe, 0xbf) |
| 0x58 | 0101_1000 | 0x2c |   0    |   Miss   | (0x58, 0x59), (0xb4, 0xb5), <br>(0x2a, 0x2b), (0xbe, 0xbf) |
| 0xbf | 1011_1111 | 0x5f |   1    |   Hit    | (0x58, 0x59), (0xb4, 0xb5), <br>(0x2a, 0x2b), (0xbe, 0xbf) |
| 0x0e | 0000_1110 | 0x07 |   0    |   Miss   | (0x0e, 0x0f), (0xb4, 0xb5), <br>(0x2a, 0x2b), (0xbe, 0xbf) |
| 0x1f | 0001_1111 | 0x0f |   1    |   Miss   | (0x1e, 0x1f), (0xb4, 0xb5), <br>(0x2a, 0x2b), (0xbe, 0xbf) |
| 0xb5 | 1011_0101 | 0x5a |   1    |   Hit    | (0x1e, 0x1f), (0xb4, 0xb5), <br>(0x2a, 0x2b), (0xbe, 0xbf) |
| 0xbf | 1011_1111 | 0x5f |   1    |   Hit    | (0x1e, 0x1f), (0xb4, 0xb5), <br>(0x2a, 0x2b), (0xbe, 0xbf) |
| 0xba | 1011_1010 | 0x5d |   0    |   Miss   | (0x1e, 0x1f), (0xb4, 0xb5), <br>(0xba, 0xbb), (0xbe, 0xbf) |
| 0x2e | 0010_1110 | 0x17 |   0    |   Miss   | (0x1e, 0x1f), (0xb4, 0xb5), <br>(0x2e, 0x2f), (0xbe, 0xbf) |
| 0xce | 1100_1110 | 0x67 |   0    |   Miss   | (0x1e, 0x1f), (0xb4, 0xb5), <br>(0xce, 0xcf), (0xbe, 0xbf) |
***
## 5.16

![](../../../assets/Pasted%20image%2020241211234341.png)

![](../../../assets/Pasted%20image%2020241211234404.png)

### 5.16.1

| Address | Virtual Page | TLB Hit/Miss | Page Table Hit/Miss | Page Fault | Valid | Tag | Physical Page |
| :-----: | :----------: | :----------: | :-----------------: | :--------: | :---: | :-: | :-----------: |
| 0x123d  |     0x1      |     Miss     |         Hit         |    True    |   1   | 0xb |      12       |
| 0x123d  |     0x1      |     Miss     |         Hit         |    True    |   1   | 0x7 |       4       |
| 0x123d  |     0x1      |     Miss     |         Hit         |    True    |   1   | 0x3 |       6       |
| 0x123d  |     0x1      |     Miss     |         Hit         |    True    |   1   | 0x1 |      13       |
| 0x08b3  |     0x0      |     Miss     |         Hit         |   False    |   1   | 0x0 |       5       |
| 0x08b3  |     0x0      |     Miss     |         Hit         |   False    |   1   | 0x7 |       4       |
| 0x08b3  |     0x0      |     Miss     |         Hit         |   False    |   1   | 0x3 |       6       |
| 0x08b3  |     0x0      |     Miss     |         Hit         |   False    |   1   | 0x1 |      13       |
| 0x365c  |     0x3      |     Hit      |         Hit         |   False    |   1   | 0x0 |       5       |
| 0x365c  |     0x3      |     Hit      |         Hit         |   False    |   1   | 0x7 |       4       |
| 0x365c  |     0x3      |     Hit      |         Hit         |   False    |   1   | 0x3 |       6       |
| 0x365c  |     0x3      |     Hit      |         Hit         |   False    |   1   | 0x1 |      13       |
| 0x871b  |     0x8      |     Miss     |         Hit         |    True    |   1   | 0x0 |       5       |
| 0x871b  |     0x8      |     Miss     |         Hit         |    True    |   1   | 0x8 |      14       |
| 0x871b  |     0x8      |     Miss     |         Hit         |    True    |   1   | 0x3 |       6       |
| 0x871b  |     0x8      |     Miss     |         Hit         |    True    |   1   | 0x1 |      13       |
| 0xbee6  |     0xb      |     Miss     |         Hit         |   False    |   1   | 0x0 |       5       |
| 0xbee6  |     0xb      |     Miss     |         Hit         |   False    |   1   | 0x8 |      14       |
| 0xbee6  |     0xb      |     Miss     |         Hit         |   False    |   1   | 0x3 |       6       |
| 0xbee6  |     0xb      |     Miss     |         Hit         |   False    |   1   | 0xb |      12       |
| 0x3140  |     0x3      |     Hit      |         Hit         |   False    |   1   | 0x0 |       5       |
| 0x3140  |     0x3      |     Hit      |         Hit         |   False    |   1   | 0x8 |      14       |
| 0x3140  |     0x3      |     Hit      |         Hit         |   False    |   1   | 0x3 |       6       |
| 0x3140  |     0x3      |     Hit      |         Hit         |   False    |   1   | 0xb |      12       |
| 0xc049  |     0xc      |     Miss     |        Miss         |    True    |   1   | 0xc |      15       |
| 0xc049  |     0xc      |     Miss     |        Miss         |    True    |   1   | 0x8 |      14       |
| 0xc049  |     0xc      |     Miss     |        Miss         |    True    |   1   | 0x3 |       6       |
| 0xc049  |     0xc      |     Miss     |        Miss         |    True    |   1   | 0xb |      12       |
***
### 5.16.2

| Address | Virtual Page | TLB Hit/Miss | Page Table Hit/Miss | Page Fault | Valid | Tag | Physical Page |
| :-----: | :----------: | :----------: | :-----------------: | :--------: | :---: | :-: | :-----------: |
| 0x123d  |     0x0      |     Miss     |         Hit         |   False    |   1   | 0xb |      12       |
| 0x123d  |     0x0      |     Miss     |         Hit         |   False    |   1   | 0x7 |       4       |
| 0x123d  |     0x0      |     Miss     |         Hit         |   False    |   1   | 0x3 |       6       |
| 0x123d  |     0x0      |     Miss     |         Hit         |   False    |   1   | 0x0 |       5       |
| 0x08b3  |     0x0      |     Hit      |         Hit         |   False    |   1   | 0xb |      12       |
| 0x08b3  |     0x0      |     Hit      |         Hit         |   False    |   1   | 0x7 |       4       |
| 0x08b3  |     0x0      |     Hit      |         Hit         |   False    |   1   | 0x3 |       6       |
| 0x08b3  |     0x0      |     Hit      |         Hit         |   False    |   1   | 0x0 |       5       |
| 0x365c  |     0x0      |     Hit      |         Hit         |   False    |   1   | 0xb |      12       |
| 0x365c  |     0x0      |     Hit      |         Hit         |   False    |   1   | 0x7 |       4       |
| 0x365c  |     0x0      |     Hit      |         Hit         |   False    |   1   | 0x3 |       6       |
| 0x365c  |     0x0      |     Hit      |         Hit         |   False    |   1   | 0x0 |       5       |
| 0x871b  |     0x2      |     Miss     |         Hit         |   False    |   1   | 0x2 |      13       |
| 0x871b  |     0x2      |     Miss     |         Hit         |   False    |   1   | 0x7 |       4       |
| 0x871b  |     0x2      |     Miss     |         Hit         |   False    |   1   | 0x3 |       6       |
| 0x871b  |     0x2      |     Miss     |         Hit         |   False    |   1   | 0x0 |       5       |
| 0xbee6  |     0x2      |     Hit      |         Hit         |   False    |   1   | 0x2 |      13       |
| 0xbee6  |     0x2      |     Hit      |         Hit         |   False    |   1   | 0x7 |       4       |
| 0xbee6  |     0x2      |     Hit      |         Hit         |   False    |   1   | 0x3 |       6       |
| 0xbee6  |     0x2      |     Hit      |         Hit         |   False    |   1   | 0x0 |       5       |
| 0x3140  |     0x0      |     Hit      |         Hit         |   False    |   1   | 0x2 |      13       |
| 0x3140  |     0x0      |     Hit      |         Hit         |   False    |   1   | 0x7 |       4       |
| 0x3140  |     0x0      |     Hit      |         Hit         |   False    |   1   | 0x3 |       6       |
| 0x3140  |     0x0      |     Hit      |         Hit         |   False    |   1   | 0x0 |       5       |
| 0xc049  |     0x3      |     Hit      |         Hit         |   False    |   1   | 0x2 |      13       |
| 0xc049  |     0x3      |     Hit      |         Hit         |   False    |   1   | 0x7 |       4       |
| 0xc049  |     0x3      |     Hit      |         Hit         |   False    |   1   | 0x3 |       6       |
| 0xc049  |     0x3      |     Hit      |         Hit         |   False    |   1   | 0x0 |       5       |

优势：更大的页面能减小 TLB Miss Rate

劣势：会大大减小页面的使用率，更加分裂
***
### 5.16.3

简写：

- Virtual Page：VP
- Physical Page：PP
- Page Table：PT
- Page Fault：PF

| Address | VP  | Tag | Index | TLB Hit/Miss | PT Hit/Miss |  PF   | Valid | Tag | PP  | Index |
| :-----: | :-: | :-: | :---: | :----------: | :---------: | :---: | :---: | :-: | :-: | :---: |
| 0x123d  | 0x1 |  0  |   1   |     Miss     |     Hit     | True  |   1   | 0xb | 12  |   0   |
| 0x123d  | 0x1 |  0  |   1   |     Miss     |     Hit     | True  |   1   | 0x7 |  4  |   1   |
| 0x123d  | 0x1 |  0  |   1   |     Miss     |     Hit     | True  |   1   | 0x3 |  6  |   0   |
| 0x123d  | 0x1 |  0  |   1   |     Miss     |     Hit     | True  |   1   | 0x0 | 13  |   1   |
| 0x08b3  | 0x0 |  0  |   0   |     Miss     |     Hit     | False |   1   | 0x0 |  5  |   0   |
| 0x08b3  | 0x0 |  0  |   0   |     Miss     |     Hit     | False |   1   | 0x7 |  4  |   1   |
| 0x08b3  | 0x0 |  0  |   0   |     Miss     |     Hit     | False |   1   | 0x3 |  6  |   0   |
| 0x08b3  | 0x0 |  0  |   0   |     Miss     |     Hit     | False |   1   | 0x0 | 13  |   1   |
| 0x365c  | 0x3 |  1  |   1   |     Miss     |     Hit     | False |   1   | 0x0 |  5  |   0   |
| 0x365c  | 0x3 |  1  |   1   |     Miss     |     Hit     | False |   1   | 0x1 |  6  |   1   |
| 0x365c  | 0x3 |  1  |   1   |     Miss     |     Hit     | False |   1   | 0x3 |  6  |   0   |
| 0x365c  | 0x3 |  1  |   1   |     Miss     |     Hit     | False |   1   | 0x0 | 13  |   1   |
| 0x871b  | 0x8 |  4  |   0   |     Miss     |     Hit     | True  |   1   | 0x0 |  5  |   0   |
| 0x871b  | 0x8 |  4  |   0   |     Miss     |     Hit     | True  |   1   | 0x1 |  6  |   1   |
| 0x871b  | 0x8 |  4  |   0   |     Miss     |     Hit     | True  |   1   | 0x4 | 14  |   0   |
| 0x871b  | 0x8 |  4  |   0   |     Miss     |     Hit     | True  |   1   | 0x0 | 13  |   1   |
| 0xbee6  | 0xb |  5  |   1   |     Miss     |     Hit     | False |   1   | 0x0 |  5  |   0   |
| 0xbee6  | 0xb |  5  |   1   |     Miss     |     Hit     | False |   1   | 0x1 |  6  |   1   |
| 0xbee6  | 0xb |  5  |   1   |     Miss     |     Hit     | False |   1   | 0x4 | 14  |   0   |
| 0xbee6  | 0xb |  5  |   1   |     Miss     |     Hit     | False |   1   | 0x5 | 12  |   1   |
| 0x3140  | 0x3 |  1  |   1   |     Hit      |     Hit     | False |   1   | 0x0 |  5  |   0   |
| 0x3140  | 0x3 |  1  |   1   |     Hit      |     Hit     | False |   1   | 0x1 |  6  |   1   |
| 0x3140  | 0x3 |  1  |   1   |     Hit      |     Hit     | False |   1   | 0x4 | 14  |   0   |
| 0x3140  | 0x3 |  1  |   1   |     Hit      |     Hit     | False |   1   | 0x5 | 12  |   1   |
| 0xc049  | 0xc |  6  |   0   |     Miss     |    Miss     | True  |   1   | 0x6 |  5  |   0   |
| 0xc049  | 0xc |  6  |   0   |     Miss     |    Miss     | True  |   1   | 0x1 |  6  |   1   |
| 0xc049  | 0xc |  6  |   0   |     Miss     |    Miss     | True  |   1   | 0x4 | 14  |   0   |
| 0xc049  | 0xc |  6  |   0   |     Miss     |    Miss     | True  |   1   | 0x5 | 12  |   1   |
***
### 5.16.4

| Address | VP  | Tag | Index | TLB Hit/Miss | PT Hit/Miss |  PF   | Valid | Tag | PP  | Index |
| :-----: | :-: | :-: | :---: | :----------: | :---------: | :---: | :---: | :-: | :-: | :---: |
| 0x123d  | 0x1 |  0  |   1   |     Miss     |     Hit     | True  |   1   | 0xb | 12  |   0   |
| 0x123d  | 0x1 |  0  |   1   |     Miss     |     Hit     | True  |   1   | 0x0 | 13  |   1   |
| 0x123d  | 0x1 |  0  |   1   |     Miss     |     Hit     | True  |   1   | 0x3 |  6  |   2   |
| 0x123d  | 0x1 |  0  |   1   |     Miss     |     Hit     | True  |   0   | 0x4 |  9  |   3   |
| 0x08b3  | 0x0 |  0  |   0   |     Miss     |     Hit     | False |   1   | 0x0 |  5  |   0   |
| 0x08b3  | 0x0 |  0  |   0   |     Miss     |     Hit     | False |   1   | 0x0 | 13  |   1   |
| 0x08b3  | 0x0 |  0  |   0   |     Miss     |     Hit     | False |   1   | 0x3 |  6  |   2   |
| 0x08b3  | 0x0 |  0  |   0   |     Miss     |     Hit     | False |   0   | 0x4 |  9  |   3   |
| 0x365c  | 0x3 |  0  |   3   |     Miss     |     Hit     | False |   1   | 0x0 |  5  |   0   |
| 0x365c  | 0x3 |  0  |   3   |     Miss     |     Hit     | False |   1   | 0x0 | 13  |   1   |
| 0x365c  | 0x3 |  0  |   3   |     Miss     |     Hit     | False |   1   | 0x3 |  6  |   2   |
| 0x365c  | 0x3 |  0  |   3   |     Miss     |     Hit     | False |   1   | 0x0 |  6  |   3   |
| 0x871b  | 0x8 |  2  |   0   |     Miss     |     Hit     | True  |   1   | 0x2 | 14  |   0   |
| 0x871b  | 0x8 |  2  |   0   |     Miss     |     Hit     | True  |   1   | 0x0 | 13  |   1   |
| 0x871b  | 0x8 |  2  |   0   |     Miss     |     Hit     | True  |   1   | 0x3 |  6  |   2   |
| 0x871b  | 0x8 |  2  |   0   |     Miss     |     Hit     | True  |   1   | 0x0 |  6  |   3   |
| 0xbee6  | 0xb |  2  |   3   |     Miss     |     Hit     | False |   1   | 0x2 | 14  |   0   |
| 0xbee6  | 0xb |  2  |   3   |     Miss     |     Hit     | False |   1   | 0x0 | 13  |   1   |
| 0xbee6  | 0xb |  2  |   3   |     Miss     |     Hit     | False |   1   | 0x3 |  6  |   2   |
| 0xbee6  | 0xb |  2  |   3   |     Miss     |     Hit     | False |   1   | 0x2 | 12  |   3   |
| 0x3140  | 0x3 |  0  |   3   |     Miss     |     Hit     | False |   1   | 0x2 | 14  |   0   |
| 0x3140  | 0x3 |  0  |   3   |     Miss     |     Hit     | False |   1   | 0x0 | 13  |   1   |
| 0x3140  | 0x3 |  0  |   3   |     Miss     |     Hit     | False |   1   | 0x3 |  6  |   2   |
| 0x3140  | 0x3 |  0  |   3   |     Miss     |     Hit     | False |   1   | 0x0 |  6  |   3   |
| 0xc049  | 0xc |  3  |   0   |     Miss     |    Miss     | True  |   1   | 0x3 | 15  |   0   |
| 0xc049  | 0xc |  3  |   0   |     Miss     |    Miss     | True  |   1   | 0x0 | 13  |   1   |
| 0xc049  | 0xc |  3  |   0   |     Miss     |    Miss     | True  |   1   | 0x3 |  6  |   2   |
| 0xc049  | 0xc |  3  |   0   |     Miss     |    Miss     | True  |   1   | 0x0 |  6  |   3   |
***
### 5.16.5

如果没有 TLB，每次内存访问都需要访问页表再访问需要的数据，这样就加倍了访问内存的时间
***
## 5.17

![](../../../assets/Pasted%20image%2020241212013744.png)

### 5.17.1

$\text{Entry Bits}=32-3-10=19\text{ bits}$

$\text{Total Size}=5\times(2^{19}\times 4\text{ Bytes})=10\text{ MB}$
***
### 5.17.2

$2^{19}$ 个条目被分成 256 组到二级页表中，那么每个二级页表有 $2^{19}/256=2^{11}$ 个条目

那么每张二级页表需要的大小为 $2^{11}\times 4\text{ Bytes}=8\text{ KB}$

最大内存容量即为 $5\times 8\text{ KB}\times 256 + 5\times 6\text{ Bytes}\times 256=10\text{ MB} + 7.5\text{ KB}$

最小内存容量即为 $5\text{ MB}+ 3.75\text{ KB}$
***
### 5.17.3

每个块大小为 16 Bytes，那么 Cache 的 Block 数量为 1K，所以它有 10 个 Index 和 4 个 Byte Offset，比要求的 13 位大，所以可以制作

设计者可以增加 Cache 的相联数
***
## 5.20

![](../../../assets/Pasted%20image%2020241212014322.png)

### 5.20.1

都不会命中
***
### 5.20.2


***
### 5.20.3

根据抛硬币结果而定
***
### 5.20.4

最佳替换策略根据后续访问控制每一次访问都命中
***
### 5.20.5

因为最佳替换策略需要知道后续的访问，但是作为机器是不知道后续的访问是什么样的，所以非常难以实现
***
### 5.20.6
