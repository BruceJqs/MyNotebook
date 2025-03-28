---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
---  

# Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks

## Abstract

说明当时的模型基于知识密集型任务（指人类也需要通过外部知识学习才能完成的任务）表现并不好，所以提出 RAG，实现方式是用一个训练好的 seq2seq 模型结合从维基百科的向量索引进行检索的神经元检索器，组合在一个端到端训练的概率模型中

![](../../../../assets/Pasted%20image%2020250328232838.png)

* * *

## Introduction

- 当时的模型无法扩展/修改他们的内存（导致幻觉）
- 已经有模型（REALM 和 ORQA）将语言模型和微分检索器结合在一起，但是它们只探索了开放域问答（即问题任意从海量数据当中获取回答）方面
- 他们将这种思想带到 NLP 的主流模型中（比如 seq2seq 模型，序列到序列）
- RAG 的思想是通用的（被称为通用微调手段）
- 检索器检索潜在的文档，seq2seq 模型以这些文档和输入为条件得到输出
- 根据前 K 近似值边缘化潜在文档（**？什么是边缘化**），有两种方式：
    - 一种是 RAG-Sequence，使用同一个文档来预测每一个目标 token
    - 另一种是 RAG-Token，根据不同的文档来预测每一个目标 token

* * *

## Methods

- 核心要义：根据输入 $x$ 获得文档 $z$，将它们作为生成目标序列 $y$ 的额外的信息
- 两个部件：一个根据查询 $x$ 和固定参数 $\eta$ 得到前 $K$ 相关文本段落 $z$ 的检索器 $p_{\eta}(z|x)$ 和一个根据一个固定参数 $\theta$，前 1～i-1 个 token，$x$ 和 $z$ 得到当前 token 的生成器 $p_{\theta}(y_i|x,z,y_{1:i-1})$

### Models

- RAG-Sequence Model：使用同样的获取的文档来生成完整的序列

![](../../../../assets/Pasted%20image%2020250328232912.png)

- RAG-Token Model：每一个目标 token 文档都不一样

![](../../../../assets/Pasted%20image%2020250328232936.png)

- 将目标类视为长度为 1 的目标序列，RAG 用于序列分类任务时两种模型是等效的（**？**）

### Retriever: DPR

> 检索器基于 DPR，一种二进制编码架构，他们使用 DPR 的预训练好的二进制编码器来初始化检索起

![](../../../../assets/Pasted%20image%2020250328232949.png)

其中 $\pmb{d}(z)$ 是经过 $\text{BERT}_{\text{BASE}}$ 文档编码器处理过的一个文档的密集表述，$\pmb{q}(x)$ 是同样经过文档编码器处理的询问表述。

- 在这其中找到前 $k$ 大的概率 $p_{\eta}(z|x)$ 是一个 MIPS 问题（即在一堆向量中找到与输入向量点积最大的那一个），可以在亚线性（Sub-linear，表达式为 $y=a+b*x^n$）时间内解决

### Generator: BART

> 生成器本质上可以用任何译码-解码器，他们使用了 BART-large，一个 400M 参数的预训练的 seq2seq transformer，用很多去噪目标和噪声函数进行训练

- 对于输入 $x$ 和 $z$ ，他们单纯将其前后拼接起来

### Training

他们共同训练检索器和生成器组件，并没有直接给出应该检索什么文档，给定输入/输出对，利用 Adam 随机梯度下降，更新文档编码器训练成本较高，但是这一步对于强大的性能没有必要，只需要微调查询编码器和生成器即可

### Decoding

> 两种模型用不同的方式来估计 $\arg\max_y p(y|x)$

- RAG-Token：可以看作是一个标准的、自回归的 seq2seq 生成器，有转换概率 $p_{\theta}'(y_i|x,y_{1:i-1})=\sum\limits_{z\in\text{top-k}(p(\cdot|x))}p_{\eta}(z_i|x)p_{\theta}(y_i|x,z_i,y_{1:i-1})$ ，我们可以直接将 $p_{\theta}'(y_i|x,y_{1:i-1})$ 插入标准解码器进行解码
- RAG-Sequence：因为 $p(y|x)$ 并不能被分解为传统的样子（没法分解为一个一个 token），所以继而在文档 $z$ 执行 beam search，用 $p_{\theta}(y_i|x,z,y_{1:i-1})$ 来打分，得到一系列 $y$ 的假设（这些假设可能都不一定出现在文档束中），对 $y$ 不在其中的文档 $z$ 进行额外的正向传递，将生成器的概率乘以 $p_{\eta}(z|x)$ 然后对 beams 求和，称为完全译码；当输出序列变得更长的时候 $y$ 的假设也会变得非常多，需要更多的正向传递，因此对于没有从基于 $x,z_i$ 的 beam search 得到的 $y$，可以估计 $p_{\theta}(y|z_i)\approx 0$ ，称之为快速译码（这段没懂）

### Experiments

- 使用 Wikipedia 2018.12 dump 作为知识库，21M 的文章，每个文章被分为 100 词的块，$k\in\{5,10\}$
- 测试了开放域问答、抽象问题回答、Jeopardy 问题生成（根据答案生成问题）、事实判断
- 对比对象：
    
    - 开放域问答：T5-11B，T5-11B+SSM，REALM，DPR
    - 抽象问题回答 & Jeopardy 问题生成 & 事实判断：SotA，BART

### Results

- RAG 证明了无论是重排序器还是分离式阅读器对于最先进的性能来说都是不必要的
- 对于 Jeopardy 问题的生成，RAG 模型比 BART 模型更真实和具体

## Related Work

- 提高 NLP 任务的性能
- 学习检索
- 单任务检索
- 以存储为基础的架构
- 检索与编辑

## Discussion

- 未来可以研究两个组件的联合预训练