# Web-1-1｜第一章 神秘的手镯_revenge

## 碎碎念

revenge 比原版难多了...
***
## Writeup

这一题设置了 debugger 设置断点来阻止自动化脚本，可以关闭（右上角）：

![](../../../../assets/Pasted%20image%2020251030194255.png)

首先题目提示有备份代码，可以访问 wanyanzhou.txt.bak 获得最新内容，并编写 js 脚本：

```javascript
(function() {
    var input = document.getElementById("passwordInput");
    var button = document.getElementById("unsealButton");
    var text = "text";

    var count = 500;
    var i = 0;

    var interval = setInterval(function() {
        if (i >= count) {
            clearInterval(interval);
            return;
        }
        input.value = text;
        button.click();
        i++;
    }, 10);
})();
```

直接复制进 console 等待即可获得 flag：

![](../../../../assets/Pasted%20image%2020251030194439.png)

最终 flag：`moectf{db268e0c-1684-5565-6f2f-c6aca3a44798}`