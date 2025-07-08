---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
---  

# Buffer Overflow

## Memory Layout

### Virtual Address v.s. Physical Address

在现代计算机中，它们都不会使用物理地址，而是使用虚拟地址。对于 RAM，每一个字节都有它们的物理地址，而对于每个进程来说，操作系统会在 RAM 当中分配一块内存给进程，在进程当中的内存则是使用虚拟地址，操作系统会将它们通过页表映射到 RAM 的物理地址上，并保证每个进程的虚拟地址空间是独立的，如果有冲突，那么就形成了内存共享。
***
### Memory Layout

![](../../../../../assets/Pasted%20image%2020250706135814.png)

以上图为例，内存的布局从低地址到高地址分为以下几个部分：

- **Text Segment**：存放程序的代码，通常是只读的
- **Data Segment**：存放已初始化的全局变量和静态变量（例如右侧代码中的全局变量 `x`）
- **BSS Segment**：存放未初始化的全局变量和静态变量（例如右侧代码中的静态变量 `y`）
- **Heap**：动态分配内存的区域，通过 `malloc` 等函数进行分配（例如右侧代码中 `ptr` 分配出的两个整数 `ptr[1], ptr[2]`），向高地址增长
- **Stack**：存放局部变量、函数参数和返回地址等信息（例如右侧代码中的局部变量 `a,b` 和 `ptr`），向低地址增长
***
## Stack Layout

> Buffer Overflow 攻击，顾名思义是要针对缓冲区进行攻击，而缓冲区是存放在栈上的，因此我们需要了解栈的布局。

### Arguments and Local Variables

![](../../../../../assets/Pasted%20image%2020250706140656.png)

以上图为例，我们定义了一个函数 `func`，当函数被调用时，操作系统会给这个函数在栈上分配一个栈帧（Stack Frame），栈帧的布局如下：

- 函数参数（例如上图中的 `a,b`）
- 特殊区域，存放两个数据，一个是父函数帧指针（也称 Old ebp，用于返回父函数），另一个是返回地址，对于 32 位系统它们各占 4 字节
- 局部变量（例如上图中的 `x,y`）

在编译过程中，编译器是无法知道这个栈帧在栈上的具体位置的，因为栈是动态分配的，有时候甚至通过改变环境变量都可以改变栈帧的位置，那么编译器也无法知道函数参数、局部变量等信息，为了解决这个问题，我们有一个特殊的寄存器叫做帧指针（Frame Pointer，在 x86 架构中也叫做 EBP），当函数被调用时，它会指向函数当中特殊区域的起始位置，那么对应地，函数参数和局部变量就可以通过帧指针来访问：

![](../../../../../assets/Pasted%20image%2020250706141755.png)

如上图，函数参数 `a,b` 分别存放在帧指针偏移 8 和 12 的位置（且位置是固定的无法改变，函数的第一个参数总是存放在帧指针偏移 8 的位置，第二个参数存放在帧指针偏移 12 的位置），这也很好解释了上面汇编语言计算 `x` 的过程

!!! example "Another Example"

	下面是一个更复杂的例子：
	
	```c
	/* stack.c */
	
	/* This program has a buffer overflow vulnerability. */
	/* Our task is to exploit this vulnerability */
	#include <stdlib.h>
	#include <stdio.h>
	#include <string.h>
	
	int foo(char *str){
		char buffer[100];
		
		/* The following statement has a buffer overflow problem */
		strcpy(buffer, str);
		
		return 1;
	}
	
	int main(int argc, char **argv){
		char str[400];
		FILE *badfile;
		
		badfile = fopen("badfile", "r");
		fread(str, sizeof(char), 200, badfile);
		foo(str);
		
		printf("Returned Properly\n");
		return 1;
	}
	```
	
	在一开始，首先运行的是 `main` 函数，那么会分配一个栈帧，当 `main` 函数调用 `foo` 函数时，会分配一个新的栈帧在 `main` 函数之上，并更新 ebp 寄存器指向新的特殊区域的起始位置
	
	当我们执行完 `foo` 函数时，需要返回到 `main` 函数，这时候特殊区域保存的第一个参数就起作用了，正是因为其保存了父函数的帧指针位置，才能够正确地返回到 `main` 函数的栈帧上；同时，我们还需要知道返回到 `main` 函数下面要执行什么指令，这个返回地址就保存在特殊区域的第二个参数当中。然后我们就可以释放掉 `foo` 函数的栈帧，更新 ebp 寄存器回到 `main` 函数的栈帧上。
	
	当然，在 `foo` 函数中我们还需要调用 `strcpy` 函数，同理，`strcpy` 函数也会分配一个新的栈帧在 `foo` 函数之上，并更新 ebp 寄存器指向新的特殊区域的起始位置，同时保存 `foo` 的 ebp 和 `strcpy` 执行完后要返回到 `foo` 函数的指令地址
	
	最后整个栈的布局如下：
	
	![](../../../../../assets/Pasted%20image%2020250706164802.png)
***
## Buffer-Overflow Vulnerability

### Copy Data to Buffer

假设我们有如下代码：

```c
#include <string.h>
#include <stdio.h>

void main()
{
	char src[40]="Hello World \0 Extra string";
	char dest[40];
	
	// copy to dest (destination) from src (source)
	strcpy(dest, src);
}
```

我们使用 `strcpy` 函数将 `src` 的内容复制到 `dest` 中，而 `strcpy` 的逻辑是遇到 `\0` 字符就停止复制，如果字符串没有 `\0` 字符，在复制完毕后编译器会自行添加一个 `\0` 字符到 `dest` 的末尾
***
### Buffer Overflow

我们有如下代码：

```c
#include <string.h>

void foo(char *str){
	char buffer[12];
	
	/* The following statement will result in buffer overflow */
	strcpy(buffer, str);
}

int main(){
	char *str = "This is definitely longer than 12";
	foo(str);
	
	return 1;
}
```

当 `foo` 函数被调用时，栈上会分配一个栈帧，里面有一个长度为 12 的缓冲区 `buffer`，但是我们传入的字符串长度超过了 12 个字节，因此在执行 `strcpy` 函数时，会将超过 12 个字节的内容写入到 `buffer` 中，这就导致了缓冲区溢出（Buffer Overflow）问题，我们可以画出栈的布局：

![](../../../../../assets/Pasted%20image%2020250706171902.png)

- 当我们执行 `strcpy` 函数时，栈帧中 `buffer` 的内容会被覆盖，导致 `buffer` 中的内容变成了 `This is definitely longer than 12`，而这个字符串长度超过了 12 个字节，因此会覆盖掉 `buffer` 之后的内容，那么就会覆盖到 old ebp 甚至是返回地址和函数参数，这样就会导致程序崩溃
	- 一个程序崩溃其中可能的原因就是返回地址被更改，而这个返回地址在栈中是一个虚拟地址，对此会有三种情况：
	1. 这个虚拟地址可能不会映射到一个真实的物理地址，CPU 会发起错误，操作系统会收到这个错误并将其传递到进程当中，如果进程没有处理这个错误，那么操作系统就会终止这个进程从而导致程序崩溃
	2. 这个虚拟地址也可能映射到一个真实的物理地址，但是其保存的可能是一个不合法的指令，CPU 不知道该怎么执行并发起错误
	3. 虚拟地址映射到一个真实的物理地址，保存的是一个合法的指令，但是这个区域是一个受限制的区域（例如操作系统 Kernel），我们也无法跳转到 Kernel 当中，同理程序也会崩溃
		- 事实上，Null Pointer 就是这种情况，它指向的就是物理地址为 0 的区域，但是这个区域是 Kernel 当中的地址，因此无法访问导致程序崩溃

那么，如果这是一个权限比较大的程序（例如 Set-UID 程序或者是一个运行在服务器上的程序），我们可以利用 Buffer Overflow 攻击来覆盖返回地址，跳转到我们想要执行的代码上，这就是 Buffer Overflow 攻击的核心思想。

具体来说，我们可以将我们的代码保存在栈上（也通过 `strcpy` 函数，但是不能覆盖 main 函数的栈帧），如果我们知道我们代码保存的地址，那么我们就可以将返回地址覆盖为我们代码的地址，这样当函数执行完毕后，就会跳转到我们的代码上执行。

![](../../../../../assets/Pasted%20image%2020250706172322.png)
***
### Exploiting Buffer Overflow

实现 Buffer Overflow 攻击主要有两点：

1. 我们需要首先知道栈帧的返回地址相对于 `buffer[0]` 的偏移量，方便我们通过溢出来覆盖返回地址
2. 其次，我们将我们需要执行的恶意代码也通过溢出的方式保存在栈上，但是我们还需要知道恶意代码的第一条指令具体的地址，即用哪个值来覆盖返回地址

对于第一点，偏移量是固定且已知的，但是对于第二点，我们无法知道准确的地址值，没有其他优化的情况下只能靠猜且成功率极低。

但是，我们可以在我们的恶意代码前面插入许多 NOP 指令（在 x86 架构中是 `0x90`），只要我们能跳入到 NOP 指令的区域，那么按照顺序我们就能来到恶意代码的区域，如下图所示：

![](../../../../../assets/Pasted%20image%2020250706225017.png)

对此，我们只要知道 ebp 的值和 buffer 的地址，就可以推算出偏移量，再在 ebp 的基础上加一个值（只要能跳到 NOP 均可）来覆盖返回地址，就能实现 Buffer Overflow 攻击
***
#### Obtaining EBP and Buffer Address

对于 ebp 和 buffer 的地址，我们可以通过调试器来获取，例如使用 `gdb` 调试器：

![](../../../../../assets/Pasted%20image%2020250706225433.png)

如上图，`-g` 选项能帮助我们编译出带有调试信息的可执行文件，便于我们使用 `gdb` 调试器来获取 ebp 和 buffer 的地址，其他参数将会在后面讲到

我们通过使用 `b foo` 命令使得当程序执行到 `foo` 函数时暂停，然后使用 `foo` 命令运行程序，这时候程序就停在了调用 `foo` 函数之前

这时候，我们就可以通过 `p $ebp` 命令来获取 ebp 的值，通过 `p &buffer` 命令来获取 buffer 的地址，这样就可以通过 `p/d` 命令计算出偏移量了

如上图，我们最后得到偏移量为 108，那么返回地址的偏移量即为 112（还要加上 old ebp 的 4 字节），并在这里覆盖值为 `ebp+8` 即可（在现实攻击中会加的更多，因为没有在 gdb 中运行的程序和在 gdb 中运行的程序的栈是不同的，在 gdb 中运行的程序的栈更深一些，那么对应到不在 gdb 中运行的程序相对应的 offset 要更大一些，通常为 100, 120 更稳妥）

- 需要注意，`strcpy` 的机制是遇到 `\0` 字符就停止复制，因此在返回地址覆盖的时候我们不能使得返回地址的值包含 `\0` 字符，否则会导致复制提前结束，返回地址无法被正确覆盖（例如上面如果 `ebp=0xbfffea98`，而我们加上了 68，最后会导致返回地址为 `0xbfffeb00`）
- 如果我们不知道 buffer 具体的大小，只知道大小范围以及 buffer 的起始地址，我们可以在 buffer 最大可能的大小情况下选取一个合适的返回地址，并在这个范围内全部都填充这个地址，不管 buffer 有多大返回地址都能覆盖到
***
#### Constructing Shellcode

对于一个攻击来说，最大的破坏就是获取到一个 Shell，这样我们就可以在上面执行任意命令了，用 C 语言实现一个 Shell 的代码如下：

```c
#include <unistd.h>

void main(){
	char *name[2];
	name[0] = "/bin/sh";
	name[1] = NULL;
	execve(name[0], name, NULL);
}
```

我们将其编译成可执行文件（例如 a.out），就可以使用 `ghex a.out` 命令来查看其十六进制内容：

![](../../../../../assets/Pasted%20image%2020250706232701.png)

但是，这个可执行文件的内容太大了（可以看到有 7400B），且包含了很多冗余信息，更重要的是，里面包含了 `\0`！所以我们不能采用这种方法，而是根据 C 代码直接使用汇编语言来编写。根据上面的 C 代码，最重要的就是 execve 这个函数，对于一般的函数，我们只需要将参数推到栈中即可，但是 execve 函数是一个系统调用函数，它的参数需要放在寄存器中来传递，在 x86 架构中，第一个参数的寄存器为 `ebx`，第二个参数的寄存器为 `ecx`，第三个参数的寄存器为 `edx`。

!!! question "如何获得地址？"

	我们可以通过栈指针（Stack Pointer）来处理，对于 `ebx` 来说，它需要指向字符串 “/bin/sh\0”，因此我们需要将这个字符串放在栈上，此时栈指针所指向的位置即为字符串的地址，将其赋值给 `ebx`；对于 `ecx` 来说，它指向的是一个数组，第一个元素是字符串，第二个元素为 0，我们可以直接将 `ebx` 赋值给第一个元素，此时栈指针所指向的位置就可以直接赋值给 `ecx`，最后 `edx` 直接赋值为 0 即可。
	
	![](../../../../../assets/Pasted%20image%2020250706234012.png)

有了上面的逻辑，我们就可以写出汇编代码：

```asm
xorl %eax, %eax ; 清零 eax 寄存器
pushl %eax ; 将 0 推到栈中，作为字符串结尾
pushl $0x68732f2f ; 推入字符串 "//sh"（等价于 "/sh"）
pushl $0x6e69622f ; 推入字符串 "/bin"
movl %esp, %ebx ; 将栈指针的值赋值给 ebx
pushl %eax ; 将 0 推到栈中，作为数组的第二个元素
pushl %ebx ; 将 ebx 的值推到栈中，作为数组的第一个元素
movl %esp, %ecx ; 将栈指针的值赋值给 ecx
movl %eax, %edx ; 将 0 赋值给 edx
movb $0x0b, %al ; 将系统调用号 11（execve）赋值给 al 寄存器（al 寄存器是 eax 寄存器的低 8 位，当 eax 为系统调用号时才能调用对应函数）
int 0x80 ; 发起系统调用
```

??? question "为什么要使用异或操作和低八位赋值操作？"

	这两个为什么的原因是一致的，我们的代码里面不能出现 `\0` 字符！因此清零寄存器需要使用 `xorl` 指令，而不是 `movl` 指令，赋值系统调用号 11 也需要使用 `movb` 指令，而不是 `movl` 指令（如果使用 movl 指令就会将 0x0000000b 推到栈上，而不是 0x0b，这样就会导致字符串中出现 `\0` 字符）

最终的示例代码如下：

![](../../../../../assets/Pasted%20image%2020250706231059.png)

!!! example "Another Example"

	如果我们想要执行命令 `/bin/bash -c '/bin/echo "Hello World"'`，汇编代码如下：
	
	同理，我们只需要修改参数数组的部分即可，第一个元素为字符串 `/bin/bash`，第二个元素为字符串 `-c`，第三个元素为字符串 `/bin/echo "Hello World"`，最后一个元素为 0
	
	![](../../../../../assets/Pasted%20image%2020250706235343.png)
	
	![](../../../../../assets/Pasted%20image%2020250706235611.png)
	
	- 写成 `/bin////bash` 和 `-ccc` 是因为要凑 4 字节
***
## Countermeasures

### Developer's Approaches

对于程序开发者来说，他们可以通过以下方式来防止 Buffer Overflow 攻击：

- 检查数据长度：在复制数据之前，检查数据的长度是否超过缓冲区的大小，如果超过则拒绝复制
- 不要让用户来决定长度，由开发者来决定长度，使用例如 `strncpy`、`strncat`、`snprintf`、`fgets` 等能决定长度的函数来代替 `strcpy`、`strcat`、`sprintf`、`gets` 等函数
- 使用安全的库例如 libsafe，它们会在运行时检查复制时是否超过 ebp，如果超过就拒绝复制
- 在不考虑性能的情况下可以使用安全的语言例如 Java，Java 有特殊的机制来防止 Buffer Overflow 攻击

!!! example "Heartbleed Attack"

	Heartbleed 攻击就是一个典型的让用户决定长度的攻击，对于一个简单的输出服务来说，用户首先会向服务器端发送一个请求，服务器端收到了请求后会将其放到内存当中，再从内存当中复制到一个 buffer 当中并返回用户。
	
	但是，用户的请求当中包含了复制的长度，如果用户指定的长度超过了实际复制的长度，那么会导致 buffer 的大小远超实际大小，这样就会导致内存当中的一些信息（例如用户的各种信息）被泄露到用户端。
***
### Address Space Layout Randomization (ASLR)

在之前的实践中，为了获取 ebp 的值，我们使用了 gdb 调试器来获取，但是在实际攻击中，我们是不会获得源代码的，更不可能通过编译加调试的方法获取 ebp 的值，因此我们才需要猜我们的恶意代码在哪里。但是在这之前，操作系统给栈分配内存时，这片内存在进程的位置是固定的，那么猜测的难度就取决于栈有多深，一般只有递归程序才会有很深的栈，再加上我们有 NOP 指令的帮助，猜测的成功率就会大大提高。

因此，大多数操作系统会使用地址空间布局随机化（ASLR）来防止这种情况发生。ASLR 会在每次程序运行时随机分配栈起始的虚拟地址，这样就使得攻击者还得去猜测栈的地址，难度大大提高

我们可以通过 `sudo sysctl -w kernel.randomize_va_space=0` 关闭 ASLR 功能

![](../../../../../assets/Pasted%20image%2020250707002744.png)

如上图，可以看到，如果我们关闭了 ASLR 功能，那么栈和堆的地址就会变得固定，但是如果我们开启了 ASLR 功能，栈的地址就会随机：

![](../../../../../assets/Pasted%20image%2020250707002845.png)

- 事实上，如果我们设置了 `kernel.randomize_va_space=2`，那么不仅是栈的地址会随机，堆的地址也会随机

但是，ASLR 也有它的缺点，它的随机取决于内存的大小，如果内存很小，那么随机的范围就很小，攻击者可以通过暴力破解来获取地址，例如对于一个 32 位系统来说，它的大小为 $2^{32}$，但是有一部分内存分给了 Kernel，剩下的部分都可以用来随机，研究表明，随机化的位数只有 19 位，可以通过 bruteforce 来暴力破解；而对于 64 位来说难度就比较大了，因此 ASLR 只能提高攻击的难度，而不能完全防止攻击。

![](../../../../../assets/Pasted%20image%2020250707003430.png)
***
### Shell Program's Defense

如我们之前所说，一般的攻击都会以获取 Shell 为目标，最粗暴的防御方式就是禁止在一些权限高的进程（例如 Set-UID 进程）中执行 Shell 程序，判别方法也非常简单，只要 Shell 程序判断 euid 和 ruid 是否相等，如果相等就可以执行 Shell 程序，否则就让 euid 和 ruid 相等，实现权限降级。实验证明，bash 有这个机制而 zsh 没有这个机制：

![](../../../../../assets/Pasted%20image%2020250707004148.png)


但是，这样的防护措施破解也非常简单，我们只要在攻击代码中添加一条语句 `setuid(0)`，使得 euid 和 ruid 相等即可：

![](../../../../../assets/Pasted%20image%2020250707004431.png)

![](../../../../../assets/Pasted%20image%2020250707004744.png)

- 如上图，前四行汇编代码就是 setuid(0) 的实现
***
### Nonexecutable Stack

在之前的攻击实践当中，我们通过将恶意代码放在栈上来实现攻击，但是如果我们将栈设置为不可执行，不能运行任何从栈上来的东西，那么即使将代码放在栈上也被视作是一堆数据，无法在栈上执行恶意代码，这样就可以防止 Buffer Overflow 攻击。

- 我们可以通过编译选项 `-z execstack` 来打开栈的可执行性，通过 `-z noexecstack` 来关闭，这在一个可执行文件的 Header 中有专门的一个位来表示

![](../../../../../assets/Pasted%20image%2020250707005156.png)

这样的硬件机制能很好地防止那些想要在栈上保存并执行恶意代码的攻击，但是还是有攻击能绕过这个机制，这个攻击被称为 Return-to-libc 攻击，其主要机制是在跳转地址时不跳转回栈上，而是跳转到 libc 库中已经存在的函数上（他们也会被保存在内存当中，例如 `system` 函数），并传入一个参数（例如 `/bin/sh`）来执行，这样就可以实现攻击。
***
### Compiler's Approach：StackGuard

StackGuard 的主要机制是通过在返回地址和 Buffer 中间添加一个 Guard，它的值在函数调用时会被设置为一个随机值，并在函数返回时检查这个值是否被修改，如果被修改了就说明发生了 Buffer Overflow 攻击，此时程序会终止。

- 我们可以通过编译选项 `-fno-stack-protector` 关闭 StackGuard

![](../../../../../assets/Pasted%20image%2020250707010237.png)

从实现上来说，我们需要定义一个全局变量 secret（全局变量是保存在堆上而不是栈上的，这样就防止每次调用一个函数时都要重新更新 secret 的值），然后在函数调用时将 secret 的值赋值给 Guard，并在函数返回时检查 Guard 的值是否被修改，如果被修改了就说明发生了 Buffer Overflow 攻击，此时程序会终止。

![](../../../../../assets/Pasted%20image%2020250707010840.png)

!!! note "StackGuard Implementation in GCC"

	![](../../../../../assets/Pasted%20image%2020250707011022.png)
	
	如上图所示我们可以得知，Guard 被保存在了 ebp-12 的位置
***
## Heap-Based Buffer Overflow

在之前我们所提到的都是在栈上的 Buffer Overflow 攻击，但是实际上，Buffer Overflow 攻击也可以发生在堆上，如下面的代码，我们利用 malloc 来构造我们的 buffer：

![](../../../../../assets/Pasted%20image%2020250707011225.png)

问题在于，返回地址在栈上，而 buffer 在堆上，而在操作系统中，是不可能实现让堆上的 buffer 溢出足够多到覆盖栈上的返回地址的。

但是，与栈只是不断弹入弹出数据而变长变短不同，操作系统对于堆的实现是，内存的分配是动态的，位置是不固定的，操作系统需要一些元数据来管理堆上的内存（例如哪些块是被占用的，哪些块是空闲的），这些元数据也同样位于堆上，且是通过链表的方式来链接空闲块和已分配块的，因此我们可以通过 Buffer Overflow 攻击来覆盖这些元数据，从而实现攻击。

对于堆上的链表（双向链表）来说，删除一个节点 p（其前继节点为 q）的 c 代码如下所示：

```c
q = p -> pre;
q -> next = p -> next;
p -> next -> pre = q;
```

这个函数调用是保存在库中，在释放内存时会自动调用，假设我们已经知道了返回地址的位置，那么我们可以通过 Buffer Overflow 让 `p -> pre` 为这个位置，`p -> next` 为恶意代码的地址，那么返回地址即为 `q -> next`，根据上面的代码我们就可以改变返回地址了，原理图如下：

![](../../../../../assets/Pasted%20image%2020250707012927.png)













