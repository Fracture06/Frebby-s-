import random

## Movement systems 145 121

xcord = 0
ycord = -1
room = 2

## Room variables
has_token = False
key = False
## Misc variables 
no_message = "Null"
leave=False
## Functions

def roomninegame():
    print ("Yous see a claw machine with a coin slot, a token machine")
    print ("despenser, and a few token machines that it despensed.")
    while 1==1:
        print ("Do you want to check the token machine, play the claw machiene, or leave the room")
        answer_room_nine = input ("token, claw, leave ")
        if answer_room_nine == ("leave"):
            break
        elif answer_room_nine == ("token"):
            print("You found a token in the tray...")
            has_token = True
           
            
        elif answer_room_nine == ("claw") and has_token == False:
            print ("You need a token")
        elif answer_room_nine == ("claw") and has_token == True:
            print ("You play the claw and win the key! Congradulations!")
            print ("Now all you need to do is GET OUT WHILE YOU STILL CAN!!!")
            print ("Exit is at the front middle")
            return(1)
        else:
            print ("Critical error, exploading in 3... 2... 1... kaboom!")
    

def get_message():
    message = random.randint(1,6)
    if message == 1:
        no_message = "oops wrong way"
    elif message == 2:
        no_message = "Nope, uuh uh"
    elif message ==3:
        no_message = "I predict great sadness when you learn this is a wall..."
    elif message ==4:
        no_message = "Do you want to be walking into a wall right now?"
    elif message == 5:
        no_message = "iooirheoingniow'IEAWF'A"
    else:
        no_message = "The Pepperoni hat man Snipper man is this way..."
    return no_message


def find_room():

    if xcord == -1 and ycord == -1:
        room = 1
    elif xcord == 0 and ycord == -1:
        room = 2
    elif xcord == 1 and ycord == -1:
        room = 3
    elif xcord == -1 and ycord == 0:
        room = 4
    elif xcord == 0 and ycord == 0:
        room = 5
    elif xcord == 1 and ycord == 0:
        room = 6
    elif xcord == -1 and ycord == 1:
        room = 7
    elif xcord == 0 and ycord == 1:
        room = 8
    elif xcord == 1 and ycord == 1:
        room = 9
    else:
        print ("Where the tops at?")

    if leave==False:
        return room

print("You see a cash register with a screen on the back, speakers, and a cardboard cutout of Dr. Shuppord.")
print("You are now in the front area you can check in for an amazing day of pizza and fun.")
print("There are doors to the North, East, and West")

while leave==False:

    dird = input("Whar do we go: east, west, north, south ")
    if dird == ("east") and xcord < 1:
        xcord += 1
        
    elif dird == ("east"):
        no_message = get_message()
        print (no_message)
        
    elif dird == ("west") and xcord > -1:
        xcord -= 1
        
    elif dird == ("west"):
        no_message = get_message()
        print (no_message)
        
    elif dird == ("north") and ycord < 1:
        ycord += 1

    elif dird == ("north"):
        no_message = get_message()
        print (no_message)

    elif dird == ("south") and ycord > -1:
        ycord -=1
        
    elif dird==("south") and ycord== -1 and xcord== 0 and key==True:
        print("Congratulation you have won")
        leave=True
        
    elif dird == ("south"):
        no_message = get_message()
        print (no_message)
   
    else:
        print ("Is mayonayse an instrument?")

    current_room = find_room()
  #  print(current_room)

    if current_room == 1:
        print("You see rows and rows of boxes on shelves, gathering dust")
        print("You are now in the storage room. Legend says that people have died here, lets hope you are not another.")
        print("There are doors to the North and East")
        
    elif current_room==2:
        print("You see a cash register with a screen on the back, speakers, and a cardboard cutout of Dr. Shuppord.")
        print("You are now in the front area you can check in for an amazing day of pizza and fun.")
        print("There are doors to the North, East, and West")
        print("There is a door to the South but it is locked")
        
    elif current_room==3:
        print("You see a security system. There are screens all over the back wall, there is a big red button that says emergency only, there are 3 radios on the charger on the wall, and a picture that says my family <3.")
        print("You are now in the security office be careful that the security guard doesn't find you in here.")
        print("There are doors to the North and West")
        
    elif current_room==4:
        print("You see closed curtains. The curtains look like they were hastily closed like someone was trying to hide something. There is what looks to be red paint on the floor of the stage.")
        print("You are now at the stage, the performers enjoy it when you pay attention to them. Please pay attention to the performers")
        print("There are doors to the North, East, and South")
        
    elif current_room==5:
        print("You see plates with food still on them, cups with some sort of drink long flat, you see a banner that says HAPPY 4th BIRTHDAY!!, and  ")
        print("You are now in the dining area. Make sure you try some of our signiture pizza and fizzy drink")
        print("There are doors to the North, East, South, and West")
        
    elif current_room==6:
        print("You see towering rockwalls and ball pits galore")
        print("You are now in the play place make sure to climb high to escape the other children")
        print("There are doors to the North, South, and West")        
        
    elif current_room== 7:
        print("YOU SHOULD NOT HAVE COME HERE!!!")
        print("You walk into the bathroom, just as Dr. Shepord was washing his hands, and he Jeff the kills you")
        break
        
    elif current_room==8:
        print("You see rows and rows of bloody cooking utencils ")
        print("You are now in the kitchen. What the chef says goes so if you have to make some suspicious pizza do it.")
        print("There are doors to the East, South, and West")
        
    elif current_room==9:
        print("You see rows of arcade machines, token machines, birthday hats and plastic cups litter the floor and the long broken arcade machines.")   
        print("You are now in the arcade have fun with all these games")
        print("There are doors to the South and West")
        bean = roomninegame()
        if bean==1 :
            key=True
          #  print("bean")
        