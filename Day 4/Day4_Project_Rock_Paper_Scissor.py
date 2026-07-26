import random
print('''Welcome to the Rock,Paper,Scissor Game !!
0 = Rock
1 = Paper
2 = Scissor ''')
user_input=int(input("Please enter the digit accordimg to your choice:"))
computer_choice=random.randint(0,2)
rock=''' 
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)'''
paper='''   
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)'''
scissor=''' 
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)'''



if user_input==0:
   if computer_choice==0:
      print(f'''
        User's Choice:    
        {rock}
        Computer's Choice:
        {rock}
        IT' a Tie!!
        ''')
   elif computer_choice==1:
      print(f'''
        User'Choice:
        {rock}
        Computer's Choice:
        {paper}
        Computer Wins!!
        ''')   
   else:
      print(f'''
        User's Choice:
        {rock}
        Computer's Choice:
        {scissor}

        User Wins!!''')

elif user_input==1:
   if computer_choice==0:
      print(f'''
        user's choice:
        {paper}
        Computer' choice:
        {rock}

        User Wins!!
        ''')
   elif computer_choice==1:
      print(f'''
        User's Choice:
        {paper}
        Computer's Choice:
        {paper}

        It's a Tie
        ''')
   else:
      print(f'''
        User's Choice:
        {paper}
        Computer's Choice:
        {scissor}

        Computer Wins!!''')
elif user_input==2:
   if computer_choice==0:
      print(f'''
        User's Choice:
        {scissor}
        Computer's Choice:
        {rock}

        Computer Wins!!''') 
   elif computer_choice==1:
      print(f'''
        User's Choice:
        {scissor}
        Computer' s Choice:
        {paper}

        User Wins!!''')    
   else:
      print(f'''
        User's Choice:
        {scissor}
        Computer's Choice:
        {scissor}

        It's a Tie''')

else:
   print("Please Enter Valid Input")

print("Thanks for using our Game!!")            
