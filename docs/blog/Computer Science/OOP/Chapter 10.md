---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
# comments: true
--- 

# Chapter 10 : Exceptions

## Exceptions

运行时错误（Run-Time Error）：

- 格式错误的代码将无法运行
- 处理未来运行中所有可能的情况非常重要

下面的代码能够处理运行代码时出现的各种异常，包括找不到文件，文件虽然存在但是打不开（没有权限、被别的进程打开），文件大小判断失败（可能是一个串口，不是磁盘上的文件，串口是没有结束的）……：

```c++
try {
    open the file;
    determine its size;
    allocate that much memory;
    read the file into memory;
    close the file;
} catch (fileOpenFailed) {
    doSomething;
} catch (sizeDeterminationFailed) {
    doSomething;
} catch (memoryAllocationFailed) {
    doSomething;
} catch (readFailed) {
    doSomething;
} catch (fileCloseFailed) {
    doSomething;
}
```
***
### Throw

我们可以使用 `throw` 关键字来抛出异常，例如对于数组越界：

```c++
template <class T>
T& Vector<T>::operator[](int indx) {
    if (indx < 0 || indx >= m_size) {
        // throw is a keyword
        // exception is raised at this point
        throw <<something>>;
    }
    return m_elements[indx];
}
```

- `throw` 语句发起的异常将控制权传播给第一个对于该异常的处理函数
- 传播遵循调用链
- 在栈上的对象会被正确销毁
- `throw exp;`：抛出匹配值
- `throw;`：重新发起被处理的异常，仅在一个处理函数中有效
***
### Try-Catch

我们可以使用 `try` 和 `catch` 语句来捕获异常：

```c++
try { ... }
catch ...
catch ...
```

它可以建立任意数量的处理函数，可以设置任何可能出现的异常情况

异常处理函数：

- 根据类型选择异常
- 能够重新发起异常
- 两种形式（都只接受一个参数）：
	
	```c++
	catch (SomeType v) {
	}
	
	catch (...) {
	}
	```
	
	- 会根据代码顺序来检查所有的处理函数
	    - 找到完全匹配的
	    - 应用基本的类转换，仅适用于引用和指针类型
	    - 省略号 `...` 匹配所有类型

我们还可以使用继承的方式来构造异常结构：

!!! example "Example"

	我们以数学错误 Matherr 为例：
	
	```c++
	class MathErr {
    ...
    virtual void diagnostic();
	};
	class OverflowErr : public MathErr { ... }
	class UnderflowErr : public MathErr { ... }
	class ZeroDivideErr : public MathErr { ... }
	
	// Using handlers
	try {
	    // code to exercise math options
	    throw UnderFlowErr();
	} catch (ZeroDivideErr& e) {
	    // handle zero divide case
	} catch (MathErr& e) {
	    // handle other math errors
	} catch (...) {
	    // any other exceptions
	}
	```
***
### Exceptions and new

- `new` 在失败时不会返回 0，而会抛出一个 `bad_alloc` 异常。

标准库异常：

![](../../../assets/Pasted%20image%2020250512140921.png)
***
### Exception Specification

当我们调用了其他函数，我们就应该为了其他函数抛异常做准备。 可以在函数头部声明会抛什么异常。不会在编译时期检查。

限制 `abc` 而非调用 `abc` 函数。如果抛出了比你声明更多的异常，异常检查机制会抛出一个终止程序的异常

!!! example "Example"

	对于如下代码：
	
	```c++
	Printer::print(Document&) :
	throw(PrinterOffLine, BadDocument) 
	{ ... 
		PrintManager::print(Document&) : 
		throw (BadDocument) { ... 
		// raises or doesn’t handle BadDocument 
		void goodguy() : throw () { 
		// handles all exceptions 
		void average() { } // no spec, no checking,
	```
	
	- 第一个表示会抛 `PrinterOffLine, BadDocument` 异常。（不一定抛，但可能）
	- 第三个表示不会抛任何异常，这样调用的时候不需要 try catch.
	- 第四个可能会抛异常，但是编译器不会进行检查。
***
## More Exceptions

如果在构造的时候发生了异常，我们需要先分配内存，再执行构造；如果构造的时候出异常，无法得到分配的地址，但是内存却没有被析构，就会发生内存泄漏

```c++
f() { 
	A *p = new A(); 
	... 
	delete p; 
}
```



