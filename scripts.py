def getkey(txt, length):
    return_txt = ""
    length_txt = len(txt)
    cycle_length = length // length_txt
    last_part_length = length % length_txt
    for i in range(cycle_length):
        return_txt = return_txt + txt
    return_txt = return_txt + txt[0:last_part_length]
    return return_txt


def text_to_bits(text, encoding='ascii', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    bit = bits.zfill(8 * ((len(bits) + 7) // 8))
    print("Мое знач : " + bit)
    return bit


def text_from_bits(bits, encoding='ascii', errors='surrogatepass'):
    n = int(bits, 2)
    print("Мое знач : " + bits)
    value = n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'
    print("Мое знач : " + value)
    return value

"""
num = int('11111', 2)
num_of_bits = 8
d = hex(num)[2:]
print(d)ХЕКС В БИТЫ
print(bin(int(d, 16))[2:].zfill(num_of_bits))#БИТЫ В ХЕКС
"""
def encrypt_msg(txt, key,base=2):
    if base == 2:
        value=encrypt_msg_base2(txt, key)
    if base == 16:
        #num_of_bits = 4*((len(bits_for_base16)+3)//4)#вдруг понадобится
        value = encrypt_msg_base16(txt, key)
        print(value)
    return value
def encrypt_msg_base16(txt, key):
    key = bin(int(key, 16))[2:]
    print("base16to2: " + key)
    bits_for_base16 = encrypt_msg_base2(txt, key)
    value = hex(int(bits_for_base16, 2))[2:]
    return value
def encrypt_msg_base2(txt, key):
    bit = text_to_bits(txt)
    value = getvalues(bit, key)
    print("Мой шифр : " + value)
    print(len(value))
    return value

def decrypt_msg_base16(bit, key):
    key = bin(int(key, 16))[2:]
    bit = bin(int(bit, 16))[2:]
    print("base16to2: " + key)
    value=decrypt_msg_base2(bit, key)
    return value
def decrypt_msg_base2(bit, key):
    print("Мой Шифр : " + bit)
    value = getvalues(bit, key)
    value=text_from_bits(value)
    return value
def decrypt_msg(bit, key, base=2):
    if base == 2:
        value=decrypt_msg_base2(bit, key)
    if base == 16:
        value=decrypt_msg_base16(bit,key)
    return value



def getvalues(bit, key):

    key = getkey(key, len(bit))
    print("Мой ключ : " + key)
    y = xor(bit, key)
    value = '{0:0{1}b}'.format(y, len(bit))
    return value


def xor(x, y):
    return (int(x, 2) ^ int(y, 2))


key = "f5c"
v = encrypt_msg("dasd", key, base=16)
print(v)
v2 = decrypt_msg(v, key,base=16)
print(v2)
