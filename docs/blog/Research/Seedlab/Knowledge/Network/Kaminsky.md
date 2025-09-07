---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
# comments: true
---  

# Kaminsky DNS Attack

!!! abstract "Abstract"

	DNS（Domain Name System）是互联网的核心协议之一，它将域名转换为 IP 地址。Kaminsky DNS Attack 是一种针对 DNS 的攻击，将用户误导至攻击者提供的 IP 地址 （该 IP 往往是恶意的）

## DNS 原理

- DNS 是一种分布式的数据库系统，负责将域名解析为 IP 地址
- 当用户用 `dig` 命令查询域名的 IP 地址时，或者在浏览器当中输入该域名时，用户主机会向本地 DNS 服务器发送 DNS 查询请求，DNS 服务器最终从域名服务器中获得 IP 地址
***
## Kaminsky 攻击原理

Kaminsky 攻击的目标是对本地 DNS 服务器进行 DNS 缓存投毒攻击，使得当用户运行 dig 命令来查找IP 地址时，本地 DNS 服务器会从攻击者的域名服务器获得 IP 地址，因此返回的 IP 地址是攻击者提供的，导致的结果是用户会被导向攻击者的恶意站点。

!!! example "Example"

	攻击者向受害 DNS 服务器（Apollo）发送 DNS 查询请求，从而触发来自 Apollo 的 DNS 查询。DNS 查询首先前往其中一个根 DNS 服务器，接着是 .COM 的 DNS 服务器，最终从 example.com 的 DNS 服务器得到查询结果，查询过程如下图所示：
	
	![](../../../../../assets/Pasted%20image%2020250404210557.png)
	
	如果 example.com 的域名服务器信息已经被 Apollo 缓存，那么查询不会前往根服务器或 .COM DNS 服务器，这个过程如下图所示：
	
	![](../../../../../assets/Pasted%20image%2020250404210921.png)
	
	当 Apollo 等待来自 example.com 域名服务器的 DNS 答复时，攻击者可以发送伪造的答复给 Apollo，假装这个答复是来自 example.com 的域名服务器。如果伪造的答复先到达而且有效，那么它将被 Apollo 接收，攻击成功。

事实上，在现实情况下攻击者与 DNS 服务器是不会在一个局域网下的，这样会使得缓存投毒攻击变得比较困难，因为 DNS 响应中的 Transcation ID 必须与查询请求中的相匹配。由于查询中的 ID 通常是随机生成的，在看不到请求包的情况下，攻击者很难猜到正确的 ID。

当然，攻击者可以猜测 Transcation ID。由于这个 ID 只有 16 个比特大小，如果攻击者可以在攻击窗口内伪造 K 个响应（即在合法响应到达之前），那么攻击成功的可能性就是 $\frac{K}{2^{16}}$。发送数百个伪造响应并不是不切实际的，因此攻击成功是比较容易的。

然而，上述假设的攻击忽略了 DNS 缓存。在现实中，如果攻击者没有在合法的响应到达之前猜中正确的 Transcation ID，那么 DNS 服务器会将正确的信息缓存一段时间。这种缓存效果使攻击者无法继续伪造针对该域名的响应，因为 DNS 服务器在缓存超时之前不会针对该域名发出另一个 DNS 查询请求。为了继续对同一个域名的响应做伪造，攻击者必须等待针对该域名的另一个 DNS 查询请求，这 意味着他必须要等到缓存超时，而等待时间会长达几小时甚至是几天。
***
## Kaminsky 攻击

对于 DNS 缓存的问题，Dan Kaminsky 提出了一个巧妙的方法来解决，通过这样的方案，攻击者可以持续地发起欺骗攻击，不需要等待，因此攻击可以在很短的一段时间内成功。继续上面的例子攻击过程如下：

1. 攻击者向 DNS 服务器 Apollo 查询 example.com 域中一个不存在的主机名，如 twysw.example.com， 其中 twysw 是一个随机的名字
2. 由于 Apollo 的 DNS 缓存中不会有这个主机名，Apollo 会向 example.com 域的域名服务器发送一个 DNS 查询请求
3. 当 Apollo 等待答复时，攻击者向 Apollo 发送大量的伪造的 DNS 响应，每个响应尝试一个不同的 Transaction ID（期望其中一个是正确的）。在响应中，攻击者不仅提供 twysw.example.com 的 IP 地址，还提供了一条 “权威授权服务器” 记录，指明 ns.attacker32.com 是 example.com 域的域名服务器。如果伪造的响应比实际响应到达的早，且 Transaction ID 与请求中的 ID 一样， Apollo 就会接受并缓存伪造的答案。这样 Apollo 的 DNS 缓存就被投毒成功了
4. 即使伪造的 DNS 响应失败了（例如，Transaction ID 不匹配或到达的太晚了），也没有关系，因 为下一次攻击者会查询另一个主机名，所以 Apollo 会发送另一个 DNS 请求，从而给攻击者提供了另一个伪造的机会。这种方法有效地克服了 DNS 缓存效果
5. 如果攻击成功，那么在 Apollo 的 DNS 缓存中，example.com 域的域名服务器会被攻击者替换成 ns.attacker32.com

