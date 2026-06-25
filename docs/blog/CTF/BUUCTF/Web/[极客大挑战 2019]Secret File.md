# [极客大挑战 2019]Secret File

## Tag

文件绕过

***

## Writeup

查看源代码能看到有隐藏 `Archive_room.php`：

![image-20260120153723229](../../../../assets/image-20260120153723229.png)

看到还有一个 action.php：

![image-20260120153813085](../../../../assets/image-20260120153813085.png)

点击一闪而过，Burp 抓包：

![image-20260120154002605](../../../../assets/image-20260120154002605.png)

有一个 secr3t.php：

![image-20260120154117499](../../../../assets/image-20260120154117499.png)

访问 flag.php 发现没有东西，Base64 加密：

![image-20260120154529812](../../../../assets/image-20260120154529812.png)