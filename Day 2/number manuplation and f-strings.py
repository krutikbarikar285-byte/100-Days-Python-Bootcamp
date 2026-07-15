weight=82
height=1.52
bmi=weight/((height)**2)
print(bmi)
#we can just use 'int' type conversiiion nstead of using floor deivision to just floor divide the rational number.
print(int(bmi))
#Using 'round' function we can directly round the number to the nearest integer , and can also specify certain lenght of number after the deciimal point by giving the specified lenght of extensiom number after the decimal point. 
print(round(bmi))
print(round(bmi,2))
#or we can use ' format(numbe,".2f") ' for preventiion of dropng traling zeros 
print(format(bmi,".9f"))
#or we can use f-strings for prevention of trilng of zeros
print(f"{bmi:.5f}")
score=0
score=score+1
print(score)
#Or we can just use assignment operators instead of using the above lenghty code to minimize our effort and save time.
score+=1
print(score)
score-=1
print(score)
#we can also use"/=' or '*=' assignment operrator


#F-strings
print("my age is "+str(73))
#as we can see in above code we had to inset personally thr string conversion to escape the type error , now thnk if we had to use so many conversions in one code line to outrun thhe error.
# Thats why the f-string come in very handy as it converts the whole block of code into string. 
print(f"my height is {height} and my weight is {weight}")