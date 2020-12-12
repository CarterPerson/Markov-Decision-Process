## Carter Person, CS76 20F, PA6


### Code description

For designing my algorithm, I tried to make it as broad as possible. Unfortunately, it wasn't very easy to make it broadly applicable, and the actual filtering method is fairly small, with the majority of the code needing to be written in the code specific to the problem.

I started off by copying the maze code for from mazeworld. This provided a good basis to represent the maze itself, as well as a good printout method that showed the state of the maze. In this, I only made a few adjustments. I represented the floor tiles with the color of the tile rather than a ".". This allowed the  maze to include the color of the floor tiles, and also made it very easy to get the tile color at any given location, since it only required a small adjustment to the is_floor method. In here, I also added the random movement method, which gives a 25% chance of moving in each of the cardinal directions.

I then moved on to creating the mazeproblem file. In this file, I first focused on what was necessary to represent the problem (for printouts and such) as well as the sensor method for the color tile. I made this method general, giving it a 84% chance of reading the color from the ground, and a 4% chance for each option. By doing this, the method has a 88% chance of returning the correct color and a 4% chance for any of the wrong colors, which is what was necesarry for the problem. I also read in the maze, counted how many tiles were floor tiles, and then made a uniform distribution of possible locations over those tiles. Then, I focused on the update and predict methods. the update method was relatively simple, I just multiplied the probability of the tile by .88 if the observed color and the color of the tile were the same, and by .04 if they were different, followed by the normalization of the new probabilities. At the end of the method, I set these new probabilities to a global variable for the object.

The predict method was a bit more complicated. For this method, I iterated through all of the tiles and all of the possible actions that the robot could take from the tile currently being looked at. I started by creating a new list that was full of zeros, representing the running probability of the robot being there after the action. For each potential movement, I checked whether there was a wall that would impede the robots action. If there wasn't, I then added .25 * the probability that the robot was at the initial tile to the new tile. This resulted in the new set of probabilities for where the robot could be after moving. After creating this new list of probabilities, I set the global probabilities to it.

In addition, I added a time step function. This simply has a time.sleep call to slow down the output of information, and a call to the maze to have the robot move.

In the actual algorithm function, Filtering, I conducted an update step, and then proceeded to iterate. In each iteration, I performed a predict step, then had a time step occur, and then performed an update step. I printed out the maze with the robot's location, as well as the 5 most likely positions with their probabilities after each update step. By only printing out after the update step, I avoided any problems from setting the general probabilities to the probabilities from the predict step.



### code efficacy

My algorithm does work well. The certainty of the robot being at any given location rarely goes above 50%, which does make sense given the occassionally false readings. The algorithm rarely runs into situations where the robot is in the wrong location, and these almost always occur along with the sensor giving the wrong reading of the tile color. When it does read the wrong color, the algorithm will oftentimes be able to correct itself and find the robot's location. The algorithm is able to run very quickly, with an unnoticeable run time if the time.sleep is removed.

Below is a sample printout from the basic 4x4 testing situation where there are no walls. I set the algorithm to perform 10 movements.

Given color is True: r
rgyr
byyr
gAgy
bryg
(1,0) : 0.18181818181818182
(1,1) : 0.18181818181818182
(3,2) : 0.18181818181818182
(0,3) : 0.18181818181818182
(3,3) : 0.18181818181818182

Given color is False: r
rgyr
byyr
grAy
bryg
(3,3) : 0.2773805043281897
(1,0) : 0.19044034625517506
(3,2) : 0.19044034625517506
(0,3) : 0.19044034625517506
(1,1) : 0.10350018818216036

Given color is True: y
rgyr
byyr
grgy
brAg
(2,3) : 0.25335107687961395
(2,2) : 0.17778735995360903
(2,0) : 0.17435264554788155
(3,1) : 0.17435264554788155
(1,2) : 0.1022236430276041

Given color is True: y
rgyr
byyr
grgy
brAg
(2,3) : 0.301308994783914
(2,2) : 0.24361671215014888
(1,2) : 0.1298374973559061
(3,1) : 0.12742947164597504
(2,0) : 0.12301475784443476

Given color is True: r
rgyr
byyr
grgy
bAyg
(3,2) : 0.33736394766156796
(3,3) : 0.2857363647245427
(1,1) : 0.13085361591346725
(1,0) : 0.11476312378303354
(2,3) : 0.022104678985623682

Given color is True: r
rgyr
byyr
gAgy
bryg
(3,3) : 0.4395798231620313
(3,2) : 0.30572383202352965
(1,0) : 0.11899295681212704
(1,1) : 0.0683787656134956
(0,3) : 0.0250029991183412

Given color is True: r
rgyr
byyr
grgy
bAyg
(3,3) : 0.4959122168774506
(3,2) : 0.3168188569026743
(1,0) : 0.08031725649416097
(1,1) : 0.05368660862528885
(0,3) : 0.02165602145375821

Given color is True: b
rgyr
byyr
grgy
Aryg
(0,0) : 0.2999826392587402
(3,3) : 0.20759424188941958
(3,2) : 0.12998247063317886
(0,2) : 0.08724513670335629
(2,3) : 0.08057890056625465

Given color is False: g
rgyr
byyr
grgy
Aryg
(0,1) : 0.47719632626464986
(2,1) : 0.15101312323574695
(1,3) : 0.11919955284872776
(3,0) : 0.0783866968113565
(0,0) : 0.03340179534438459

Given color is True: b
rgyr
byyr
grgy
Aryg
(0,0) : 0.4713571071083419
(0,2) : 0.41663513129649093
(1,1) : 0.02495074225446818
(0,1) : 0.01978169469269081
(3,1) : 0.010016567117606307

Given color is True: b
rgyr
byyr
grgy
Aryg
(0,0) : 0.6308017956450037
(0,2) : 0.2922640954115969
(0,1) : 0.027723293782889232
(1,0) : 0.015099803710757519
(1,2) : 0.013524190088450254
