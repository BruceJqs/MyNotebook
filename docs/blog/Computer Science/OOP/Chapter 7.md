---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
--- 

# Chapter 07 : Copy Constructor

## Copying

> 复制构造函数（Copy Constructor）是一个特殊的构造函数，用于创建一个对象作为另一个对象的副本，经常会出现在函数被调用传递参数时

复制构造函数有唯一的签名：`T::T(const T&)`，即一个参数是引用类型的对象

- 如果没有给拷贝一个构造函数，C++ 会自动创造一个
- 如果有成员是一个对象，会调用对象自己的拷贝函数
- 如果有成员变量是指针，会和原来对象一样指向同一块内存。如果有一个对象被析构，那么这块内存就被 delete, 这就变成了无效内存
- 因此我们不一定要有拷贝构造函数，有指针时必须要有

!!! example "Example"

	我们有如下代码：
	
	```c++
	#include <cstring>
	#include <iostream>
	using namespace std;
	
	struct Person {
	    char * name;
	    Person(const char* s) {
	        name = new char[strlen(s) + 1];
	        strcpy(name, s);
	    }
	    ~Person() {
	        delete[] name;
	    }
	};
	
	int main() {
	    Person p1("Trump");
	    Person p2 = p1;
	
	    cout << (void*)p1.name << endl;
	    cout << (void*)p2.name << endl;
	}
	```
	
	运行结果：
	
	![](../../../assets/Pasted%20image%2020250414135033.png)
	
	可以看到我们并没有写复制构造函数，这是 C++ 默认帮我们写好的，同时 `p2 = p1` 使用了复制构造，所以 `p2` 和 `p1` 指向同一块内存，导致 `delete[] name` 语句执行了两次，出现内存错误


