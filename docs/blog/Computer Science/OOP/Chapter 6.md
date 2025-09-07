---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
# comments: true
--- 

# Chapter 06 : Polymorphism

## Upcasting

> 向上转型指的是将子类的一个对象也视为父类的一个对象

- 向上转型只能通过指针或者引用来实现
- 但是会失去关于对象的类型信息

```c++
Manager pete( "Pete", "444-55-6666", "Bakery");
Employee* ep = &pete; // Upcast
Employee& er = pete;  // Upcast

ep->print(cout); // The base print() is called
```
***
## Polymorphic

**多态变量**（Polymorphic Variable）：

- 对象的指针或引用变量是多态变量
- 这些变量保留了对象的声明类型及其子类型

**多态**（Polymorphism）包括：

- 向上转型：将派生类的对象作为基类的对象
- 动态绑定：绑定被调用的函数
    - 静态绑定：调用作为代码的函数
    - 动态绑定：调用对象的函数

!!! example "Example"

	我们有如下代码：
	
	```c++
	#include <iostream>
	using namespace std;
	
	class Shape{
	public:
	    void move(){
	        cout << "Shape::move()" << endl;
	    }
	    void render(){
	        cout << "Shape::render()" << endl;
	    }
	};
	
	class Ellipse : public Shape{
	public:
	    void render(){
	        cout << "Ellipse::render()" << endl;
	    }
	};
	
	class Circle : public Ellipse{
	public:
	    void render(){
	        cout << "Circle::render()" << endl;
	    }
	};
	
	void foo(Shape *p){
	    p->move();
	    p->render();
	}
	
	int main(){
	    Ellipse e;
	    Circle c;
	    foo(&e);
	    foo(&c);
	    return 0;
	}
	```
	
	希望能在调用 `foo` 函数时，根据对象的实际类型来调用 `render` 函数，但是事实上：
	
	![](../../../assets/Pasted%20image%2020250331143526.png)
	
	它一直在调用 `Shape` 的 `render` 函数，这是因为这是一种利用指针的静态绑定，即在编译时就已经确定了调用的函数，而不是在运行时根据对象的实际类型来调用函数
***
### Virtual Functions

**虚函数**（Virtual Functions）：

- 非虚函数：编译器为指定类型生成静态或直接的调用，它执行更快
- 虚函数：
    - 在派生类中能被**透明地**（Transparently）重写
    - 对象携带一组虚拟函数
    - 编译器检查这组虚拟函数，并动态调用正确的函数
    - 如果编译器在编译时知道函数，那么就会生成静态调用

多态变量（Polymorphic Variables）：

- 对象的指针或引用变量是多态变量
- 它们可以保存声明类型的对象，或声明类型的子类型的对象

对于上面这个例子，我们在 `Shape` 类的 `render` 函数前加上 `virtual` 关键字：

```c++
...
	virtual void render(){
	    cout << "Shape::render()" << endl;
	}
...
```

这时我们再运行程序，便会得到想要的结果：

![](../../../assets/Pasted%20image%2020250331144131.png)

这样，当形状非常多的时候，我们就可以进行批量的管理了：

```c++
#include <iostream>
#include <vector>
using namespace std;

class Shape{
public:
    virtual ~Shape() {}
    void move(){
        cout << "Shape::move()" << endl;
    }
    virtual void render(){
        cout << "Shape::render()" << endl;
    }
};

class Ellipse : public Shape{
public:
    ~Ellipse(){
        cout << "Ellipse::~Ellipse()" << endl;
    }
    void render(){
        cout << "Ellipse::render()" << endl;
    }
};

class Circle : public Ellipse{
public:
    ~Circle(){
        cout << "Circle::~Circle()" << endl;
    }
    void render(){
        cout << "Circle::render()" << endl;
    }
};

void foo(Shape *p){
    p->move();
    p->render();
}

void move_and_redraw_all(std::vector<Shape*> &shapes){
    for(auto p : shapes)
        foo(p);
}

int main(){
    std::vector<Shape*> all_shapes;
    all_shapes.push_back(new Circle());
    all_shapes.push_back(new Ellipse());
    
    move_and_redraw_all(all_shapes);

    delete all_shapes[0];
    delete all_shapes[1];
    return 0;
}
```

![](../../../assets/Pasted%20image%2020250331144633.png)

- 这里 Ellipse 的析构函数调用了两次，是因为 Circle 是继承自 Ellipse 的

??? question "Virtual 函数是如何运作的？"

	我们先来看一个例子：
	
	```c++
	#include <iostream>
	#include <vector>
	using namespace std;
	
	class Base{
	public:
	    Base() : data(10) {}
	    void foo() {
	        cout << "Base::foo(): data = " << data << endl;
	    }
	private:
	    int data;
	};
	
	int main(){
	    Base b;
	    b.foo();
	
	    cout << "Size of b is: " << sizeof(b) << endl;
	    return 0;
	}
	```
	
	![](../../../assets/Pasted%20image%2020250331145438.png)
	
	这是因为我们有一个字段 data，大小为 4 字节。我们在这基础上在多加一个虚函数 bar：
	
	```c++
	virtual void bar() {
        cout << "Base::bar()" << endl;
    }
	```
	
	![](../../../assets/Pasted%20image%2020250331145719.png)
	
	发现多了个虚函数大小增加了 12，我们可以看看到底多出了什么：
	
	```c++
	int *p = (int*)&b;
    cout << *p << endl;
    p++;
    cout << *p << endl;
    p++;
    cout << *p << endl;
    ```
    
    ![](../../../assets/Pasted%20image%2020250331224014.png)
    
    可以看到我们跳过了八个字节才到了 data 这四个字节，然后还有四个字节（用于内存补齐），我们可以再看看这前八个字节是什么：
    
	```c++
	int *p = (int*)&b;
    void* *pp = (void* *)p;
    void* pwhatever = *pp;
    cout << (void *)main <<endl;
    cout << pwhatever << endl;
    p += 2;
    cout << *p <<endl;
	```
	
	![](../../../assets/Pasted%20image%2020250331224543.png)
	
	实际上前八个字节是一个函数指针，跟 main 函数处于同一个代码段，我们称之为 Virtual Pointer，它会指向一个虚函数表，这个表里面存放了虚函数的地址，这样我们就可以在运行时找到正确的函数进行调用，如果我们再来一个 Base 类 b2，会发现它的虚函数指针跟 b 是一样的：
	
	```c++
	int main(){
	    Base b;
	    b.foo();
	
	    cout << "Size of b is: " << sizeof(b) << endl;
	
	    int *p = (int*)&b;
	    void* *pp = (void* *)p;
	    void* vptr = *pp;
	    cout << "vptr: " << vptr << endl; 
	
	    Base b2;
	    void *vptr2 = *((void**)&b2);
	    cout << "vptr2: " << vptr2 << endl;
	    return 0;
	}
	```
	
	![](../../../assets/Pasted%20image%2020250331225233.png)
	
	所以说虚函数表是共享的。我们再来看看子类的情况：
	
	```c++
	class Derived : public Base{
	public:
	    void bar0(){
	        cout << "Derived::bar0()" << endl;
	    }
	    void bar1(){
	        cout << "Derived::bar1()" << endl;
	    }
	};
	Derived d;
    void *vptrd = *((void**)&d);
    cout << "vptrd: " << vptrd << endl;
	```
	
	![](../../../assets/Pasted%20image%2020250331225352.png)
	
	我们可以再看看父类和子类的成员函数：
	
	```c++
	void* *vfuncs = (void* *)vptr;
    void* f0 = vfuncs[0];
    cout << "f0: " << f0 << endl;
    void* f1 = vfuncs[1];
    cout << "f1: " << f1 << endl;
    
    void* *vfuncsd = (void* *)vptrd;
    void* fd0 = vfuncsd[0];
    cout << "fd0: " << fd0 << endl;
    void* fd1 = vfuncsd[1];
    cout << "fd1: " << fd1 << endl;
	```
	
	![](../../../assets/Pasted%20image%2020250331225744.png)
	
	可以看到父类和子类的成员函数地址也是不一样的，如果我们把子类的 bar0 函数注释掉，那么会发现子类和父类的两个 bar0 函数地址一样了：
	
	![](../../../assets/Pasted%20image%2020250331225949.png)
	
	这是因为我们没有复写 bar0 函数，所以它会默认调用父类的 bar0 函数。

根据上面的思考，我们也可以发现多态实现的原理：如果我们有一个子类的指针，并执行它的成员函数，它会从指针先找到类，再找到虚函数表，再找到函数的地址，然后执行函数。

!!! tip "Tips"

	如果我们有如下操作：
	
	```c++
	Ellipse elly(20F, 40F);
	Circle circ(60F);
	elly = circ;
	```
	
	这样只会把 circ 对应的部分赋值给 elly, 但虚函数的 VPTR 不会. VPTR 只会在构造函数执行的时候对其进行赋值。
	
	如果我们用指针来构造 elly 和 circ，那么就是指针级别上的赋值，最后 elly 就完全变为 circ 了
***
### Overriding

- **重写**（Overriding）会重新定义虚函数体（相当于根据子类的实际情况重新定义父类的虚函数）
- 在子类中，仍然还是可以调用父类的函数（可以是个虚函数）