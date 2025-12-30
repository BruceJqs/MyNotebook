# DS-1-dsEnData

照着 encode.py 写一个 decode.py 就可以了，读读写写格式处理一下，提交即可。

```python
import base64

def decode(D, K='a1a60171273e74a6'):
    D = D.hex()
    res = b''
    for i in range(len(D)//2):
        data = D[i*2:i*2+2]
        c = K[i+1&15]
        res += bytes.fromhex(hex(int(data,16)^ord(c))[2:].zfill(2))
    return res

with open("encoded_data.csv", "r") as f:
    output = open("decoded_data.csv", "w", encoding="utf-8")
    output.write("username,name,phone,email,address\n")
    data_all = f.read().replace("\n", ",")
    data_all = data_all.split(",")
    for i in range(5,len(data_all)):
        data = data_all[i]
        decode_data = (decode(base64.b64decode(data))).decode()
        output.write(f"{decode_data}")
        if(i%5==4):
            output.write("\n")
        else:
            output.write(",")
```

提交得到 `DASCTF{73232900174455106405161084559005}`