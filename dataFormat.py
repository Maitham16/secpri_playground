"""
from Crypto.PublicKey import RSA

# read .pem file
with open('privacy_enhanced_mail.pem', 'r') as f:
    pem = f.read()

# Import the key
key = RSA.importKey(pem)

# Extract d as decimal integer
d = key.d
print(d)
"""
# --------------------------------------------------------
"""
from cryptography import x509
from cryptography.hazmat.backends import default_backend

# read der
with open('2048b-rsa-example-cert.der', 'rb') as f:
    der_data = f.read()

# Load the certificate
cert = x509.load_der_x509_certificate(der_data, default_backend())

# Get the public key
public_key = cert.public_key()

# Extract modulus (n)
n = public_key.public_numbers().n

# Print modulus as decimal
print(n)
"""
# --------------------------------------------------------
"""
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

# Bruce's SSH public key
with open('bruce_rsa.pub', 'rb') as f:
    ssh_key_bytes = f.read()

# Load OpenSSH public key and extract modulus
pub = serialization.load_ssh_public_key(ssh_key_bytes, backend=default_backend())
n = pub.public_numbers().n
print(n)
"""
# --------------------------------------------------------
"""
from Crypto.PublicKey import RSA

# Read Bruce's SSH public key (OpenSSH format)
with open('bruce_rsa.pub', 'r') as f:
    ssh_key = f.read()

# Import the OpenSSH public key directly
key = RSA.import_key(ssh_key)

# Print modulus as decimal
print(key.n)
"""
# --------------------------------------------------------
import hashlib
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

with open('transparency.pem','rb') as f:
	pem = f.read()

key = serialization.load_pem_public_key(pem, backend=default_backend())
spki = key.public_bytes(
	encoding=serialization.Encoding.DER,
	format=serialization.PublicFormat.SubjectPublicKeyInfo,
)
h = hashlib.sha256(spki).hexdigest()

print(f'https://crt.sh/?spkisha256={h}')
