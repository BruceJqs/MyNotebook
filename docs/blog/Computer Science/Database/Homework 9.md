---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - [footer]()
  - feedback
comments: true
--- 

# Homework 09

## 12.1

> SSDs can be used as a storage layer between memory and magnetic disks, with some parts of the database (e.g., some relations) stored on SSDs and the rest on magnetic disks. Alternatively, 
> SSDs can be used as a buffer or cache for magnetic disks; frequently used blocks would reside on the SSD layer, while infrequently used blocks would reside on magnetic disks. 
> 
> a. Which of the two alternatives would you choose if you need to support real-time queries that must be answered within a guaranteed short period of time? Explain why. 
> 
> b. Which of the two alternatives would you choose if you had a very large _customer_ relation, where only some disk blocks of the relation are accessed frequently, with other blocks rarely accessed. 

（a）更倾向于选择第一种方案，因为第一种方案能保证保持一定的读取速率，而如果采用第二种方案，如果碰到 Cache Miss 的情况会造成非常大的时延

（b）更倾向于选择第二种方案，因为只有一些关系会被频繁访问而其他的关系不会被频繁访问，所以可以将频繁访问的关系放在 SSD 上，其他关系放在磁盘上，将 SSD 作为缓存处理
***
## 13.5

> It is important to be able to quickly find out if a block is present in the buffer, and if so where in the buffer it resides. Given that database buffer sizes are very large, what (in-memory) data structure would you use for this task? 

使用 Hash 表来存储，Hash 函数能快速计算出数据块是否在 buffer 当中，且能找到具体的位置
***
## 13.9

> In the variable-length record representation, a null bitmap is used to indicate if an attribute has the null value. 
> 
> a. For variable-length fields, if the value is null, what would be stored in the offset and length fields?
> 
> b. In some applications, tuples have a very large number of attributes, most of which are null. Can you modify the record representation such that the only overhead for a null attribute is the single bit in the null bitmap? 

（a）设置 length field 为 -1，offset field 为任意值

（b）将 null bitmap 放到记录的前面
***
## 13.11

> List two advantages and two disadvantages of each of the following strategies for storing a relational database: 
> 
> a. Store each relation in one file. 
> 
> b. Store multiple relations (perhaps even the entire database) in one file. 

（a）优点：

- 可以更好地将经常访问的关系放在 SSD，不常访问的关系放在磁盘上
- 每个表对应一个独立文件，​结构简单直观，方便直接定位和管理维护

缺点：

- 跨表操作效率低
- 管理复杂度高

（b）优点：

- 跨表操作效率高
- 无须跨文件协调，操作更加便捷

缺点：

- 高并发场景容易造成竞争
- 单文件体积变大，读写性能下降

