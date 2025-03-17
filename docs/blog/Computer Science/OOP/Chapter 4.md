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

- 但是，仅仅靠 private 和 public 还是能让用户看到 struct 当中存在这些变量的，事实上还有一种 [Pimpl Technique](https://en.wikipedia.org/wiki/Pimpl) 可以实现更好的封装，隐藏 private 的成员，但是这里不做展开
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
	
	- 需要注意的是，C++ 建议将类的声明和定义分开（就像我们这里使用 Point.h 来声明，用 Point.cpp 来定义具体功能），这样可以更好的维护代码
		- .h 文件就像是作者和使用者之间的合约，讲述了所有的函数、类、变量等等的声明，而所有的定义都在 .cpp 文件中
	
	![](../../../assets/Pasted image 20250317190006.png)

总的来说，OOP 就是认为所有的事物都是对象，程序就是一些对象，他们通过消息传递来交互，而不是直接操作对象，每一个对象都有自己的状态和行为（可以看作一个个 Agent）
***
## `::` Resolver

在上面的例子中，我们使用了 `Point::` 来指定这个函数是属于 `Point` 这个类的，这个操作符叫做作用域解析运算符，一般使用方法为 `Class::Function` 或 `Class::Attribute`，如果冒号前面没有类名，那么就是全局作用域
***
## Computation Unit

- 在 C++ 中，一个 `.cpp` 文件就是一个编译单元（Computation Unit）
	- 编译器会将 `.cpp` 文件编译成 `.obj` 文件
- 链接器会讲所有的 `.obj` 文件链接成一个可执行文件
- 如果要在多个 `.cpp` 文件共享信息，可以使用 `.h` 文件

### `#include`

- `#include` 指令会将 `.h` 文件的内容直接复制到 `.cpp` 文件中，一般来说有两种：
	- `#include "xx.h"`，一般会在当前目录下寻找文件
	- `#include <xx.h>`，一般会在特定的目录下（取决于编译环境）寻找文件
- 以下是一个标准的头文件结构，里面的声明仅出现一次，这样可以避免头文件内容被多次包含，从而导致编译失败的问题

```c++
#ifndef HEADER_FLAG
#define HEADER_FLAG
// Type declaration here...
#endif // HEADER_FLAG
```

!!! example "Example"

	假设我们在上面的 "Point.h" 最上面加一行 `int globalx = 10;`，编译会出现以下情况：
	
	![](../../../assets/Pasted image 20250317191339.png)
	
	这是因为我们在 main.cpp 中 `#include "point.h"` 了一次，在 point.cpp 中又 `#include "point.h"` 了一次，所以编译器会认为 `globalx` 被定义了两次，所以会报错
	
	所以说我们在 .h 文件中一般只放声明（比如说 `extern int globalx;`），而在 .cpp 文件中放定义，这样可以避免这种情况的发生
	
	但是还有一种情况，如果我们还有一个 Line_segment.h 文件利用 point.h 实现线段（即在其中也要 `#include "point.h"`），那我们在 main.cpp 中如果同时使用这两个功能时，既要 `#include "point.h"` 又要 `#include "Line_segment.h"`，这样就会出现整个头文件被重复包含的情况
	
	为了更加保险，我们可以添加上面的头文件结构（称为 Safeguard），从而也避免这种情况的发生
***
## Build Automation Tools

- 为了在工程中更好的管理代码，我们可以使用一些自动化工具来帮助我们编译代码
	- 例如 `make`、`cmake` 等等
	- `cmake` 并非是一个构造系统，而是一个构建系统生成器，可以根据不同的构造系统生成不同的构建文件

!!! example "Example"

	例如我们将上面的 Point 用 cmake 来管理
	
	在目录下创建一个 CMakeLists.txt 文件：
	
	```cmake
	cmake_minimum_required(VERSION 2.8.9)
	project(Point)
	add_executable(Point main.cpp point.cpp)
	```
	
	然后创建一个 build 文件夹，进入 build 文件夹：
	
	![](../../../assets/Pasted image 20250317193138.png)
	
	执行 `cmake ..`，根据外层目录的 CMakeLists.txt 文件生成 Makefile 文件：
	
	![](../../../assets/Pasted image 20250317200351.png)
	
	build 文件夹下会生成相关 `make` 文件：
	
	![](../../../assets/Pasted image 20250317200507.png)
	
	使用 `make` 命令编译即可生成：
	
	![](../../../assets/Pasted image 20250317200751.png)
	
	![](../../../assets/Pasted image 20250317200807.png)
	
	![](../../../assets/Pasted image 20250317200822.png)
***
## Constructor

我们需要有机制，保证对象被创建时有合理的初值，如果没有赋初值，那么对象的状态就是不确定的，这时候就需要构造函数（Constructor）

- 构造函数名字和结构名字完全相同，没有返回类型
- 本地变量被创建时，构造函数被调用

!!! example "Example"

	构造函数的定义一般有下列形式：
	
	```c++
	#include<iostream>
	using namespace std;
	
	struct Y{
		int i;
		float x;
		Y(int a) { i = a; }
	};
	
	int main(){
		Y y1[2] = {Y(1), Y(2)};
	}
	```
	
	这样是没问题的，但是如果我们将 `y1` 的长度设置为 3，那么会报错：
	
	![](../../../assets/Pasted image 20250317203259.png)
	
	这是因为 `Y y1[3]` 会调用默认构造函数，即 `Y y1[3] = {Y(1), Y(2), Y()}`，但是我们并没有定义默认构造函数，所以会报错，那么我们可以定义一个默认构造函数：
	
	```c++
	#include<iostream>
	using namespace std;
	
	struct Y{
		int i;
		float x;
		Y(int a) { i = a; }
		Y() {}
	};
	
	int main(){
		Y y1[3] = {Y(1), Y(2)};
	}
	```
	
	- 事实上，有了默认构造函数，我们甚至可以直接使用 `Y y1[3]`，不需要再赋初值

