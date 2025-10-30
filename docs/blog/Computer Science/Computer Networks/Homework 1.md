# Homework 1

> 1. What is the name of PDU at the network layer of the OSI reference model?
> A. message
> B. frame
> C. packet
> D. segment

C. packet. 网络层的数据传输单元（PDU）是数据包。
***
> 2. Connectionless Services is also called
> A. virtual circuit service
> B. acknowledged datagram service
> C. client-server service
> D. datagram service

D. datagram service. 无连接服务也被称为数据报服务。
***
> 3. Which of the OSI layers handlers each of the following:
> (a) Dividing the transmitted bit stream into frames.
> (b) Determining which route through the subnet to use.

(a) 数据链路层从物理层的比特流中提取出完整的帧
(b) 网络层决定选择哪个路由进行传输
***
> 4. A system has an 7-layer protocol hierarchy. Applications generate messages of length 1000 bytes. At each of the layers, an 20 byte header is added. What fraction of the network bandwidth is filled with headers? (round to one decimal place)

比例为 $\frac{7*20}{1000+7*20}=\frac{7}{57}$
***
> 5. How long was a bit on the original 802.3 standard in meters? Use a transmission speed of 10 Mbps and assume the propagation speed in coax is 2/3 the speed of light in vacuum. (round to one decimal place)

长度为 $\frac{2}{3}*3*10^8\text{m/s}*\frac{1}{10\text{Mbps}}=20\text{m/bit}$
***
> 6. A client-server system uses a satellite network, with the satellite at a height of 40000 km. What is the best-case delay in response to a request? (round to one decimal place)

最好情况下的时延为 $\frac{40000\text{km}*2}{3*10^8\text{m/s}}=\frac{4}{15}\text{s}\approx0.3\text{s}$
***
> 7. An image is 1024 x 768 pixels with 3 bytes/pixel. Assume the image is uncompressed. (round to one decimal place)
> (a) How long does it take to transmit it over a 56-kbps modem channel?
> (b) How long does it take to transmit it over a 1-Mbps cable modem?
> (c) How long does it take to transmit it over a 10-Mbps Ethernet?
> (d) How long does it take to transmit it over 100-Mbps Ethernet?

(a) 时间为 $\frac{1024*768*3*8}{56K}\approx337.0\text{s}$
(b) 时间为 $\frac{1024*768*3*8}{1M}\approx18.9\text{s}$
(c) 时间为 $1.9\text{s}$
(d) 时间为 $0.2\text{s}$
***
> 8. A collection of five routers is to be connected in a point-to-point subnet. Between each pair of routers, the designers may put a high-speed line, a medium-speed line, a low-speed line, or no line. If it takes 100ms of computer time to generate and inspect each topology, how long will it take to inspect all of them? (round to one decimal place)

时间约为 $4^{C_{5}^{2}}*100\text{ms}\approx29.1\text{h}$