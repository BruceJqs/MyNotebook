# Web-26｜这是...Webshell？

## 碎碎念

无字母数字 RCE，教程参见 [无字母数字 RCE 的总结](https://www.qwesec.com/2024/03/noLettersOrNumbersRCE.html)
***
## Writeup

运用里面的异或方法，拿某两个非字母/数字的字符，异或结果是想要的字母即可：

![](../../../../assets/Pasted%20image%2020251030223025.png)

上图的含义最后转化为 `assert($_POST[_]);`

P.S. hackbar 是真的好用，做好直接 execute 即可得到 phpinfo：

![](../../../../assets/Pasted%20image%2020251030223148.png)

得到最终 flag：`moectf{202bc852-e9a0-940b-3827-06431a919b26}`