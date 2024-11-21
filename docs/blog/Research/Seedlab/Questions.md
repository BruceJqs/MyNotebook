---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
---  

# 配置问题及解决办法

## Urllib3 包版本过老

- 当进行配置试验时，运行 Python 文件会出现报错：`ModuleNotFoundError: No module named 'urllib3.packages.six.moves'`

这是因为 requirement.txt 当中设定的 urllib3 包可能有些老了，升级一下 `pip install --upgrade urllib3` 即可
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