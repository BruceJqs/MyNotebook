---
title: 为网站添加评论系统
comments: true
tags:
  - Mkdocs
---
官方文档：[Adding a comment system](https://squidfunk.github.io/mkdocs-material/setup/adding-a-comment-system/)  

这里我同样推荐[giscus](https://giscus.app/zh-CN)


利用 GitHub Discussions 实现的评论系统，让访客借助 GitHub 在你的网站上留下评论和反应吧！本项目深受 utterances 的启发。

* 开源。🌏
* 无跟踪，无广告，永久免费。📡 🚫
* 无需数据库。所有数据均储存在 GitHub Discussions 中。:octocat:
* 支持自定义主题！🌗
* 支持多种语言。🌐
* 高可配置性。🔧
* 自动从 GitHub 拉取新评论与编辑。🔃
* 可自建服务！🤳

言归正传

## 第一步
mkdocs.yml中添加
```
theme:
  name: material
  custom_dir: docs/overrides  #主要是这一行
```
参考下图新建overrides文件，在此文件下参考下图新建覆盖html文件  
树状结构如下:  
```
$ tree -a
.
├── .github
│   ├── .DS_Store
│   └── workflows
│       └── PublishMySite.yml
├── docs
│   └── index.md
│   └──overrides
│       └──assets
│       └──main.html
│       └──partials
│          └──comments.html
│
└── mkdocs.yml
``` 

![img](https://s1.imagehub.cc/images/2024/02/02/214447b92070792905259a843de3e233.png)

在comments.html中

评论功能已暂时关闭，`comments.html` 中不再加载第三方评论脚本。
## 第二步
打开<https://giscus.app/zh-CN>  走完这个页面的流程就会得到(这会在你的Github创建新的仓库，建议自己先去新建个 Discussions)
![](https://s1.imagehub.cc/images/2024/02/02/b0fabd6a0c967d5a846c087adea5b680.png)  

![](https://s1.imagehub.cc/images/2024/02/02/d0c7b4e08a714b5c2b60421f58159c62.png)  

评论系统重新启用前，不要复制外部评论脚本到模板里。

终端里`mkdocs server`一下

## 最后
在你想插入评论的地方的元数据：`comments: true `

```
---
title: 留言板
hide:
  #  - navigation # 显示右
  #  - toc #显示左
  #  - footer
  #  - feedback  
comments: true  #默认不开启评论
---
```
## 效果  

完美!快速相应  

<figure markdown >
  ![](https://s1.imagehub.cc/images/2024/02/02/0619f922f930e7649fb40405c7e49339.png)
  <figcaption>这是图片↑↑↑</figcaption>
</figure>

## 其他评论系统

先不启用其他评论系统，避免评论数据进入第三方或别人的后端。
