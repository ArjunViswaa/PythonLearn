print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

direction = input('You\'re at a crossroad now... Where do you want to go ? "left" or "right"... ').lower()
if(direction == "left") : 
    print("Great!! Now how do you wanna go about it")
    choice_2 = input("swim (or) wait")
    if choice_2 == "wait" : 
        print("Great!! Now you have 3 doors in front of you, "
              "which one do you want to select here ??")
        choice_3 = input("red (or) yellow (or) green").lower()
        if choice_3 == "yellow" : 
            print("Success!!! You found the treasure ;)")
        elif choice_3 == "red" : 
            print("No... You're dead it's a rooom full of fire")
        elif choice_3 == "green" : 
            print("No... You drowned in the infinte ocean")
        else : 
            print("SOrry select one of red, yellow or blue")
    
    else : 
        print("No... You swam in the lake of crocodiles and died")


else : 
    print("Game over ... you fell into a hole")