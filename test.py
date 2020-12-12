from mazeProblem import mazeProblem
from maze import Maze
from Filtering import filtering
import random


test1 = Maze("testmaze1")
problem = mazeProblem(test1)
filtering(problem, 50)

# to generate random maze
teststr = ""
for x in range(10):
    for y in range(10):
        rand = random.random()
        if rand < .2:
            teststr += "#"
        elif rand < .4:
            teststr += "r"
        elif rand < .6:
            teststr += "b"
        elif rand < .8:
            teststr += "y"
        else:
            teststr += "g"
    teststr += '\n'

# to make a new random maze, uncomment below lines, run the program, then place a robot in an non-wall location

#f = open("randomtest", "w")
#f.write(teststr)
#f.close()