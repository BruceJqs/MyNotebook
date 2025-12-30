# Lab Report

## Tag

PDF xref 表隐写

## Writeup

观察 PDF 结尾 xref 表不正常，增量只有 10/20，所以合理猜测对应 01 串，Payload 如下：

```python
xref_data = """
...
"""

def decode_xref(xref_text):
    lines = xref_text.strip().split('\n')
    offsets = []
    for line in lines:
        parts = line.split(' ')
        if len(parts) >= 1:
            offsets.append(int(parts[0]))
    
    binary_str = ""
    for i in range(len(offsets) - 1):
        diff = offsets[i+1] - offsets[i]
        
        if diff == 20:
            binary_str += "1" 
        elif diff == 10:
            binary_str += "0"
        else:
            print(f"Warning: Unexpected diff {diff} at index {i}")

    print(f"Binary: {binary_str}")
    
    flag = ""
    for i in range(0, len(binary_str), 8):
        byte = binary_str[i:i+8]
        if len(byte) == 8:
            flag += chr(int(byte, 2))
    print(f"Flag Result: {flag}")

decode_xref(xref_data)
```

得到 flag：`ZJUCTF{PDF_0ff5e7_c4N_H1D3_m3ss4g3}`
