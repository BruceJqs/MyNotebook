# Crypto-2-ez_stream

简单流加密，前期所有数据已知，最后一步利用异或可逆即可，Payload 如下：

```python
t = [164, 34, 242, 5, 234, 79, 16, 182, 136, 117, 78, 78, 71, 168, 72, 79, 53, 114, 117]
ans = [164, 34, 242, 5, 234, 79, 16, 182, 136, 117, 78, 78, 71, 168, 72, 79, 53, 114, 117]
N,K,S=[256,[0]*256],[0]*256,[i for i in range(256)]
key='love'
for i in range(256):S[i],K[i]=i,ord(key[i%len(key)])
j=0
for i in range(256):j=(j+S[i]+K[i])%256;S[i],S[j]=S[j],S[i]
i,j=0,0
for k in range(len(t)):i=(i+1)%256;j=(j+S[i])%256;S[i],S[j]=S[j],S[i];t[k]^=S[(S[i]+S[j])%256]
for k in range(len(t)):
    print(chr(t[k]), end='')
```