---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
--- 

# Chapter 05 : Composition & Inheritance

## Composition

> **组合**（Composition）：从已存在的对象中构造新的对象，即复用已有的实现

- 包含（Inclusion）方式：
    - **完全**（Fully）包含
        - 构造函数和析构函数会被自动调用
    - **引用**（Reference）包含
        - 需要手动初始化和销毁对象
- 嵌入对象（Embedded Objects）：
    - 所有的嵌入对象都必须被初始化
        - 当不提供参数时，默认的构造函数（或者自己创建的构造函数）就会被调用
    - 构造函数可以用初始化列表
	    - 可以给子构造函数传递参数
    - 析构函数会被自动调用
***
## Inheritance

> **继承**（Inheritance）：从已存在的类中克隆新的类并扩展

- 定义一个基类（Base class，或称为超类），用于定义共同属性
- 定义多个派生类（Derived Class，或称为子类），用于继承基类的属性，并添加自己的属性
- 派生类通过 `:` 指定基类，例如 `class Derived : public/protected/private Base`
	- 默认为 `private`

### Scopes and Access

- 对于继承类型的不同，访问权限也不同：

| 关键词       | 在同一个类中 | 在派生类中 | 在类外 |
| --------- | ------ | ----- | --- |
| private   | Yes    | No    | No  |
| protected | Yes    | Yes   | No  |
| public    | Yes    | Yes   | Yes |

***
!!! example "Example"

	```c++
	#include <iostream>
	using namespace std;
	
	struct Base{
	public:
	    Base() : data(10) {cout << "Base::Base()" << endl;}
	    ~Base() {cout << "Base::~Base()" << endl;}
	    void print() {cout << "Base::print()" << endl;}
	    void setdata(int i) {data = i;}
	private:
	    int data;
	};
	
	struct Derived : public Base{
	    void foo(){
	        setdata(30);
	        print();
	    }
	};
	    
	int main(){
	    Derived d;
	    d.setdata(20);
	    d.foo();
	    d.print();
	    return 0;
	}
	```
	
	![](../../../assets/Pasted%20image%2020250325140352.png)
	
	但是如果我们在 `foo()` 中添加一句 `data *= 2`，则会报错：
	
	![](../../../assets/Pasted%20image%2020250325140512.png)
	
	但是如果我们将 `data` 从 `private` 改为 `protected`，则又可以正常运行了
