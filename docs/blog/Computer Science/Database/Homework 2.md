---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
# comments: true
--- 

# Homework 02

## 2.7

> Consider the bank database of Figure 2.18. Give an expression in the relation algebra for each of the following queries:
> 
> a. Find the name of each branch located in "Chicago"
 >
 >b. Find the ID of each borrower who has a loan in branch "Downtown"
>
> branch(branch_name, branch_city, assets)
> 
> customer(ID, customer_name, customer_street, customer_city)
> 
> loan(loan_number, branch_name, amount)
> 
> borrower(ID, loan_number)
> 
> account(account_number, branch_name, balance)
> 
> depositor(ID, account_number)

(a) $\prod_{\text{branch_name}}(\sigma_{\text{branch_city}=\text{“Chicago”}}(\text{branch}))$

(b) $\prod_{ID}(\text{borrower}\Join\sigma_{\text{loan.branch_name}=\text{“Downtown”}}(\text{loan}))$
***
## 2.12

> Consider the bank database of Figure 2.18. Assume that branch names and customer names uniquely identify branches and customers, but loans and accounts can be associated with more than one customer.
>
> a. What are the appropriate primary keys?
> 
> b. Given your choice of primary keys, identify appropriate foreign keys.

(a) 下划线为主键

branch(<u>branch_name</u>, branch_city, assets)

customer(<u>ID</u>, customer_name, customer_street, customer_city)

loan(<u>loan_number</u>, branch_name, amount)

borrower(<u>ID, loan_number</u>)

account(<u>account_number</u>, branch_name, balance)

depositor(<u>ID, account_number</u>)

(b) 对于 loan 来说，外键为 branch_name，引用 branch

对于 borrower 来说，外键为 ID，引用 customer；外键为 loan_number，引用 loan

对于 account 来说，外键为 branch_name，引用 branch

对于 depositor 来说，外键为 ID，引用 customer；外键为 account_number，引用 account
***
## 2.13

> Construct a schema diagram for the bank database of Figure 2.18.

![](../../../assets/Pasted%20image%2020250606153613.png)

***
## 2.15

> Consider the bank database of Figure 2.18. Give an expression in the relational algebra for each of the following queries:
> 
> a. Find each loan number with a loan amount greater than $10000
> 
> b. Find the ID of each depositor who has an account with a balance greater than $6000
> 
> c. Find the ID of each depositor who has an account with a balance greater than $6000 at the "Uptown" branch

(a) $\prod_{\text{loan_number}}(\sigma_{\text{amount}>10000}(\text{loan}))$

(b) $\prod_{ID}(\sigma_{\text{balance}>6000}(\text{account}\Join\text{depositor}))$

(c) $\prod_{ID}(\sigma_{\text{balance}>6000\land\text{branch_name}=\text{“Uptown”}}(\text{account}\Join\text{depositor}))$




