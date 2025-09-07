---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
# comments: true
--- 

# Homework 05

## 4.7

> Consider the employee database of Figure 4.12. Give an SQL DDL definition of this database. Identify referential-integrity constraints that should hold, and include them in the DDL definition.
> 
> employee (<u>ID</u>, person_name, street, city)
> 
> works (<u>ID</u>, company_name, salary)
> 
> company (<u>company_name</u>, city)
> 
> manages (<u>ID</u>, manager_id)

```sql
create table employee(
	ID integer,
	person_name varchar(20),
	street varchar(20),
	city varchar(20),
	primary key (ID)
);

create table works(
	ID integer,
	company_name varchar(20),
	salary integer,
	primary key (ID),
	foreign key (ID) references employee(ID),
	foreign key (company_name) references company(company_name)
);

create table company(
	company_name varchar(20),
	city varchar(20),
	primary key (company_name)
);

create table manages(
	ID integer,
	manager_id integer,
	primary key (ID),
	foreign key (ID) references employee(ID),
	foreign key (manager_id) references employee(ID)
);
```
***
## 4.9

> SQL allows a foreign-key dependency to refer to the same relation, as in the following
> example: 
> 
> ```sql
> create table manager ( 
>     employee_id char(20),
>     manager_id char(20), 
>     primary key employee_id,
>     foreign key (manager_id) references manager (employee_id)
>         on delete cascade
> ); 
> ```
> Here, _employee_id_ is a key to the table _manager_, meaning that each employee has at 
> at most one manager. The foreign-key clause requires that every manager also be an employee. 
> Explain exactly what happens when a tuple in the relation _manager_ is deleted. 

当删除 manager 当中的一个元组后，这个 manager 的直系下属对应的元组会被删除，这样会造成链式反应，导致 manager 的二级下属对应的元组被删除，最后和这个 manager 下级的所有 employee 相关的元组都会被删除
***
## 4.12

> Suppose a user wants to grant **select** access on a relation to another user. Why should the user include (or not include) the clause **granted by current role** in the **grant** statement?

如果这次授予权限是基于当前角色，那么当当前角色被删除或者改动时，权限也会仍旧生效，这样可以保证权限的稳定性

