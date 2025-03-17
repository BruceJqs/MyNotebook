---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
--- 

# Homework 06

## 5.6

> Consider the bank database of Figure 5.21. Let us define a view _branch_cust_ as 
> follows: 
> 
```sql
CREATE VIEW branch_cust AS 
	SELECT branch_name, customer_name
	FROM depositor, account
	WHERE depositor.account_number = account.account_number
```
>
> Suppose that the view is _materialized_; that is, the view is computed and stored.
> 
> Write triggers to _maintain_ the view, that is, to keep it up-to-date on insertions
> to _depositor_ or _account_. It is not necessary to handle deletions or updates. 
> 
> Note that, for simplicity, we have not required elimination of duplicates.
> 
> ![](../../../assets/Pasted%20image%2020250317205731.png)

```sql
create trigger insert_depositor after insert on depositor
referencing new row as nrow
for each row
insert into branch_cust
select branch_name, customer_name
from account
where nrow.account_number = account.account_number;

create trigger insert_account after insert on account
referencing new row as nrow
for each row
insert into branch_cust
select branch_name, customer_name
from depositor
where nrow.account_number = depositor.account_number;
```
***
## 5.15

> Consider an employee database with two relations:
>
> _employee(<u>employee_name</u>, street, city)_ <br>
> _works(<u>employee_name</u>,company_name, salary)_
>
> where the primary keys are underlined. Write a function _avg_salary_
> that takes a company name as an argument and finds the average salary of 
> employees at that company. Then, write an SQL statement, using that function, 
> to find companies whose employees earn a higher salary, on average, than
> the average salary at "First Bank."

```sql
create function avg_salary(company_name varchar(20))
	returns integer
	begin
		declare avg integer;
		select avg(salary) into avg
		from works
		where company_name = company_name;
		return avg;
	end;
	
select distinct company_name
from works
where avg_salary(company_name) > avg_salary('First Bank');
```
***
## 5.19

> Suppose there are two relations _r_ and _s_, such that the foreign key _B_ of _r_
> references the primary key _A_ of _s_. Describe how the trigger mechanism can be used
> to implement the **on delete cascade** option when a tuple is deleted from _s_. 

当一个元组从 s 中被删除后，触发器会被激活，触发器会删除所有在 r 中引用了这个元组的元组。这样就实现了级联删除的效果

