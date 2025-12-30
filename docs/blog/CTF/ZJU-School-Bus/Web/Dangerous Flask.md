# Dangerous Flask

## Tag

Flask Debug 模式
***
## Writeup

观察题目是一个投票系统，投票会传一个 POST 包过去，我们使用 Burp 改动中间的参数，整一个不存在的格式过去，触发调试返回输出：

![](../../../../assets/PixPin_2025-11-13_19-26-16.png)

里面就含有 Flag