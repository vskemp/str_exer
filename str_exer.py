# CAPITALIZE A STRING
# REVERSE A STRING
# LEETSPEAK A STRING

ex_string = str.upper("can you snarkle my larkle?")
print(ex_string)
reverse_str = ex_string[::-1]
print(reverse_str)

replace_please = (
    ex_string
        .replace("A", "4")
        .replace("E", "3")
        .replace("G", "6")
        .replace("I", "1")
        .replace("O", "0")
        .replace("S", "5")
        .replace("T", "7")
)
print(replace_please)


#LONG VOWELS

long_str = ("Spoons ween off cheese weeaboos.")
replace_long = (
    long_str
        .replace("oo", "oooo")
        .replace("ee", "eeee")
)
print(replace_long)

encrypt_str = "lbh zhfg hayrnea jung lbh unir yrnearq"
new_str = " "
for letter in encrypt_str: 
    if letter == "a":
        new_str += "n"
    elif letter == "b":
        new_str += "o"
    elif letter == "c":
        new_str += "p"
    elif letter == "d":
        new_str += "q"
    elif letter == "e":
        new_str += "r"
    elif letter == "f":
        new_str += "s"
    elif letter == "g":
        new_str += "t"
    elif letter == "h":
        new_str += "u"
    elif letter == "i":
        new_str += "v"
    elif letter == "j":
        new_str += "w"
    elif letter == "k":
        new_str += "x"
    elif letter == "l":
        new_str += "y"
    elif letter == "m":
        new_str += "z"
    elif letter == "n":
        new_str += "a"
    elif letter == "o":
        new_str += "b"
    elif letter == "p":
        new_str += "c"
    elif letter == "q":
        new_str += "d"
    elif letter == "r":
        new_str += "e"
    elif letter == "s":
        new_str += "f"
    elif letter == "t":
        new_str += "g"
    elif letter == "u":
        new_str += "h"
    elif letter == "v":
        new_str += "i"
    elif letter == "w":
        new_str += "j"
    elif letter == "x":
        new_str += "k"
    elif letter == "y":
        new_str += "l"
    elif letter == "z":
        new_str += "m"
    else:
        new_str += " "

print(new_str)