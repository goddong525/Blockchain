from ecdsa import SigningKey
import hashlib
import os

new_private_key = SigningKey.generate()
new_public_key = new_private_key.get_verifying_key()
new_wallet_address = hashlib.sha256(new_public_key.to_string()).hexdigest()

print(new_private_key.to_string())
print(new_private_key.to_pem())
print(new_private_key.to_string())
print(new_wallet_address)

if not os.path.exists('../wallets'):
    os.mkdir('../wallets')

f = open('../wallets/wallet.pem', 'wb')
f.write(new_private_key.to_pem())
f.close()

# 불러오기 ㅡ

f = open('../wallets/wallet.pem', 'rb')  # rb 모드로 열어주는거.
pem = f.read()
f.close()


SigningKey.from_pem(pem)
