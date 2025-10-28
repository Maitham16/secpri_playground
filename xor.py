# first convert integers from decimal to binary
# convert each character to integer
# XOR each character with integer 13
# convert back to string
from pwn import *
import json

"""
from pwntools_example import json_send

r = remote('socket.cryptohack.org', 13377, level='debug')

label = "label"
num = 13

n = len(label)
decoded_chars = []
for i in range(n):
    char = label[i]
    char_int = ord(char)  # convert character to integer
    xored_int = char_int ^ num  # XOR with num
    decoded_char = chr(xored_int)  # convert back to character
    decoded_chars.append(decoded_char)
decoded = ''.join(decoded_chars)

r.sendline(json.dumps({'decoded': decoded}))
json_send({'decoded': decoded})

print(f"crypto{{{decoded}}}")"""

#--------------------------------------------------------

# Decode hex to bytes
"""KEY1 = bytes.fromhex('a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313')
KEY2_XOR_KEY1 = bytes.fromhex('37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e')
KEY2_XOR_KEY3 = bytes.fromhex('c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1')
FLAG_XOR_KEY1_XOR_KEY3_XOR_KEY2 = bytes.fromhex('04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf')

# Step 1: Get KEY2
# KEY2 ^ KEY1 = given, so KEY2 = (KEY2 ^ KEY1) ^ KEY1 (since A ^ A = 0, A ^ 0 = A)
KEY2 = bytes(a ^ b for a, b in zip(KEY2_XOR_KEY1, KEY1))

# Step 2: Get KEY3
# KEY2 ^ KEY3 = given, so KEY3 = (KEY2 ^ KEY3) ^ KEY2
KEY3 = bytes(a ^ b for a, b in zip(KEY2_XOR_KEY3, KEY2))

# Step 3: Get FLAG
# FLAG ^ KEY1 ^ KEY3 ^ KEY2 = given
# FLAG = (FLAG ^ KEY1 ^ KEY3 ^ KEY2) ^ KEY1 ^ KEY2 ^ KEY3
FLAG = bytes(a ^ b ^ c ^ d for a, b, c, d in zip(FLAG_XOR_KEY1_XOR_KEY3_XOR_KEY2, KEY1, KEY2, KEY3))

# Convert FLAG to string and format
flag_str = FLAG.decode()
print(flag_str)"""

# --------------------------------------------------------
# Decode hex to bytes
"""data = bytes.fromhex('73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d')

# Try all possible single-byte keys (0-255)
for key in range(256):
    # XOR each byte with the key
    result = bytes(b ^ key for b in data)
    # Check if result is printable ASCII
    flag = result.decode()
    if flag.isprintable() and flag.startswith('crypto'):
        print(flag)
        break
"""
# --------------------------------------------------------
"""# Repeating-key XOR solver
hex_string = '0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104'
data_bytes = bytes.fromhex(hex_string)

known_prefix = "crypto{"
closing = "}"
n = len(data_bytes)

for key_length in range(2, 21):
    key_chars = [None] * key_length
    valid_key = True

    # Apply prefix constraints
    for i in range(len(known_prefix)):
        pos = i % key_length
        val = data_bytes[i] ^ ord(known_prefix[i])
        if key_chars[pos] is None:
            key_chars[pos] = val
        elif key_chars[pos] != val:
            valid_key = False
            break

    # Apply closing brace constraint
    if valid_key:
        pos_last = (n - 1) % key_length
        val_last = data_bytes[n - 1] ^ ord(closing)
        if key_chars[pos_last] is None:
            key_chars[pos_last] = val_last
        elif key_chars[pos_last] != val_last:
            valid_key = False

    if valid_key:
        unknown_pos = []
        for p in range(key_length):
            if key_chars[p] is None:
                unknown_pos.append(p)
        
        if len(unknown_pos) == 0:
            full_key = []
            for i in range(n):
                full_key.append(key_chars[i % key_length])
            decoded_chars = []
            for i in range(n):
                decoded_chars.append(chr(data_bytes[i] ^ full_key[i]))
            decoded = ''.join(decoded_chars)
            print(decoded)
            break
        elif len(unknown_pos) == 1:
            pos = unknown_pos[0]
            for k in range(256):
                key_chars[pos] = k
                full_key = []
                for i in range(n):
                    full_key.append(key_chars[i % key_length])
                decoded_chars = []
                for i in range(n):
                    decoded_chars.append(chr(data_bytes[i] ^ full_key[i]))
                decoded = ''.join(decoded_chars)
                all_printable = all(32 <= ord(c) < 127 for c in decoded)
                if decoded.startswith('crypto{') and decoded.endswith('}') and all_printable:
                    print(decoded)
            break
        elif len(unknown_pos) == 2:
            pos0 = unknown_pos[0]
            pos1 = unknown_pos[1]
            for k0 in range(256):
                key_chars[pos0] = k0
                for k1 in range(256):
                    key_chars[pos1] = k1
                    full_key = []
                    for i in range(n):
                        full_key.append(key_chars[i % key_length])
                    decoded_chars = []
                    for i in range(n):
                        decoded_chars.append(chr(data_bytes[i] ^ full_key[i]))
                    decoded = ''.join(decoded_chars)
                    all_printable = all(32 <= ord(c) < 127 for c in decoded)
                    if decoded.startswith('crypto{') and decoded.endswith('}') and all_printable:
                        print(decoded)
            break
        else:
            for p in range(key_length):
                if key_chars[p] is None:
                    col_bytes = [data_bytes[j] for j in range(p, n, key_length)]
                    best_key_byte = 0
                    best_score = -1
                    for k in range(256):
                        score = sum(1 for b in col_bytes if 32 <= (b ^ k) < 127)
                        if score > best_score:
                            best_score = score
                            best_key_byte = k
                    key_chars[p] = best_key_byte
            
            full_key = []
            for i in range(n):
                full_key.append(key_chars[i % key_length])
            decoded_chars = []
            for i in range(n):
                decoded_chars.append(chr(data_bytes[i] ^ full_key[i]))
            decoded = ''.join(decoded_chars)
            all_printable = all(32 <= ord(c) < 127 for c in decoded)
            if decoded.startswith('crypto{') and decoded.endswith('}') and all_printable:
                print(decoded)
                break
"""
# --------------------------------------------------------
from PIL import Image

# Load the two images
img1 = Image.open('lemur.png').convert('RGB')
img2 = Image.open('flag.png').convert('RGB')

# Get dimensions
width, height = img1.size

# Create a new image for the result
result = Image.new('RGB', (width, height))

# XOR RGB values of corresponding pixels
for x in range(width):
    for y in range(height):
        r1, g1, b1 = img1.getpixel((x, y))
        r2, g2, b2 = img2.getpixel((x, y))
        # XOR each RGB component
        r = r1 ^ r2
        g = g1 ^ g2
        b = b1 ^ b2
        result.putpixel((x, y), (r, g, b))

# display the result
result.show()
