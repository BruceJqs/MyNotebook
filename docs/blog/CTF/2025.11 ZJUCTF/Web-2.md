---
typora-copy-images-to: ../../../assets
---

# 你说你不懂 Linux

## Tag

路径欺骗，结尾绕过

## Writeup

题目要求路径中有 `.log` 检查，以及 `flag` 和 `.txt` 检查，同时还有一个 `substr_compare` 检查结尾是否为 `flag.txt` ，因此有三步，Payload：`/?file=../../systeminfo.log/../FLAG.TXT.`

- 在路径中包含 `systeminfo.log`，但是用 `../` 跳过
- 将文件名全大写为 `FLAG.TXT`
- 最后添加一个 `.` 绕过 `substr_compare` 检查

![PixPin_2025-11-23_09-15-31](../../../assets/PixPin_2025-11-23_09-15-31.png)

最终 flag：`ZJUCTF{don't_say_you_are_unfamiliar_with_paths_again!_2575dc961faa}`