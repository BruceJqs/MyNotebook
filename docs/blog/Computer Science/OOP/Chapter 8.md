---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
--- 

# Chapter 08 : Operator Overloading

## Introduction

**重载运算符**（Overloaded Operators）允许用户定义的类型和内建类型的行为类似，且提供了另一种调用函数的方式

下面是能够被重载的一元或二元运算符：

```c++
+ - * / % ^ & | ~
= < > += -= *= /= %=
^= &= |= << >> >>= <<= ==
!= <= >= ! && || ++ --
, ->* -> () []
new delete
new[] delete[]
```

不能被重载的运算符：

```c++
. .* :: ?:
sizeof typeid
static_cast dynamic_cast const_cast
reinterpret_cast
```

- 只能重载已有的运算符（比如不能创建一个用于指数运算的运算符 `**` ）
- 必须重载某个类或枚举类型里的运算符
- 重载运算符必须保留操作数的个数，以及优先级
***
## Declaration

重载运算符的声明：

- 跟函数声明十分类似，运算符名称配上一个 `operator` 前缀作为名称：`operator *(...)`
- 能够作为成员函数：`const String String::operator +(const String& that);`
    - 不会进行类型转换
    - 必须能访问类里面的定义
    - 第一个参数是隐式的，因此对于二元运算符只需一个参数，而对于一元运算符则无需参数

!!! example "Example"

	```c++
	class Integer {
	public:
	    Integer( int n = 0 ) : i(n) {}
	    const Integer operator+(const Integer& n) const{
	        return Integer(i + n.i);
	    }
	//...
	private:
	    int i;
	};
	```
	
	在这里，有一个隐式的参数，定义加号时只需要定义 a + b 的 b（而因为这是一个成员函数 a 就是隐式的 this）

重载运算符也能作为全局（自由）函数：`const String operator +(const String& r, const String& l);`

- 所有参数都是显式的
- 所有参数都会进行类型转换
- 可以以 `friend` 的方式访问类里面的定义
- 如果没有访问私有成员的权限的话，那么全局函数必须通过公有接口来访问
- 如果是一元运算符，或者是 `=`（包括赋值运算符）、`()`、`->`、`->*` 这些运算符的话，应该声明为成员。而其余的二元运算符均不必作为成员

- 参数传递
    - 对于成员函数，如果不想要改变类里的内容，那就加一个 `const`
    - 对于全局函数，如果要改变左侧参数的话，那就按引用传递
- 返回值：具体取决于运算符的含义
    - 比如对于 `operator +`，它应该产生一个新的对象，那么就将它作为 `const` 对象返回，这个结果就像左值一样不能被修改
    - 对于逻辑运算符，则需要返回 `bool` 类型的值
***
## Prototypes

运算符的原型：

- `+ - * / % ^ & | ~`
    - `const T operator X(const T& l, const T& r);`
- `! && || < <= == >= >`
    - `bool operator X(const T& l, const T& r);`
- `[]`
    - `E& T::operator [](int index);`

运算符 `++` 和 `--`

- 对于其后缀形式，它们会接受一个 `int` 参数，编译器会传递一个 0

```c++
class Integer {
public:
    ...
    const Integer& operator++(); //prefix++
    const Integer operator++(int); //postfix++
    const Integer& operator--(); //prefix--
    const Integer operator--(int); //postfix--
    ...
};

const Integer& Integer::operator ++() {
    *this += 1; // increment
    return *this; // fetch
}
// int argument not used so leave unnamed so
// won't get compiler warnings
const Integer Integer::operator ++(int){
    Integer old(*this); // fetch
    ++(*this); // increment
    return old; // return
}
```

- 用户定义的前缀运算符比后缀运算符更快

关系运算符：

- `!=` 基于 `==` 实现
- `>`、`>=`、`<=` 基于 `<` 实现

```c++
class Integer {
public:
    ...
    bool operator ==(const Integer& rhs) const;
    bool operator !=(const Integer& rhs) const;
    bool operator <(const Integer& rhs) const;
    bool operator >(const Integer& rhs) const;
    bool operator <=(const Integer& rhs) const;
    bool operator >=(const Integer& rhs) const;
}

bool Integer::operator ==(const Integer& rhs) const {
    return i == rhs.i;
}

// implement lhs != rhs in terms of !(lhs == rhs)
bool Integer::operator !=(const Integer& rhs) const {
    return !(*this == rhs);
}

bool Integer::operator <(const Integer& rhs) const {
    return i < rhs.i;
}

// implement lhs > rhs in terms of lhs < rhs
bool Integer::operator >(const Integer& rhs) const {
    return rhs < *this;
}
// implement lhs <= rhs in terms of !(rhs < lhs)
bool Integer::operator <=(const Integer& rhs) const {
    return !(rhs < *this);
}
// implement lhs >= rhs in terms of !(lhs < rhs)
bool Integer::operator >=(const Integer& rhs) const {
    return !(*this < rhs);
}
```
***
## Other Operators

### `[]`

- 必须是一个成员函数
- 单参数
- 它表明对象的行为类似一个数组，所以它需要返回一个引用
***
### `()`

- 重载函数调用运算符（Functor）

!!! example "Example"

	我们首先有如下代码：
	
	```c++
	#include <iostream>
	#include <vector>
	using namespace std;
	
	int main(){
	    vector<int> v {1, 3, 5, 7, 9};
	
	    for(int& x : v){
	        x *= 3;
	    }
	
	    for(int& x : v){
	        x *= 5;
	    }
	
	    for(int& x : v){
	        x = x * 2 + 1;
	    }
	
	    for(int& x : v){
	        cout << x << " ";
	    }
	    cout << endl;
	    return 0;
	}
	```
	
	![](../../../assets/Pasted%20image%2020250421142059.png)
	
	但是我们希望将这些函数统一化，我们可以首先把 for 循环进行封装：
	
	```c++
	#include <iostream>
	#include <vector>
	#include <functional>
	using namespace std;
	
	void transform(vector<int>& v, function<int(int)> f){
	    for(int& x : v){
	        x = f(x);
	    }
	}
	
	int main(){
	    vector<int> v {1, 3, 5, 7, 9};
	
	    transform(v, [](int x){return x * 3;});
	    transform(v, [](int x){return x * 5;});
	    transform(v, [](int x){return x * 2 + 1;});
	
	    for(int& x : v){
	        cout << x << " ";
	    }
	    cout << endl;
	    return 0;
	}
	```
	
	其中我们传递了一个函数指针，且在 main 函数中用了 lambda 表达式简化函数的定义（即我们不用单独去分别定义三个函数了，结果是一样的
	
	然后我们希望把函数的功能变得更多元一些，我们可以构造类和重载操作符来实现乘任意数和一次线性变换的功能：
	
	```c++
	#include <iostream>
	#include <vector>
	#include <functional>
	using namespace std;
	
	void transform(vector<int>& v, function<int(int)> f){
	    for(int& x : v){
	        x = f(x);
	    }
	}
	
	class mul_by{
	public:
	    mul_by(int n): n_(n){};
	    int operator()(int x){
	        return x * n_;
	    }
	private:
	    int n_;
	};
	
	class line{
	public:
	    line(int a, int b): a_(a), b_(b){};
	    int operator()(int x){
	        return a_ * x + b_;
	    }
	private:
	    int a_;
	    int b_;
	};
	
	int main(){
	    vector<int> v {1, 3, 5, 7, 9};
	
	    transform(v, mul_by(3));
	    transform(v, mul_by(5));
	    transform(v, line(2, 1));
	
	    for(int& x : v){
	        cout << x << " ";
	    }
	    cout << endl;
	    return 0;
	}
	```
	
	结果仍然是一样的
***
### `>>` and `<<`

流提取符 `>>` 是一个双参数的自由函数

- 其中第一个参数为 `istream&`，第二个参数为值的引用

```c++
istream& operator >>(istream& is, T& obj) {
    // specific code to read obj
    return is;
}
```

- 返回值类型也是 `istream&`，因此可被链式使用

```c++
cin >> a >> b >> c;
((cin >> a) >> b) >> c;
```

流插入符 `<<` 也是一个双参数的自由函数

- 其中第一个参数为 `ostream&`，第二个参数为值的引用

```c++
ostream& operator <<(ostream& os, const T& obj) {
    // specific code to write obj
    return os;
}
```

 - 返回值类型也是 `ostream&`，因此可被链式使用

```c++
cout << a << b << c;
((cout << a) << b) << c;
```

我们可以自定义**操纵符**（Manipulators）：

```c++
// skeleton for an output stream manipulator
ostream& manip(ostream& out) {
    ...
    return out;
}

ostream& tab ( ostream& out ) {
    return out << '\t';
}

cout << "Hello" << tab << "World!" << endl;
```
***
### `=`

赋值运算符：

- 必须是一个成员函数
- 编译器会自动创建一个 `type::operator=(type)`，如果没有手动创建的话
    - 和拷贝构造函数的行为一致
    - 按成员赋值
- 检查自身的赋值情况
- 确保为所有的数据成员赋值
- 返回 `*this` 的引用
- 大致结构：

```c++
T& T::operator=( const T& rhs ) {
    // check for self assignment
    if ( this != &rhs) {
        // perform assignment
    }
    return *this;
}
//This checks address vs. check value (*this != rhs)
```

- 对于动态分配内存的类，需要声明一个赋值运算符（以及一个拷贝构造函数）
- 为了阻止赋值，可以讲 `operator=` 显式声明为私有

值类（Value Classes）：

- 看起来就像原始数据类型
- 可作为函数的参数和返回值
- （通常）有重载运算符
- 能够被转换为其他类型，也可以从其他类型转换而来
- 例子：Complex、Date、String
***
## Type Conversion

用户定义的类型转换：

- 转换运算符用于将某个类的一个对象转换至另一个类的对象或内建类型
- 编译器会使用单参数的构造函数，或者隐式的类型转换运算符来执行隐式类型转换
- 我们可以用 `explicit` 关键字阻止隐式的类型转换：

```c++
class PathName {
    string name;
public:
    explicit PathName(const string&);
    ~ PathName();
};
...
string abc("abc");
PathName xyz(abc); // OK!
xyz = abc; // error!
```

运算符转换：

- 函数会被自动调用
- 返回类型和函数名相同

```c++
class Rational {
public:
    operator double() const; // Rational to double
}
Rational::operator double() const {
    return numerator_/(double)denominator_;
}
Rational r(1,3); double d = 1.3 * r; // r=>double
```

- 转换运算符的一般形式：`X::operator T()`
    - 运算符名称是任意类型描述符
    - 没有显式的参数，且没有返回类型
    - 编译器将其用于类型转换`X` -> `T`
- 对于原始的内建类型，转换规则为：

```c++
char ⇒ short ⇒ int ⇒ float ⇒ double
char ⇒ short ⇒ int ⇒ long
```

- 隐式规则（对于任何类型 `T`）
    `T ⇒ T& t& ⇒ T T* ⇒ void* T[] ⇒ T* T* ⇒ T[] T ⇒ const T`
- 用户定义的 `T -> C`
    - 对类型 `C` 而言，`C(T)` 是有效的构造函数调用
    - 或者对类型 `T` 而言，定义了 `operator C()`
- 重载和类型转换：C++ 会检查每个参数，以做到“最佳匹配”——意味着最节省成本的做法
