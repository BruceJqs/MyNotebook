# 国内测试方案

## Docker 换源

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

## APT 问题

## npm 问题

## Github 问题