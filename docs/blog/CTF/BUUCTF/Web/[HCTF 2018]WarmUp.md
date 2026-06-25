
# [HCTF 2018]WarmUp

## Tag

文件包含绕过

***

## Writeup

访问源代码可以看到有 source.php：

![image-20260120104216847](../../../../assets/image-20260120104216847.png)

访问可以得到 source.php 源代码：

![image-20260120104301870](../../../../assets/image-20260120104301870.png)

访问 hint.php 可以得到：

![image-20260120112714412](../../../../assets/image-20260120112714412.png)

因此只要通过 `checkFile` 检查即可，Payload：`/?file=source.php?/../../../../ffffllllaaaagggg`，`checkFile` 检测到 ? 后截取前半部分为白名单中的 source.php，因此返回 True，而 include 解析会将 `source.php?` 作为一个文件名，层级跳到根目录从而得到 flag：

![image-20260120112641361](../../../../assets/image-20260120112641361.png)