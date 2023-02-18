def getkey(txt,length):
            return_txt="";
            length_txt=len(txt)
            cycle_length=length//length_txt
            last_part_length = length % length_txt
            for i in range(cycle_length):
                return_txt=return_txt+txt
            return_txt=return_txt+txt[0:last_part_length]
            return return_txt
def text_to_bits(text, encoding='ascii', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    bit=bits.zfill(8 * ((len(bits) + 7) // 8));
    print("Мое знач : " + bit)
    return bit
def text_from_bits(bits, encoding='ascii', errors='surrogatepass'):
    n = int(bits, 2)
    print("Мое знач : " + bits)
    value =n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0';
    print("Мое знач : " + value)
    return value
def encrypt_msg(txt,key):
    bit = text_to_bits(txt)
    value=getvalues(bit,key)
    print("Мой шифр : " + value)
    print(len(value))
    return value
def decrypt_msg(bit,key):
    print("Мой Шифр : "+bit)
    value = getvalues(bit, key)
    return(text_from_bits(value))
def getvalues(bit,key):
    key = getkey(key, len(bit))
    print("Мой ключ : " + key)
    y=xor(bit, key)
    value = '{0:0{1}b}'.format(y, len(bit))
    return value
def xor(x,y):
    return(int(x, 2) ^ int(y, 2))
key="1010101001"
v=encrypt_msg("d",key)
print(v)
v2=decrypt_msg(v,key)
print(v2)
