---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
--- 

# Chapter 03 : Memory Model

!!! abstract "Lead-in"

	```c++
	int a; // Global Vars.
	static int b; // Static Global Vars.
	
	void f(){
		int k; // Local Vars.
		static int l; // Static Local Vars.
		
		int *p = malloc(sizeof(int)); // Allocated Vars.
	}
	```
	
	上面的程序展现了 C++ 中的四种变量类型，也是这个章节需要介绍的部分

## Memory Layout

![](../../../assets/Pasted%20image%2020250310194209.png)

上面的图展示了程序在内存中的布局，其中：

- Stack：存放函数的局部变量
- Heap：存放动态分配的内存
- Code / Data：存放全局变量，静态全局变量和静态局部变量

!!! example "Example"

	我们可以写个程序来看不同类型变量的地址：
	
	```c++
	#include<cstdlib>
	#include<iostream>
	using namespace std;
	
	int globalx = 10;
	
	int main(){
	    static int staticx = 3;
	    int localx = 5;
	    int *px = (int*)malloc(sizeof(int));
	
	    cout << "&globalx = " << &globalx << endl;
	    cout << "&staticx = " << &staticx << endl;
	    cout << "&localx = " << &localx << endl;
	    cout << "&px = " << &px << endl;
	    cout << "px = " << px << endl;
	    free(px);
	
	    return 0;
	}
	```
	
	运行结果如下：
	
	![](../../../assets/Pasted image 20250310194738.png)
	
	可以看到，静态全局变量和全局变量的地址是比较接近的，而局部变量和指针（普通的局部变量）是比较接近的，指针动态分配的地址是比较远的。

## Global Vars

- 全局变量定义于所有函数之外，可以在不同的 .cpp 文件中共享
	- 共享需要使用 `extern` 关键字，声明整个程序的某个地方会定义这个变量
	
	!!! example "Example"
	
		事实上，不光是普通的全局变量，函数也可以共享，我们编写一个 Lec04.cpp 文件：
		
		```c++ title="Lec04.cpp"
		#include<cstdlib>
		#include<iostream>
		using namespace std;
		
		extern int globalx = 10;
		double pi();
		
		int main(){
		    cout << "globalx = " << globalx << endl;
		    cout << "pi = " << pi() << endl;
		    return 0;
		}
		```
		
		这样直接编译是不行的，因为并没有其他的文件来共享 `globalx` 这个变量，我们再写一个 Lec04_1.cpp 文件：
		
		```c++ title="Lec04_1.cpp"
		int globalx = 10;
		
		double pi(){
		    return 3.14;
		}
		```
		
		使用编译命令时同时编译 Lec04.cpp 和 Lec04_1.cpp 两个文件就可以实现共享了：
		
		![](../../../assets/Pasted image 20250310200157.png)
***
### Static Vars

> Static（静态）一词关键体现在两个方面：永久的存储和受限的访问范围

- 静态全局变量只能在定义它的编译单元（即一个 .cpp 文件）中使用，不能在其他编译单元中使用

!!! example "Example"

	我们把上面的 Lec04_1.cpp 修改一下：
	
	```c++ title="Lec04_1.cpp"
	static int globalx = 10;
	
	static double pi(){
	    return 3.14;
	}
	```
	
	此时再次进行编译，会发现报错：
	
	![](../../../assets/Pasted image 20250310200559.png)
***
### Static Local Vars

- 静态局部变量只会在第一次调用函数时初始化，之后不会再次初始化，它会在多次调用函数时保持状态

!!! example "Example"

	```c++
	#include<cstdlib>
	#include<iostream>
	using namespace std;
	
	void access_count(){
	    static int count = 0;
	    cout << "access count: " << ++count << endl;
	}
	
	int main(){
	    for(int i = 0; i < 10; i++)
	        access_count();
	
	    return 0;
	}
	```
	
	编译运行结果如下：
	
	![](../../../assets/Pasted image 20250310200919.png)
	
	这说明静态局部变量在函数调用之间是保持状态的，每次调用函数时，静态局部变量的值不会进行初始化。这是因为静态局部变量的存储位置在全局数据区，而不是栈上，所以不会被释放
***
## Pointers to Objects

假设我们有：

```c++
string s = "hello"; 
string *ps = &s;
```
***
### Operators with pointers

我们也可以通过 `*ps` 来访问 `s` 这个对象，继而访问其成员函数：

```c++
string *ps = &s;
int len = (*ps).length(); // Get the length of string
int len = ps -> length(); // Equivalent to the above
```
***
### Two Ways to Access

```c++
string s; // 定义一个字符串对象，并且也被初始化了
string *ps; // 定义一个指向字符串对象的指针，但是并没有初始化
```
***
### Assignment

```c++
string s1, s2 = "hello";
s1 = s2; // Copy the value of s2 to s1

string *ps1, *ps2;
ps1 = ps2; // Copy the address of ps2 to ps1
```
***
### Defining References

```c++
char c; // A character
char* p = &c; // A pointer to a character
char& r = c; // A reference to a character
```

- 用 `type& refname = name` 可以为名为 `name` 的变量起一个别名 `refname`
	- 这里的 `r` 是 `c` 的别名，修改 `r` 也会修改 `c` 的值，即用 `r` 就是在用 `c`，用 `c` 就是在用 `r`
- 在函数的参数表 / 成员函数中使用引用也可以写为 `type& refname`
- 

!!! example "Example"

	


