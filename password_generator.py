#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
password_list = []

pass_let_num = int(input('Enter how many letters do you want in the password: '))
for num in range(0, pass_let_num):
    ctrl_num = random.randint(0, len(letters)-1)
    password_list.append(letters[ctrl_num])

pass_num = int(input("Enter how many numbers would you like in ur password: "))
for num in range(0, pass_num):
    ctrl_num = random.randint(0, len(numbers)-1)
    password_list.append(numbers[ctrl_num])

pass_symb = int(input('Enter how many symbols would u like to have in your passowrd: '))
for num in range(0, pass_symb):
    ctrl_num = random.randint(0, len(symbols)-1)
    password_list.append(symbols[ctrl_num])

random.shuffle(password_list)

password = ''
for item in password_list:
    password += item

print(f'Your new password is: {password}')