# Lab1-Misc Report

**<font size=5>Contents</font>**

[TOC]

<div style="page-break-after:always;"></div>

## Task 1.1：乱码情形探究

这里我们把 python，vscode，CyberChef 都尝试一下，输出不同的就都截图放在报告里，相同的就只选择 python 的输出结果了。

### 乱码情况 1：用 GBK 解码 UTF-8 编码的文本

<img src="/Users/bruce/Library/Application Support/typora-user-images/image-20240704164145984.png" alt="image-20240704164145984"  />

首先我们知道 utf-8 与 GBK 两种编码方式都是兼容 ASCII 码的，都是使用一个字节来表示 ASCII 码能表示的字符。

![image-20240704164527201](/Users/bruce/Library/Application Support/typora-user-images/image-20240704164527201.png)

因此对于大小写字母这些包含在 ASCII 码中的两者转换并没有区别。

在 utf-8 编码中，汉字是用 3 个字节来表示的，特殊的汉字还会用 4 个字节来表示，于是“战队”二字在 utf-8 编码下就形成了 6 个字节。

但是在 GBK 编码中，一个汉字是用 2 个字节来表示的，于是对于 utf-8 形成的 6 个字节的编码在 GBK 中就会被解码为 3 个汉字，形成乱码问题。

### 乱码情况 2：用 UTF-8 解码 GBK 编码的文本

![image-20240704165631177](/Users/bruce/Library/Application Support/typora-user-images/image-20240704165631177.png)

![image-20240704165744834](/Users/bruce/Library/Application Support/typora-user-images/image-20240704165744834.png)

![image-20240705122606661](/Users/bruce/Library/Application Support/typora-user-images/image-20240705122606661.png)

跟 1.1 中的解释相似，GBK 编码将"战队"编码为 `11010101 10111101 10110110 11010011`，而对于 utf-8 编码来说，第一个字节前三位为 `110`，这意味着这个字符应当是两个字节来保存的，因此 utf-8 将前两个字节编为一个字符，但是第三个字节前两位却显示的是 10，utf-8 就不知道该怎么解码了，因此在 python 中会显示 UnicodeDecodeError；CyberChef 则将错误的字节解码为了其他奇怪的字符；而 vscode 则将其解码为奇怪的符号。

### 乱码情况 3：用 latin-1 解码 UTF-8 编码的文本

![image-20240705123531833](/Users/bruce/Library/Application Support/typora-user-images/image-20240705123531833.png)

![image-20240705123848770](/Users/bruce/Library/Application Support/typora-user-images/image-20240705123848770.png)

![image-20240705123922961](/Users/bruce/Library/Application Support/typora-user-images/image-20240705123922961.png)

Latin-1，即 ISO-8859-1，是单字节编码，本身无法表示中文。由上面所说的，utf-8 将每个汉字编码为三个字节，因此用 Latin-1 解码 utf-8 编码的文本会出现 6 个奇怪的字符。

### 乱码情况 4：用 latin-1 解码 GBK 编码的文本

![image-20240705124712035](/Users/bruce/Library/Application Support/typora-user-images/image-20240705124712035.png)

同理，GBK 将每个汉字编码为两个字节，因此用 Latin-1 解码 utf-8 编码的文本会出现 4 个奇怪的字符。

### 乱码情况 5：先用 GBK 解码 UTF-8 编码的文本，再用 UTF-8 解码前面的结果

这里我们只使用 vscode 实现（python 在该文本下 GBK 解码就报错，无法解码）

原文本：

![image-20240705125818551](/Users/bruce/Library/Application Support/typora-user-images/image-20240705125818551.png)

GBK 解码：

![image-20240705125846700](/Users/bruce/Library/Application Support/typora-user-images/image-20240705125846700.png)

重新用 GBK 编码再用 utf-8 解码：

![image-20240705125930682](/Users/bruce/Library/Application Support/typora-user-images/image-20240705125930682.png)

可以看到，“逼”这一个字被编成了奇怪的字符，我们查看原文本与最后文本的十六进制：

![image-20240705130251037](/Users/bruce/Library/Application Support/typora-user-images/image-20240705130251037.png)

![image-20240705130254429](/Users/bruce/Library/Application Support/typora-user-images/image-20240705130254429.png)

这是可以解释的，在起初“牛逼”二字被编码为 `11100111 10001001 10011011  111010001 10000000 10111100` ，用 GBK 解码时会被错误地解释为其他字符或者无法识别的字节序列（这也就是为什么 python 会报错），那么解码后的十六进制就已经编成了下面的那些，最后 utf-8 转换时也就出现了乱码。

### 先用 UTF-8 解码 GBK 编码的文本，再用 GBK 解码前面的结果

原文本：

![image-20240705132648897](/Users/bruce/Library/Application Support/typora-user-images/image-20240705132648897.png)

utf-8 解码：

![image-20240705132716676](/Users/bruce/Library/Application Support/typora-user-images/image-20240705132716676.png)

再用 GBK 解码：

![image-20240705132749889](/Users/bruce/Library/Application Support/typora-user-images/image-20240705132749889.png)

锟斤拷乱码出现了！我们查看十六进制：

![image-20240705132925968](/Users/bruce/Library/Application Support/typora-user-images/image-20240705132925968.png)

![image-20240705132928866](/Users/bruce/Library/Application Support/typora-user-images/image-20240705132928866.png)

根据 1.2 也可以解释这个，因为 utf-8 特定的编码格式，导致解码时有些字符无法被解读，而 vscode 将错误的字节流替换，才得到了现在的乱码。

### 研究后的讨论

#### 可恢复？

从之前的研究来看，不可恢复的情况在于解码时若遇到不存在于解码格式当中的十六进制字节流时，vscode 会进行篡改使得其符合解码格式，这样就造成了不可恢复。而且我们默认解码之后同时用这种编码方式重新编码，并保存字节流到文件。那理论上来说，以上六种乱码形式都有不可恢复的可能，因为重新编码会导致篡改的发生。

#### “锟斤拷”？

“锟斤拷”乱码的来源就在于 utf-8 特殊的编码格式，当解码时有些字符不符合编码格式时，无法匹配到正确的 utf-8 码，vscode 会将其填充为 `EF BF BD`。我们假设有三个连续的字符不符合编码格式，那么最后填充完得到的字节流是 `EF BF BD EF BF BD EF BF BD EF BF BD`，在GBK编码表中，查找对应编码，并解码为汉字，由于 `EF BF` 对应锟，`BD EF` 对应斤，`BF BD`对应拷，从而得到“锟斤拷锟斤拷”。

## Task 1.2 NATO26



## Challenge 2

### Task 1: 45gfg9's easy OSINT

观察图片，其中最有特征的点在于建筑的 SPARKPLUS 以及侧边的 SPLOUNGE，将这部分图片放入 Google 识图，我们能找到一篇 blog：

![image-20240705151840491](/Users/bruce/Library/Application Support/typora-user-images/image-20240705151840491.png)

![image-20240705151848546](/Users/bruce/Library/Application Support/typora-user-images/image-20240705151848546.png)

这里的 blog 也提及了 SPLOUNGE：

![image-20240705151915185](/Users/bruce/Library/Application Support/typora-user-images/image-20240705151915185.png)

根据 Blog 所给的地址，我们可以找到：

![image-20240705151933808](/Users/bruce/Library/Application Support/typora-user-images/image-20240705151933808.png)

#### 所在位置

根据图片最左边出现了 7-Eleven：我们可以锁定位置在下图红圈范围内：

![image-20240705152244951](/Users/bruce/Library/Application Support/typora-user-images/image-20240705152244951.png)

方框所示即为图中的建筑。

#### 路牌内容

查看街景图，可能是图片过于早（2015），并没有路牌，那么我们直接顺着这条路找，找到了 Seoul Medical Center，与图中下面两行隐隐约约的韩文对比完全一致。

![image-20240705153102049](/Users/bruce/Library/Application Support/typora-user-images/image-20240705153102049.png)

对于上面两行的内容，我们从图标 “88” 入手，接着往右找能发现：

![image-20240705153324481](/Users/bruce/Library/Application Support/typora-user-images/image-20240705153324481.png)

猜想这是一个道路，应该叫 Olympic-daero

### Task 2: pumpk1n's real OSINT

开启随便盲猜瞎猜模式：

根据飞机图标和机翼上的文字可以看出，pumpk1n 乘坐的是天津航空的航班。

用 exiftools 查看这张图片的时间，看到这样的信息：

![image-20240706005237767](/Users/bruce/Library/Application Support/typora-user-images/image-20240706005237767.png)

那就查看 6 月 23 日左右的 CTF 竞赛，查到了：

![image-20240706005432042](/Users/bruce/Library/Application Support/typora-user-images/image-20240706005432042.png)

比赛地点在四川大学，又知道是天津航空的航班（GCR 开头），那么就查询当天从成都到杭州的飞机：

![image-20240706185623294](/Users/bruce/Library/Application Support/typora-user-images/image-20240706185623294.png)

![image-20240706191028812](/Users/bruce/Library/Application Support/typora-user-images/image-20240706191028812.png)

再查看 18:32 时这架飞机的位置：

![image-20240706190440139](/Users/bruce/Library/Application Support/typora-user-images/image-20240706190440139.png)

定位，找到了附近的江心岛：

![image-20240706190634819](/Users/bruce/Library/Application Support/typora-user-images/image-20240706190634819.png)

最终答案：

- 比赛名称：第十七届全国大学生信息安全竞赛——创新实践能力赛分区赛（华中赛区）
- 航班号：GCR6508/GS6508
- 起飞时间：2024.6.23 16:25，落地时间：2024.6.23 18:49
- 江中岛：如上图，名称为大桐洲。