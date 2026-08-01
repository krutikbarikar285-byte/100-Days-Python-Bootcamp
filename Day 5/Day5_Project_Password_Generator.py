import random
print("Welcome to the Password Generator!!")
print("Let's Make Your Password Strong")
letter=int(input("Plese enter the number of letters you need for your password:\n"))
number=int(input("Please enter the total no. of numbers in your password:\n"))
special_characters=int(input("Please enter total no of special characters you need in your password:\n"))
total=letter+number+special_characters
list1=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",0,1,2,3,4,5,6,7,8,9,"!","@","#","$","%","^","&","*","<","(",")"]
password=""
for i in range(total):
    password += str(random.choice(list1))
print(f"Your Passwor is:{password}")