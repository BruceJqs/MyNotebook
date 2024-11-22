---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
---  

# 配置问题及解决办法

## 部署问题

### Windows

对于 Windows 用户，按照 [Github](https://github.com/seed-labs/seed-labs/blob/master/manuals/vm/seedvm-manual.md) 中的建立 Virtualbox 即可，需要注意的是，这里提供的 Ubuntu 是有 Python3.8 的，为了后续管理方便&可能遇到的奇怪错误建议下一个 conda 建立 Python3.12 虚拟环境来运行。
***
### Mac

对于 Mac 用户可就闹腾了，需要首先有一个 Ubuntu 系统，来源可以有以下几个：

- Parallel/VMware Fusion 虚拟机（这个是最方便的，同时具有 UI 界面）
- 服务器（需要建立 UI 界面，根据 [Github](https://github.com/seed-labs/seed-labs/blob/master/manuals/cloud/seedvm-cloud.md) 的指导下载 VNCServer 即可，但是对于 Ubuntu20.04 来说这个教程是没有问题的；对于 Ubuntu22.04 来说会出现在 seed 账户下命令行 `vncserver -localhost no` 执行报错【No Display】情况，这大概是因为 22.04 的普通账户没有 Screen 的权限，一种方法是找到 Screen 赋予权限【待试验】；另一种是在 root 下启动 vncserver，然后转移至 seed 账户当中【也还没试验过】）
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
***
## 在服务器上安装 TexStudio

