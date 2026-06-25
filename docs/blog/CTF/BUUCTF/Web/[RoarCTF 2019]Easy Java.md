# [RoarCTF 2019]Easy Java

## Tag

Java 任意文件下载

***

## Writeup

访问 help 发现：

![image-20260131162040276](../../../../assets/image-20260131162040276.png)

说明到达了 Download 路由但是没下载下来，用 POST 请求再发一遍即可：

![image-20260131162142424](../../../../assets/image-20260131162142424.png)

得到：

![image-20260131162255089](../../../../assets/image-20260131162255089.png)

说明可以下载任意文件，`WEB-INF` 是 Java Web 应用的安全目录，它包含了应用的配置文件、类文件（.class）和库文件（.jar），而 WEB-INF/web.xml 是 Java Web 的部署描述文件，里面记录了所有的 **Servlet 映射路径** 和 **类名**，下载下来：

![image-20260131162316428](../../../../assets/image-20260131162316428.png)

里面有一个 FlagController，对应的路径为 `/WEB-INF/classes/com/wm/ctf/FlagController.class`，下载并反编译得到：

![image-20260131171026442](../../../../assets/image-20260131171026442.png)

cyberchef 一解即可：

![image-20260131171241057](../../../../assets/image-20260131171241057.png)

