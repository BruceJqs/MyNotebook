# Misc-1-什么密码

下载附件得到一个无法解压的压缩包，提示密码错误，根据题目名称猜测为伪加密。用 010editor 打开压缩包，将 `frFlags` 字段修改为 2048 后可以正常解压压缩包，得到图片1.png。

zsteg 一把梭，文件结尾有 Base64 表`ZYXABCDEFGHIJKLMNOPQRSTUVWzyxabcdefghijklmnopqrstuvw0123456789+/`，rgb 最低为LSB 读到`OBCQN1ODbwx3KwihVQRwITNtWgBqKAChKf1eWgKeIQGjWAh2LQehJjKeKU0`，使用 cyberchef

![](../../../assets/Pasted%20image%2020251108164649.png)

flag 为 `DASCTF{7779da53-d0f1-41d6-af3a-2fd9698d2ca5}