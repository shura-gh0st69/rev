import socket
import struct

def build_checksum(one, two, payload_id):
    return ((one ^ two) << 16) | (payload_id & 0xFFFF)

HOST = '127.0.0.1'
PORT = 4444

# These can be arbitrary, but must be internally consistent
one = 0xAAAA
two = 0x0100        # triggers sub_1421
payload_id = 0x41424344  # just a test value

checksum = build_checksum(one, two, payload_id)

# Header (12 bytes): one, two, checksum, payload_id
header = struct.pack(">HHII", one, two, checksum, payload_id)

# Metadata (8 bytes): payload_id again, and size (can be 0 since this command doesn't read data)
metadata = struct.pack(">II", payload_id, 0)

with socket.create_connection((HOST, PORT)) as s:
    s.sendall(header)
    s.sendall(metadata)
    print("[+] Sent header and metadata")

    response = s.recv(4096)
    print("[+] Received:")
    print(response.decode(errors="ignore"))
