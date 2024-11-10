---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
---  

# Seedlab

## Introduction

### Sources

[Link](https://seedsecuritylabs.org)

[Github](https://github.com/seed-labs/seed-emulator/)
***
### Requirement

- Docker
- Docker-Compose
- Python3
***
## Lab0-simple_as

进入文件夹 `A00_simple_as` ，查看内部文件有一个 `simple_as.py`

![](../../../assets/Pasted%20image%2020241110135258.png)

命令行 `python3 ./simple_as.py` 构建 Dockerfile，会生成一个 `output` 文件夹：

![](../../../assets/Pasted%20image%2020241110135856.png)

随后 `docker-compose build && docker-compose up` 即可构建完成。

