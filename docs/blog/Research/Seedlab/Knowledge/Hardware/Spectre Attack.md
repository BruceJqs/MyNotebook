---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
---  

# Spectre Attack

> Spectre Attack 与 Meltdown Attack 类似，它们都是利用了 CPU 的缓存侧信道攻击，且都是面临 CPU 的乱序执行，但是不同的地方在于 Meltdown Attack 窃取的是内核空间的数据，且面对的防护措施是硬件级别的防护，而 Spectre Attack 窃取的是同一用户空间的其他进程的数据，面对的防护措施是软件级别的防护（通常是一个沙箱，负责检查访问数据地址是否位于被允许的范围之内）

### Out-of-Order Execution

同样地，类似 Meltdown，沙箱检查的代码也会被 CPU 乱序执行，如下图所示：

![](../../../../../assets/Pasted%20image%2020250825155108.png)

因为 CPU 对于条件语句会采取预测执行（Speculative Execution）的方式，即 CPU 会预测条件语句的结果，并且提前执行条件语句之后的代码，如果预测错误，则会回滚到条件语句处重新执行。CPU 的预测行为非常简单，通常是根据历史记录进行预测，例如如果之前几次条件语句的结果均为 true，那么这一次条件语句的结果也很有可能为 true，它就会预测结果为 true。

那么，我们只需要首先“训练”出一个历史记录，让条件语句结果为 true，然后再次执行一个条件语句结果为 false 的语句，因为预测执行的原因 true 分支的代码仍然会被提前执行，那么这其中的指令就被缓存，我们就可以通过缓存侧信道攻击来获取数据。



