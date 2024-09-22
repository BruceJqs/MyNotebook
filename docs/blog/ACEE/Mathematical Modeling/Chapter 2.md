---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
---  
# Chapter 02 : 数学规划
## 运筹学

运筹学的主要分支：

- 数学规划（Mathematical Programming）
    - 线性规划（Linear Programming）
    - 非线性规划（Nonlinear Programming）
    - 整数规划（Integer Programming）
    - 多目标规划（Multiobjective Programming）
- 组合优化（Combinatorial Optimization）
- 随机运筹
    - 排队论（Queuing Theory）
    - 库存论（Inventory theory）
    - 可靠性理论（Reliability Theory）
- 博弈论（Game Theory）与决策理论（Decision Theory）
***
## 数学规划

- 若干个变量在满足一些等式或不等式限制条件下，使目标函数取得最大值或最小值
- 研究问题的数学性质，构造求解问题的方法，实现求解问题的算法，以及将算法应用于实际问题

![](../../../assets/Pasted%20image%2020240922143328.png)

!!! 数学规划分类

	=== "按函数性质"
	
		- 线性规划（linear programming）
		    - 目标函数为线性函数，约束条件为线性等式或不等式
		- 非线性规划（nonlinear programming）
		    - 目标函数为非线性函数，或至少有一个约束条件为非线性等式或不等式
		        - 二次规划（Quadratic Programming, QP）：目标函数为二次函数，约束条件为线性等式或不等式
		        - 带二次约束的二次规划（Quadratically Constrained Quadratic Program， QCQP）：目标函数为二次函数，约束条件为线性或二次等式或不等式
		        - 线性分式规划（linear fractional programming）：目标函数为两个线性函数的商，约束条件为线性等式或不等式
	
	=== "按变量性质"
	
		整数规划（integer programming）：至少有一个决策变量限定取整数值 
		
		- 整数决策变量意义 
		- 用于表示只能取离散值的对象的数量
		- 用于表示约束条件之间的逻辑关系或复杂的函数形式
		- 用于表示非数值的优化或可行性问题
		- 特殊整数规划 
		- 部分决策变量取整数值的数学规划特称为混合整数规划（Mixed Integer Programming, MIP） 
		- 0-1规划：决策变量仅取值0或1的数学规划
	
	=== "按约束条件"
	
		- 无约束优化
		- 约束优化