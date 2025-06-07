from pwn import *
from base64 import b64decode 

def get_from_base64_string(b64str):
    with open("elf", "wb") as f:
        f.write(b64decode(b64str))

    e = ELF("elf", checksec=False)
    epoint = e.entrypoint
    lea_addr = epoint + 4 
    buf_offset = u32(e.read(lea_addr + 3, 4), sign='signed')

    epoint = e.entrypoint
    lea_addr = epoint + 4
    buf_offset = u32(e.read(lea_addr + 3, 4), sign='signed')

    buf_addr = epoint + 4 + 7 + buf_offset
    values = e.read(buf_addr, 24)

    return values.hex()

r = remote(*(sys.argv[1].split(":")))

with log.progress("Solving...") as p:
    for i in range(129):
        r.recvuntil("ELF: ")
        b64str = r.recvline()
        base64str = get_from_base64_string(b64str)


        r.sendline(base64str.encode())
        p.status(f"solving {i + 1}")


print(r.recvall().decode().strip())