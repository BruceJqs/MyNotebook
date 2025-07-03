---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
---  

# Linux Security Basics

## User and Group

在 Linux 当中，每个用户都有一个唯一的用户 ID（UID），每个组也有一个唯一的组 ID（GID）。用户和组的管理是 Linux 安全的基础。同时，Linux 有一个特殊的用户 `root`，它的 UID 为 0，拥有系统的最高权限。

- Linux 当中可以不止一个用户的 UID 为 0，即使这个 user 的名字不是 `root`，只要它的 UID 为 0，就拥有最高权限
***
### User File

Linux 的用户数据存储在 `/etc/passwd` 文件中，每行代表一个用户，格式如下：

![](../../../../../assets/Pasted%20image%2020250629155243.png)

每个字段用冒号分割，它们的含义如下：

1. 用户名
2. 密码（通常是一个占位符，如 `x`，实际密码存储在 `/etc/shadow` 中）
3. 用户 ID（UID）
4. 组 ID（GID）
5. 用户全名或描述
6. 主目录（Home Dir）
7. 默认 shell

从默认 shell 可以看出，某些用户可能并非实际的用户（例如上面的 games, man, vboxadd 等等），它们可能是系统用户或服务用户
***
### Group File

Linux 的组数据存储在 `/etc/group` 文件中，每行代表一个组，格式如下：

![](../../../../../assets/Pasted%20image%2020250629155817.png)

每个字段用冒号分割，它们的含义如下：

1. 组名
2. 密码（通常是一个占位符，如 `x`）
3. 组 ID（GID）
4. 组成员列表（逗号分隔）

当我们需要进行权限管理的时候，我们可以对一整个组的用户进行操作，而不需要单独对每个用户进行操作
***
### Password and Shadow Files

Linux 的密码存储在 `/etc/shadow` 文件中，每行代表一个用户，格式如下：

![](../../../../../assets/Pasted%20image%2020250629160105.png)

值得注意的是，`/etc/shadow` 文件的权限通常设置为 640，这样只有 root 用户和组内的用户可以读取密码信息，而其他用户无法访问（访问需要 sudo 命令）

!!! note "Related Commands"

	=== "查看用户 ID 和组信息"
	
		在当前用户下，我们可以使用 `id` 命令查看当前用户的 UID 和 GID 信息：
		
		![](../../../../../assets/Pasted%20image%2020250629160457.png)
		
		如果需要查看其他用户的信息，可以使用 `id username` 命令
	
	=== "切换用户"
	
		我们可以使用 `su` 命令切换到其他用户，使用 `su  username` 切换到指定用户，并加载该用户的环境变量：
		
		![](../../../../../assets/Pasted%20image%2020250629160630.png)
	
	=== "命令使用手册"
	
		我们可以使用 `man` 命令查看命令的使用手册，例如查看 `su` 命令的手册，我们就可以用 `man su`：
		
		![](../../../../../assets/Pasted%20image%2020250629160753.png)
		
		手册中包含了命令的详细信息、选项和用法等
	
	=== "更改密码"
	
		我们可以使用 `passwd` 命令更改当前用户的密码：
		
		如果需要更改其他用户的密码，可以使用 `sudo passwd username` 命令
	
	=== "添加新用户"
	
		我们可以使用 `useradd` 命令添加新用户，例如添加一个名为 bob 的用户：
		
		![](../../../../../assets/Pasted%20image%2020250629161216.png)
***
## Access Control and Permissions

> Linux 使用文件权限和访问控制列表（ACL, Access Control List）来管理用户对文件和目录的访问权限

### File Permissions

每个文件和目录都有一个所有者（Owner）、一个组（Group）和其他用户（Others）的权限设置，例如：

![](../../../../../assets/Pasted%20image%2020250629161627.png)

每个文件或目录的权限由三个部分组成：

1. 所有者权限（Owner Permissions）
2. 组权限（Group Permissions）
3. 其他用户权限（Other Permissions）

每个部分可以有以下权限：

- 读（Read, r）
- 写（Write, w）
- 执行（Execute, x）

可以使用 `ls -l` 命令查看文件或目录的权限信息，我们还可以用二进制数表示权限，例如：

![](../../../../../assets/Pasted%20image%2020250629161844.png)

这样，我们就可以用 `chmod` 命令来修改权限，例如：

```bash
chmod 640 myfile
```

这将设置文件 `myfile` 的权限为所有者读写，组内读，其他用户无权限
***
### Directory Permissions

目录的权限与文件类似，但有一些额外的含义：

- 读（r）：允许列出目录中的文件
- 写（w）：允许在目录中创建、删除或重命名文件/目录
- 执行（x）：允许进入目录（即访问目录中的文件）
***
### Default Permissions

在 Linux 中，`umask` 是一个用于设置新创建文件和目录的默认权限掩码的命令。它定义了新文件和目录的默认权限，通常是通过从系统默认权限中减去 `umask` 值来计算的。

!!! example "Example"

	![](../../../../../assets/Pasted%20image%2020250701175010.png)
	
	例如上图，当 umask 为 0002 时，新创建的文件默认权限为 664（rw-rw-r--），新创建的目录默认权限为 775（rwxrwxr-x）。这意味着新文件对所有者和组成员可读写，对其他用户只读；新目录对所有者和组成员可读写执行，对其他用户只读执行。
	
	而当我们将 umask 改为 0077 时，新创建的文件默认权限为 600（rw-------），新创建的目录默认权限为 700（rwx------）。这意味着新文件和目录只能被所有者访问，其他用户无权访问。
***
### Changing Ownership

如果我们需要更改文件或目录的所有者或组，可以使用 `chown` 命令，例如我们将文件 `xyz` 的所有权交给 root：

```bash
chown root xyz
```
***
### Full Access Control List

Linux 还支持更细粒度的访问控制，称为访问控制列表（ACL）。ACL 允许我们为文件或目录设置多个用户或组的权限，而不仅仅是所有者、组和其他用户。我们可以使用 `getfacl` 命令查看 ACL 信息，也可以使用 `setfacl` 命令设置 ACL，例如：

![](../../../../../assets/Pasted%20image%2020250701203414.png)
***
## Running Commands as Superuser

在 Linux 中，root 用户是系统的超级用户，拥有最高权限。为了安全起见，我们通常不直接以 root 用户身份登录，而是使用 `sudo` 命令来临时获取超级用户权限。

![](../../../../../assets/Pasted%20image%2020250702131202.png)

例如上图，`sudo` 命令允许我们以超级用户身份运行命令，而无需切换到 root 用户。使用 `sudo` 时，系统会提示输入当前用户的密码，以验证权限，随后可以临时获取超级用户权限（即使用用户 ID 为 0 的用户执行命令）

!!! example "Another Example"

	sudo 不仅能让我们执行特权命令，还能让我们以其他用户身份执行命令，例如：
	
	![](../../../../../assets/Pasted%20image%2020250702131417.png)
	
	只要我们加上 `-u` 选项，就可以指定以其他用户身份执行命令

那什么样的用户可以使用 `sudo` 呢？这取决于 `/etc/sudoer` 文件中的配置。通常，只有在该文件中被授权的用户才能使用 `sudo` 命令

![](../../../../../assets/Pasted%20image%2020250702131531.png)

例如上图，`%sudo ALL=(ALL:ALL) ALL` 表示属于 `sudo` 组的用户可以使用 `sudo` 命令执行任何命令
