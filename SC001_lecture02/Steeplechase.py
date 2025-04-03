"""
File: Steeplechase.py
Name: TODO:
---------------------------------
TODO:
"""

from karel.stanfordkarel import *


def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """
    for i in range(11):
        if front_is_clear():
            move()
        else:
            jump()
            turn_left()



def jump():
    """
    Pre-condition:Karel is on the left side of the wall,facing East.
    Past-condition:Karel is on the right side of the wall.
    """
    up()
    cross()
    down()


def down():
    """
    Pre-condition:Karel is at the upper right, facing South.
    Past-condition:Karel is on the left side of the wall,facing East.
    """
    while front_is_clear():
        move()


def cross():
    """
    Pre-condition::Karel is on the upper left of the wall, facing North.
    Past-condition:Karel is at the upper right, facing South.
    """
    turn_right()
    move()
    turn_right()



def up():
    """
    Pre-condition:Karel is on the left side of the wall,facing East.
    Past-condition:Karel is on the upper left of the wall,facing North.
    """
    turn_left()
    while not right_is_clear():
        move()
    # alternative:
    # while not front_is_clear():
    #     turn_left()
    #     move()
    #     turn_right()



def turn_right():
    for i in range(3):
        turn_left()


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
