# Git Leak

## Tag

dirsearch 工具，Git Leak，GitHack 工具，md5
***
## Writeup

使用 dirsearch 工具搜索目录，得到：

![](../../../../assets/PixPin_2025-11-11_00-17-33.png)

可以看到里面有 .git 目录泄露，使用 GitHack 工具尝试还原：

![](../../../../assets/PixPin_2025-11-11_00-18-27.png)

查看内容即可得到：

![](../../../../assets/PixPin_2025-11-11_00-18-44.png)

需要我们输入一个值，使得其 md5 值对应上，然后才能获得完整的 flag，通过 [md5 查询网站](cmd5.com) 可解得最终 flag：

![](../../../../assets/PixPin_2025-11-11_00-38-39.png)