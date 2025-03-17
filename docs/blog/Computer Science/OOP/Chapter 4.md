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

但是事实上，我们希望它成为一个进行封装过的，能够被更高层面的程序调用的功能，这时候我们有了结构体和函数：

```c++
#include<iostream>
using namespace std;

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


