---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
---  

# Misc-7｜Signin

## 复盘心得

这么简单一题……

哎终究还是 Bruce 懒 WebSocket Reflector X 在 Mac 上安装出错也不好好去找解决方法（悲）

解决方法如下：

下载 WebSocketReflectorX-0.2.23-macOS-arm64.dmg，把软件拖到 Applications 里面之后点开会发现软件包出错，命令行输入 `sudo xattr -rd com.apple.quarantine /Applications/WebSocketReflectorX.app` 即可解决。
***
## Writeup

WSRX 直接连接进入，将所有人除了 `luo` 都设置为出勤即可获得 flag : `moectf{Thanks_For_You_signing_in_4ND_W3l0c0me_T0_M0ecTf_2024!!!}`

![](../../../../assets/Pasted%20image%2020241025192446.png)