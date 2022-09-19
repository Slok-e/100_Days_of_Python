# code for Reeborg's World
def turn_left():
    turn_left()
def move():
    move()
def front_is_clear():
    front_is_clear()
def wall_in_front():
    wall_in_front()
def at_goal():
    at_goal()
def wall_on_right():
    wall_on_right()

#Actual Functions
def avoid_wall():
    turn_left()
    while wall_on_right():
        move()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def hurdle():
    move()
    turn_left()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

def scale_wall():
    turn_left()
    while wall_on_right():
        move()
        if not wall_on_right():
            turn_right()
            move()
            turn_right()
    


for i in range(6):
    hurdle()

while not at_goal():
    move()
    if wall_in_front():
        scale_wall()
    else:
        continue
    

