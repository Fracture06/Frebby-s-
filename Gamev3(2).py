import random

## Movement systems 145 121

xcord = 0
ycord = 0
room =4

## Room variables
roomninecomplete = False
has_token = False
key = False
## Misc variables 
no_message = "Null"

## Functions

def roomninegame():
    print ("Yous see a claw machine with a coin slot, a token machine")
    print ("despenser, and a few token machines that it despensed.")
    while 1==1:
        print ("Do you want to check the token machine, play the claw machiene, or leave the room")
        answer_room_nine = input ("token, claw, leave")
        if answer_room_nine == ("leave"):
            break
        elif answer_room_nine == ("token"):
            print("You found a token in the tray...")
            has_token = True
            roomninecomplete = True
            
        elif answer_room_nine == ("claw") and has_token == False:
            print ("You need a token")
        elif answer_room_nine == ("claw") and has_token == True:
            print ("You play the claw and win the key! Congradulations!")
            print ("Now all you need to do is GET OUT WHILE YOU STILL CAN!!!")
            print ("Exit is at the front middle")
            return roomninecomplete
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

    return room
while 1==1:
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
    elif dird == ("south"):
        no_message = get_message()
        print (no_message)
    else:
        print ("Is mayonayse an instrument?")

    current_room = find_room()
    print(current_room)
    print (str(xcord), str(ycord))

    if current_room == 1:
        print("You are now in the arcade have fun with all these games")
        
    elif current_room==2:
        print("You are now in the front area you can check in for an amazing day of pizza and fun")
    elif current_room==3:
        print("You are now in the security office be careful that the security guard doesn't find you in here.")
    elif current_room==4:
        print("You are now at the stage, the performers enjoy it when you pay attention to them. Please pay attention to the performers")
    elif current_room==5:
        print("You are now in the dining area. Make sure you try some of our signiture pizza and fizzy drink")
    elif current_room==6:
        print("You are now in the play place make sure to climb high to escape the other children")
    elif current_room==7:
        print("You are now in the bathrooms. If you have to hide from someone only one of the stalls lock")
    elif current_room==8:
        print("You are now in the kitchen. What the chef says goes so if you have to make some suspicious pizza do it.")
    elif current_room==9:
        print("You are now in the storage room. Legend says that people have died here, lets hope you are not another.")
        roomninegame()
        if roomninegame = True:
            key == True
    else:
        print ("Somehow, you entered an invalid room")