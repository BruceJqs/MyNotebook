---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
--- 

# Homework 14

## 18.1

> Show that the two-phase locking protocol ensures conflict serializability and that transactions can be serialized according to their lock points.

使用反证法。假设存在一个遵循两阶段封锁协议的调度 $S$，但它不是冲突可串行化的。这意味着其优先图 $G_S$​ 包含一个环

假设这个环是 $T_1​\rightarrow T_2​\rightarrow\cdots\rightarrow T_k​\rightarrow T_1​$ （其中 $k\geq 1$）

- 边 $T_i​\rightarrow T_{i+1}​$ （对于 $i=1,\cdots,k−1$）的存在意味着 $T_i​$ 中有一个操作 $op_i​(X)$ 在 $T_{i+1}​$ 中的某个操作 $op_{i+1}​(X)$ 之前执行，并且这两个操作在数据项 $X$ 上冲突。
- 类似地，边 $T_k​\rightarrow T_1​$ 的存在意味着 $T_k​$ 中有一个操作 $op_k​(Y)$ 在 T1​ 中的某个操作 $op_1​(Y)$ 之前执行，并且这两个操作在数据项 $Y$ 上冲突

考虑任意一条边 $T_i \rightarrow T_j$：

1. $T_i$ 执行了某个操作 $op_i(Q)$，之后 $T_j$ 执行了某个操作 $op_j(Q)$，这两个操作在数据项 $Q$ 上冲突
2. 为了执行 $op_i(Q)$，$T_i$ 必须持有对 $Q$ 的一个锁（称之为 $lock_i(Q)$）
3. 为了执行 $op_j(Q)$，$T_j$ 必须持有对 $Q$ 的一个与 $lock_i(Q)$ 不兼容的锁（称之为 $lock_j(Q)$）
4. 因此，$T_i$ 必须在 $T_j$ 获得 $lock_j(Q)$ 之前释放 $lock_i(Q)$
5. 根据两阶段封锁协议，$T_i$ 一旦释放了任何锁（如 $lock_i(Q)$），它就进入了收缩阶段，不能再获得任何新的锁。这意味着 $T_i$ 的锁点 $LP(T_i)$ 必定在释放 $lock_i(Q)$ 的时刻之前或之时发生。所以，$LP(T_i) \le \text{time}(\text{release } lock_i(Q))$
6. $T_j$ 必须在执行 $op_j(Q)$ 之前获得 $lock_j(Q)$。根据两阶段封锁协议，$T_j$ 获得锁是在其扩展阶段。所以，获得 $lock_j(Q)$ 的时刻必定在其锁点 $LP(T_j)$ 之前或之时发生。所以，$\text{time}(\text{acquire } lock_j(Q)) \le LP(T_j)$
7. 由于 $T_i$ 必须在 $T_j$ 获得 $lock_j(Q)$ 之前释放 $lock_i(Q)$，所以： 

$$
LP(T_i) \le \text{time}(\text{release } \text{lock}_i(Q)) < \text{time}(\text{acquire } \text{lock}_j(Q)) \le LP(T_j)
$$

因此，我们得出 $LP(T_i) < LP(T_j)$

现在回到优先图中的环 $T_1 \rightarrow T_2 \rightarrow \dots \rightarrow T_k \rightarrow T_1$。根据上面的推论： 

 - $T_1 \rightarrow T_2 \implies LP(T_1) < LP(T_2)$ 
 - $T_2 \rightarrow T_3 \implies LP(T_2) < LP(T_3)$ 
 - ... 
 - $T_{k-1} \rightarrow T_k \implies LP(T_{k-1}) < LP(T_k)$ 
 - $T_k \rightarrow T_1 \implies LP(T_k) < LP(T_1)$ 
 
 将这些不等式串联起来，我们得到： 
 
 $$
 LP(T_1) < LP(T_2) < \dots < LP(T_k) < LP(T_1)
 $$
  
  得到矛盾，假设不成立
  ***
## 18.7

> Consider a database system that includes an atomic increment operation, in addition to the read and write operations. Let $V$ be the value of data item X. The operation $\text{increment}(X)$ by C sets the value of $X$ to $V + C$ in an atomic step. The value of $X$ is not available to the transaction unless the latter executes a $\text{read}(X)$.
> 
> Assume that increment operations lock the item in increment mode using the compatibility matrix in Figure 18.25.
> 
> ![](../../../assets/Pasted%20image%2020250519203109.png)
> 
> a. Show that, if all transactions lock the data that they access in the corresponding mode, then two-phase locking ensures serializability.
> 
> b. Show that the inclusion of increment mode locks allows for increased concurrency.

（a）

我们构建一个优先图，图中的节点代表各个事务，如果存在一条从事务 $T_i$ 到事务 $T_j$ 的有向边（$T_i \rightarrow T_j$），这表示 $T_i$ 的某个操作与 $T_j$ 的某个操作在同一数据项上发生冲突，并且 $T_i$ 的操作先于 $T_j$ 的操作执行

*  假设我们有一个遵循 2PL 协议的调度，并且其优先图中存在一个环路，例如： 

$$
T_1 \rightarrow T_2 \rightarrow \dots \rightarrow T_k \rightarrow T_1
$$

* 边 $T_i \rightarrow T_j$ 意味着 $T_i$ 在某个数据项 $D$ 上执行了一个操作，之后 $T_j$ 在 $D$ 上执行了一个冲突操作。根据锁协议， $T_i$ 必须持有 $D$ 上的锁，并在其操作完成后（或在其缩减阶段的某个时刻）释放该锁，之后 $T_j$ 才能获取 $D$ 上的（冲突类型的）锁。因此，$T_i$ 对 $D$ 的解锁操作（记为 $\text{unlock}_i(D)$）必须早于 $T_j$ 对 $D$ 的加锁操作（记为 $\text{lock}_j(D)$）
* 所以，对于环路中的边： 
	* $T_1 \rightarrow T_2$ 意味着 $T_1$ 的某个解锁点早于 $T_2$ 的某个加锁点
	* $T_2 \rightarrow T_3$ 意味着 $T_2$ 的某个解锁点早于 $T_3$ 的某个加锁点
	* ... 
	* $T_k \rightarrow T_1$ 意味着 $T_k$ 的某个解锁点早于 $T_1$ 的某个加锁点
- 根据 2PL 的规则：
	* 当 $T_1$ 释放一个锁（为了让 $T_2$ 能够获取锁）时，$T_1$ 就进入了其缩减阶段
	* 考虑环路中的最后一条边 $T_k \rightarrow T_1$。这意味着 $T_k$ 释放了一个锁，然后 $T_1$ 获取了一个锁
	* 如果 $T_1$ 在其早期（为了 $T_1 \rightarrow T_2$）释放了一个锁，它就已经处于缩减阶段。在缩减阶段， $T_1$ 不能再获取任何新的锁。然而，为了完成 $T_k \rightarrow T_1$ 这条边所暗示的依赖关系，$T_1$ 必须在 $T_k$ 释放锁之后获取一个新的锁
	* 这就产生了一个矛盾：$T_1$ 在释放了一个锁之后（进入缩减阶段），又去获取了一个新的锁。这直接违反了 2PL 的核心规则

因此，如果所有事务都遵循 2PL，优先图中就不可能形成环路。由于优先图无环，所以任何由 2PL 允许的调度都是可串行化的

（b）与仅使用共享锁（S-lock）和排他锁（X-lock）的传统并发控制情况进行对比

**如果仅使用 S 锁和 X 锁**：

* 一个增量操作，例如将数据项 $X$ 的值 $V$ 更新为 $V+C$ (表示为 $X \leftarrow X+C$ 或 $V \leftarrow V+C$），本质上包含以下步骤：
    1.  读取 $X$ 的当前值
    2.  计算新值
    3.  写入 $X$ 的新值
* 为了确保这个读-修改-写序列的原子性和隔离性（防止其他事务读取中间值或干扰更新），事务通常需要获取对数据项 $X$ 的**排他锁（X-lock）**
    * 如果只用 S-lock，它允许多个事务同时读取，但不能阻止其他事务也尝试修改，可能导致丢失更新或不一致的结果
* 因此，如果两个事务 $T_1$ 和 $T_2$ 都希望对同一个数据项 $X$ 执行增量操作，它们都需要获取 X-lock。如果 $T_1$ 持有 X-lock，$T_2$ 必须等待 $T_1$ 完成并释放该锁。这意味着对同一数据项的多个增量操作会被串行化，从而限制了并发性

**如果引入增量模式锁（I-lock）**：

* 这意味着如果事务 $T_1$ 想要对数据项 $X$ 执行增量操作并持有了 I-lock，事务 $T_2$ 也可以**同时**获取数据项 $X$ 的 I-lock 并执行其增量操作
* 由于多个事务可以并发地持有对同一数据项的 I-lock 并执行增量操作，它们不需要像在仅有 X-lock 的情况下那样互相等待。这直接导致了并发性的提高，特别是在存在大量针对同一数据项的原子增量/减量操作（如更新计数器、统计数据等）的工作负载中

这说明引入 I-lock 显著提高了并发处理能力
***
## 18.18

> Most implementations of database systems use strict two-phase locking. Suggest three reasons for the popularity of this protocol.

- **保证严格调度，避免连锁回滚：** 严格两阶段锁定协议规定，事务持有的所有排他锁（写锁）必须在事务提交（Commit）或中止（Abort）之后才能释放。这意味着，一个事务在修改数据后，直到它成功提交，其他任何事务都不能读取或覆盖这些被修改的数据。如果一个事务中止了，它不会影响到其他已经读取了其未提交数据的事务，因为根本没有其他事务能读取到这些未提交的数据。这就避免了“连锁回滚”的发生
- **保证可串行化：** 与基本的两阶段锁定一样，严格两阶段锁定能够保证并发事务执行的结果是可串行化的
- **实现相对简单且高效：** 相比于其他一些并发控制技术，两阶段锁定（包括其严格版本）在概念上更为直观，其机制主要依赖于锁的获取和释放，逻辑清晰，易于管理和调试，并且在数据库管理系统的锁管理器中实现起来相对容易