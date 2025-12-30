# Pwn-1-rop

程序维护了一个数组，主要分为 input, output 操作，数组最高的 index 为 meta，即整个数组的 count。 input 函数（401339）根据 meta 的 count 决定数据存放的位置

output 函数（4013DF） 读入的变量为 int，因此输入负数可以绕过检测，可以用来泄露 libc 基址。gdb 看一下，index 为 -13 有一个 libc 地址，读一下做差即可算出 libc 基址。

![](../../../assets/Pasted%20image%2020251108165035.png)

而且程序没有对 meta 数据 count 的保护，只要 output 的比 input 多，就可以减到负数，然后此时如果调用 input，就可以反向溢出到 input 函数的 return address。

然后就可以直接 one_gadget getshell。