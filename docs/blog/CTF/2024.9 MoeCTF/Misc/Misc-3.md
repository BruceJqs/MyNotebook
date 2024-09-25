---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
---  

# Misc-3｜ez_Forensics

## 做题心得 & 感想

当附件一下下来发现是一个 .raw 文件，Bruce 就开始狂喜了（短学期学的用上了！）

此时此刻真的感受到了“学有所用”这四个字！
***
## Writeup

一道典型的内存取证问题，命令行 `strings flag.raw|grep flag`，发现是有 flag.txt 存在的：

![](../../../../assets/Pasted%20image%2020240922225941.png)

命令行 `foremost flag.raw` 尝试分离，但是没有发现 flag.txt 文件：

![](../../../../assets/Pasted%20image%2020240922234156.png)

祭出我们的最后武器：Volatility！命令行 `python2 volatility/vol.py -f flag.raw imageinfo` 查看操作系统：

![](../../../../assets/Pasted%20image%2020240922234327.png)

可以发现是 win7x64 系统，再利用命令行 `python2 volatility/vol.py -f flag.raw --profile Win7SP1x64 cmdscan`查看 cmd 历史：

![](../../../../assets/Pasted%20image%2020240922234435.png)

其中就出现了 flag：`moectf{WWBGY-TLVC5-XKYBZ}`
