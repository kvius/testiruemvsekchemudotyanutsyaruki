def getkey(txt, length):
    full_cycles, remaining_chars = divmod(length, len(txt))
    return txt * full_cycles + txt[:remaining_chars]

def text_to_bits(text):
    bits = bin(int.from_bytes(text.encode(), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def text_from_bits(bits):
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()

def encrypt_msg(txt, key, base=2):
    if base == 2:
        return encrypt_msg_base2(txt, key)
    if base == 16:
        key = bin(int(key, 16))[2:]
        bits_for_base16 = encrypt_msg_base2(txt, key)
        return hex(int(bits_for_base16, 2))[2:]

def encrypt_msg_base2(txt, key):
    bit = text_to_bits(txt)
    value = getvalues(bit, key)
    return value

def decrypt_msg(bit, key, base=2):
    if base == 2:
        return decrypt_msg_base2(bit, key)
    if base == 16:
        key = bin(int(key, 16))[2:]
        bit = bin(int(bit, 16))[2:]
        num_of_bits = 4 * ((len(bit) + 3) // 4)
        bit = bit.zfill(num_of_bits)
        value = decrypt_msg_base2(bit, key)
        return value

def decrypt_msg_base2(bit, key):
    value = getvalues(bit, key)
    return text_from_bits(value)

def getvalues(bit, key):
    key = getkey(key, len(bit))
    y = xor(bit, key)
    return '{0:0{1}b}'.format(y, len(bit))

def xor(x, y):
    return int(x, 2) ^ int(y, 2)


if __name__ == '__main__':
    znach = "sdfфывфs"
    key = "1011"
    print("Введённое значение : " + znach)
    print("Введённое ключ : " + key)
    v = encrypt_msg(znach, key, base=16)
    v2 = decrypt_msg(v, key, base=16)
    print(v2)
