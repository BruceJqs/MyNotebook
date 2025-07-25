---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
---  

# Dirty COW

## 任务 1：修改一个只读的虚拟文件

### 创建虚拟文件

按照任务要求创建文件 `/zzz`，并将其权限设置为普通用户只读，可以看到，我们只能通过 `sudo` 命令来修改这个文件的内容，无法以 seed 用户的身份写入内容。

![](../../../../../assets/Pasted%20image%2020250725160446.png)
***
### 发起攻击

编译并运行 `cow_attack.c` 程序，我们可以发现 `/zzz` 文件修改成功：

![](../../../../../assets/Pasted%20image%2020250725161102.png)
***
## 任务 2：修改密码文件以获取 Root 权限

我们添加新用户 charlie：

![](../../../../../assets/Pasted%20image%2020250725161323.png)

同时，我们修改 `cow_attack.c` 文件使得其能将 charlie 用户的 UID 修改为 0：

![](../../../../../assets/Pasted%20image%2020250725161915.png)

运行即可将 charlie 用户的 UID 修改为 0，从而获得 Root 权限：

![](../../../../../assets/Pasted%20image%2020250725161704.png)
