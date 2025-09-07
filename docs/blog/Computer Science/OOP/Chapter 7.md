---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
# comments: true
--- 

# Chapter 07 : Copy Constructor

## Copying

> 复制构造函数（Copy Constructor）是一个特殊的构造函数，用于创建一个对象作为另一个对象的副本，经常会出现在函数被调用传递参数、结束返回参数时、初始化等情况

复制构造函数有唯一的签名：`T::T(const T&)`，即一个参数是引用类型的对象

- 如果没有给拷贝一个构造函数，C++ 会自动创造一个 memwise 初始化函数
	- 对于每一个类成员，分别调用他们的拷贝构造函数
	- 如果成员是基本类型（整型、指针等），直接赋值
	- 这就导致如果有成员变量是指针，会和原来对象一样指向同一块内存。如果有一个对象被析构，那么这块内存就被 delete, 这就变成了无效内存
- 因此我们不一定要有拷贝构造函数，有指针时必须要有

![](../../../assets/Pasted%20image%2020250414135451.png)

!!! example "Example"

	我们有如下代码：
	
	```c++
	#include <cstring>
	#include <iostream>
	using namespace std;
	
	struct Person {
	    char * name;
	    Person(const char* s) {
	        name = new char[strlen(s) + 1];
	        strcpy(name, s);
	    }
	    ~Person() {
	        delete[] name;
	    }
	};
	
	int main() {
	    Person p1("Trump");
	    Person p2 = p1;
	
	    cout << (void*)p1.name << endl;
	    cout << (void*)p2.name << endl;
	}
	```
	
	运行结果：
	
	![](../../../assets/Pasted%20image%2020250414135033.png)
	
	可以看到我们并没有写复制构造函数，这是 C++ 默认帮我们写好的，同时 `p2 = p1` 使用了复制构造，所以 `p2` 和 `p1` 指向同一块内存，导致 `delete[] name` 语句执行了两次，出现内存错误
	
	我们手动写一个复制构造函数：
	
	```c++
	Person(const Person & other) {
        name = new char[strlen(other.name) + 1];
        strcpy(name, other.name);
    }
    ```
    
	这样我们就使得两者不会打架，也不会报错了：
	
	![](../../../assets/Pasted%20image%2020250414135401.png)
	
	那如果我不用字符数组的指针形式而是用字符串对象呢？
	
	```c++
	#include <cstring>
	#include <string>
	#include <iostream>
	using namespace std;
	
	struct Person {
		string name;
		Person(const string & s) : name(s) {}
	};
	
	int main() {
		Person p1("Trump");
		Person p2 = p1;
	
		cout << (void*)p1.name.data() << endl;
		cout << (void*)p2.name.data() << endl;
	}
	```
	
	这么做也能避免内存错误：
	
	![](../../../assets/Pasted%20image%2020250414135953.png)
	
	??? question "拓展"
	
		如果我们还是用字符数组的指针形式，但是我们在 main 函数中再加一行 `p2 = p1;`，运行会发现：
		
		![](../../../assets/Pasted%20image%2020250414141249.png)
		
		这是因为在 C++ 中，赋值操作符还是会去调用默认的赋值函数，这也使得 `p2` 和 `p1` 指向同一块内存，导致 `delete[] name` 语句执行了两次，出现内存错误
		
		我们可以手动重载赋值操作符：
		
		```c++
		Person & operator=(const Person & other) {
	        if (this != &other){
	            delete[] name;
	            name = new char[strlen(other.name) + 1];
	            strcpy(name, other.name);
	        }
	        return *this;
	    }
	    ```
	    
		需要 `delete[] name` 是因为 `name` 在赋值前已持有动态分配的内存。若直接覆盖指针而不释放旧内存，原内存将无法被回收，导致内存泄漏
		
		判断 `this != &other` 是因为若出现 `person = person`（自我赋值），`delete[] name`会提前释放内存，后续复制时将访问已释放的内存（`other.name` 即 `name`），导致**未定义行为**​（如崩溃或数据损坏）
***
### Return Value Optimization

我们有如下代码：

```c++
#include <cstring>
#include <string>
#include <iostream>
using namespace std;

struct Person {
    string name;
    Person(const char* s) : name(s) {
        cout << "Person(const char*)" << endl;
    }
    Person(const Person& other) {
        cout << "Person(&)" << endl;
    }
};

Person foo(Person p){
    cout << "in foo()" << endl;
    return p;
}

Person bar(const char *s) {
    cout << "in bar()" << endl;
    return Person(s);
}

int main() {
    Person p1 = foo("Trump");
    cout << "-----------------------" << endl;
    Person p2 = bar("Biden");
}
```

运行结果如下：

![](../../../assets/Pasted%20image%2020250414143019.png)

这是因为我们在 `p1` 的构造中直接传的是字符串，这并没有调用拷贝函数，但是在 `return p` 当中就调用拷贝函数了，而在 `bar` 函数中 `Person(s)` 会直接在 `p2` 的内存地址上构造，无需中间临时对象，因此不会触发拷贝构造函数

这是因为在 C++ 中有一个**返回值优化**（Return Value Optimization，RVO）机制，它允许编译器在函数返回时直接在调用者的内存空间中构造对象，而不是先在临时对象中构造再拷贝到调用者的内存空间。这种优化可以避免不必要的拷贝，提高性能，我们添加选项 `-fno-elide-constructors` 可以关闭这个优化：

![](../../../assets/Pasted%20image%2020250414143559.png)
***


