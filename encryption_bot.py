data = "RSTUVWXYZ0123456789ABCDEFGHIJKLMNOPQabcdefghijklmnopqrstuvwxyz"
enc_data = "9W8TLp4k7t0vJW7n3VvMCpWq9WzT3C8pZ9Wz"

index = [data.index(char) for char in enc_data if char in data]
print(index)

binary_changer = ''.join(format(binary, '06b') for binary in index)
print(binary_changer)

binary_chunks = [binary_changer[i: i+8] for i in range(0, len(binary_changer), 8)]
print(binary_chunks)

print([chr(int(x, 2)) for x in binary_chunks])