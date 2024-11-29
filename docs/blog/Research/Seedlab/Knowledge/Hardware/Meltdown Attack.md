---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
---  

# Meltdown 攻击

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
			printf("访问array[%d*4096] 的时间：%d 个CPU周期\n",i, (int)time2);
		}
		return 0;
	}
	```
	
	用 `gcc -march=native CacheTime.c` 编译并运行上面的代码，我们首先访问了数组的 `array[3*4096]` 和 `array[7*4096]`，然后查看访问数组 `array[k*4096]`（$k=0,1,2,...,9$）需要的时间，可以发现 `array[3*4096]` 和 `array[7*4096]` 比其他元素访问时间更短，这是因为他们先提前被访问过，已经放入了 CPU 的缓存。


