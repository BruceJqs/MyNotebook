---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
--- 

# Chapter 01 : Introduction

## The First C++ Program

```c++
#include<iostream>
using namespace std;

int main()
{
	int age, sid;
	cin >> age >> sid;
	cout << "Hello, World! I am " << age << "Today!" << endl;
	return 0;
}
```

- `cout` : 标准输出流
- `<<` : 把东西插入到左边去
- `cout << ""` 的副作用是字符串被输出，但结果是字符串本身
- `cin >> age` 同理，副作用是读入，结果是 `age` 本身。(读到空格为止)

!!! tip "Tip"

	`cin`,`cout` 本质上都是变量，而对应的 `<<`,`>>` 是经过重载的属于这些变量的位移运算符，表示的含义是将之后的 token 塞入输出流 / 从输入流读取，并且返回一个 cin / cout 变量。
***
## String

- String 是 C++ 中的一个类（调用需要 `#include<string>`）
- 可以像定义其他类型一样定义变量。 e.g. `string str;`
- 可以对字符串初始化，用 `cin, cout` 输入输出。
***
### Assignment

```c++
char charr1[20]; 
char charr2[20] = "jaguar"; 
string str1; 
string str2 = "panther"; 
charr1 = charr2; // illegal
str1 = str2; // legal
```

- 字符数组不能赋值，字符串是可以的
- 这里 `"panther"` 是一个字符串字面量

!!! tip "补充"

	```c++
	string str4("Hello, ZJU!"); //legal
	string str5(str2); //legal
	string str6(str4, 7, 3); //legal
	```
	
	上面的表述都是合法的，是 string 类的生成函数，具体后面会讲到，效果如下：
	
	![](../../../Pasted%20image%2020250217164448.png)
***
### Concatentation

```c++
string str3; 
str3 = str1 + str2;
str1 += str2;
str1 += "lalala";
```

