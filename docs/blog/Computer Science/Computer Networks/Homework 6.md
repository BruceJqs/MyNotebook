# Homework 6

> 1. If the TCP round-trip time, RTT, is currently 30 msec and the following acknowledgements come in after 26,32, and 24 msec, respectively, what is the new RTT estimate using the Jacobson algorithm? Use alpha =0.9.

收到第一个 ACK 包：$\text{SRTT}=0.9*30+0.1*26=29.6$

收到第二个 ACK 包：$\text{SRTT}=0.9*29.6+0.1*32=29.84$

收到第三个 ACK 包：$\text{SRTT}=0.9*29.84+0.1*24=29.256$

最终的 RTT 估计值为 29.256

***

> 2. Consider the effect of using slow start on a line with a 10-msec round-trip time and no congestion. The receive window is 24 KB and the maximum segment size is 2 KB. How long does it take before the first full window can be sent?

一个满窗口一共包含 $24/2=12$ 个段，当 $T=4*\text{RTT}$ 时，拥塞窗口大小超过了接收窗口大小，因此需要时间为 40ms 

***

> 3. In TCP Tahoe suppose that the TCP congestion window is set to 128 KB and a timeout occurs. How big will the window be if the next 10 transmission bursts are all successful? Assume that the maximum segment size is 1 KB.

$\text{ssthresh}=128\text{KB}/2=64\text{KB}$

$\text{cwnd}$ 在第六次达到 $\text{ssthresh}$，第 7,8,9,10 次线性增加，因此最后的窗口大小为 $64\text{KB}+4\text{KB}=68\text{KB}$

***

> 4. Suppose that the TCP congestion window is set to 18 KB and a timeout occurs. How big will the window be if the next four transmission bursts are all successful? Assume that the maximum segment size is 1 KB.

$\text{ssthresh}=18\text{KB}/2=9\text{KB}$

$\text{cwnd}$ 在第四次达到 $\text{ssthresh}$，最后窗口大小为 16KB

***

> 5. A TCP machine is sending full windows of 65,535 bytes over a 1-Gbps channel that has a 10-msec one-way delay. What is the maximum throughput achievable? What is the line efficiency? (give your answer as xx.x)
>    - maximum throughput: 
>    - line efficiency: 

最大吞吐量为 $65535\text{Bytes}/0.02s=3276750\text{Bytes/s}=26.214\text{Mbps}$

线路效率为 $26.214\text{Mbps}/1\text{Gbps}=2.6\%$

***

> 6. In a network that has a maximum TPDU size of 128 bytes, a maximum TPDU lifetime of 30 sec, and an 8-bit sequence number, what is the maximum data rate per connection?

最大数据速率为 $\frac{2^8*128\text{Bytes}}{30s}=1092.3\text{Bytes/s}$

***

> 7. The maximum payload of a TCP segment is 65,495 bytes. Why was such a strange number chosen?

这个数字是因为 IP 数据报和 TCP 段的头部结构：

1. IP 数据报总长度字段：IP 协议头部的总长度字段是 16 位的，它表示整个 IP 数据报（包括 IP 头部和数据部分）的最大长度。因此，一个 IP 数据报最大可以是 $2^{16} - 1 = 65,535$ Bytes
2. 最小的 IP 头部：一个标准的 IP 头部（无选项）是 20 Bytes
3. 最小的 TCP 头部：一个标准的 TCP 头部（无选项）是 20 Bytes

TCP 段被封装在 IP 数据报的数据部分。因此我们需要从 IP 数据报的最大长度中减去 IP 头部和 TCP 头部的最小长度，因此最后的最大有效载荷为 $65535-20-20=65495\text{Bytes}$

***

> 8. If the window size field of the acknowledgement TCP segment is 100 KB, and the congestion window size is 50 KB, how many bytes could the sender transmit next time?

可以发送 50 字节

***

> 9. What is used at the transport layer to stop a receiving host's buffer from overflowing?
>
> A. Segmentation
>
> B. Packets
>
> C. Acknowledgments
>
> D. Flow control

D. Flow control

***

> 10. Which type of service is provided by TCP?
>
> A. request-reply
>
> B. acknowledged datagram 
>
> C. reliable message stream 
>
> D. reliable byte stream

D. reliable byte stream

