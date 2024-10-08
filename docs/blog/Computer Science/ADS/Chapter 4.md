---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
--- 

# Chapter 04 : Leftist Heaps and Skew Heaps

## Leftist Heap

### 概念

**左偏堆(Leftist Heap)**，它相比于普通的堆，更好的一点在于它支持快速的堆合并操作。“左偏”，并不断将新的东西往右侧合并，来实现每次都是往相对小的那一侧塞进东西，进而保相对证了这个

由于左偏堆不再是一个完全二叉树，所以我们不能再像维护大根堆小跟堆那样用数组来维护它了。

一个左偏堆的结点维护了左右子堆的地址、自身的键值、和一个“**距离(dist)**”。