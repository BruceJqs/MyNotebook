# Homework 3

> 1. A bit string, 0111101111101111110, needs to be transmitted at the data link layer. What is the string actually transmitted after bit stuffing?

经过比特填充后的字符串为 011110111110011111010
***
> 2. What is the remainder obtained by dividing $x^7+x^5+1$ by the generator polynomial $x^3+1$?

$x^7+x^5+1$ 转换为二进制为 10100001，$x^3+1$ 转换为二进制为 1001

两者相除得到余数为 111，则最后的 remainder 为 $x^2+x+1$
***
> 3. Data link protocols almost always put the CRC in a trailer rather than in a header. Why?

将 CRC 放在帧尾允许设备在发送数据的同时进行 CRC 计算，减少了处理延迟，还避免了对数据的二次处理，降低了对缓冲存储器的需求，使得硬件实现更为简单和高效。
***
> 4. A 100-km-long cable runs at the T1 data rate. The propagation speed in the cable is 2/3 the speed of light in vacuum. How many bits fit in the cable?

比特数为 $1.544\times 10^6\text{bits/s}\times \frac{10^5\text{m}}{\frac{2}{3}\times 3\times 10^8\text{m/s}}=772\text{bits}$
***
> 5. Consider an error-free 64-kbps satellite channel used to send 512-byte data frames in one direction, with very short acknowledgements coming back the other way. What is the maximum throughput for window sizes of 1, 7, 15, 127? The earth-satellite propagation time is 270 msec. (give your answer as an integer)

发送一个帧的时间为 $\frac{512*8\text{bits}}{64\times 10^3\text{bps}}=64\text{ms}$

往返时延为 $2*270\text{ms}=540\text{ms}$

总周期为 $64\text{ms}+540\text{ms}=604\text{ms}$，因此窗口达到 $\lfloor \frac{604\text{ms}}{64\text{ms}} \rfloor=9$ 时，窗口饱和

- 窗口大小为 1 时，吞吐量为 $\frac{1*4096\text{bits}}{0.604\text{ms}}=6781\text{bits/s}$
- 窗口大小为 7 时，吞吐量为 $\frac{7*4096\text{bits}}{0.604\text{ms}}=47470\text{bits/s}$
- 窗口大小为 15 时，吞吐量为 $64\text{Kbps}$
- 窗口大小为 127 时，吞吐量为 $64\text{Kbps}$
***
> 6. A channel has a bit rate of 4 kbps and a propagation delay of 20 msec. For what range of frame sizes does stop-and-wait give an efficiency of at least 50 percent?

$\eta=\frac{t_{tx}}{t_{tx}+2\times t_{prop}}\geq 0.5$，由 $t_{prop}=20\text{ms}$ 解得 $t_{tx}\geq 40\text{ms}$

因此帧大小 $L\geq 4\text{kbps}\times 40\text{ms}=160\text{bits}$
***
> 7. Alice and Bob agrees to use Hamming codes to encode message which has 7 data bits and 4 check bits with even parity sums. Now Bob receives a message: 
> 	                        0 0 1 0 0 1 0 1 0 0 1
>    Bits are numbered from left to right, starting with 1. please help Bob to check the message.
>    Does it has error? If has, which bit is error?

校验位为第 1、2、4、8 位，检查位 1：第 1、3、5、7、9、11 位之和为 0（正确）

检查位 2：第 2、3、6、7、10、11 位之和为 1（错误）

检查位 4：第 4、5、6、7 位之和为 1（错误）

检查位 8：第 8、9、10、11 位之和为 0（正确）

有错误，错误的位置为 $2+4=6$，即第 6 位有错误
