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

#Actual Functions
def avoid_wall():
    turn_left()
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

for i in range(6):
    hurdle()

while not at_goal():
    if front_is_clear():
        move()
    elif wall_in_front():
        avoid_wall()