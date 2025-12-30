# Rev-1-DontDebugMe

反编译为

```cpp
int __cdecl main(int argc, const char **argv, const char **envp)
{
  int i; // [esp+E8h] [ebp-12Ch]
  unsigned int v5; // [esp+100h] [ebp-114h]
  _WORD Buf2[130]; // [esp+10Ch] [ebp-108h] BYREF

  __CheckForDebuggerJustMyCode(byte_452015);
  memset(Buf2, 0, 0x100u);
  sub_401550("Please input the flag and I will verify it: ");
  sub_4015C0("%256s", (const char *)Buf2);
  if ( IsDebuggerPresent() )
    _loaddll(0);
  v5 = sub_401000();
  for ( i = 0; i < 20; ++i )
  {
    Buf2[i] += HIWORD(v5);
    Buf2[i] ^= v5;
  }
  if ( !memcmp(&Buf1_, Buf2, 0x28u) )
    sub_401550("Right flag!\n");
  else
    sub_401550("Wrong flag\n");
  return 0;
```

patch 掉反调试后直接动态调试到 `sub_401000()` 的结果为 0x685EE20，从内存中复制出 `Buf1_` 的值后直接反向运算回 Buf2。

```python
IDA_450000 = [0xa9e9, 0xa7f8, 0xa2f9, 0xd620, 0xd69a, 0xd9c8, 0xd399, 0x85cb, 0xd29b, 0xd5c7, 0x8496, 0xd4c9, 0xd89a, 0xd7ca, 0xd59c, 0x85c8, 0xd597, 0x859e, 0xd49c, 0x6dca]
for i in range(len(IDA_450000)):
    IDA_450000[i] ^= 109440544
    IDA_450000[i] -= (109440544 >> 16 ) & 0xFFFF
for i in range(len(IDA_450000)):
    print(chr(IDA_450000[i] & 0xFF)+chr(IDA_450000[i]>>8 & 0xFF), end='')
```

![](../../../assets/Pasted%20image%2020251108164529.png)

运行得到 flag 为 `DASCTF{152c147fe66b51dd450e375ce259e74e}`