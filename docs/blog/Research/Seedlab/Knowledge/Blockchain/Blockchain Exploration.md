# Blockchain Exploration

## Task 1: Setting Up MetaMask Wallet

安装好 MetaMask 插件后，启动 Emulator，用 `dockps | grep Geth` 随便找一个 Geth 节点，用 8545 端口作为 RPC，可以用 `curl -X POST http://10.150.0.71:8545 -H 'Content-Type: application/json' --data '{"jsonrpc":"2.0","method":"eth_chainId","params":[],"id":1}'` 查看 Chain ID：

![image-20260514150646298](../../../../../assets/image-20260514150646298.png)

设置网络，并连接，添加账户，可以看到我们有一个 10 ETH 的账户：

![image-20260519100633198](../../../../../assets/image-20260519100633198.png)

用 Metamask 转给一个账户 1ETH：

![image-20260519100730076](../../../../../assets/image-20260519100730076.png)

确认后发现转账成功：

![image-20260519100810437](../../../../../assets/image-20260519100810437.png)

在 Etherview 当中我们也可以看到交易细节：

![image-20260519100952604](../../../../../assets/image-20260519100952604.png)

****

## Task2: Interacting with Blockchain Using Python

直接用 `pip install web3 eth-account` 下载相关包，编写程序获取账号的 balance：

```python 
from web3 import Web3

RPC = 'http://10.150.0.71:8545'
w3 = Web3(Web3.HTTPProvider(RPC))

accounts = [
    "0xA2a28c011e281CA0dA0D878A82d854FD789C154c",
    "0x513C434dBA61AE5CFEf4552daC2D2f85450870aA",
    "0xBaED4A4Fffff4e047B8a39F00284732eF6244f4B"
]

print("connected: ", w3.is_connected())
print("chain id: ", w3.eth.chain_id)
print("latest block: ", w3.eth.block_number)

for a in accounts:
    addr = Web3.to_checksum_address(a)
    bal = w3.eth.get_balance(addr)
    print(addr, Web3.from_wei(bal, "ether"), "ETH")
```

运行可以得到：

![image-20260519102319563](../../../../../assets/image-20260519102319563.png)

查看其中一个账号的 private key：`Account Details > Private Keys`，编写代码来发送 TX：



运行得到：

![image-20260519103014339](../../../../../assets/image-20260519103014339.png)

并且在 etherview 当中也能看到：

![image-20260519103105158](../../../../../assets/image-20260519103105158.png)

****

## Task 3: Interacting with Blockchain Using Geth

进入一个 Geth 节点的终端，运行 `geth attach /root/.ethereum/geth.ipc` 进入交互界面：

![image-20260519103303471](../../../../../assets/image-20260519103303471.png)

可以通过交互获得信息：

![image-20260519103551469](../../../../../assets/image-20260519103551469.png)、

但是新版 Geth 似乎没有启用 Personal API，可能无法用 Geth 节点发 TX，也无法加入新节点：

![image-20260519103905573](../../../../../assets/image-20260519103905573.png)
