print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
******************************************************************************* 
''')
#above we have used 3 single quotes in the print statement which allows us to write multiple line of string in a single print statement
print("Welcome to the Treasure Island !!!")
print('''Your mission is to find the Treature on the Laughtale Island , The "One Piece" which has been left by your grandfathere "Vegapunk".''')
print("Let's start you journey")
obstacle1=int(input('''You just defeated Kaido and you are about to sale for the Treasure  but there is only two routes:
                1.The one which leads to Shanks
                2.The one which leads to Punk Hazzard
                    choose the correct  path  accoding to the One Piece story:'''))
if obstacle1 == 1:
    print("You got one shotted by shanks overwelming haki dominance")
    print("You did't found the Treasue ") 
elif obstacle1== 2:
    print('''You met the world's smartest man alive, "The Vegapunk"''')
    obstacle2=int(input('''Vegapunk had two doors leading to diffrent paths :
                1.The one where the world's strongest Swordsman Mihalk lives
                2.The one where the cursed prince "Loki" has been impisoned in the path
                    So,which option are you gonna choose:'''))                    
    if obstacle2  == 1 :
        print("Congratts you chosed the right path , you just got beheaded by Mihalk :)")
    elif obstacle2 == 2:
        print('''Good you ignored Loki , Congratts!!! now you have reached the final island Laughtale where the the world's greatest treature "The One Piece" has been left for you.''')
    else :
        print("Vegapunk got angry with your answer and decided to execute you as gave the incorrect input.")    
else:
    print("The path did't exist")    
print("The END")