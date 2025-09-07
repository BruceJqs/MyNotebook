---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
# comments: true
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
	
	上面的表述都是合法的，是 string 类的生成函数（类似的，也可以 `int age(18);`）：
	
	``` c++
	string (const char *cp, int len);
	string (const string& s2, int pos);
	string (const string& s2, int pos, int len);
	```
	
	效果如下：
	
	![](../../../assets/Pasted%20image%2020250217164448.png)
***
### Concatenation & Length

```c++
string str3; 
str3 = str1 + str2;
str1 += str2;
str1 += "lalala";
cout << str1.length() << endl;
```

- `s.length()` 得到字符串的长度。(C++ 中字符串没有 `\0`)
***
### Sub-string & Search

```c++
substr (int pos, int len);
find (const string& str, int pos = 0);
```

- `substr` 拷贝字符串从 `pos` 位置开始的 `len` 个字符
	- 如果 `pos` 超出了字符串长度，那么会产生异常
	- 如果 `pos` 等于字符串长度，那么会得到空字符串
	- 如果 `pos + len` 超出了字符串长度，那么只会拷贝到字符串末尾
- `find` 从 `pos` 开始查找字符串 `str`, 返回第一次匹配的第一个字符的位置
***
### Modification

!!! note "Modification"

	=== "Assign"
	
		```c++
		//assign 将一个新的值赋给字符串
		assign (const string& str); //string 
		assign (const string& str, size_t subpos, size_t sublen); //substring 
		assign (const char* str); //C-string 
		assign (const char* str, size_t n); //buffer 
		assign (int n, char c); //fill
		```
	
	=== "Insert"
	
		```c++
		//insert 在 pos 之前插入字符
		insert (int pos, const string& str);
		insert (int pos, const string& str, int subpos, int sublen); 
		insert (int pos, const char* str); 
		insert (int pos, const char* str, int n); 
		insert (int pos, int n, char c);
		```
	
	=== "Erase"
	
		```c++
		//erase 擦除从 pos 开始 len 个字符的字符串（如果超出字符串长度则到字符串末尾），默认参数擦除字符串中所有字符
		erase (int pos = 0, int len = npos);
		```
	
	=== "Append"
	
		```c++
		//append 在字符串的末尾添加字符串 str
		append (const string& str);
		append (const char* s);
		```
	
	=== "Replace"
	
		```c++
		//replace 代替从 pos 开始 len 的字符串
		replace (int pos, int len, const string& str);
		replace (int pos, int len, const string& str, int subpos, int sublen); 
		replace (int pos, int len, const char* str); 
		replace (int pos, int len, const char* str, int n); 
		replace (int pos, int len, int n, char c);
		```

!!! Example

	```c++
	#include<iostream>
	#include<string>
	#include<regex>
	using namespace std;
	
	int main()
	{
		string str1 = "Hello, China!";
		string str2 = str1.substr(7, 5);
		cout << "str2: " << str2 << endl;
		string str3 = str1;
		str3.replace(7, 5, "zjg");
		cout << "str3: " << str3 << endl;
		  
		str3.assign(10, 'A');
		cout << "str3: " << str3 << endl;
		
		string str4 = "Hello, HangZhou City!";
		cout << "str4: " << str4 << endl;
		string string_to_find = "HangZhou";
		cout << "index: " << str4.find(string_to_find) << endl;
		str4.replace(str4.find(string_to_find), string_to_find.length(), "JinHua");
		cout << "str4: " << str4 << endl;
		
		regex re("a|e|i|o|u"); // 正则表达式匹配
		string str5 = regex_replace(str4, re, "*");
		cout << "str5: " << str5 << endl;
		
		return 0;
	}
	```
	
	其中 `regex` 为正则表达式匹配，结果如下：
	
	![](../../../assets/Pasted%20image%2020250217184630.png)
***
## File I/O

```c++
#include<fstream> // Dealing with file reading and writing
using namespace std;

ofstream File1("test.txt");
File1 << "Hello World" << endl;

ifstream File2("test.txt");
string str;
File2 >> str;
```
***



