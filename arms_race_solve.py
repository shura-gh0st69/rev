# fixed with gitlens

from unicorn import *
from unicorn.arm_const import *
from pwn import *
import sys

EMU_ADDRESS = 0x10000

def r0_calculator(bytecode):
    try:
        emu = Uc(UC_ARCH_ARM, UC_MODE_ARM)

        emu.mem_map(EMU_ADDRESS, 2 * 1024 * 1024)
        emu.mem_write(EMU_ADDRESS, bytes(bytecode))
        emu.emu_start(EMU_ADDRESS, EMU_ADDRESS + len(bytecode))

        return emu.reg_read(UC_ARM_REG_R0)

    except UcError as e:
        print(f'ERROR: {e}')

r = remote(*(sys.argv[1].split(":")))

with log.progress ("") as p:
    for i in range(50):
        r.recvuntil(b":")

        arm_bytes_hex = r.recvline().strip()
        arm_bytes = bytes.fromhex(arm_bytes_hex.decode())

        r0 = r0_calculator(arm_bytes)

        print(f"[+] {r0}")

        r.recvuntil(b":")
        r.sendline(str(r0).encode())

        p.status(f"trying to solve {i + 1}")

r.interactive()
