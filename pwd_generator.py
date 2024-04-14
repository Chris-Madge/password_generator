#Password Generator Project
import random



letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#holders for variables
rdm_numbers = ""
rdm_letters = ""
rdm_symbols = ""

#gets randomized numbers by checking the len of rdm_numbers against what the user entered
#once rdm_numbers len = user input, loop ends
for number in numbers:
  if len(rdm_numbers) < nr_numbers:
    rdm_numbers += random.choice(numbers)

for letter in letters:
  if len(rdm_letters) < nr_letters:
    rdm_letters += random.choice(letters)
    
for symbol in symbols:
  if len(rdm_symbols) < nr_symbols:
    rdm_symbols += random.choice(symbols)

#puts uder input into one string
password = (rdm_letters + rdm_numbers + rdm_symbols)

#list to store broken up password
#this is where the "easy challenge" ends
lst_password = []

#breaks up password into individual list items
for letter in password:
  lst_password.append(letter)
  #randomizes order or password
  rdm_password = random.sample(lst_password, (len(lst_password)))

#variable to store new, randomized password
new_password = ""
#loop that adds items from rdm_passwords together
for letter in rdm_password:
  new_password += letter


print(new_password)

