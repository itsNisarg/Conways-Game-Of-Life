"""
CONWAY'S GAME OF LIFE

@author Nisarg Suthar (nisargsuthar0@gmail.com)

@brief Classic cellular automata simulation.
Find out more at : https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
GitHub link of this code : https://github.com/itsNisarg/Conways-Game-Of-Life

"""

# Imports required.

import copy
import sys
import random
import time
import os


# Utility function

def clear():

    if(os.name == 'nt'):        # for Windows
        _ = os.system('cls')
#    else:                       # for UNIX systems
#        _ = os.system('clear')


# Setting the constants.

WIDTH = 200         # width of cell grid
HEIGHT = 40         # height of cell grid

ALIVE = chr(9689)         # Representation of live cell
DEAD = chr(32)          # Representation of dead cell

"""
nextcells is a dictionary that hold the state of the npopulation.
The keys are (x,y) tuples which correspond to the rows and columns
of the cell grid. The values of the are randomly initialised to ALIVE
state with a probability of 8%.
"""
nextcells = dict()

# Assigning cell states with 8 % probabiliy of being ALIVE

for x in range(HEIGHT):                 # looping over rows
    for y in range(WIDTH):              # looping over columns

        if(random.random() < 0.08):      # 8% chance of being ALIVE
            nextcells[(x, y)] = ALIVE    # adding live cell at (x, y)
        else:
            nextcells[(x, y)] = DEAD     # adding dead cell at (x, y)

######################################################################
#                         MAIN PROGRAM                               #
######################################################################

# Introductory Information

clear()

print("""

CONWAY'S GAME OF LIFE

@author Nisarg Suthar (nisargsuthar0@gmail.com)

@brief Classic cellular automata simulation.
Find out more at : https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life


RULES OF THE GAME:

1. Any live cell with two or three live neighbours survives.
2. Any dead cell with three live neighbours becomes a live cell.
3. All other live cells die in the next generation.
   Similarly, all other dead cells stay dead.
""".center(200, ' '))

time.sleep(5)

# Each loop iteration is astep of the simulation

while(True):

    clear()                             # separating new iterations
    cells = copy.deepcopy(nextcells)    # making an extra copy of states

    for x in range(HEIGHT):             # looping over rows
        for y in range(WIDTH):          # looping over columns

            print(cells[(x, y)], end='')        # printing cell state

        print()                                 # new line after every row

    # giving a way to exit simulation
    print("\n Press Ctrl + C to QUIT.")

    # Finding the new cell states based upon current cell states

    for x in range(HEIGHT):
        for y in range(WIDTH):

            left = (y - 1 + WIDTH) % WIDTH
            right = (y + 1) % WIDTH
            above = (x - 1 + HEIGHT) % HEIGHT
            below = (x + 1) % HEIGHT

            # List of neighbouring cells

            neighbours = [(above, left), (above, y), (above, right),
                          (x, left), (x, right),
                          (below, left), (below, y), (below, right)]

            # Finding the number of live neighbouring cells

            num_alive = 0

            for neighbour in neighbours:
                if(cells[neighbour] == ALIVE):
                    num_alive += 1

            # Setting the cell state based on the RULES

            if(cells[(x, y)] == ALIVE and 2 <= num_alive <= 3):
                nextcells[(x, y)] = ALIVE
            elif(cells[(x, y)] == DEAD and num_alive == 3):
                nextcells[(x, y)] = ALIVE
            else:
                nextcells[(x, y)] = DEAD

    try:
        time.sleep(2)     # ading a 2 second pause

    except KeyboardInterrupt:
        clear()
        st = "CONWAY'S GAME OF LIFE".center(200, ' ')
        space = "\n"*20
        print(f'{space}{st}{space}')
        sys.exit(0)


######################################################################
#                      END OF MAIN PROGRAM                           #
######################################################################
