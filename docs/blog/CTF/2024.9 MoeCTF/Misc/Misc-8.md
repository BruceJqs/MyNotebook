---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
---  

# Misc-8｜ez_F5

## 复盘心得

处理图片隐写题还是没个章程啊……

这回 MoeCTF 真的还是规范了一下 Bruce 的做题方法，也新了解了一种隐写方法
***
## Writeup

拿到图片第一件事：exiftool！（不要太依赖 Mac 自带的一些信息，exiftool 还是能 get 到额外的信息的！）

![](../../../../assets/Pasted%20image%2020241025204452.png)

有一个重要的 XP Comment：`NZXV64DBONZXO33SMQ======`，可以合理猜测这是一个 Base32 编码，CyberChef 转换可解码得 `no_password`

根据题目描述，“按下了 F5”，以及题目 ”ez_F5“ 可以得知 F5 是一个关键词，与图片相关搜索可得一种新型隐写：[F5 隐写](https://blog.csdn.net/m0_46296905/article/details/116942784)。

总的来说原理应该不太需要知道吧（bushi）主要是解密工具：[F5-steganography](https://github.com/matthewgao/F5-steganography)

同时，刚刚解出的 `no_password` 也得用上，其实就是解密时需要的密码，输入命令行  `java Extract "suantouwangba.jpg" -p no_password` 提取即可得到 flag : `moectf{F5_15_s0_lntere5t1n9}`