---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
---  

# Misc-4 so many 'm'

## 做题心得 & 感想

这道题被题目迷惑的……让 Bruce 冲着 m 分割了半天也没搞出个所以然……

还是在群 u 提醒之下三两下直接就出了（做完马后炮才发现原来题目是说 m 字频最高所以 flag 第一个字符即为 m）

还是得多熟悉熟悉各类编码啊……
***
## Writeup

根据提示：

![](../../../../assets/Pasted%20image%2020240925132449.png)

判断顺序？要根据什么判断顺序？（且不是字典序）

~~合理推测~~（拉倒吧 Bruce 就这个想了半天，不过马后炮根据题目 many 也可以看出）是通过字母出现频率进行排序，相同即按照字典序排序，最后即可得到 flag

编一个 python 程序如下：

``` python

text = "a!{ivlotzkEm{CtsvEpbDkwexsotyMuECs!mvlhmenrhwpMh0leydsMbC#CC}sii}tkb}ugCD{zlEeT#kyC0fbukglpopmaekbEthmjcMdsgkvmTnC}eot#dcf{ec@ccgqpfqMycysMuuou!en#{g0cDmoyxTCMgt{joT{jnl0rhoklCe{n0CnxprydeaTg0r{avkEjckjEsxhaohs{Trbkr!ffqip444uwrc}nnevgtCT{jCipogtipzdeDiqsy44rMfj{MzCw#qwg{T4m{cuk!hwuncxdmddeurtsojakrjC#vTDd}0poTT@c!DftjwuDp@mcuheeDtfao!iEcEq}kcf#Mpcam{mml4i4mpDnedamcwtC0nem{mDotnmp4jf@TpxfqMoiqwtdijDfimmCzmxe#gsTu{poeTEhD!u0anvTTTbbi{q}zapcksMifDlovoeac@{0keh0dg{Mi!@tfftqitmuMoMcuTpmcgnmozyrrv#zfmzmetyxxa0wczE}eoD{xcMnoCuebu0otdusiDknfvo0{fEsMftzT!eoslegbypspC4vkxm#uaf@acuemhMyiDou#at0rfl4a}0ixeEktws}pMCfCigaTafg}ffssmwwuTkTuls0{M@c4e@{D{tuorzmyqptChpngkeCohCCMTwqctinc0mcjemclv@cMoqf00poarte@oqmuysm#mo{et4kcCpcgcT}vD}m!g4{E0!Mol0fpo!{srT0pf{cMuCx0bp{ftTmExcrn}0etonez!@C4tfa4aM00siztb@fomfD#{#tMbo@jgb4CM0dEk0tea4aMCafn"

count = []
for i in range(256):
    count.append([i, 0])

for ch in text:
    count[ord(ch)][1] += 1

count.sort(key=lambda x: x[1], reverse=True)
for i in range(256):
    if count[i][1] > 0:
        print(chr(count[i][0]), end = "")

```

运行即可得到 flag：`moectf{C0MpuTaskingD4rE}` （后面的字符就直接不要了）