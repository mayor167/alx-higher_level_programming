#!/usr/bin/python3
def uppercase(str):
    for chara in str:
        check = ord(chara)
        if check >= 97 and check <= 122:
            dig = check - 32
            chara = chr(dig)
        print("{}".format(chara), end="")
    print()
