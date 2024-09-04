# Iterm2

!!!Abstract
    iTerm2 是一款针对 macOS 的终端替代品，为用户提供了一种先进和现代的访问命令行的方式。它具有诸如快速打开、实时图形和改进的连接一致性等功能。

## 安装

- [官网](https://iterm2.com/#:~:text=iTerm2%20is%20a%20replacement%20for%20Terminal%20and)下载 Iterm2，安装。
- 查看 zsh 路径：`which zsh`
- 更改默认 Shell：`sudo chsh -s {zsh 路径}`

## 主题

- 安装 oh-my-zsh：`sh -c "$(wget https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)"`
- 安装 powerlevel10k(p10k)：``git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k``
- 命令行 `vim ~/.zshrc ` 打开，设置 `ZSH_THEME="powerlevel10k/powerlevel10k"`

## 插件

- 命令行辅助输入：``git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions``

- 高亮显示：`git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting`

- 命令行 `vim ~/.zshrc ` 打开，设置 `plugins=(git zsh-autosuggestions zsh-syntax-highlighting)`