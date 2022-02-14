n=-5

print(bin(n))

print(n.bit_length())

print(n.to_bytes(2,byteorder='big',signed=True))

print(n.as_integer_ratio())