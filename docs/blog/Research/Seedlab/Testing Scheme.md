# 国内测试方案

## Docker 换源

### 方法一

涉及全部 Examples，需要在<font color="red">运行 VM</font> 中换源，步骤如下：

- 切换目录 `cd /etc/docker/`
- 编辑守护进程文件 `sudo vim daemon.json` 复制粘贴以下内容：
	
	```json
	{
	  "registry-mirrors": [
	          "https://docker.13140521.xyz",
	          "https://docker.mirrors.ustc.edu.cn",
	          "https://docker.lpanel.live",
	          "https://docker.anyhub.us.kg",
	          "https://dockerhub.icu",
	          "https://docker.1panel.live",
	          "https://kfwkfulq.mirror.aliyuncs.com",
	          "https://2lqq34jg.mirror.aliyuncs.com",
	          "https://pee6w651.mirror.aliyuncs.com",
	          "https://registry.docker-cn.com",
	          "https://hub-mirror.c.163.com",
	          "https://hub.rat.dev",
	          "https://yxzrazem.mirror.aliyuncs.com"
	  ]
	}
	```

### 方法二（可以作为备用方案）

预先使用 `docker save -o base.tar handsonsecurity/seedemu-multiarch-router:buildx-latest` 把所有镜像都保存到项目当中，用户就可以通过 `docker load -i base.tar` 把镜像拖到本地 Docker 中
***
## APT 问题

换源，通过更改 Dockerfile：

![](../../../../Pasted%20image%2020250213204819.png)

test 内容为新 apt 源配置，红框已测试可以将 apt 源替换，在代码中的部分为：

![](../../../../Pasted%20image%2020250213211112.png)

两红箭头处均可插入（应该？阅读代码不是很仔细不知道有没有条件限制）

- 值得一提的是，任何需要换源的情况都可以通过这个方法解决
***
## Ubuntu 版本兼容性更新

- 22.04 目前测试没有任何问题
- 24.04 配置问题
	- pip 安装
		
		![](../../../assets/Pasted%20image%2020250228134304.png)
		
		- 原因：Manjaro 22、Ubuntu 23+.04、Fedora 38 以及其他的最新发行版中，正在使用 Python 包来实现此增强功能。这个更新是为了避免操作系统包管理器（如 pacman、yum、apt）和 pip 等特定于 Python 的包管理工具之间的冲突，这些冲突包括 Python 级 API 不兼容和文件所有权冲突。
		- 目前采用方案：强行去掉这个提示 `sudo mv /usr/lib/python3.12/EXTERNALLY-MANAGED /usr/lib/python3.12/EXTERNALLY-MANAGED.bk`
	- python 版本问题
		- 24.04 默认安装 python3.12，对于仿真器的许多 example 有问题
		- 解决方案：install.sh 修改重装 python（3.8？3.10？）

## GETH 安装

已知最新版本 v1.15.3，大概是改 git checkout，未测试（不知道怎么改）

![](../../../assets/Pasted%20image%2020250228150627.png)

