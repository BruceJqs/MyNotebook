---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
--- 

# Homework 02

## 2.7

> Consider the bank database of Figure 2.18. Give an expression in the relation algebra for each of the following queries:
> 
 a. Find the name of each branch located in "Chicago"
 b. Find the ID of each borrower who has a loan in branch “Downtown"
>
> branch(branch_name, branch_city, assets)
> customer(ID, customer_name, customer_street, customer_city)
> loan(loan_number, branch_name, amount)
> borrower(ID, loan_number)
> account(account_number, branch_name, balance)
> depositor(ID, account_number)

(a) $\prod_{\text{branch\_name}}(\sigma_{\text{branch\_city}=\text{“Chicago”}}(\text{branch}))$

(b) $\prod_{ID}(\)$




