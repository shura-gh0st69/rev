from base64 import b64decode

with open("fixed_payload.txt", "rb") as r:
    r = r.read()

bdecode = b64decode(r)

decoded_bytes = bytes([b ^ 119 for b in bdecode])

with open("nft.exe", "wb") as out:
    out.write(decoded_bytes)

print(decoded_bytes)
