num = int('01111101', 2)
num_of_bits = 8
d = hex(num)[2:]
print(d)
print(bin(int(d, 16))[2:].zfill(num_of_bits))
