---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
--- 

# Chapter 09 : Templates

??? question "为什么需要模板？"

	假如我们有两个对象 `X` 和 `Y`，它们需要相同的代码，但是存储元素的类型不同。这时，你也许会想到以下解决方案：
	
	- 使用共同的基类
	- 直接克隆代码：能够保证类型安全，但是不易管理
	- 无类型列表：这样会产生类型不安全的问题
	
	但这些方案似乎都不太好，所以我们引入了一种更优的方法：**模板**（Templates）

模板的主要思想是重用源代码，将使用类型作为类或函数定义中的参数，主要包括两类：

- 函数模板（Function Template）
	- e.g. 排序函数
    - **模板函数**（Template Function）是函数模板的实例
    - 参数不支持隐式的类型转换
- **类模板**
    - 例子：像栈、列表、队列等容器，其中栈的运算和栈里面项的类型无关
    - 模板成员函数

!!! example "Swap Function"

	```c++
	template <class T>
	void swap(T &x, T &y) {
	    T temp = x;
	    x = y;
	    y = temp;
	}
	```

模板的语法：

- `template` 关键字用于引入模板
- `class T` 指明参数化的类型名称
    - 类可以是内建类型或用户定义的类型
    - 这里也可以用 `typename T` 替代
- 在模板内部，使用 `T` 作为类型名称，可以写在传入传出参数类型中，也可以是函数当中的局部变量

模板的**实例化**（Instantiation）：从模板类 / 函数和模板参数重得到一个声明

- 类型被替代为模板
- 创建了新的函数体或类定义
    - 语法错误、类型检查
- 专一化（Specialization）：对于特定参数的模板版本
***
## Function Templates

> 事实上，我们定义了一个函数模板，在编译时只有当我们调用它的某个匹配类型的时候才会实例化和重载它

函数重载规则：

- 先检查唯一的函数匹配
- 然后检查唯一的函数模板匹配
- 再对函数进行重载

```c++
void f(float i,float k) {};
template <class T>
void f(T t, T u) {};
f(1.0,2.0);
f(1,2);
f(1,2.0);
```

函数实例化：

- 编译器从传递给函数的实参中推断模板类型
- 可以显式实现，参数可以不在函数签名内

```c++
template < class T >
void foo(void) {/*... */ }
foo<int>(); // type T is int
foo<float>(); // type T is float
```
***
## Class Templates

- 类型实现了对类的参数化
    - 从被操作的类型中提取抽象操作
    - 可能会定义类的无限集合
    - 另一种重用方法
- 典型用法：容器类，比如 `stack<int>`、`list<Person&>`、`queue<Job>`

模板能用于多个类型，比如：

```c++
template< class Key, class Value>
class HashTable {
    const Value& lookup(const Key&) const;
    void install(const Key&, const Value&);
    ...
};
```

- 模板嵌套：本质上得到的是一个新类型
    - 举例：`Vector< Vector< double *> > // note space > >`
- 类型参数可以很复杂
    - 举例：`Vector< int (*)(Vector<double>&, int)>`

模板参数还可以是一个常量表达式，或者是无类型的参数

- 默认参数：

```c++
template <class T, int bounds = 100>
class FixedVector {
public:
    FixedVector();
    // ...
    T& operator[](int);
private:
    T elements[bounds]; // fixed size array!
};
```

- 无类型参数：
	
	```c++
	template <class T, int bounds>
	T& FixedVector<T,bounds>::operator[]( int i ) {
	    return elements[i]; // no error checking
	}
	
	// Usage
	FixedVector<int, 50> v1;
	FixedVector<int, 10*5> v2;
	FixedVector<int> v3; // uses default
	```
	
	- 嵌入 size 并不常用
	- 能够让代码更快
	- 但使用起来更复杂
	- 可能导致（甚至更多的）代码膨胀

模板和继承：

- 模板能够继承自非模板类

```c++
template <class A>
class Derived : public Base { ...
```

- 模板能够继承自模板类

```c++
template <class A>
class Derived : public List<A> { ...
```

- 非模板类可继承自模板类

```c++
class SupervisorGroup : public
List<Employee*> { ...
```

