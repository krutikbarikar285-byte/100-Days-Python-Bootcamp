#here below we have used elif statement to add multiple conditions in the code , 
# elif condition can be added infinite times , and they run when if lock is false
print("Welcome to the pizza order machine")
# here below i have used .upper() to convert the user's input "s" or "S"  to "S" 
size=input("Please select you pizza size?S,M and L:\n").upper()
#Aove i have used "\n" at the end of the input so the we can enter the answer on the next  new line
bill=0
if size == "S":
    bill+=15
elif size == "M":
    bill+=20
elif size == "L":
    bill+=25    
else:
    print("Please select correct size")
    
pepperoni=input("Do you want pepperoni on your \"pizza\"?Y or N:\n").upper()
# As you can see i have used "\" in the above line , which is used to escape the forward written string o symbol(") 
# as it would create an error in the code as the computer would interpret (") as an end of the string
extra_cheese=input("Do you want extra cheese on your pizza?Y or N:\n").upper()
#below is an example of nested if and also multiple ifs .
if pepperoni == "Y":
    if size == "S":
        bill+=2
    else :

        bill+=3
if extra_cheese == "Y":
    bill+=1

print(f"Your final bill is {bill}")    

            