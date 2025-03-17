---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
--- 

# Chapter 04 : Class

## Introduction

假设我们需要实现一个点移动的功能，正常情况下我们会这样写：

```c++
#include<iostream>
using namespace std;

int px, py;

int main(){
	px = 2, py = 3;
	cout << "Point at [" << px << "," << py << "]" << endl;

	px += 5, py += 5;
	cout << "Point at [" << px << "," << py << "]" << endl;
	return 0;
}
```

![](../../../assets/Pasted%20image%2020250317133122.png)
***
### Struct and Function

但是事实上，在工程中我们希望它成为一个进行封装过的，能够被更高层面的程序调用的功能，这时候我们有了结构体和函数：

```c++
#include<iostream>
using namespace std;

struct Point;
// Point* point_create();
void point_init(Point *p, int ix, int iy);
void point_print(Point *p);
void point_move(Point *p, int dx, int dy);

struct Point{
    int x, y;
};

void point_init(Point *p, int ix, int iy){
    p -> x = ix;
    p -> y = iy;
}

void point_print(Point *p){
    cout << "Point at [" << p -> x << "," << p -> y << "]" << endl;
}

void point_move(Point *p, int dx, int dy){
    p -> x += dx;
    p -> y += dy;
}

int main(){
    Point p;

    point_init(&p, 2, 3);
    point_print(&p);
    point_move(&p, 5, 5);
    point_print(&p);
    return 0;
}
```

![](../../../assets/Pasted%20image%2020250317133715.png)

 这样，不仅实现了原样的功能，代码的可读性也得到了提高（因为对于用户来说只需要看第 4～8 行 的内容就能知道这个结构体的功能）
***
### Member Function

上面其实对于 c 语言来说也可以同样实现，但是在 C++ 等一众面向对象编程语言中，上面的函数我们还可以并入 struct 当中使其成为结构体的成员函数：

```c++
#include<iostream>
using namespace std;

struct Point{
    int x, y;
    // Point* point_create();
    void init(int ix, int iy);
    void print();
    void move(int dx, int dy);
    ...
};

int main(){
	...
}
```

实现的功能还是相同的
***
### Private & Public

但是在上面的代码中，我们发现结构体的成员变量是可以直接访问的，这在工程中是不被允许的，我们希望这些变量只能通过结构体的成员函数来访问，而不是通过直接访问的方式，这时候我们就需要将这些变量设置为私有变量：

```c++
#include<iostream>
using namespace std;

struct Point{
private:
    int x, y;
public:
    // Point* point_create();
    void init(int ix, int iy);
    void print();
    void move(int dx, int dy);
    ...
}
	...
```

这样就实现了对于成员变量的封装，只能通过成员函数来访问
***
## Objects

何为“对象”？在面向对象编程语言当中，对象可以抽象成两个部分：属性（Attributes）和服务（Services）

- 数据（Data）：属性或状态（例如上面的 `x, y`）
- 操作（Operation）：服务或行为（例如上面的 `init, print, move`）

在 C++ 中，对象只是一个变量，最纯粹的定义是“存储区域”，之前学习的结构变量只是C++中的对象

!!! example "Example"

	对于一个售票机来说，它可能会有以下属性和服务：
	
	- 属性：票价、余票、总票数
	- 服务：打印票、收钱、展现余票、打印错误…
	
	在 C++ 当中，我们可以定义一个类来表示这个售票机：
	
	```c++
	class TicketMachine{
	private:
	    const int PRICE;
	    int balance;
	    int total;
	public:
	    void getMoney();
	    void printTicket();
	    void showBalance();
	    void printError();
	};
	```

??? question "Question"

	说了这么多，对象和类到底有什么关系和区别？
	
	事实上，类就是对象抽象出来的模板，而对象就是类的实例化，我们把对象比作一只猫，描述这只猫独有的特点，那么类就是猫这一类群体，描述了猫的共性。
	
	对象表示事物、事件或概念，会在运行时响应消息；而类则定义对象这类实例的属性和行为（有点像 `typedef`

!!! example "Example"

	回到上面的点的例子，对于开发者来说，他需要定义点的属性和服务，那么我们就可以定义一个类来表示这个点：
	
	```c++ title="Point.h"
	class Point{
	private:
	    int x, y;
	public:
	    void init(int ix, int iy);
	    void print();
	    void move(int dx, int dy);
	};
	```
	
	```c++ title="Point.cpp"
	#include "point.h"
	#include <iostream>
	using namespace std;
	
	void Point::init(int ix, int iy){
	    x = ix;
	    y = iy;
	}
	
	void Point::print(){
	    cout << "Point at [" << x << "," << y << "]" << endl;
	}
	
	void Point::move(int dx, int dy){
	    x += dx;
	    y += dy;
	}
	```
	
	那么对于用户来说，他只需要调用这个类的服务即可完成更高层面的调用：
	
	```c++ title="main.cpp"
	#include<iostream>
	#include "point.h"
	using namespace std;
	
	int main(){
	    Point p;
	
	    p.init(2, 3);
	    p.print();
	    p.move(5, 5);
	    p.print();
	    return 0;
	}
	```
	
	同样也能实现原样的功能：
	
	![](../../../assets/Pasted image 20250317141648.png)
	
	需要注意的是，最好将类的声明和定义分开（就像我们这里使用 Point.h 来声明，用 Point.cpp 来定义具体功能），这样可以更好的维护代码
***
## `::` Resolver

在上面的例子中，我们使用了 `Point::` 来指定这个函数是属于 `Point` 这个类的，这个操作符叫做作用域解析运算符



