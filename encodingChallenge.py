from pwn import *
import json
import base64
import codecs
from Crypto.Util.number import long_to_bytes

r = remote('socket.cryptohack.org', 13377, level='debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)


while True:
    received = json_recv()

    if 'flag' in received:
        print('Flag:', received['flag'])
        break

    typ = received.get('type')
    enc = received.get('encoded')

    print('Received type:', typ)
    print('Received encoded value:', enc)

    if typ == 'base64':
        decoded = base64.b64decode(enc).decode()
    elif typ == 'hex':
        decoded = bytes.fromhex(enc).decode()
    elif typ == 'rot13':
        decoded = codecs.decode(enc, 'rot_13')
    elif typ == 'bigint':
        decoded = long_to_bytes(int(enc, 16)).decode()
    elif typ == 'utf-8':
        decoded = ''.join(chr(i) for i in enc)
    else:
        decoded = ''
        

    print('Decoded ->', decoded)

    json_send({'decoded': decoded})