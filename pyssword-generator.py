import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password = []
characters = [letters, numbers, symbols]

print("Welcome to the Py_ssword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_characters = nr_numbers + nr_letters + nr_symbols

def get_type():
    global nr_letters
    global nr_symbols
    global nr_numbers
    chr_type = random.randint(0, 2)
    if chr_type == 0:
        if nr_letters > 0:
            nr_letters -= 1
            return chr_type
        else:
           return get_type()
    if chr_type == 1:
        if nr_numbers > 0:
            nr_numbers -= 1
            return chr_type
        else:
            return get_type()
    if chr_type == 2:
        if nr_symbols > 0:
            nr_symbols -= 1
            return chr_type
        else:
           return get_type()

length = nr_characters

print("Your password is: ", end = " ")
while length > 0:
    char_type = get_type()
    ch = random.randint(0, (len(symbols) - 1))
    if char_type == 0:
        ch = random.randint(0, (len(letters) - 1))
    elif char_type == 1:
        ch = random.randint(0, (len(numbers) - 1))
    print(characters[char_type][ch], end = " ")
    length -= 1
print("\n")
