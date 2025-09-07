---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
# comments: true
---  

# A00_simple_as

## 构建方法

进入文件夹 `A00_simple_as` ，查看内部文件有一个 `simple_as.py`

![](../../../../assets/Pasted%20image%2020241110135258.png)

命令行 `python3 ./simple_as.py` 构建 Dockerfile，会生成一个 `output` 文件夹，内含我们构建互联网的一个个主机/路由/...的 docker 文件（每个相当于是一个 docker 容器）：

![](../../../../assets/Pasted%20image%2020241110135856.png)

随后 `docker-compose build && docker-compose up` 即可构建完成。

![](../../../../assets/Pasted%20image%2020241113142544.png)

最终我们可以通过访问 localhost 的 8080 端口里面的 map.html 文件（即 https://localhost:8080/map.html ），可看到可视化界面：

![](../../../../assets/Pasted%20image%2020241113150602.png)
***
## 代码分析

这里将 `simple_as.py` 进行详细分析：

!!! note "Explanation"

	=== "Import"
	
		```python
		from seedemu.layers import Base, Routing, Ebgp
		from seedemu.services import WebService
		from seedemu.compiler import Docker, Platform
		from seedemu.core import Emulator, Binding, Filter
		import sys, os
		```
		
		其中 `sys, os, Platform` 是用于系统和架构识别用的，`Docker` 是用来构建互联网的硬件基础（因为每一台主机/BGP 路由/...都是一个 Docker 容器），我们重点要关注的是 `Base, Routing, Ebgp, WebService`。
	
	
	=== "Initialization"
	
		```python
		# Initialize the emulator and layers
		emu     = Emulator()
		base    = Base()
		routing = Routing()
		ebgp    = Ebgp()
		web     = WebService()
		```
		
		在这之中：
		
		- `Emulator` 是整个仿真器的大模块
		- `Base` 提供仿真基础
			- 描述每个主机属于哪个自治系统，以及主机之间是如何相互连接的
		- `Routing` 提供路由协议的基础
			- 在每个具有路由器角色的主机上安装 BIRD 互联网路由守护进程
			- 提供用于操作 BIRD 的 FIB（转发信息库）和添加新协议等的低级 API
			- 在非路由器角色主机上设置适当的默认路由，以指向网络中的第一个路由器
		- `Ebgp` 提供对外 BGP 连接的 API
		- `WebService` 提供在主机上安装 nginx web server 的 API
	
	=== "Creation"
	
		```python
		# Create an Internet Exchange
	    base.createInternetExchange(100)
		```
		
		在这里函数 `Base::createInternetExchange` 建立了一个新的数据交换中心。默认情况下，它建立了一个全局网络 10.$\{\text{id}\}$.0.0/24(其中 $\text{id}$ 为数据交换中心的 ID，随后可以通过函数 `Node::joinNetwork` 将路由加入网络。
		
		```python
	    # Create and set up AS-150
		
	    # Create an autonomous system 
	    as150 = base.createAutonomousSystem(150)
		
	    # Create a network 
	    as150.createNetwork('net0')
		
	    # Create a router and connect it to two networks
	    as150.createRouter('router0').joinNetwork('net0').joinNetwork('ix100')
		
	    # Create a host called web and connect it to a network
	    as150.createHost('web').joinNetwork('net0')
		
	    # Create a web service on virtual node, give it a name
	    # This will install the web service on this virtual node
	    web.install('web150')
		
	    # Bind the virtual node to a physical node 
	    emu.addBinding(Binding('web150', filter = Filter(nodeName = 'web', asn = 150)))
		```
		
		 - 函数 `Base::createAutonomousSystem` 返回一个自治系统的类实例，可以被用于建立主机和网络
		- 函数 `AutonomousSystem::createNetwork` 建立了一个新的本地网络，和我们在 `Base::createInternetExchange` 建立的网络不同，它只能加入自治系统当中的节点；和 `Base::createInternetExchange` 建立的网络相同的是，默认情况下它使用 10.$\text{asn}$.$\text{id}$.0/24，其中 $\text{asn}$ 为
		- 函数 `AutonomoousSystem::createRouter` 建立了一个 BGP 路由
		- 函数 `Node::joinNetwork` 指的是将一个节点连接到一个网络当中，这个网络可以是自治系统的全局网络，也可以是自治系统的本地网络，这个函数默认会先搜寻本地网络有没有可连接的
		- 函数 `AutonomousSystem::createHost` 将会返回一个主机节点实例，在这个例子里面我们将其命名为 `Web` 因为我们将会在其上面建立 Web 服务
		- 函数 `web.install` 将会建立一个虚拟的节点（在这个例子当中为 `web150`），在这个虚拟节点上面配置 Web 服务
		- 函数 `emu.addBinding` 将我们建立的虚拟节点绑定到真实的节点上面（在这个例子当中为 `web`）
		
		??? question "为什么要建立一个虚拟节点?"
		
			或许有人会问，为什么要多此一举建立这个虚拟的节点，再去绑定，这是因为虚拟的节点可以看作是真实节点的模板（或者叫蓝图），一来是能复用这个模板更加方便，二来所有的改动都是在模板上进行改动，也比较方便。
	
	=== "BGP Peering"
	
		```python
		# Peering these ASes at Internet Exchange IX-100
		
		ebgp.addRsPeer(100, 150)
		ebgp.addRsPeer(100, 151)
		ebgp.addRsPeer(100, 152)
		```
		
		函数 `ebgp.addRsPeer` 通过建立的数据交换中心建立不同 BGP 路由之间的联系，能让不同的自治系统能相互连接传递数据。
	
	=== "Rendering"
	
		```python
		# Rendering 
		
	    emu.addLayer(base)
	    emu.addLayer(routing)
	    emu.addLayer(ebgp)
	    emu.addLayer(web)
		
	    if dumpfile is not None:
	        emu.dump(dumpfile)
	    else:
	        emu.render()
		```
		
		这段代码就实现了将所有的功能下放到各节点当中（软件会被安装到节点上，路由表、协议和 BGP 连接会被配置……）
	
	=== "Compilation"
	
		```python
		# Compilation
        emu.compile(Docker(platform=platform), './output', override=True)
		```
		
		这段代码就将所有的文件通过 docker 编译器编译成 Docker 文件，并放入 output 目录当中。

***
## 功能展示

这是一个最简单最小型的互联网仿真，有三套自治系统【每套自治系统掩码位为 24 位，内含一台 BGP 路由（圆形表示），连接一个构建网络的 Network（菱形表示），每个 Network 上连接一台主机（分别为 10.150/151/152.0.71.24，正六边形表示，在真实情况下可能连接非常多的主机）】、一个数据交换中心（五角星表示，负责和 BGP 路由进行数据交换）和控制数据交换中心的主机（100/ix100，正六边形表示）。

当我们想从 10.152.0.71 传输数据到 10.150.0.71，我们只需要在 10.152.0.71 的终端（点击 Launch Console）命令行 `ping 10.150.0.71` 即可，同时在最上面输入 `icmp`（显示 `icmp` 包的流向），那么网页便会通过闪烁的方式来展示整个数据传输的路径（从当前主机走出自治系统，来到数据交换中心，经过数据交换中心处理之后送到对方的自治系统进入对方主机），如下图所示：

![](../../../../assets/Pasted%20image%2020241113153326.png)