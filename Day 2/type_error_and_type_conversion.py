#the lenght fuction can only count string,list,tuplrr,dictionary,etc. due to which it gives type error once an integer is written into it.
#len(4567)
#using typefunction we can find the data type of any characters
print(type(4764))
print(type(True))
print(type("hello"))
print(type(34.64))
#Using type convesion
#Earlier we saw that in concatenation of integers and string the python gave error rather just to add them , due to which here we can use type conversion
print("number of letters in hello is:"+str(len("hello"))) 
