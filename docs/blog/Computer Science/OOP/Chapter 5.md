---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
# comments: true
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

- `class` 默认为 `private`，`struct` 默认为 `public`

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

C++ 在访问保护当中还有令一种关键词为 `friend`，可以让一个函数或者类访问另一个类的私有成员

- 由类本身来控制访问权限
- `friend` 可以是：
	- 一个函数
	- 一个成员函数或者其他类
	- 甚至是整个类

??? tip "Tips"

	事实上，private 并非真正的无法访问，它只是对类来说无法访问而非对象
	
	我们事实上可以通过指针来变相地绕过 private 来访问成员（这需要我们通过猜测类的地址来获取）
	
	cx 说这就是破解软件的原理，但不鼓励我们去做这玩意，~~因为没前途~~因为都慢慢开始开源了
***
### Initialization

!!! question "思考"

	从父类继承而来的子类，会拥有父类的成员变量和函数，也会有自己特制的成员变量和函数，那么他们都该如何进行初始化呢？

!!! example "Example"

	```c++
	#include <iostream>
	using namespace std;
	
	struct Base{
	public:
	    Base(int i) : data(i) {cout << "Base::Base()" << endl;}
	    ~Base() {cout << "Base::~Base()" << endl;}
	    void print() {cout << "Base::print()" << endl;}
	protected:
	    void setdata(int i) {data = i;}
	private:
	    int data;
	};
	
	struct Derived : public Base{
	    Derived() : name("zju"), address("hangzhou") {}
	    void foo(){
	        setdata(30);
	        print();
	    }
	private:
	    string name;
	    string address;
	};
	    
	int main(){
	    Derived d;
	    d.print();
	    return 0;
	}
	```
	
	在子类中，如果我们只初始化自己的成员变量，那么会发生报错：
	
	![](../../../assets/Pasted%20image%2020250331134224.png)
	
	这是因为我们没给父类进行初始化，编译器走默认构造函数，却发现我们也没有定义默认构造函数，因此，我们需要在子类的构造函数当中也顺便执行父类的构造函数：
	
	```c++
	...
		Derived() : name("zju"), address("hangzhou"), Base(10){
	        cout << "Derived::Derived()" << endl;
	    }
	    ~Derived() {
	        cout << "Derived::~Derived()" << endl;
	    }
	...
	```
	
	![](../../../assets/Pasted%20image%2020250331134621.png)
	
	这里我们同时也加上了子类的析构函数，也可以看到程序这些函数的运行顺序。

根据上面的例子，我们可以有：

- 子类在初始化时也需要调用父类的构造函数，如果父类的构造函数不是默认的也需要在子类调用
- 基类的构造函数最先执行，然后是派生类的构造函数

另外，如果我们在子类中重定义成员函数，那么其他父类的重载函数都会变得不可访问
