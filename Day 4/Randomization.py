import random
#above is an module imported fo applying randomiation on the ange of numbers
random_number=random.randint(0,1)
# randint called using the module name
print(random_number)
#below randomissation of floating number is used
random_numer_1_to_2=random.random()
#Here the random function andoms the number between 0.0<=N<1.0
# and below is another function called uniform that randoms brtween two numbers includingg both the number 
random_floating_number=random.uniform(1,10)
print(random_numer_1_to_2)
print(random_floating_number)

if random_number == 0 :
    print("Heads")
else:
    print("Tails")    