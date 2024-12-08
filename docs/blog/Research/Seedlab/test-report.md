# Test Report

## Compile-and-Build-Test

> 顾名思义，编译所有 Examples 的 Python 代码、生成 output 目录并 Build 建立网络，检查是否能正常编译生成，是否能正常建立网络

运行 `compile-and-build-test.py`，明显看见分为 `compile` 和 `build` 两部分，两个部分只要遇到错误就会终止

- `test_log/log.txt` 保存本次测试的 Examples 条目
	- 如果不完全（即与 `compile-and-build-test.py` 设置的不对应）说明最后一行出现编译错误
- `test_log/build_log.txt` 保存所有 Examples `docker-compose build` 的输出信息
	- 可以具体搜索 Build 发生的错误
	
	![](../../../assets/Pasted%20image%2020241205230652.png)
	![](../../../assets/Pasted%20image%2020241205230802.png)

运行成功该有的样子：

![](../../../assets/Screenshot%202024-12-05%20at%2023.25.48.png)

![](../../../assets/Pasted%20image%2020241205232749.png)

## Dynamic-Test

> 对于生成构建好的网络进行功能测试

<font color="red">需要非常注意 Python 版本！</font>

- 版本太高（Python3.12）：
	
	![](../../../assets/Pasted%20image%2020241205233046.png)
	
	- 原因是 `inspect` 里面已经没有 `getargspec` 了，新版本 Python 换成 `signature` 即可（直接到底层代码 `/root/miniconda3/lib/python3.12/site-packages/parsimonious/expressions.py` 修改）

- 版本太低（低于 Python3.8 包都装不了）：
	
	![](../../../assets/Pasted%20image%2020241205234556.png)

运行 `run-test.py`，它会根据文档针对 example 做的 testcase 进行测试

例如，mini_internet 当中针对建立的网络进行了连通性测试、自定义 IP 地址测试、现实 IP 地址测试

- 每个 testcase 目录下自动生成 test_log，内含 build_log、compile_log、container_log 和 results.txt，`cat test_result.txt | grep score` 可以得到每个测试的结果得分 

## 一些想法

- 整体无论是 requirements.txt 还是其他版本都有点过时了，test 的 requirements.txt 写的 docker 是 4.1.0 但是现最新版本已经是 7.1.0 了，这也导致会报错
- 很多出错都是 Github 连接问题（尤其区块链那片），需要换源
