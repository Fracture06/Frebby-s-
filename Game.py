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

