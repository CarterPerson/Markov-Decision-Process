import random
import time

class mazeProblem:

    def __init__(self, maze):

        self.locprobs = list()
        self.maze = maze
        size = 0

        for x in range(maze.width):
            for y in range(maze.height):
                self.locprobs.append(0)
                if maze.is_floor(x, y):
                    size = size + 1

        for x in range(maze.width):
            for y in range(maze.height):
                if maze.is_floor(x, y):
                    self.locprobs[maze.index(x, y)] = 1/size


    def time_step(self):
        #time.sleep(1)
        rand = random.randint(0, 3)
        self.maze.move_robot(rand)


    # returns string representing 5 most likely states
    def highest_probs(self):
        topProbs = ""
        probCopy = self.locprobs.copy()
        for iterator in range(5):
            topProb = self.locprobs[0]
            toploc = 0
            for x in range(len(probCopy)):
                if probCopy[x] > topProb:
                    toploc = x
                    topProb = probCopy[x]
            loc = self.maze.unindex(toploc)
            probCopy.pop(toploc)
            topProbs += "(" + str(loc[0] + "," + str(loc[1]) + ") : " + str(topProb) + '\n')
        return topProbs


    def get_color(self):
        rand = random.random()
        returner = ""
        if rand < .84:
            returner = self.maze.get_color()
        elif rand < .88:
            returner = "r"
        elif rand < .92:
            returner = "b"
        elif rand < .96:
            returner = "g"
        else:
            returner = "y"
        correct = (returner==self.maze.get_color())
        print("Given color is " + str(correct)+": "+ returner)
        return returner


    def update(self):
        color = self.get_color()
        newpos = self.locprobs.copy()

        # gets new probabilities
        for x in range(len(self.locprobs)):
            loc = self.maze.unindex(x)
            if color == self.maze.get_color(loc[0], loc[1]):
                newpos[x] = .88 * self.locprobs[x]
            else:
                newpos[x] = .04 * self.locprobs[x]

        # normalizes probabilities
        divider = sum(newpos)
        for x in range(len(newpos)):
            newpos[x] = newpos[x] / divider

        self.locprobs = newpos


    def predict(self):
        # creates new probability distribution full of 0s
        newpos = list()
        for x in range(len(self.locprobs)):
            newpos.append(0)

        #motion model, iterates through all current probabilities and adds up probabilities for next location
        for x in range(len(self.locprobs)):
            # west movement
            loc = self.maze.unindex(x)
            if self.maze.is_floor(loc[0] - 1, loc[1]):
                newpos[x-1] += self.locprobs[x] * .25
            else:
                newpos[x] += self.locprobs[x] * .25

            # east movement
            if self.maze.is_floor(loc[0] + 1, loc[1]):
                newpos[x+1] += self.locprobs[x] * .25
            else:
                newpos[x] += self.locprobs[x] * .25

            # north movement
            if self.maze.is_floor(loc[0], loc[1] + 1):
                newpos[x + self.maze.width] += self.locprobs[x] * .25
            else:
                newpos[x] += self.locprobs[x] * .25

            # south movement
            if self.maze.is_floor(loc[0], loc[1] - 1):
                newpos[x - self.maze.width] += self.locprobs[x] * .25
            else:
                newpos[x] += self.locprobs[x] * .25

        self.locprobs = newpos



    def __str__(self):
        topProbs = ""
        probCopy = self.locprobs.copy()
        for iterator in range(5):
            topProb = probCopy[0]
            toploc = 0
            for x in range(len(probCopy)):
                if probCopy[x] > topProb:
                    toploc = x
                    topProb = probCopy[x]
            loc = self.maze.unindex(toploc)
            probCopy[toploc] = 0
            topProbs += "(" + str(loc[0]) + "," + str(loc[1]) + ") : " + str(topProb) + "\n"
        return str(self.maze) + topProbs






