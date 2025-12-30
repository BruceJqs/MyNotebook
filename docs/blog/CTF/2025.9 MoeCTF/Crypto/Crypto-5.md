# Crypto-5｜ezAES

## Tag

AES
***
## WriteUp

漏洞就在于各种加密 key 全部泄露了，直接逆回去即可：

```python
def key_expansion(grid):
    for i in range(10 * 4):
        r = grid[-4:]
        if i % 4 == 0:
            for j, v in enumerate(r[1:] + r[:1]):
                r[j] = s_box[v >> 4][v & 0xf] ^ (rc[i // 4] if j == 0 else 0)

        for j in range(4):
            grid.append(grid[-16] ^ r[j])

    return grid

def add_round_key(grid, round_key):
    for i in range(16):
        grid[i] ^= round_key[i]

def inv_sub_bytes(grid):
    for i, v in enumerate(grid):
        grid[i] = s_box_inv[v >> 4][v & 0xf]

def inv_shift_rows(grid):
    for i in range(4):
        grid[i::4] = grid[i::4][4-i:] + grid[i::4][:4-i]
        grid = grid[0::4] + grid[1::4] + grid[2::4] + grid[3::4]

def inv_mix_columns(grid):
    def mul_by_9(n):
        return mul_by_2(mul_by_2(mul_by_2(n))) ^ n
    
    def mul_by_11(n):
        return mul_by_2(mul_by_2(mul_by_2(n)) ^ n) ^ n
    
    def mul_by_13(n):
        return mul_by_2(mul_by_2(mul_by_2(n) ^ n)) ^ n
    
    def mul_by_14(n):
        return mul_by_2(mul_by_2(mul_by_2(n) ^ n) ^ n)
    
    def mul_by_2(n):
        s = (n << 1) & 0xff
        if n & 128:
            s ^= 0x1b
        return s

    def inv_mix_column(c):
        return [
            mul_by_14(c[0]) ^ mul_by_11(c[1]) ^ mul_by_13(c[2]) ^ mul_by_9(c[3]),
            mul_by_9(c[0]) ^ mul_by_14(c[1]) ^ mul_by_11(c[2]) ^ mul_by_13(c[3]),
            mul_by_13(c[0]) ^ mul_by_9(c[1]) ^ mul_by_14(c[2]) ^ mul_by_11(c[3]),
            mul_by_11(c[0]) ^ mul_by_13(c[1]) ^ mul_by_9(c[2]) ^ mul_by_14(c[3]),
        ]

    for i in range(0, 16, 4):
        grid[i:i + 4] = inv_mix_column(grid[i:i + 4])

def decrypt(b, expanded_key):
    add_round_key(b, expanded_key[-16:])
    inv_shift_rows(b)
    inv_sub_bytes(b)

    for i in range(9, 0, -1):
        add_round_key(b, expanded_key[i * 16:(i + 1) * 16])
        inv_mix_columns(b)
        inv_shift_rows(b)
        inv_sub_bytes(b)

    add_round_key(b, expanded_key[:16])
    
    return b

def aes_decrypt(key, ciphertext):
    expanded = key_expansion(bytearray(key))
    
    b = bytearray(ciphertext)
    for i in range(0, len(b), 16):
        b[i:i + 16] = decrypt(b[i:i + 16], expanded)
    
    return bytes(b)

if __name__ == '__main__':
    key = b'Slightly different from the AES.'

    enc = b'%\x98\x10\x8b\x93O\xc7\xf02F\xae\xedA\x96\x1b\xf9\x9d\x96\xcb\x8bT\r\xd31P\xe6\x1a\xa1j\x0c\xe6\xc8'
    
    plaintext = aes_decrypt(key, enc)
    plaintext = plaintext.rstrip(b'\x00')
    
    print(f"[+] Flag：{plaintext.decode()}")
```

得到最终 flag：`moectf{Th1s_1s_4n_E4ZY_AE5_!@#}`