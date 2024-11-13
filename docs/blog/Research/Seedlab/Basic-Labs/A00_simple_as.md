---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
---  

# A00_simple_as

## 构建方法

进入文件夹 `A00_simple_as` ，查看内部文件有一个 `simple_as.py`

![](../../../../assets/Pasted%20image%2020241110135258.png)

命令行 `python3 ./simple_as.py` 构建 Dockerfile，会生成一个 `output` 文件夹：

![](../../../../assets/Pasted%20image%2020241110135856.png)

随后 `docker-compose build && docker-compose up` 即可构建完成。

![](../../../../assets/Pasted%20image%2020241113142544.png)

最终我们可以通过访问 localhost 的 8080 端口里面的 map.html 文件（即https://localhost:8080/map.html），可看到可视化界面：

![](../../../../assets/Pasted%20image%2020241113150602.png)
***
## 功能展示

这是一个最简单最小型的互联网仿真，有三套自治系统【每套自治系统内含一台 BGP 路由（圆形表示）、一个构建网络的 Network（菱形表示）以及一台主机（分别为 10.150/151/152.0.71，正六边形表示）】、一个数据交换中心（五角星表示）和控制数据交换中心的主机（100/ix100，正六边形表示）

当我们想从 10.152.0.71 传输数据到 10.150.0.71，我们只需要在 10.152.0.71 的终端（点击 Launch Console）命令行 `ping 10.150.0.71` 即可，同时在最上面输入 `icmp`（显示 `icmp` 包的流向），那么网页便会通过闪烁的方式来展示整个数据传输的路径（从当前主机走出自治系统，来到数据交换中心，经过数据交换中心处理之后送到对方的自治系统进入对方主机），如下图所示：

![](../../../../assets/Pasted%20image%2020241113153326.png)