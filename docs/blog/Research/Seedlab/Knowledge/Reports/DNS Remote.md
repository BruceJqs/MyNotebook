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
	






