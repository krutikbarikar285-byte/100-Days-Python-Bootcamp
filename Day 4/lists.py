# A list is an sequence which is used to store multiple elements in an single variable, it can store any data type in a single variable  
# A list is an data stucture which is an unique way of oganising and storing of data
list=[1,"aman",4]
#list uses square racket to store item and can be accesed using the indexing method on it. 
print(list[2])
#we can perform various operations on list , like append,update,remove,pop,extend,etc
list[2]="jay"
print(list)
list.append(6)
list.extend([2,0])
print(list)


#we can use choice function for randomization of the sequence data structures 
import random
print(random.choice(list))

#Or

Random=random.randint(0,4)
print(list[Random])

#Nested lists
list.extend([8,"harish",[55,34]])
#indexing of nested lists
print(list[8][1])
print(len(list))
