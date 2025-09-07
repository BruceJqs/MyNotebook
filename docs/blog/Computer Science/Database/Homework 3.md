---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
# comments: true
--- 

# Homework 03

## 3.8

> Consider the bank database of Figure 3.18, where the primary keys are underlined. Construct the following SQL queries for this relational database.  
> 
> a. Find the ID of each customer of the bank who has an account but not a loan.  
> 
> b. Find the ID of each customer who lives on the same street and in the same city as customer '12345'.  
> 
> c. Find the name of each branch that has at least one customer who has an account in the bank and who lives in "Harrison".
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
select ID from depositor
except (select ID from borrower);
```

(b)

```sql
select F.ID 
from customer as F, customer as T
where F.customer_street = T.customer_street and
	F.customer_city = T.customer_city and
	T.ID = '12345';
```

(c)

```sql
select distinct branch_name
from account, depositor, customer
where customer.ID = depositor.ID and
	account.account_number = depositor.account_number and
	customer.customer_city = 'Harrison';
```
***
## 3.9

> Consider the relational database of Figure 3.19, where the primary keys are underlined. Give an expression in SQL for each of the following queries.
> 
> a. Find the ID, name, and city of residence of each employee who works for "First Bank Corporation".  
> 
> b. Find the ID, name, and city of residence of each employee who works for "First Bank Corporation" and earns more than $10000. 
>  
> c. Find the ID of each employee who does not work for "First Bank Corporation".  
> 
> d. Find the ID of each employee who earns more than every employee of "Small Bank Corporation".  
> 
> e. Assume that companies may be located in several cities. Find the name of each company that is located in every city in which "Small Bank Corporation" is located.  
> 
> f. Find the name of the company that has the most employees (or companies, in the case where there is a tie for the most).  
> 
> g. Find the name of each company whose employees earn a higher salary, on average, than the average salary at "First Bank Corporation".
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
select e.ID, e.person_name, e.city
from employee as e, works as w
where e.ID = w.ID and
	w.company_name = 'First Bank Corporation';
```

(b)

```sql
select e.ID, e.person_name, e.city
from employee as e, works as w
where e.ID = w.ID and
	w.company_name = 'First Bank Corporation' and
	w.salary > 10000;
```

(c)

```sql
select ID from works
where company_name <> 'First Bank Corporation';
```

(d)

```sql
select ID from works
where salary > all (
	select salary from works 
	where company_name = 'Small Bank Corporation');
```

(e)

```sql
select c1.company_name
from company as c1
where not exists(
	select city from company
	where company_name = 'Small Bank Corporation')
	except(
	select city from company as c2
	where c1.company_name = c2.company_name);
```

(f)

```sql
select company_name
from works
group by company_name
having count(distinct ID) >= all(
	select count(distinct ID) from works
	group by company_name);
```

(g)

```sql
select company_name
from works
group by company_name
having avg(salary) > (
	select avg(salary) from works
	where company_name = 'First Bank Corporation');
```
