import random

xcord = 1
ycord = -1
room =4

no_message = "Null"

def get_message():
    message = random.randint(1,5)
    if message == 1:
        no_message = "oops wrong way"
    elif message == 2:
        no_message = "Nope, uuh uh"
    elif message ==3:
        no_message = "I predict great sadness when you learn this is a wall..."
    elif message ==4:
        no_message = "Do you want to be walking into a wall right now?"
    else:
        no_message = "The Penar Snipper man is this way..."
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

dird = input("Whar do we go: east, west, north, south")
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
elif dird == ("north") and

current_room = find_room()
print(current_room)

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
elif current_room== 7:
    print("You are now in the bathrooms. If you have to hide from someone only one of the stalls lock")
elif current_room==8:
    print("You are now in the kitchen. What the chef says goes so if you have to make some suspicious pizza do it.")
elif current_room==9:
    print("You are now in the storage room. Legend says that people have died here, lets hope you are not another.")
    
    
    