---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
# comments: true
--- 

# Homework 01

## 1.7

> List four significant differences between a file-processing system and a DBMS.

- 数据结构：文件处理系统使用简单的文件结构，缺乏复杂的数据关系；而 DBMS 使用复杂的数据模型，允许数据间建立关系
- 数据冗余：文件处理系统冗余导致数据重复，造成数据冗余，增加存储和维护压力；而 DBMS 减少冗余，提高数据存储效率
- 数据一致性：文件处理系统难以确保数据一致；而 DBMS 通过事务管理和约束机制，确保数据一致性
- 并发访问：文件处理系统不可避免地会造成并发访问冲突；而 DBMS 则不会造成冲突
***
## 1.8

> Explain the concept of physical data independence and its importance in database systems.

- 概念：物理数据独立指在不更改逻辑架构的情况下修改物理架构的能力
- 重要性：物理数据独立性高的数据库系统各层级与组件之间的接口较为清晰，组件或者是层级的变化不会严重影响其他部分，这样就可以层次分明
***
## 1.9

> List five responsibilities of a database-management system. For each responsibility, explain the problems that would arise if the responsibility were not discharged.

- 并发控制：DBMS 允许多个用户同时访问和操作数据库，同时确保数据的一致性；如果没有并发控制，多个用户同时修改数据可能会导致数据的不一致性，从而发生更多错误
- 数据完整性：DBMS 需要保证数据的完整性，满足预定义的规则和约束，防止无效或不完整数据进入系统；如果没有满足数据完整性，那么数据质量会下降
- 数据安全：DBMS 需要控制访问机制保护数据，只有授权用户可以访问或者修改授权的数据；如果不满足数据安全性，那么用户隐私数据将会被非授权用户窃取，造成数据安全问题
- 减少数据冗余：DBMS 需要通过规范化设计来减少数据冗余，这有助于提高存储效率；如果没有规范化设计，那么会导致存储空间浪费，维护成本增加
- 备份与恢复：DBMS 需要有可靠的备份与恢复机制；如果没有，那么会导致在灾难或者硬件故障中数据的丢失
***
## 1.15

> Describe at least three tables that might be used to store information in a social-networking system such as Facebook.

- 存储用户信息的表格，包含用户名、邮箱、密码、手机号等信息
- 存储好友关系的表格，记录用户之间的好友关系
- 存储用户消息的表格，记录用户的私信消息

