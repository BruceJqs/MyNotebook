# Misc-2-RecoverWallet

少了一个助记词，有钱包地址后缀，题目描述里提示了了解 `BIP-39`，可以尝试遍历 2048 个助记词进行爆破，写个 Python 脚本：

```python
import time
from mnemonic import Mnemonic
from eth_account import Account
from eth_utils import to_checksum_address

Account.enable_unaudited_hdwallet_features()
known_parts = ["ankle", "assume", "estate", "permit", None, "eye", "fancy", "spring", "demand", "dial", "awkward", "hole"]
target_suffix = "700f80"
mnemo = Mnemonic("english")
wordlist = mnemo.wordlist
derivation_path = "m/44'/60'/0'/0/0"

for word in wordlist:
    current_mnemonic_list = known_parts.copy()
    current_mnemonic_list[4] = word
    current_mnemonic = " ".join(current_mnemonic_list)
    
    if not mnemo.check(current_mnemonic):
        continue

    account = Account.from_mnemonic(current_mnemonic, account_path=derivation_path)
    address = to_checksum_address(account.address)
    
    if address.endswith(target_suffix):
        print("完整助记词:")
        print(current_mnemonic)
        print("钱包地址:")
        print(address)
        break
```

