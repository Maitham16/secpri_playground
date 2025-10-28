"""
def bytes2matrix(text):
    """""" Converts a 16-byte array into a 4x4 matrix.  """"""
    return [list(text[i:i+4]) for i in range(0, len(text), 4)]

def matrix2bytes(matrix):
"""    """ Converts a 4x4 matrix into a 16-byte array.  """
"""    return bytes([b for row in matrix for b in row])

matrix = [
    [99, 114, 121, 112],
    [116, 111, 123, 105],
    [110, 109, 97, 116],
    [114, 105, 120, 125],
]

print(matrix2bytes(matrix))

# second solution:
def matrix2bytes(matrix):
    """""" Converts a 4x4 matrix into a 16-byte array. """"""
    return bytes(sum(matrix, []))

matrix = [
    [99, 114, 121, 112],
    [116, 111, 123, 105],
    [110, 109, 97, 116],
    [114, 105, 120, 125],
]

result = matrix2bytes(matrix)
print(result.decode())"""

# ------------------------------------------------------------
"""
def add_round_key(s, k):
    return [[s[i][j] ^ k[i][j] for j in range(4)] for i in range(4)]

def matrix2bytes(matrix):
    return bytes(sum(matrix, []))

state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]

result = matrix2bytes(add_round_key(state, round_key))
print(result.decode())
"""