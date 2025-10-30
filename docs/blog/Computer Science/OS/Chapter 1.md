# Chapter 1: Operating-System Structures

## Operating System Services

一组操作系统服务为用户提供了有用的功能：

- 用户界面——几乎所有操作系统都有用户界面（UI）
    - 用户界面可以是命令行界面（CLI）、图形用户界面（GUI）或批处理
- 程序执行——系统必须能够将程序加载到内存中并运行该程序，并能结束程序的执行（正常或异常，异常时提示错误）
- 输入/输出操作——正在运行的程序可能需要输入/输出操作（I/O），这可能涉及一个文件或输入/输出设备
- 文件系统操作——文件系统是特别重要的。例如，程序需要读写文件和目录，创建或删除它们，搜索和列出文件信息，管理权限等
- 通信——进程可以在同一台计算机上或通过网络在不同计算机之间交换信息
    - 通信可以通过共享内存或消息传递（由操作系统传递的数据包）实现
- 错误检测——操作系统需要时刻警觉可能出现的错误
    - 错误可能出现在 CPU 和内存硬件、I/O 设备或用户程序中
    - 针对每种类型的错误，操作系统应采取适当的措施，以确保计算的正确性和一致性
    - 调试功能可以极大提升用户和程序员高效使用系统的能力
***
## User Operating System Interface

### CLI

命令行界面（CLI，Command Line Interface）允许用户直接输入命令。

- 有时 CLI 是在内核中实现的，有时则由系统程序实现
- 有时会实现多种类型的 CLI —— shell
- 主要作用是从用户那里获取命令并执行
    - 有些命令是内置的（例如 DOS），有些只是程序的名字（例如 Unix）
        - 如果是后者，添加新功能不需要修改 shell
***
### GUI

- 用户友好的桌面界面
    - 通常使用鼠标、键盘和显示器
    - 图标代表文件、程序、操作等
    - 在界面中的对象上使用不同的鼠标按钮可以触发各种操作（提供信息、选项、执行功能、打开目录，目录通常称为文件夹）
- 许多系统现在同时包含CLI和GUI界面
    - 微软 Windows 是图形界面（GUI），同时带有命令行（CLI）“命令” shell
    - 苹果 Mac OS X 带有“Aqua”图形界面，底层是 UNIX 内核，并且有 shell 可用
    - Solaris 是命令行界面（CLI），可选用 Java Desktop、KDE 等图形界面（GUI）
***
## System Calls

- 操作系统提供的服务的编程接口
- 通常用高级语言（如 C 或 C++）编写
- 程序通常通过高级应用程序接口（API）访问这些服务，而不是直接使用系统调用
- 三大主流 API：Windows 的 Win32 API，POSIX 系统（包括几乎所有 UNIX、Linux 和 Mac OS X 版本）的 POSIX API，以及 Java 虚拟机（JVM）的 Java API

!!! note "常见的函数调用"

	=== "头文件"
	
		在头文件中，系统调用的形式如下：
		
		```c
		#include <sys/socket.h>
		int socket(int socket_family, int socket_type, int protocol);
		int bind(int sockfd, const struct sockaddr *addr, socklen_t addrlen);
		int accept(int sockfd, struct sockaddr *addr, socklen_t *addrlen);
		int connect(int sockfd, const struct sockaddr *addr, socklen_t addrlen);
		```
	
	=== "层级模型"
	
		在层级模型中，系统调用形式如下图：
		
		![](../../../assets/Pasted%20image%2020250929160439.png)
***
### System Call Implementation

- 通常，每个系统调用都会关联一个数字
    - 系统调用接口会维护一个以这些数字为索引的表（table）
- 系统调用接口会调用操作系统内核中指定的系统调用，并返回系统调用的状态及任何返回值
- 调用者无需了解系统调用是如何实现的
    - 只需要遵守 API，并理解操作系统会根据调用做出什么反应
    - 操作系统接口的大部分细节对于程序员来说通过 API 都是隐藏的
        - 由运行时支持库进行管理（这些函数集成在随编译器一起提供的库中）

使用系统调用的 API 示意图如下：

![](../../../assets/Pasted%20image%2020250929162238.png)

使用 C 语言函数 `printf`，进而调用系统函数 `write` 的示意图如下：

![](../../../assets/Pasted%20image%2020250929163126.png)
***
### System Call Parameter Passing

- 通常，仅仅知道所需的系统调用身份是不够的，还需要更多的信息
    - 具体的信息类型和数量会根据操作系统和具体调用而变化
- 向操作系统传递参数有三种常见方法：
    - 最简单的方式：将参数通过寄存器（Registers）传递
        - 在某些情况下，参数的数量可能超过寄存器数量
    - 参数存放于内存中的块（Block）或表中，通过寄存器传递块的地址作为参数
        - Linux 和 Solaris 采用了这种方法
    - 程序将参数推送（Push）到栈（Stack）上，操作系统通过弹出（Pop）栈来获取参数
	- 块（Block）和栈（Stack）方法不会限制所传参数的数量或长度

![](../../../assets/Pasted%20image%2020250929164136.png)
***
## Type of System Calls

系统调用主要分为五种类型：

- 进程控制（Process Control）
- 文件管理（File Management）
- 设备管理（Device Management）
- 信息维护（Information Maintenance），例如日期、时间等
- 通信（Communication）

