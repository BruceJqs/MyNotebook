---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
# comments: true
---  

# Set UID

## The Set-UID Mechanism

在 Linux 当中，Set-UID 是一种特殊的权限机制，它允许用户以文件所有者的身份执行文件。这样，即使普通用户执行该文件，也能获得文件所有者的权限。

通常，在 Linux 当中，当我们运行一个程序时，操作系统会建立一个新的进程，程序将会在这个进程当中运行，每个进程都有自己的用户 ID（UID），即运行这个程序的用户 ID，当程序想要获取文件或者是一些资源时，操作系统会检查当前进程的 UID 是否有权限访问这些资源，如果有权限，则允许访问，否则拒绝访问（这时候我们就用到了 Access Control List，ACL）

但是当我们要运行一个 Set-UID 的程序，我们仍然会建立一个进程，但是这个进程有两个用户 ID，一个被称为 Real User ID，即运行程序的用户 ID；另一个被称为 Effective User ID，即程序所有者的用户 ID。操作系统在检查权限的时候，会使用 Effective User ID 来检查是否有权限访问资源。在大多数情况下，Effective User ID 通常为 root，这样即使普通用户执行这个程序，也能获得 root 的权限

!!! note "Turn a Program Into a Set-UID Program"

	对于每一个程序，其附带了一个特殊的位（Set-UID 位），当操作系统运行该程序时，它会通过这个位来识别当前程序是否为一个 Set-UID 程序
	
	事实上，对于一个文件，它不仅仅包含 owner, group, other 所各自带的 3 个位来分别表示读取权限、写入权限和执行权限，还在这三个之前还有三个特殊的位，这其中第一个就为 Set-UID 位，第二个为 Set-GID 位，Set-GID 和 Set-UID 是类似的
	
	![](../../../../../assets/Pasted%20image%2020250702214159.png)
	
	要将一个程序设置为 Set-UID 程序，我们可以使用 `chmod` 命令，命令格式如下：
	
	```
	chmod 4755 <filename>
	```
	
	这样就会将该文件的 Set-UID 位设置为 1，同时将 owner 的权限设置为 7（即 rwx），group 和 other 的权限设置为 5（即 r-x）
	
	![](../../../../../assets/Pasted%20image%2020250702214605.png)

!!! question "Question"

	如果 Bob 给你一个机会使用他的 Unix 账户，而且你在同样的系统里面有你自己的账户，如何在 10 秒内获取接管 Bob 的账户？
	
	正确的做法是，我们先在 Bob 的电脑上将他的 shell 程序拷贝到 `/tmp` 当中（每个用户都能访问 `/tmp` 目录），此时这个 shell 程序的所有者为 Bob，然后将这个 shell 程序设置为 Set-UID 程序，这样当我们执行这个 shell 程序时，就能以 Bob 的身份执行命令了
	
	```bash
	cp /bin/sh /tmp/mysh
	chmod 4755 /tmp/mysh
	```
***
## Attacks via Environment Variables

### Environment Variables

环境变量是操作系统用来存储系统信息和用户信息的变量（在 Linux 系统中为名字-值对【Name-Value Pairs】），在每一个进程当中都会有一部分内存来保存来自父进程的环境变量，同时当前进程也可以设置自己的环境变量，这样可以将自己的环境变量和父进程的环境变量一同传递给子进程
***
### Environment Variables and Set-UID Programs

在 Set-UID 程序当中，父进程通常为一个 shell 进程，这个 shell 进程归属当前用户且有自己的环境变量，同时这个 shell 进程也能创建自己的环境变量。当这个 shell 进程运行了一个 Set-UID 程序时，子进程变成了 Set-UID 程序，Set-UID 程序会继承这个 shell 进程的环境变量。用户可以通过这种方式将环境变量作为输入将数据放到子进程的内存当中，如果这个 Set-UID 程序不合理地使用这些输入，那么可能会造成一些意想不到的后果。

!!! example "Example"

	假设我们有一个很简单的拥有者为 root 的 Set-UID 程序：
	
	```c
	#include <stdlib.h>
	int main()
	{
		system("cal");
	}
	```
	
	这个程序会调用 `system` 函数来执行 `cal` 命令，`cal` 命令会打印当前月份的日历
	
	但是事实上，`system` 会首先调用的是 `/bin/sh`，也就是一个 shell 程序，再利用 shell 程序来执行 `cal` 命令，但是这个 shell 程序会读取环境变量来获取一些信息，如果我们在执行这个 Set-UID 程序之前设置了一个名为 `PATH` 的环境变量，那么这个 Set-UID 程序就会使用这个环境变量来查找 `cal` 命令的位置，如果我们不提供绝对路径那么这个 Set-UID 程序就会使用我们设置的 `PATH` 环境变量来查找 `cal` 命令的位置，这样就可能导致执行一个恶意程序而不是我们期望的 `cal` 命令
***
### IFS Attacks

对于上面我们提到的例子，虽然看起来我们只要提供绝对路径就可以避免环境变量带来的问题，但是实际上还有一个更严重的问题，那就是 IFS 攻击（IFS Attack）。

IFS（Internal Field Separator）是一个环境变量，用于分隔字符串中的字段。默认情况下，IFS 包含空格、制表符和换行符。当 shell 解析命令时，它会使用 IFS 来分隔命令的参数。

!!! example "Example"

	还是上面的例子，但是这次我们使用绝对路径调用 `cal`：
	
	```c
	#include <stdlib.h>
	int main()
	{
		system("/usr/bin/cal");
	}
	```
	
	当我们定义 IFS 为 `/` 时，那么命令就变成了：
	
	```bash
	 usr bin cal
	```
	
	这时候命令就变成了 usr，而 bin 和 cal 就变成了参数，那么只要我们定义一个名为 `usr` 且含有两个输入参数的程序，那么这个 Set-UID 程序就会执行这个程序，而不是我们期望的 `/usr/bin/cal` 命令
***
### LD_PRELOAD Attacks

那么，如果我们不用 `system` 函数来执行命令，而是直接调用一个函数，那么就不会受到环境变量的影响吗？答案是否定的，因为在 Linux 中，动态链接库（Dynamic-Link Library）也会受到环境变量的影响

通常当一个程序被编译为二进制文件时，它会静态链接一些库函数，这些库函数会被编译进二进制文件当中，但是有些库函数是动态链接的，也就是说它们会在运行时被加载到内存中，这样可以节省磁盘空间和内存空间

!!! tip "Tips"

	比如我们有一个 Hello World 程序：
	
	```c
	# include <stdio.h>
	int main()
	{
		printf("Hello World!\n");
		return 0;
	}
	```
	
	当我们编译这个程序时，编译器会将 `printf` 函数链接到一个动态链接库（通常是 `libc.so`），这个动态链接库会在运行时被加载到内存中
	
	默认情况下，gcc 编译器会使用动态链接，如果我们想要加上静态链接，可以使用 `-static` 选项：
	
	```bash
	gcc -o hello_dynamic hello.c // Dynamic Linking
	gcc -o hello_static hello.c -static // Static Linking
	```
	
	我们会发现，动态链接的程序体积更小，而静态链接的程序体积更大，因为它将所有的库函数都编译进了二进制文件当中
	
	我们还可以使用 `ldd` 命令来查看一个程序所依赖的动态链接库：
	
	![](../../../../../assets/Pasted%20image%2020250703144701.png)
	
	可以看到，一个简单的 Hello World 程序都链接了 3 个库，其中第一个是用于系统函数调用，第二个是用于标准输入输出（包含 printf），第三个是链接器本身

动态链接库的加载是由操作系统负责的，通常操作系统会根据环境变量 `LD_LIBRARY_PATH` 来查找动态链接库的位置，但是如果我们设置了 `LD_PRELOAD` 环境变量，那么操作系统会优先加载这个环境变量指定的动态链接库，而不是默认的动态链接库

!!! example "Example"

	假设我们有一个 Set-UID 程序，它调用了一个动态链接库中的函数：
	
	```c
	void main()
	{
		printf("Hello World\n");
		sleep(2);
	}
	```
	
	如果我们设置了 `LD_PRELOAD` 环境变量，那么操作系统会优先加载这个环境变量指定的动态链接库：
	
	![](../../../../../assets/Pasted%20image%2020250703145054.png)

但是，目前利用环境变量进行攻击的方式已经不再有效，因为现代的 Linux 系统通常会对 Set-UID 程序进行一些安全措施，对一些敏感的环境变量进行限制和过滤，不再让父进程中一些敏感的环境变量传递给子进程，从而避免了这些攻击方式

![](../../../../../assets/Pasted%20image%2020250703145835.png)
***
## Attacks via Explicit User Input

对于环境变量来说，这是一个非常难以察觉的攻击方式，因为它本质上是从父进程送到子进程当中，不需要用户的输入就能进行隐式的攻击，但是对于一些需要用户输入的程序来说，攻击者可以通过一些特殊的输入来进行攻击

!!! example "Example"

	假设我们有一个 SetUID 程序为 `catall`，功能是打开并显示所有文件的内容：
	
	```c
	#include <string.h>
	#include <stdio.h>
	#include <stdlib.h>
	
	int main(int argc, char *argv[]){
		char *cat = "/bin/cat";
		
		if(argc < 2){
			printf("Please type a file name.\n");
			return 1;
		}
		
		char *command = malloc(strlen(cat) + strlen(argv[1]) + 2);
		sprintf(command, "%s %s", cat, argv[1]);
		system(command);
		return 0;
	}
	```
	
	那么这个程序所执行的命令，一部分来自于开发这个程序的人所固定的 `/bin/cat`，另一部分来自于用户的输入 `argv[1]`，我们知道在 shell 命令当中，分号（`;`）可以用来分隔多个命令，如果我们输入一个包含分号的文件名，那么这个 SetUID 程序就会执行多个命令，而不仅仅是 `cat` 命令
	
	![](../../../../../assets/Pasted%20image%2020250703222249.png)
	
	如上图，那么我们就可以通过这种方式执行 `/bin/sh`，从而获得 root 权限
	
	- 需要注意的是，我们需要在恶意的文件名两边加上引号，如果我们不加引号，那么获得的 shell 将会是以 $ 符号开头（正常的 shell）而不是图中的 # 符号（root shell），这是因为在 shell 中，分号是一个特殊字符，用于分隔命令，如果我们不加引号，那么当前 shell 会将分号后的内容作为一个新的命令来执行，而不是作为文件名的一部分传入到我们的程序当中，利用我们的程序来打开一个 shell
***
### Secure Way to Invoke External Programs

为了避免上述问题，我们可以使用一些安全的方式来调用外部程序，在 C 语言当中有一个函数叫 `execve`，它可以用来执行一个程序，并且可以指定环境变量和参数，这样就可以避免一些安全问题

!!! example "Example"

	我们还是以 `catall` 程序为例，使用 `execve` 函数来执行 `/bin/cat` 命令，而不是使用 `system` 函数：
	
	```c
	#include <stdio.h>
	#include <stdlib.h>
	#include <string.h>
	
	int main(int argc, char *argv[]){
		char *v[3];
		
		if(argc < 2){
			printf("Please type a file name.\n");
			return 1;
		}
		
		v[0] = "/bin/cat"; v[1] = argv[1]; v[2] = 0;
		execve(v[0], v, 0);
		
		return 0;
	}
	```
	
	![](../../../../../assets/Pasted%20image%2020250703225328.png)
	
	execve 函数很好地将命令和数据分开，第一个参数为命令，第二个参数为命令所需要的数据，第三个参数为环境变量，这样就可以避免命令和数据拼接的问题。同时，execve 还很好地避免了“中间人”的情况（用 system 函数会调用一个 shell 程序作为“中间人”，从而大大扩大程序的攻击面）
***
## Capability Leaking

### Dropping Privileges

对于一个有权限的程序来说，通常在执行完某些特权操作后，它会将自己的权限降低到普通用户的权限，这样可以避免程序在后续的操作中继续拥有特权，但是在这期间，如果程序泄露了某些资源，那么攻击者仍然可以利用这些资源来提升权限

!!! example "Example"

	=== "Example 01"
	
		假设我们有如下 Set-UID 程序：
		
		```c
		#include <stdio.h>
		#include <stdlib.h>
		#include <fcntl.h>
		
		void main(){
			int fd;
			char *v[2];
			
			/* Assume that /etc/zzz is an important system file,
			 * and it is owned by root with permission 0644.
			 * Before running this program, you should create the file /etc/zzz first */
			 
			 fd = open("/etc/zzz", O_RDWR | O_APPEND);
			 if (fd == -1){
				 printf("Cannot open /etc/zzz\n");
				 exit(0);
			 }
			 
			// Print out the file descriptor value
			printf("fd is %d\n", fd);
			
			// Permanently disable the privilege by making the
			// effective uid the same as the real uid
			setuid(getuid());
			
			// Execute /bin/sh
			v[0] = "/bin/sh"; v[1] = 0;
			execve(v[0], v, 0);
		}
		```
		
		这个程序最大的问题在于，它在执行完特权操作后，使用 `setuid(getuid())` 将有效用户 ID 设置为实际用户 ID，这样就降低了程序的权限，但是在这之前我们通过 `open` 函数打开了一个重要的系统文件 `/etc/zzz`，并且获得了这个文件的文件描述符 `fd`，如果我们在执行完特权操作后，继续使用这个文件描述符进行读写操作，那么就会导致权限提升，因为这个文件描述符仍然拥有 root 权限
		
		![](../../../../../assets/Pasted%20image%2020250703232425.png)
		
		如上图，我们正是泄露了文件描述符 fd 为 3，然后在执行完特权操作后，仍然使用这个文件描述符进行读写操作，从而能修改 `/etc/zzz` 文件，获得 root 权限
	
	=== "Example 02"
	
		事实上，这样的漏洞在 OS X 10.10(2015) 就曾出现过，它引入了一个环境变量 
		`DYLD_PRINT_TO_FILE`，用于给链接器 `dyld` 来打印错误日志的信息
		
		当 `dyld` 被运行时，它会打开一个文件，文件名由这个环境变量指定，将错误日志写入到这个文件中，第一个问题在于，这个环境变量是由用户控制的，如果程序是一个 Set-UID 程序，那么链接器将会在 Set-UID 进程当中执行，如果用户让这个环境变量指向一个任意文件，那么链接器就会打开这个文件，并且将错误日志写入到这个文件中，这样就可以利用这个漏洞来修改任意文件使得这个文件崩溃
		
		当然，这个问题并不是最严重的，因为我们无法控制输入的内容（输入的内容都是链接器的错误日志），而 OS X 10.10 犯了一个更大的错误，当链接器写完文件后，它将控制权重新送回了 Set-UID 程序，但是没有关掉文件，权限仍然被送到了程序当中。当一个 Set-UID 程序完成了它的任务后，通常有两种结束的方法，一种是退出 Set-UID 程序，进程也被销毁，这样进程中的东西都将被销毁，这样是没问题的，因为权限就随之而被销毁了；但是第二种方式就是它会成为一个没权限的程序，继续执行，将控制权交还给用户，那么如 Example 01，权限就被传到了用户手上
		
		![](../../../../../assets/Pasted%20image%2020250703234020.png)
		
		如上图，我们将 `DYLD_PRINT_TO_FILE` 设置为一个我们想要攻击的文件，然后运行 `su <some_username>`（这是一个 Set-UID 程序，当它完成任务会降低权限，调用 `/bin/sh` 程序，把控制权交还给用户），即使我们已经回到了普通用户的 shell 中，我们仍然能通过文件描述符对文件进行写操作
***
## Security Analysis

!!! note "Definition"

	对于攻击者来说，我们定义一个软件环境的攻击面（Attack Surface）为不同点（攻击向量，the Attack Vectors）的总和，未经授权的用户（即攻击者）可以尝试在环境中通过这些点修改数据或读取数据。
	
	简单来说，攻击面即一个程序与用户交互的所有方式，每一个用户能修改或读取数据的方式都是一个可能的攻击点

总结上面的来说，一个 Set-UID 程序主要有四个攻击面：

![](../../../../../assets/Pasted%20image%2020250703234649.png)

其中第一个攻击面即隐式用户输入攻击，第三个攻击面即通过环境变量攻击，第四个攻击面则是通过权限泄露攻击，第二个攻击面将会在后面涉及
***
### Set-UID versus Server Approach

当我们想要执行一些超出我们权限的事情，我们主要有两种方法，一种是 Set-UID，给予我们一个有权限的进程（即 Set-UID 进程）；另一种方法是我们仍然在一个正常的进程中执行，但是会有另一个有权限的进程（通常为根守护进程，Root Daemon）帮助我们获取资源，我们只需要发送请求即可

- 从资源消耗来说，Set-UID 方法消耗的资源更少
- 从安全方面来说，Set-UID 方法更不安全，以环境变量为例，Set-UID 让用户通过环境变量的传递隐式输入一些内容到 Set-UID 进程当中；而根守护进程则会用根的 shell 来传递环境变量到一个子进程（这个子进程的 euid 和 ruid 均为 0，并非一个 Set-UID 进程），而根传递的环境变量只能由根来修改，普通用户就无法通过这种方式来进行攻击了
	- 事实上，很多现代的操作系统如 Android OS，干脆直接去掉了 Set-UID 这一种机制

因为 Set-UID 程序的危险性，我们制定了一条原则，称为最低权限准则（Principle of Least Privilege）：每一个程序和有权限的用户完成任务都必须只使用最少但有必要使用的权限（即需要多少权限就给多少，不能给多）

在现代的操作系统中，它们将 root 权限分解成更小的部分，将这些分解的小部分的权限分配给需要它们的程序（如 Linux 的 POSIX capability、Android 的 Permissions【例如 GPS 访问权限...】）






