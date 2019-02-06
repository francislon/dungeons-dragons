import sys

code=sys.argv[1]
code=code.upper()

dictionary = {
    "M":"Methionine",
    "A":"Alanine",
    "R":"Arginine"
}

print(dictionary[code], end="")

if(code == "M"):
    print(" is an essential amino acid.")
elif(code == "A"):
    print(" is a non essential amino acid.")
else:
    print(" is a conditional essential amino acid.")
