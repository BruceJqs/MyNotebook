---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
# comments: true
--- 

# Homework 04

## 3.10

> Consider the relational database of Figure 3.19. Give an expression in SQL for each of the following : 
> 
> a. Modify the database so that the employee whose ID is '12345' now lives in “Newtown"
> 
> b. Give each manager of "First Bank Corporation" a 10 percent raise unless the salary becomes greater than $100000; in such cases, give only a 3 percent raise.
> 
> employee (<u>ID</u>, person_name, street, city)
> 
> works (<u>ID</u>, company_name, salary)
> 
> company (<u>company_name</u>, city)
> 
> manages (<u>ID</u>, manager_id)

(a)

```sql
update employee
set city = 'Newtown'
where ID = '12345';
```

(b)

```sql
update works
set salary = salary * (
	case
		when salary * 1.1 <= 100000 then 1.1
		else 1.03
	end
)
where company_name = 'First Bank Corporation' and ID in (
	select manage_id from manages
);
```

## 3.11

> Write the following queries in SQL, using the university schema. 
> 
> a. Find the ID and name of each student who has taken at least one Comp. Sci. course; make sure there are no duplicate names in the result.
> 
> b. Find the ID and name of each student who has not taken any course offered before 2017.
> 
> c. For each department, find the maximum salary of instructors in that department. You may assume that every department has at least one instructor.
> 
> d. Find the lowest, across all departments, of the per-department maximum salary computed by the preceding query.

(a)

```sql
select distinct student.ID, student.name
from student join takes on student.ID = takes.ID
join course on takes.course_id = course.course_id
where course.dept_name = 'Comp. Sci.';
```

(b)

```sql
select ID, name
from student as s
where not exists(
	select * from takes as t
	where s.ID = t.ID and year < 2017
);
```

(c)

```sql
select dept_name, max(salary)
from instructor
group by dept_name;
```

(d)

```sql
with max_salary as (
	select dept_name, max(salary)
	from instructor
	group by dept_name
)
select min(max_salary)
from max_salary;
```
***
## 3.15

> Consider the bank database of Figure 3.18, where the primary keys are underlined. Construct the following SQL queries for this relational database.
> 
> a. Find each customer who has an account at _every_ branch located in "Brooklyn".  
> 
> b. Find the total sum of all loan amounts in the bank.  
> 
> c. Find the names of all branches that have assets greater than those of at least one branch located in "Brooklyn"
> 
> branch(<u>branch name</u>, branch_city, assets)
> 
> customer(<u>ID</u>, customer_name, customer_street, customer_city)
> 
> loan(<u>loan_number</u>, branch name, amount)
> 
> borrower(<u>ID</u>, <u>loan number</u>)
> 
> account(<u>account_number</u>, branch_name, balance)
> 
> depositor(<u>ID</u>, <u>account_number</u>)

(a)

```sql
with brooklyn_branch as (
	select branch_name
	from branch
	where branch_city = 'Brooklyn'
)
select ID, customer_name
from customer
where not exists(
	select branch_name from brooklyn_branch
	except
	select branch_name from account join depositor on account.account_number = depositor.account_number
	where customer.ID = depositor.ID
);
```

(b)

```sql
select sum(amount)
from loan;
```

(c)

```sql
select branch_name
from branch
where assets > some(
	select assets
	from branch
	where branch_city = 'Brooklyn'
);
```
