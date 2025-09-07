---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
# comments: true
--- 

# Homework 15

## 19.2

> Explain the purpose of the checkpoint mechanism. How often should check points be performed? How does the frequency of checkpoints affect:
> 
> - System performance when no failure occurs?
> - The time it takes to recover from a system crash?
> - The time it takes to recover from a media (disk) failure?

检查点机制在 DBMS 中目的有：

- **减少恢复时间**：当系统发生崩溃（例如，由于断电或软件错误）时，数据库需要从一个一致的状态恢复。如果没有检查点，系统可能需要重做（Redo）自数据库启动以来所有的已提交事务的日志记录，并撤销（Undo）所有未完成的事务，从而大大缩短了恢复过程
- **刷新脏页到磁盘**：将内存中已修改但尚未写入磁盘的数据页（脏页）强制写入磁盘，确保数据的持久性，并减少恢复时需要重做的工作量
- **截断和重用日志空间**：在某些日志策略中，一旦检查点完成并且相关的脏页已安全写入磁盘，检查点之前的某些日志记录对于崩溃恢复可能不再是必需的。这使得系统可以截断或重用这部分日志空间

检查点的执行频率没有最佳答案，需要在系统开销和恢复时间之间进行权衡，如果检查点过于频繁，会显著增加系统正常运行的开销；如果检查点过于稀疏，崩溃后的恢复时间会很长

- 在没有故障发生时：
	- 频率越高，对系统性能的负面影响越大
	- 频率越低，对系统性能的负面影响越小
- 从系统崩溃中恢复所需的时间：
	- 频率越高，所需的时间越短
	- 频率越低，所需的时间越长
- 从介质（磁盘）故障中恢复所需的时间：
	- 检查点频率并不直接决定备份频率和归档日志的生成，一般更频繁的检查点可以使得重放的日志量相对可控
***
## 19.10

> Explain the reasons why recovery of interactive transactions is more difficult to deal with than is recovery of batch transactions. Is there a simple way to deal with this difficulty? (Hint: Consider an automatic teller machine transaction in which cash is withdrawn.)

交互式事务的恢复之所以比批处理事务更为复杂和困难，原因如下：

- **与外部世界的交互和不可逆操作**：交互式事务互动一旦发生，往往是不可逆的，或者撤销成本很高；相比之下批处理事务通常主要在数据库内部对数据进行操作，可以通过事务日志进行回滚
- **用户交互和状态依赖**：交互式事务通常涉及用户输入和反馈，用户可能在事务执行过程中做出决策，这使得恢复过程更为复杂，因为需要考虑用户的状态和期望，在出现失败恢复还需要让用户从中断点有效地继续；而批处理事务是可预测的

可以采用一些设计原则和策略来显著降低复杂性、提高可靠性：

- **将不可逆的外部操作尽可能推迟**：例如，在 ATM 取款流程中，应确保在数据库层面完成所有检查（如账户验证、余额检查）、更新（如扣款或预授权/冻结金额）并基本确保事务能够成功提交之后，才向ATM硬件发出吐钞指令
- **精确记录交互状态和使用持久化消息队列**：日志中不仅要记录数据库状态的改变，还应详细记录与外部系统交互的关键步骤和状态（例如，“已向 ATM 发送吐钞请求”，“ATM 确认已吐钞”）
***
## 19.21

> Consider the log in Figure 19.5. Suppose there is a crash just before the log record $<T_0 ,\text{ abort}>$ is written out. Explain what would happen during recovery.
> 
> ![](../../../assets/Pasted%20image%2020250531172846.png)
> 

1. 分析阶段：

从最后一个检查点开始扫描日志到末尾：

- 遇到 $<T_1, C, 700, 600>$：$T_1$​ 对页 C 进行了修改。C 加入 DPT，并记录其 `RecLSN`（即此日志记录的 LSN）
- 遇到 $<T_1 \text{ commit}>$：$T_1$​ 提交。$T_1$​ 从 ATT 中移除
- 遇到 $<T_2 \text{ start}>$：$T_2$​ 开始。$T_2$​ 加入 ATT
- 遇到 $<T_2, A, 500, 400>$：$T_2$​ 对页 A 进行了修改。A 加入 DPT，并记录其 `RecLSN`
- 遇到 $<T_0, B, 2000>$：这是 $T_0$​ 在正常操作期间执行回滚时写入的日志记录（它将 B 的值从 2050 改回 2000）。$T_0$​ 仍然在 ATT 中，因为它既没有提交记录也没有中止记录。B 加入 DPT，并记录其 `RecLSN`

2. 重做阶段

- 对于日志记录 $<T_1, C, 700, 600>$：如果磁盘上页 C 的 `PageLSN` 小于此记录的 LSN，则将页 C 的值重做为 600，并更新页 C 的 `PageLSN`
- 对于日志记录 $<T_2, A, 500, 400>$：如果磁盘上页 A 的 `PageLSN` 小于此记录的 LSN，则将页 A 的值重做为 400，并更新页 A 的 `PageLSN`
- 对于日志记录 $<T_0, B, 2000>$：如果磁盘上页 B 的 `PageLSN` 小于此记录的 LSN，则将页 B 的值重做为 2000（这是 $T_0$ ​在正常操作中回滚其先前更新的结果），并更新页 B 的`PageLSN`

3. 撤销阶段

撤销阶段会回滚在分析阶段确定在 `undo-list` 中的所有未完成事务（即 $T_0$​ 和 $T_2$​）。它从后向前扫描这些事务的日志记录
***
## 19.25

> In the ARIES recovery algorithm:
> 
> a. If at the beginning of the analysis pass, a page is not in the checkpoint dirty page table, will we need to apply any redo records to it? Why?
> 
> b. What is RecLSN, and how is it used to minimize unnecessary redos?

（a）我们可能仍然需要对其进行 redo 记录，是因为 ARIES 的分析阶段会从最后一个检查点开始，向前扫描直到日志的末尾，如果这其中有一个干净的页面被修改了，那么就变成了脏页，会将它们及其对应的 RecLSN 添加到分析阶段构建的脏页表中，在重做阶段中，ARIES 会尝试重做所有在分析阶段确定的脏页表中的操作

（b）RecLSN（Recovery Log Sequence Number）是脏页表中与每个脏页关联的一个日志序列号。它通常指使该页面首次变脏的那条日志记录的 LSN，RecLSN 用于确定重做起点，筛选需要重做的日志记录