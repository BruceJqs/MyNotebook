---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
---  

# Misc｜Master of C++

## 做题历程 & 感想

这是一个全新的 Misc 题型：PPC（Professionally Program Coder），即编程类题目，梦回 NOIP（bushi）

Bruce 完全没学过 C++ 的 template 折腾了半天还请教了潘神帮忙才弄出来（悲）
***
## Writeup

没什么好说的，其实本身难度应该不高（）无非只是要掌握 template 的语法 qwq 。代码如下：

```c++
template <int N, int I> struct is_prime{
  static const bool value = (N % I) && is_prime<N, I-1>::value;
};
template <int N> struct is_prime<N, 1>{
  static const bool value = (N>1);
};
int main(){
  return is_prime<ARG, ARG<=1?1:ARG/2>::value ? 0 : 1;
}
```

这里大致讲一下代码的思路，非常的常规（即枚举 2 到 $\frac{N}{2}$ 是否有 $N$ 的因数），通过类似嵌套递归迭代的方式枚举。

为了题目的要求压缩代码，这里对特判花了一些心思（也是潘神提出的）：

首先是迭代的终止条件，当枚举到 1 时默认返回 True（当 $N>2$ 时）

其次是小于等于 1 的情况，我们将这种情况和上种情况统一起来就是第二个 template 当中的 $N>1$，同时在 main 中用一个三目运算符把第二个参数调整一下。

最后得到 flag：`ZJUCTF{pR3m4tuR3_0PT1miz4t1oN_1s_thE_R00t_of_4LL_3v1l}`