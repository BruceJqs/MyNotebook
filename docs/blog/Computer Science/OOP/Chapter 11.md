---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
--- 

# Chapter 11 : Smart Pointers

!!! abstract "Abstract"

	在标准库中，有一些原始指针：
	
	- `std::unique_ptr`：独占所有权，不能被复制
	- `std::shared_ptr`：共享所有权，可以被复制
	- `std::weak_ptr`：不拥有所有权，不能被复制
	- `std::auto_ptr`：过时的智能指针，不能被复制，在 C++11 中被删除


