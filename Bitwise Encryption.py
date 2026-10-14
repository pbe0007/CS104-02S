key = 30000

"""
def comparator(substrate, value):
    num = ""
    for char in substrate:
        num += format(ord(char), "#010b")[2:]
    num2 = ""
    for char in value:
        num2 += format(ord(char), "#010b")[2:]
    return int(num)^int(num2)
"""

with open("gettysburg_address.txt", "r") as f:
    encrypted = ""
    for char in f.read():
        encrypted += chr(ord(char)^key)

    print(encrypted)

    decrypted = ""
    for char in encrypted:
        decrypted += chr(ord(char)^key)

    print(decrypted)
