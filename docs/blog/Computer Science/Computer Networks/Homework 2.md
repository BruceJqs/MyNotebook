# Homework 2

> 1. Television channels are 14 MHz wide. How many bits/sec can be sent if 256-level digital signals are used? Assume a noiseless channel.  

最大速率为 $2*14\text{MHz}*\log_{2}(256)=224\text{Mbps}$
***
> 2. If a binary signal is sent over a 12-kHz channel whose signal-to-noise ratio is 30 dB, what is the maximum achievable data rate?

最大速率为：

$$
C=B\log_{2}\left( 1+\frac{S}{N} \right)=12\text{KHz}*\log_{2}(1+10^{\frac{30\text{dB}}{10}})\approx 119.6\text{Kbps}
$$

***
> 3. 10 signals, each requiring 4000 Hz, are multiplexed on to a single channel using FDM. How much minimum bandwidth is required for the multiplexed channel? Assume that the guard bands are 100 Hz wide.

带宽为 $10*4\text{KHz}+9*100\text{Hz}=40.9\text{KHz}$
***
> 4. Suppose that A, B, and C are simultaneously transmitting 0 bits, using a CDMA system with the chip sequence of figure following:
> ![](../../../assets/Pasted%20image%2020251012144940.png)
> What is the resulting chip sequence? give your answer as (+x,-x,-x, ...)

$S=(-A)+(-B)+(-C)=(+3,+1,+1,-1,-3,-1,-1,+1)$
***
> 5. A CDMA receiver gets the following chips: (-1 +1 -3 +1 -1 -3 +1 +1). Assuming the chip sequences defined in figure following,
> ![](../../../assets/Pasted%20image%2020251012144940.png)
> (a)Which bits did station A send? (bit 1, bit 0, or silence) 
> (b)Which bits did station B send? (bit 1, bit 0, or silence)
> (c)Which bits did station C send? (bit 1, bit 0, or silence)
> (d)Which bits did station D send? (bit 1, bit 0, or silence)

(a) $S\cdot A=1-1+3+1-1+3+1+1=8\Rightarrow$ A 发送了 1

(b) $S\cdot B=1-1-3-1-1-3+1-1=-8\Rightarrow$ B 发送了 0

(c) $S\cdot C=1+1+3+1-1-3-1-1=0\Rightarrow$ C 保持静默

(d) $S\cdot D=1+1+3-1+1+3+1-1=8\Rightarrow$ D 发送了 1
***
> 6. What is the percent overhead on a T1 carrier; that is, what percent of the 1.544 Mbps are not delivered to the end user?

比例为 $\frac{1}{8*24+1}\times 100\%=0.518\%$
***
> 7. A What is the percent overhead on a E1 carrier; that is, what percent of the 2.048 Mbps are not delivered to the end user? (round to one decimal place)

比例为 $\frac{16}{32*8}\times 100\%\approx 6.3\%$
***
> 8. Why has the PCM sampling time been set at 125 µsec?

因为电话系统设计的语音信道带宽为 4kHz，根据奈奎斯特定理，采样频率必须至少是其两倍，即 8kHz。采样时间是采样频率的倒数，即 1/8000 秒，也就是 125 微秒。
***
> 9. A simple telephone system consists of two end offices and a single toll office to which each end office is connected by a 1-MHz full-duplex trunk. The average telephone is used to make four calls per 8-hour workday. The mean call duration is 6 min. Ten percent of the calls are long-distance (i.e., pass through the toll office). What is the maximum number of telephones an end office can support? (Assume 4 kHz per circuit.)

同时处理的长途电话数量为 $\frac{1\text{MHz}}{4\text{kHz}}=250$

每部电话的负载为 $\frac{4*6}{8*60}*10\%=0.005$

所以每个局可以支持的电话数量为 $\frac{250}{0.005}=50000$