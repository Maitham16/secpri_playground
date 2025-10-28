"""def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

print(gcd(12, 8))
print(gcd(66528, 52920))"""
# ------------------------------
"""def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

# Given primes
p = 26513
q = 32321

# Calculate GCD and coefficients u, v
gcd, u, v = extended_gcd(p, q)

# Since p and q are prime, GCD should be 1
print(f"GCD: {gcd}")  # Expected GCD = 1
print(f"u: {u}, v: {v}")

# Flag is the lower of u and v
flag = min(u, v)
print(f"Flag: {flag}")"""
# --------------------------------------------------------
"""# Calculate 11 ≡ x mod 6
x = 11 % 6  # 11 ÷ 6

# Calculate 8146798528947 ≡ y mod 17
y = 8146798528947 % 17 

# Find the smaller of x and y
print(min(x, y)) """
# --------------------------------------------------------
"""# For p = 17
# Calculate 3^17 mod 17
print(pow(3, 17, 17))  # 3^17 ≡ 1 mod 17

# Calculate 5^17 mod 17
print(pow(5, 17, 17))  # 5^17 ≡ 1 mod 17

# Calculate 7^16 mod 17
print(pow(7, 16, 17))  # 7^16 ≡ 1 mod 17

# For p = 65537
# Calculate 273246787654^65536 mod 65537
print(pow(273246787654, 65536, 65537))  # 273246787654^65536 ≡ 1 mod 65537"""
#--------------------------------------------------------
# Find the multiplicative inverse of 3 mod 13 using Fermat's Little Theorem
# Since 13 is prime, 3^(13-1) ≡ 1 mod 13, so 3^12 ≡ 1 mod 13
# Thus, 3^11 is the inverse of 3 mod 13
p = 13
g = 3
d = pow(g, p-2, p)  # 3^(13-2) = 3^11 mod 13
print(d)  # Prints 9