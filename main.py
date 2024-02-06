#Password Generator Project
import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

gPasswordLetters = ""
gPasswordNumbers = ""
gPasswordSymbols = ""
for _ in range(0, nr_letters):
  gPasswordLetters += str(letters[random.randint(0, 25)])
for _ in range(0, nr_numbers):
  gPasswordNumbers += str(numbers[random.randint(0, 9)])
for _ in range(0, nr_symbols):
  gPasswordSymbols += str(symbols[random.randint(0, 8)])

gRandomPassword = list(gPasswordLetters + gPasswordNumbers + gPasswordSymbols)
random.shuffle(gRandomPassword)
gRandomPassword = ''.join(gRandomPassword)
print(f"Your strong password is: {gRandomPassword}")
