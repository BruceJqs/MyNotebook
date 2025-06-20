---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
--- 

# Chapter 11 : Smart Pointers

## Smart Pointers in Standard Library

在标准库中，有一些原始指针：

- `std::unique_ptr`：独占所有权，不能被复制
	- 支持移动操作（`std::move`），允许将所有权从一个 `std::unique_ptr` 转移到另一个。当所有权转移后，原 `std::unique_ptr` 不再指向该对象
- `std::shared_ptr`：共享所有权，可以被复制
	- 它内部通过**引用计数**(reference count) 机制来跟踪有多少个 `std::shared_ptr` 实例正共享该对象
	- **引用计数**：
	    - 当一个新的 `std::shared_ptr` 指向该对象（例如通过拷贝构造或赋值），引用计数会增加
	    - 当一个 `std::shared_ptr` 被销毁或不再指向该对象时，引用计数会减少
	- 自动销毁：只有当最后一个指向对象的 `std::shared_ptr` 被销毁，使得引用计数降为零时，该对象才会被自动删除
- `std::weak_ptr`：不拥有所有权，不能被复制
- `std::auto_ptr`：过时的智能指针，不能被复制，在 C++11 中被删除

!!! example "Example"

	假如我们有以下代码：
	
	```cpp
	#include <iostream>
	#include <memory>
	using namespace std;
	
	struct Resource{
	    int data;
	    Resource(int d = 0): data(d) {}
	    ~Resource(){
	        cout << "Resource destroyed, data = " << data << endl;
	    }
	};
	
	int main(){
	    {
	        unique_ptr<Resource> p1(new Resource);
	        unique_ptr<Resource> p2(new Resource(7));
	        cout << "p1->data = " << p1->data << endl;
	
	        p1 = p2;
	    }
	    cout << "\nbefore quit..." << endl;
	}
	```
	
	编译运行会发现会报错：
	
	![](../../../assets/Pasted%20image%2020250620122513.png)
	
	这是因为 `std::unique_ptr` 不允许被复制，只能转移所有权，我们用 `std::move` 函数可以转移：
	
	```cpp
	int main(){
	    {
	        cout << "--- before move ---" << endl;
	        unique_ptr<Resource> p1(new Resource);
	        unique_ptr<Resource> p2(new Resource(7));
	        cout << "p1 = " << p1.get() << endl;
	        cout << "p1->data = " << p1->data << endl;
	        cout << "p2 = " << p2.get() << endl;
	        cout << "p2->data = " << p2->data << endl;
	
	        p1 = std::move(p2);
	
	        cout << "--- after move ---" << endl;
	        cout << "p1 = " << p1.get() << endl;
	        cout << "p1->data = " << p1->data << endl;
	        cout << "p2 = " << p2.get() << endl;
	        cout << "p2->data = " << p2->data << endl;
	    }
	    cout << "\nbefore quit..." << endl;
	}
	```
	
	但是会出现 Segmentation Fault：
	
	![](../../../assets/Pasted%20image%2020250620131606.png)
	
	这是因为 `std::move` 只是转移了所有权，`p2` 变成了空指针，所以不能再访问 `p2->data`
