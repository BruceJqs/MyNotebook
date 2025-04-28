---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
--- 

# Homework 08

## 7.1

> Suppose that we decompose the schema $R = (A, B, C, D, E)$ into 
> 
 $$
 \begin{aligned}
 (A, B, C) \\
 (A, D, E)
 \end{aligned}
 $$
> 
> Show that this decomposition is a lossless decomposition if the following
> set $F$ of functional dependencies holds: 
> 
 $$
 \begin{aligned}
 A \rightarrow BC   \\
 CD \rightarrow E  \\
 B \rightarrow D  \\
 E \rightarrow A  \\
 \end{aligned}
 $$

$R_1\cap R_2=A$，根据给定的函数依赖我们有：

$$
\begin{aligned}
A\rightarrow BC\Rightarrow A\rightarrow B,A\rightarrow C\\
A\rightarrow B, B\rightarrow D\Rightarrow A\rightarrow D\\
A\rightarrow C\Rightarrow A\rightarrow CD\\
A\rightarrow CD, CD\rightarrow E\Rightarrow A\rightarrow E\\
\end{aligned}
$$

所以 A 为候选键，即 $R_1\cap R_2\rightarrow R_1$，所以这个分解是无损分解
***
## 7.13

> Show that the decomposition in Exercise 7.1 is not a dependency-preserving 
> decomposition.

对于 $R_1$ 来说，令 $\text{result}=CD,\text{result}\cup((\text{result}\cap R_1)_F^+\cap R_1)=\{C,D\}$

对于 $R_2$ 来说，令 $E\notin\text{result}=CD,\text{result}\cup((\text{result}\cap R_2)_F^+\cap R_1)=\{C,D\}$

所以这个分解不是依赖保持分解
***
## 7.21

> Give a lossless decomposition into BCNF of schema $R$ of Exercise 7.1. 

首先 E 为超键，那么选 $CD\rightarrow E$

对于 $\{A,B,C,D\}$ 来说 A/CD 是超键，选 $B\rightarrow D$

分解为 $\{C,D,E\},\{B,D\},\{A,B,C\}$
***
## 7.22

> Give a lossless, dependency-preserving decomposition into 3NF of schema $R$ of Exercise 7.1.

候选键为 A,E

$F_c=F=\{A\rightarrow BC,CD\rightarrow E,B\rightarrow D,E\rightarrow A\}$

对于 $A\rightarrow BC$，$R_1=(A,B,C)$

对于 $CD\rightarrow E$，$R_2=(C,D,E)$

对于 $B\rightarrow D$，$R_3=(B,D)$

对于 $E\rightarrow A$，$R_4=(E,A)$
***
## 7.30

> Consider the following set $F$ of functional dependencies on the relation 
> schema $(A, B, C, D, E, G)$: 
> 
 $$
 \begin{aligned}
 A \rightarrow BCD \\
 BC \rightarrow DE \\
 B \rightarrow D \\
 D \rightarrow A \\
 \end{aligned}
 $$
> 
> a. Compute $B^+$.
> 
> b. Prove (using Armstrong's axioms) that $AG$ is a superkey. 
> 
> c. Compute a canonical cover for this set of functional dependencies $F$; give
> each step of your derivation with an explanation. 
> 
> d. Give a 3NF decomposition of the given schema based on a canonical cover. 
> 
> e. Give a BCNF decomposition of the given schema using the original set $F$ 
> of functional dependencies. 

（a）$B^+=ABCDE$

（b）

$$
\begin{aligned}
A\rightarrow BCD&\Rightarrow A\rightarrow BC\\
A\rightarrow BC,BC\rightarrow DE&\Rightarrow A\rightarrow DE\\
A\rightarrow DE,A\rightarrow BCD&\Rightarrow A\rightarrow ABCDE\Rightarrow AG\rightarrow ABCDEG
\end{aligned}
$$

由上可得 AG 为超键

（c）因为 $D\in A_{F_c'}^+=ABCDE,D\in BC_{F_c'}^+=ABCDE$，所以 D 在 $A\rightarrow BCD$ 和 $BC\rightarrow DE$ 都是多余的

因为 $C\in B_{F_c'}^+=ABCDE$，所以 C 在 $BC\rightarrow E$ 中是多余的

得到 $F=\{A\rightarrow BC,B\rightarrow E,B\rightarrow D,D\rightarrow A\}$

合并 $B\rightarrow E,B\rightarrow D$ 可以得到 $F=\{A\rightarrow BC,B\rightarrow DE,D\rightarrow A\}$

（d）候选键为 AG/BG/DG

对 $A\rightarrow BC$，$R_1=(A,B,C)$

对 $B\rightarrow DE$，$R_2=(B,D,E)$

对 $D\rightarrow A$，$R_3=(D,A)$

对 $AG$，$R_4=(A,G)$

（e）超键为 $A,B,D$

对于 $BC\rightarrow DE$，选 $BC\rightarrow DE$，$R_1=(B,C,D,E)$

剩下的为 $(A,B,C,G)$，选择 $B\rightarrow A,A\rightarrow BC$

所以最后为 $R_1=(B,C,D,E),R_2=(A,B,C,G)$


