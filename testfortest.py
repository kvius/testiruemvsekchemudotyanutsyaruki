import re

string = "1111f4911a11d113"
pattern_for_utf8="[A-Za-zА-Яа-я0-9\sёЁіІїЇ.,?!]+"
pattern_for_bits="(?:[0-1]{8})+"
pattern_for_base16="[0-9a-f]+"

regular = re.fullmatch(pattern_for_base16, string)
print(regular[0])
