---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
--- 

# Chapter 15 : Recovery System

## Failure Classification

![](../../../assets/Pasted%20image%2020250526100643.png)


- **事务失败**：
    - **逻辑错误**：由于某些内部错误条件，事务无法完成
    - **系统错误**：数据库系统必须由于错误条件（例如，死锁）而终止活动事务
- **系统崩溃**：电源故障或其他硬件或软件故障导致系统崩溃
	- **故障停止假设**：假设非易失性存储内容不会因系统崩溃而损坏
	    - 数据库系统具有众多完整性检查，以防止磁盘数据损坏
- **磁盘故障**：磁头碰撞或类似的磁盘故障会破坏磁盘存储的全部或部分
    - **破坏可检测假设**：假设破坏是可检测的；磁盘驱动器使用校验和来检测故障
***
## Storage Structure

- **易失性存储**：
	- 无法在系统崩溃后保存数据
	- e.g.：主内存，缓存
- **非易失性存储**：
    - 可以在系统崩溃后保存数据
    - 示例：磁盘，磁带，闪存，非易失性（电池备份）RAM
    - 但仍可能失败，导致数据丢失
- **稳定存储**：
    - 一种神奇的存储形式，可以在所有故障中保存数据
    - 通过在不同的非易失性介质上维护多个副本来**近似**实现
***
### Stable-Storage Implementation

- 在不同的磁盘上维护每个块的多个副本
- 数据传输过程中的故障仍可能导致副本不一致
- 保护存储介质在数据传输过程中免受故障影响

![](../../../assets/Pasted%20image%2020250526101354.png)
***
## Recovery and Atomicity

### Database Recovery

恢复算法是尽管发生故障，仍能确保数据库**一致性**以及事务**原子性和持久性**的技术

恢复算法有两个部分：

1.  在**正常事务处理**期间采取的行动，以确保存在足够的信息从故障中恢复
2.  故障发生后为**恢复**数据库内容至确保原子性、一致性和持久性的状态而采取的行动

我们假设严格的**两阶段锁定**确保**无脏读**

**幂等性（Idempotent）**：如果一个恢复算法执行多次与执行一次得到相同的结果，则称该算法是幂等的
***
### Log-Based Recovery

为确保故障下的原子性，我们首先将描述修改的信息（日志）输出到**稳定存储**，而不修改数据库本身

- 日志保存在稳定存储器（Stable Storage）上
	- 日志是**日志记录**的序列，并维护数据库上更新活动的记录
- 当事务 $T_i$ 启动时，它通过写入“**start**”日志记录来注册自己：$<T_i, \text{start}>$
- 在 $T_i$ 执行 write(X) 之前，写入“**update**”日志记录：$<T_i, X, V_1, V_2>$
	- 其中 $V_1$ 是写入前 X 的值（**旧值**），$V_2$ 是要写入 X 的值（**新值**）
- 当 $T_i$ 完成其最后一条语句时，写入“**commit**”日志记录：$<T_i, \text{commit}>$
- 当 $T_i$ 完成回滚时，写入“**abort**”日志记录：$<T_i, \text{abort}>$
***
#### Write-Ahead Logging

**先写日志原则（Write-Ahead Logging，WAL）**：在主内存中的数据输出到数据库之前，与数据相关的日志记录必须已经输出到**稳定存储（Stable Storage）**
***
### Concurrency Control and Recovery

- 对于并发事务，所有事务共享一个磁盘缓冲区和一个日志文件
	- 一个缓冲块可以包含由一个或多个事务更新的数据项
- 我们假设**如果一个事务 $T_i$ 修改了一个项目，那么在 $T_i$ 提交或中止之前，没有其他事务可以修改同一个项目**
	- 即未提交事务的更新不应对其他事务可见
	    - 否则，如果 $T_1$ 更新 A，然后 $T_2$ 更新 A 并提交，最后 $T_1$ 不得不中止，该如何执行撤销 （Undo）？
	- 可以通过获取更新项上的排他锁并将锁保持到事务结束（**严格两阶段锁定**）来确保
- 具有逻辑撤销日志的恢复支持提前释放锁
***
### Transaction Commit

- 当事务的**提交日志记录（Commit Log Record）** 输出到**稳定存储（Stable Storage）** 时，称该事务已提交
	- 该事务之前的所有日志记录必须已经输出
- 事务执行的写入操作在事务提交时可能仍位于**缓冲区（Buffer）** 中，并可能稍后输出
***
### Undo and Redo Operations

- 撤销（Undo）日志记录 $<T_i, X, V_1, V_2>$ 将旧值 $V_1$ 写入 $X$
- 重做（Redo）日志记录 $<T_i, X, V_1, V_2>$ 将新值 $V_2$ 写入 $X$

- undo($T_i$) 将 $T_i$ 更新的所有数据项的值恢复为其旧值，从 $T_i$ 的最后一条日志记录开始向后处理
    - 每次数据项 X 恢复为其旧值 V 时，都会写出一条特殊的日志记录 $<T_i, X, V>$ — 补偿日志（Compensation Log）
    - 当事务的撤销完成时，会写出一条日志记录 $<T_i, \text{abort}>$
- redo($T_i$) 将 $T_i$ 更新的所有数据项的值设置为其新值，从 $T_i$ 的第一条日志记录开始向前处理
    - 在这种情况下不进行日志记录
***
### Recovering from Failure

故障恢复时：

- 如果日志包含记录 $<T_i, \text{start}>$，但不包含记录 $<T_i, \text{commit}>$ 或 $<T_i, \text{abort}>$，则事务 $T_i$ 需要被**撤销（Undone）**
- 如果日志包含记录 $<T_i, \text{start}>$，并且包含记录 $<T_i, \text{commit}>$ 或 $<T_i, \text{abort}>$，则事务 $T_i$ 需要被**重做（Redone）**

可以注意到，如果事务 $T_i$ 早先被撤销，并且 $<T_i, \text{abort}>$ 记录已写入日志，然后发生故障，则从故障中恢复时 $T_i$ 会被**重做** 

- 这样的重做会重新执行所有原始操作，*包括恢复旧值的步骤* 
* 被称为**重复历史**（Repeating History）
- 这虽然看起来很浪费，但极大地简化了恢复过程

!!! example "Example"

	下图展示了日志在三个时间点的显示情况：
	
	![](../../../assets/Pasted%20image%2020250526221715.png)
	
	上述每种情况下的恢复操作是：
	
	(a) 撤销 ($T_0$)：B 恢复到 2000，A 恢复到 1000，并写出日志记录 $<T_0, B, 2000>$，$<T_0, A, 1000>$，$<T_0, \text{abort}>$
	
	(b) 重做 ($T_0$) 和 撤销 ($T_1$)：A 和 B 设置为 950 和 2050，C 恢复到 700。写出日志记录 $<T_1, C, 700>$，$<T_1, \text{abort}>$
	
	(c) 重做 ($T_0$) 和 重做 ($T_1$)：A 和 B 分别设置为 950 和 2050。然后 C 设置为 600
***
### Checkpoints

重做/撤销日志中记录的所有事务可能非常缓慢

1.  如果系统已经运行了很长时间，处理**整个日志**将非常**耗时**
2.  我们可能会不必要地重做那些已经将其更新输出到数据库的事务

因此，我们可以通过定期执行**检查点**（Checkpoint）来简化恢复过程

1.  将当前驻留在主内存中的所有**日志记录**输出到稳定存储
2.  将所有**修改过的缓冲块**输出到磁盘
3.  将日志记录 $<\text{checkpoint}, L>$ 写入稳定存储，其中 $L$ 是检查点时刻所有活动事务的列表

- 执行检查点操作时，所有更新都会停止

!!! example "Example"

	![](../../../assets/Pasted%20image%2020250526223545.png)
***
## Recovery Algorithm

日志记录（正常操作期间）：

- 事务开始时记录 $<T_i, \text{start}>$
- 每次更新记录 $<T_j, X_j, V_1, V_2>$，并且
- 事务结束时记录 $<T_i,\text{commit}>$

事务回滚（正常操作期间）：

- 设 $T_i$ 为要回滚的事务
- 从末尾向后扫描日志，对于每个形式为 $<T_i, X_j, V_1, V_2>$ 的 $T_i$ 日志记录
    * 通过将 $V_1$ 写入 $X_j$ 来执行撤销
    * 写入一条日志记录 $<T_i, X_j, V_1>$
        - 此类日志记录称为**补偿日志记录**(补偿记录)
- 一旦找到 $<T_i,\text{start}>$ 记录，停止扫描并写入日志记录 $<T_i,\text{abort}>$

从故障中恢复：两个阶段

- **重做阶段**：重放**所有**事务的更新，无论它们是已提交、已中止还是未完成
- **撤销阶段**：撤销所有未完成的事务

重做阶段：

1.  找到最后一个 $<\text{checkpoint},L>$ 记录，并将 **undo-list** 设置为 $L$
2.  从上述 $<\text{checkpoint},L>$ 记录向前扫描
    1.  每当找到记录 $<T_i, X_j, V_1, V_2>$ 时，通过将 $V_2$ 写入 $X_j$ 来重做它
    2.  每当找到（补偿）日志记录 $<T_i, X_j, V_2>$ 时，通过将 $V_2$ 写入 $X_j$ 来重做它
    3.  每当找到日志记录 $<T_i,\text{start}>$ 时，将 $T_i$ 添加到 **undo-list**
    4.  每当找到日志记录 $<T_i,\text{commit}>$ 或 $<T_i,\text{abort}>$ 时，从 **undo-list** 中移除 $T_i$

撤销阶段：从末尾向后扫描日志

1.  每当找到日志记录 $<T_j, X_j, V_1, V_2>$，其中 $T_i$ 在 undo-list 中时，执行与事务回滚相同的操作：
	1.  通过将 $V_1$ 写入 $X_j$ 来执行撤销
	2.  写入日志记录 $<T_i, X_j, V_1>$
2.  每当找到日志记录 $<T_i,\text{start}>$，其中 $T_i$ 在 undo-list 中时，
	1.  写入日志记录 $<T_i,\text{abort}>$
	2.  从 undo-list 中移除 $T_i$
3.  当 undo-list 为空时停止，即已为 undo-list 中的每个事务找到 $<T_i,\text{start}>$

撤销阶段完成后，可以开始正常的事务处理

!!! example "Example"

	![](../../../assets/Pasted%20image%2020250527211222.png)
***
## Log Buffer & Database Buffer

### Log Record Buffering

![](../../../assets/Pasted%20image%2020250527211844.png)

- **日志记录缓冲**：日志记录被缓冲在主内存中，而不是直接输出到稳定存储
	- 当缓冲区中的日志记录块已满，或者执行**日志强制**（Log Force）操作时，日志记录会输出到稳定存储
- 执行日志强制操作以提交事务，方法是将其所有日志记录（包括提交记录）强制写入稳定存储
- **组提交**（Group Commit）：可以使用单个输出操作输出多个日志记录，从而降低 I/O 成本

如果日志记录被缓冲，则必须遵循以下规则：

- 日志记录按照其创建顺序输出到稳定存储
- 只有当日志记录 $<T_i,\text{commit}>$ 已输出到稳定存储时，事务 $T_i$ 才会进入提交状态
- 在主内存中的数据块输出到数据库之前，与该块中数据相关的所有日志记录都必须已输出到稳定存储
    * 此规则称为**预写日志**（Write-Ahead Logging）或 **WAL** 规则，严格来说，WAL 仅要求输出撤销信息
***
### Database Buffering

- 数据库维护一个内存中的数据块缓冲区
	- 当需要一个新块时，如果缓冲区已满，则需要从缓冲区中移除一个现有块
	- 如果选择移除的块已被更新，则必须将其输出到磁盘
- 恢复算法支持**非强制策略**（No-Force Policy）：即，事务提交时不需要将更新的块写入磁盘
	- **强制策略**（Force Policy）：要求在提交时写入更新的块
    * 提交成本更高
* 恢复算法支持**窃取策略**（Steal Policy）：即，包含未提交事务更新的块可以在事务提交之前写入磁盘
***
### Fuzzy Checkpointing

为避免在**检查点（Checkpointing）** 期间**长时间中断（Long Interruption）** 正常处理，允许在检查点期间进行更新

**模糊检查点（Fuzzy Checkpointing）** 的执行方式如下：

1.  临时停止所有事务的更新
2.  写入一个 $<\text{checkpoint} L>$ 日志记录并强制将日志写入稳定存储
3.  记录已修改缓冲区块的列表 $M$
4.  现在允许事务继续执行其操作
5.  将列表 $M$ 中的所有已修改缓冲区块输出到磁盘
    * 在输出期间不应更新块
    * 遵循 WAL：与块相关的所有日志记录必须在块输出之前输出
6.  将指向**检查点（Checkpoint）** 记录的指针存储在磁盘上的固定位置 `last_checkpoint`

使用模糊检查点进行恢复时，从 `last_checkpoint` 指向的**检查点（Checkpoint）** 记录开始扫描

* `last_checkpoint` 之前的日志记录的更新已反映在磁盘上的数据库中，无需重做
* 不完整的检查点（即系统在执行检查点时崩溃）可以被安全地处理

![](../../../assets/Pasted%20image%2020250527214742.png)
***
## Failure with Loss of Nonvolatile Storage

到目前为止，我们都在假设非易失性存储没有丢失，但事实上并非如此，我们使用类似于检查点的技术来处理非易失性存储的丢失。

* 定期将数据库的全部内容**转储（Dump）** 到稳定存储
* 在转储过程中不能有任何活动的事务；必须执行类似于检查点的过程
    1.  将当前驻留在主内存中的所有日志记录输出到稳定存储
    2.  将所有缓冲区块输出到磁盘
    3.  将数据库的内容复制到稳定存储
    4.  将 `<dump>` 记录输出到稳定存储上的日志中

从磁盘故障中恢复：

1.  从最近的转储中恢复数据库
2.  查阅日志并重做转储后提交的所有事务

- 可以扩展为允许事务在转储期间处于活动状态；称为模糊转储（Fuzzy Dump）或在线转储（Online Dump），类似于模糊检查点
***
## Recovery with Early Lock Release and Logical Undo Operations

### Recovery with Early Lock Release

- 支持高并发锁定技术，例如用于B+树并发控制的技术，这些技术会提前释放锁
	* 支持“逻辑撤销（Logical Undo）”
* 基于“重复历史（Repeating History）”的恢复，即恢复过程执行与正常处理完全相同的操作
***
### Logical Undo Logging

像 B+ 树插入和删除这样的操作会**提前释放锁**。

* 它们无法通过恢复旧值（**物理撤销，Physical Undo**）来撤销，因为一旦锁被释放，其他事务可能已经更新了 B+ 树
* 相反，插入（或删除）操作是通过执行删除（或插入）操作来撤销的（称为**逻辑撤销，Logical Undo**）

对于此类操作，撤销日志记录应包含要执行的撤销操作

* 这种日志记录称为**逻辑撤销日志记录 Logical Undo Logging**，与**物理撤销日志记录（Physical Undo Logging）** 相对
    * 这些操作称为**逻辑操作（Logical Operations）**
* e.g.：
    * 删除元组，以撤销插入元组的操作，允许提前释放在空间分配信息上的锁
    * 减去存入的金额，以撤销存款操作，允许提前释放在银行余额上的锁

即使对于具有逻辑撤销的操作，重做（Redo）信息也是**物理（Physically）** 记录的（即每次写入都有新值）

* 逻辑重做（Logical Redo）非常复杂，因为恢复开始时磁盘上的数据库状态可能不是“操作一致（Operation Consistent）”的
* 物理重做日志记录（Physical Redo Logging）与提前释放锁不冲突
***
### Operation Logging

操作日志记录的执行方式如下：

1.  当操作开始时，记录日志 $<T_i, O_j, \text{operation-begin}>$。这里的 $O_j$ 是操作实例的唯一标识符
2.  在操作执行期间，记录带有物理重做和物理撤销信息的正常日志记录
3.  当操作完成时，记录日志 $<T_i, O_j, \text{operation-end}, U>$，其中 $U$ 包含执行逻辑撤销所需的信息

- 如果崩溃/回滚发生在操作完成之前：**operation-end** 日志记录未找到，并且使用物理撤销信息来撤销操作
- 如果崩溃/回滚发生在操作完成之后：**operation-end** 日志记录被找到，在这种情况下使用 $U$ 执行逻辑撤销；该操作的物理撤销信息将被忽略

操作的重做（崩溃后）仍然使用物理重做信息
***
### Transaction Rollback with Logical Undo

事务 $T_i$ 的回滚执行方式如下：

- 向后扫描日志
	1.  如果找到日志记录 $<T_i, X, V_1, V_2>$，则执行撤销并记录 $<T_i, X, V_1>$
	2.  如果找到 $<T_i, O_j, \text{operation-end}, U>$ 记录
	    * 使用撤销信息 $U$ 逻辑地回滚该操作
	        * 回滚期间执行的更新会像正常操作执行期间一样被记录
	        * 在操作回滚结束时，不记录 **operation-end** 记录，而是生成一个记录 $<T_i, O_j, \text{operation-abort}>$
	    * 跳过 $T_i$ 的所有先前日志记录，直到找到记录 $<T_i, O_j, \text{operation-begin}>$
	3. 如果找到仅重做记录，则忽略它
	4. 如果找到 $<T_i, O_j, \text{operation-abort}>$ 记录：跳过 $T_i$ 之前的所有日志记录，直到找到 $<T_i, O_j, \text{operation-begin}>$ 记录
	5. 当找到 $<T_i, \text{start}>$ 记录时停止扫描
	6. 向日志中添加一条 $<T_i, \text{abort}>$ 记录

一些注意事项：

- 只有当数据库在事务回滚时崩溃，才会发生上述情况 c 和 d
- 像情况 d 那样跳过日志记录对于防止同一操作的多次回滚非常重要

!!! example "Example"

	=== "Transaction Rollback with Logical Undo"
	
		![](../../../assets/Pasted%20image%2020250527233317.png)
	
	=== "Failure Recovery with Logical Undo"
	
		![](../../../assets/Pasted%20image%2020250527233747.png)
***
### Recovery Algorithm with Logical Undo

基本与之前提到的算法相同，除了先前描述的事务回滚更改

1.  **（重做阶段）**：从最后一个 $<\text{checkpoint } L>$ 记录向前扫描日志直到日志末尾
    1.  通过物理上重做所有事务的所有更新来**重复历史记录**，
    2.  在扫描期间按如下方式创建一个 $\text{undo-list}$
        * $\text{undo-list}$ 最初设置为 $L$
        * 每当找到 $<T_i, \text{start}>$ 时，将 $T_i$ 添加到 $\text{undo-list}$
        * 每当找到 $<T_i, \text{commit}>$ 或 $<T_i, \text{abort}>$ 时，从 $\text{undo-list}$ 中删除 $T_i$
2.  **（撤销阶段）**：向后扫描日志，对在 $\text{undo-list}$ 中找到的事务的日志记录执行撤销操作。
	- 正在回滚的事务的日志记录在找到时按先前描述的方式处理
	    * 对所有正在撤销的事务进行单次共享扫描
    - 当为 $\text{undo-list}$ 中的事务 $T_i$ 找到 $<T_i, \text{start}>$ 时，写入一条 $<T_i, \text{abort}>$ 日志记录。
    - 当为 $\text{undo-list}$ 中的所有 $T_i$ 找到 $<T_i, \text{start}>$ 记录时停止扫描

这**将数据库带到崩溃时的状态**，已提交和未提交的事务都已被重做

现在 $\text{undo-list}$ 包含**不完整**的事务，即既未提交也未完全回滚的事务
***
## ARIES Recovery Algorithm

**ARIES** 是一种最先进的恢复方法

- 集成了许多优化，以减少正常处理期间的开销并加速恢复
- 我们之前研究的恢复算法是以 **ARIES** 为模型的，但通过移除优化大大简化了

与之前描述的恢复算法不同，**ARIES**：

1.  使用**日志序列号（LSN）** 来识别日志记录
    * 将 LSN 存储在页面中，以识别哪些更新已应用于数据库页面
2.  **生理性重做**
3.  **脏页表**以避免恢复期间不必要的重做
4.  **模糊检查点**，仅记录有关脏页的信息，并且不要求在检查点时间写出脏页

ARIES 使用多种数据结构：

- **日志序列号（LSN）** 标识每个日志记录
    * 必须是顺序递增的
    * 通常是日志文件开头的偏移量，以允许快速访问
        - 可以轻松扩展以处理多个日志文件
- **页面 LSN**
- **多种不同类型的日志记录**
- **脏页表**
***
### Page LSN

每个页面包含一个 **Page LSN**，它是其效果已反映在页面上的最后一条日志记录的 LSN

- 要更新一个页面：
    * 对页面进行 X-latch（异或锁存），并写入日志记录
    * 更新页面
    * 在 PageLSN 中记录日志记录的 LSN
    * 解锁页面
- 要将页面刷新到磁盘，必须首先对页面进行 S-latch（共享锁存）
    * 因此磁盘上的页面状态是操作一致的
        — 支持生理性重做所必需的
- **PageLSN** 在恢复期间用于防止重复重做
    * 从而确保**幂等性**
***
### Log Record

- 每个日志记录包含同一事务的先前日志记录的 LSN
	
	![](../../../assets/Pasted%20image%2020250531132804.png)
	
	- 日志记录中的 LSN 可能是隐式的

- 特殊只重做日志记录（称为**补偿日志记录，CLR**）用于记录恢复期间执行的、永远不需要撤销的操作
	- 扮演早期恢复算法中使用的操作中止日志记录的角色
	- 有一个字段 UndoNextLSN 来记录下一个（更早的）要撤销的记录
	    * 中间的记录应该已经被撤销了
	    * 为避免对已撤销操作的重复撤销所必需
	
	![](../../../assets/Pasted%20image%2020250531133000.png)
	
***
### DirtyPage Table

- 缓冲区中已更新页面的列表
- 对于每个这样的页面，包含
    * 页面的 **PageLSN**
    * **RecLSN** 是一个 LSN，使得此 LSN 之前的日志记录已应用于磁盘上的页面版本
        - 当页面插入脏页表时（在更新之前），设置到当前日志的末尾
        - 记录在检查点中，有助于最小化重做工作

![](../../../assets/Pasted%20image%2020250531133621.png)
***
### Checkpoint Log

- 包含:
    * DirtyPageTable (脏页表) 和活动事务列表
    * 对于每个活动事务，LastLSN，即该事务写入的最后一条日志记录的 LSN
- 磁盘上的固定位置记录了最后完成的检查点日志记录的 LSN
- 脏页在检查点时间不会被写出
    * 相反，它们在后台被持续刷新出去
* 因此检查点的开销非常低，我们可以频繁执行
***
### Algorithm

ARIES 恢复涉及三个阶段

- **Analysis pass (分析阶段)**: 确定
    - 哪些事务需要撤销 ($\text{undo-list}$)
    - 在崩溃时哪些页面是脏的（磁盘版本不是最新的）
	- $\text{RedoLSN}$: 应从中开始重做的 LSN
- **Redo pass (重做阶段)**:
	- **重复历史**，从 $\text{RedoLSN}$ 开始重做所有操作
        * 使用 $\text{RecLSN}$ 和 $\text{PageLSN}$ 来避免重做已反映在页面上的操作
- **Undo pass (撤销阶段)**:
	- 回滚所有未完成的事务
        * 其终止操作先前已完成的事务不会被撤销
            - 关键思想：无需撤销这些事务：早期的撤销操作已被记录，并按需重做

![](../../../assets/Pasted%20image%2020250531134639.png)
***
#### Analysis

- 从最后一个完整的检查点日志记录开始
    - 从日志记录中读取 $\text{DirtyPageTable}$
	- 设置 $\text{RedoLSN} = \min(\text{DirtyPageTable}中所有页面的 \text{RecLSN})$
        * 如果没有任何脏页，则 $\text{RedoLSN} = \text{检查点记录的 LSN}$
    - 设置 $\text{undo-list} = \text{检查点日志记录中的事务列表}$
    - 从检查点日志记录中读取 $\text{undo-list}$ 中每个事务的最后一条日志记录的 $\text{LSN}$
- 从检查点向前扫描
    - 如果发现任何不在 $\text{undo-list}$ 中的事务的日志记录，则将该事务添加到 $\text{undo-list}$
	- 每当找到更新日志记录时
        * 如果页面不在 $\text{DirtyPageTable}$ 中，则将其添加，并将 $\text{RecLSN}$ 设置为更新日志记录的 $\text{LSN}$
    - 如果找到事务结束日志记录，则从 $\text{undo-list}$ 中删除该事务
	- 跟踪 $\text{undo-list}$ 中每个事务的最后一条日志记录
        * 稍后的撤销操作可能需要
- 在分析阶段结束时：
    - $\text{RedoLSN}$ 决定从何处开始重做阶段
    - $\text{DirtyPageTable}$ 中每个页面的 $\text{RecLSN}$ 用于最小化重做工作
    - $\text{undo-list}$ 中的所有事务都需要回滚
***
#### Redo Pass

通过重放磁盘页面上尚未反映的每个操作来**重复历史**，如下所示：

- 从 $\text{RedoLSN}$ 向前扫描。每当找到更新日志记录时：
    1.  如果页面不在 $\text{DirtyPageTable}$ 中，或者日志记录的 $\text{LSN}$ 小于 $\text{DirtyPageTable}$ 中页面的 $\text{RecLSN}$，则跳过该日志记录
    2.  否则从磁盘获取页面。如果从磁盘获取的页面的 $\text{PageLSN}$ 小于日志记录的 $\text{LSN}$，则重做该日志记录

注意：如果任一测试为 Negative（条件不满足），则日志记录的效果已出现在页面上。第一个测试甚至避免了从磁盘获取页面！
***
#### Undo Actions

- 当对更新日志记录执行撤销操作时
    - 生成一个包含已执行撤销操作的 $\text{CLR}$（撤销期间执行的操作以物理或生理方式记录）。
        * 记录 $n$ 的 $\text{CLR}$ 在下图中记为 $n'$
    - 将 $\text{CLR}$ 的 $\text{UndoNextLSN}$ 设置为更新日志记录的 $\text{PrevLSN}$ 值
        * 箭头指示 $\text{UndoNextLSN}$ 值
- ARIES 支持**部分回滚**
    - 例如，用于通过回滚刚好足以释放所需锁定的方式来处理死锁
    - 图表指示部分回滚后的正向操作
        * 最初是记录 3 和 4，然后是 5 和 6，最后是完全回滚

![](../../../assets/Pasted%20image%2020250531135246.png)
***
#### Undo Pass

- 对日志执行向后扫描，撤销 $\text{undo-list}$ 中的所有事务
    - 通过跳过不需要的日志记录来优化向后扫描，如下所示：
        * 每个事务要撤销的下一个 $\text{LSN}$ 设置为分析阶段找到的该事务的最后一条日志记录的 $\text{LSN}$。
        * 在每一步中，选择这些 $\text{LSN}$ 中最大的一个进行撤销，跳回到它并执行撤销
        * 撤销一条日志记录后
	        - 对于普通日志记录，将事务要撤销的下一个 $\text{LSN}$ 设置为日志记录中注明的 $\text{PrevLSN}$
	        - 对于补偿日志记录 ($\text{CLR}$)，将要撤销的下一个 $\text{LSN}$ 设置为日志记录中注明的 $\text{UndoNextLSN}$
                - 所有中间记录都被跳过，因为它们应该已经被撤销了
- 按照先前描述的方式执行撤销






