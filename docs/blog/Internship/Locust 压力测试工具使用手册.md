# Locust 压力测试工具使用手册

**<font size=5>目录</font>**

[TOC]

<div style="page-break-after:always;"></div>

## 工具相关信息

Locust 完全基于 Python 编程语言，采用 Python 编写压测脚本，且所有请求完全基于 requests 库。除了 HTTP/HTTPS 协议，Locust 也可以测试其它协议的系统，只需要采用 Python 调用对应的库进行请求描述即可。Locust 是一个分布式用户性能测试的工具但是单台压力机也能产生数千并发请求数。

### 安装部署

命令行 `pip3 install locust` 即可。

## 工具使用方法

### 例一：获取手机验证码（单一任务）

编写 python 脚本 test1.py 如下：

```python
from locust import HttpUser, between, task

class WebsiteUser(HttpUser):
    wait_time = between(5, 15)
    
    @task
    def test1(self):
        post_url = "/platform/mbvercode/get"
        headers = {
            "Content-Type": "application/json"
        }
        data = {
            "MBPhone": "18657100000"
        }
        self.client.post(post_url, json = data, headers = headers, verify = False)
```

然后在 test1.py 目录下运行命令行：`locust -f test1.py --host=https://posdemo3.hzgolong.com:13443`

可以看到如下提示：

![image-20240828160133224](/Users/bruce/Library/Application Support/typora-user-images/image-20240828160133224.png)

浏览器访问 https://localhost:8089 即可进入界面：

![image-20240828160207269](/Users/bruce/Library/Application Support/typora-user-images/image-20240828160207269.png)

其中设置 Number of users（即最大用户量）和 Ramp up（每过一段时间用户的增加量），START 即可进行压力测试。

![image-20240828160554053](/Users/bruce/Library/Application Support/typora-user-images/image-20240828160554053.png)

### 例二：多线程任务与比例分配

编写 python 脚本如下：

```python
from locust import HttpUser, between, task

Phone_Success = "13500000036"
Password_Right = "12345678"

class WebsiteUser(HttpUser):
    wait_time = between(5, 15)
    
    @task(10)
    def test1(self):
        post_url = "/platform/mbvercode/get"
        headers = {
            "Content-Type": "application/json"
        }
        data = {
            "MBPhone": "18657100000"
        }
        self.client.post(post_url, json = data, headers = headers, verify = False)

    @task(3)
    def test2(self):
        post_url = "/platform/userlogin/put"
        headers = {
            "Content-Type": "application/json"
        }
        data = {
            "UserId": Phone_Success,
            "Password": Password_Right
        }
        self.client.post(post_url, json = data, headers = headers, verify = False)
    
    @task(5)
    def test3(self):
        post_url = "/platform/mbphonelogin/put"
        headers = {
            "Content-Type": "application/json"
        }
        data = {
            "MBPhone": Phone_Success,
            "VerifyCode": "1234"
        }
        self.client.post(post_url, json = data, headers = headers, verify = False)
```

其中 `@task` 后的数字表示执行请求的权重，权重越大请求数量越多。

![image-20240828163439109](/Users/bruce/Library/Application Support/typora-user-images/image-20240828163439109.png)

