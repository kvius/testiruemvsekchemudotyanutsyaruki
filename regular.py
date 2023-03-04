import re

def checkregular(x,base,crypt):

    patterns={
    "pattern_for_utf8":"[A-Za-zА-Яа-я0-9\sёЁіІїЇ.,?!]+",
    "pattern_for_bits":"(?:[0-1]{8})+",
    "pattern_for_base16" : "[0-9a-f]+",
    "pattern_for_passbits" : "[0-1]+",}
    if crypt == "text":
        pattern=patterns["pattern_for_utf8"]
    if base==2 and crypt == "num":
        pattern=patterns["pattern_for_bits"]
    if base==2 and crypt == "numpass":
        pattern=patterns["pattern_for_passbits"]
    if base==16 and crypt == "num":
        pattern=patterns["pattern_for_base16"]
    print("1")
    regular = re.fullmatch(pattern, x)
    return True if regular else False