#conditions are used to develop an condition for python to run the backup code if the given code has an error.
#we use if-else for creating an control flow in codes
#Below is an example

print("Welcome to the Rollercoaster!!")
height=int(input("Enter your Height:"))
#here below logical operato is used 'Or' , logical opeators ae used to show multiple conditions in a single line of code .
#"and","or","not" are the three logical operators of python
if height>200 or height<20 :
    print("Enter correct height")
elif  height>=120:
    print("You'r welcome to the rollercoaster")
    age=int(input("Enter your age:"))
    if age>=18:
        print("Your ride charge is 5$")
    else:
        print("Your ride charge is 3$") 
else :
    print("Go increase your height")    
