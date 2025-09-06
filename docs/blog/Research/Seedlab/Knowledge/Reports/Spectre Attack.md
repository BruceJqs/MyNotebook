---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
---  

# Spectre Attack

> 任务 1 和任务 2 与 Meltdown 完全一致

## 任务 3：乱序执行与分支预测

编译并运行程序，结果如下：

![](../../../../../assets/Pasted%20image%2020250826132110.png)

可以看到，程序成功获得了 Secret 97，注释掉 `_mm_clflush(&size);` 语句后，重新编译运行程序后，结果如下：

![](../../../../../assets/Pasted%20image%2020250826132336.png)

此时，程序并没有获得 Secret，这是因为缓存没有正确地清除，噪声较大导致攻击失败。替换 `victim(i + 20);` 并重新编译运行，结果如下：

![](../../../../../assets/Pasted%20image%2020250826132948.png)

仍然没有获得 Secret，这是因为我们训练 CPU 预测执行为 false 了，自然就无法从缓存中获取指令并运行了
***
## 任务 4：Spectre 攻击

编译并运行程序，得到结果如下：

![](../../../../../assets/Pasted%20image%2020250826133624.png)

可以看到，有的时候我们无法攻击成功，但是大多数情况下是可以成功拿到 Secret 值的
***
## 任务 5：提高攻击准确性

编译并运行改进过后的代码，结果如下：

![](../../../../../assets/Pasted%20image%2020250826133845.png)

可以看到，代码将 0 作为最后的结果了，这是因为 restrictedAccess 访问越界时的返回值为 0，那么自然 0 的得分最高。因此我们可以修改 restrictedAccess 函数的返回值为 -1，但是这会导致 `array[s * 4096 + DELTA] += 88;` 语句数组越界，因此我们修改 DELTA 为 4096。同时，由于 restrictedAccess 的返回类型为 uint8_t，这回导致整数溢出，所以修改 restrictedAccess 的返回值和spectreAttack 中的参数 s 的类型为 int 即可正确得到 Secret 的值，编译并运行代码，结果如下：

![](../../../../../assets/Pasted%20image%2020250826134758.png)

当我们注释掉看似无用的语句之后，重新编译运行代码，得到结果：

![](../../../../../assets/Pasted%20image%2020250826134944.png)

可以看到，没有看似无用的语句，攻击就不成功了。当我们尝试用 `usleep(1)` 时得到结果：

![](../../../../../assets/Pasted%20image%2020250826135115.png)

用 `usleep(100)` 时得到结果：

![](../../../../../assets/Pasted%20image%2020250826135240.png)

用 `usleep(1000)` 时得到结果：

![](../../../../../assets/Pasted%20image%2020250826135324.png)

用 `usleep(10000)` 时得到结果：

![](../../../../../assets/Pasted%20image%2020250826135415.png)

用 `usleep(100000)` 时得到结果：

![](../../../../../assets/Pasted%20image%2020250826135720.png)

可以看到，随着 sleep 时间的增加，攻击成功率逐渐升高，但是当 sleep 时间过长时，攻击就失败了。
***
## 任务 6：窃取整个秘密字符串

修改代码如下：

![](../../../../../assets/Pasted%20image%2020250826141116.png)

多次运行，结果如下：

![](../../../../../assets/Pasted%20image%2020250826141017.png)

结合之前我们获得的第一个字符为 S，可以拼凑出整个秘密字符串 "Some Secret Value"
