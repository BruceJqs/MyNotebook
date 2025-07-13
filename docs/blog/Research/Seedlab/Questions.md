---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
---  

# 各类问题及解决办法

## 部署问题

### Windows

对于 Windows 用户，按照 [Github](https://github.com/seed-labs/seed-labs/blob/master/manuals/vm/seedvm-manual.md) 中的建立 Virtualbox 即可，需要注意的是，这里提供的 Ubuntu 是有 Python3.8 的，为了后续管理方便&可能遇到的奇怪错误建议下一个 conda 建立 Python3.12 虚拟环境来运行。
***
### Mac

对于 Mac 用户可就闹腾了，需要首先有一个 Ubuntu 系统，来源可以有以下几个：

- Parallel Desktop/VMware Fusion 虚拟机（这个是最方便的，同时具有 UI 界面），VMware Fusion 详见 [Bruce 写的教程](https://github.com/seed-labs/seed-labs/tree/master/lab-setup/apple-arm/seedvm-fusion-v2)
- 服务器（需要建立 UI 界面，根据 [Github](https://github.com/seed-labs/seed-labs/blob/master/manuals/cloud/seedvm-cloud.md) 的指导下载 VNCServer 即可，但是对于 Ubuntu20.04 来说这个教程是没有问题的；对于 Ubuntu22.04 来说会出现在 seed 账户下命令行 `vncserver -localhost no` 执行报错【No Display】情况，这大概是因为 22.04 的普通账户没有 Screen 的权限，一种方法是找到 Screen 赋予权限【待试验】，另一种是在 root 下开启 vncserver（这个非常危险）

随后在 Ubuntu 当中进行相应配置即可。
***
## Urllib3 包版本过老

当进行配置试验时，运行 Python 文件会出现报错：`ModuleNotFoundError: No module named 'urllib3.packages.six.moves'`

- 这是因为 requirement.txt 当中设定的 urllib3 包可能有些老了，升级一下 `pip install --upgrade urllib3` 即可
***
## Docker 换源问题

杜老师的项目是在国外开发的，所以 Docker 源默认用官方源是没有问题的，但是要在国内普及还是使用镜像源比较好，不然很容易出现 pull 不了 docker image 的情况，Bruce 的 daemon.json 配置供参考：

```json
{
  "registry-mirrors": [
		  "https://docker.1ms.run",
          "https://docker.anyhub.us.kg",
          "https://dockerhub.icu",
          "https://docker.1panel.live"
  ]
}
```
***
## Docker Compose 版本问题

当运行 `docker-compose up` 时，可能会出现以下情况：

![](../../../assets/Pasted%20image%2020241124173115.png)

这是因为对老版本 docker-compose（Ubuntu20.04 之前），V1 语法 docker-compose 仍然适用，但是到新版本 docker-compose（Ubuntu 22.04 之后）时，转换成 V2 语法 docker compose，因此把命令行变更为 `docker compose up` 即可。
***
## 清理“缓存” docker 问题

举例来说，当我们运行完 B00_mini_internet 这个 lab 之后，再重新运行 A00_simple_as 这个 lab，在可视化（即 http://localhost:8080/map.html ）中会出现下面的情况：

![](../../../assets/Pasted%20image%2020241124175022.png)

可以看到 B00 建立的东西还是存在，而 A00 则是把 B00 建立和其重复的部分又重新拼了起来，那么为了观察方便我们就应该在运行完 B00 之后清理掉这些类似“缓存”的东西

请谨记：我们应当<font color="red">在上一个 lab 的 output 目录当中</font>使用命令行 `docker-compose down`（因为 docker-compose 需要通过 output 当中的 docker-compose.yml 文件来进行清理）将上一个 lab 建立的所有 docker 及其 network 清理干净，再去运行下一个 lab 的相关程序。
***
## B00_mini_internet 网段冲突

B00_mini_internet 实验在 VM 当中运行到 `docker-compose up` 时会发生如下错误：

![](../../../assets/Pasted%20image%2020241124170509.png)

发生这样的情况的原因在于我们创建的 networks 手动指定了 subnet 网段地址，而该网段地址已经存在，因此产生了冲突，我们可以通过命令行 `docker system prune -a` 和 `docker network prune` 清除未被使用的网络（或者跟上面一样，直接运行 `docker-compose down` 即可）。再次运行 `docker-compose up` 即可。
***


