#First code for my first experiment using the coder!
#This code is for a experimental task which implement two tests for habits after 
#reward learning. 
#One test is the one described in Luque et al. (2020), based on the idea that 
#changing a habitual responses takes more time when the habit is stronger.
#The other test is the described in Hardwick et al. (2019), in which participant 
#have to respond very fast, what produces more habitual perseverations.
#Both tests share the idea that when you are making a goal-directed response, 
#the speed-accuracy trade-off is less efficient if an incompatible habit is 
#activated (by the S).
#Also, they also share the idea that habits can be active very rapidly, while 
#proper goal-directed actions may need more time. Hence in both tests 
#participants have relatively little time to think.
#-the task-
#the S is presented at the center up of the screen
#4 different response options are shown below (the four direc arrows)
#-reward training
#4 S-R mapps
#then feedback, correct response -> +5 points, errors or too slow-->-1
#the total number of points is shown every 100 trials
#-Tests for habits
#participants are instructed that two S have swapped their responses, 
#the new mapping is shown on the screen
#the experiment continous, trials with the swapped S are tests for habits
#normal trials will be used for measuring RT cost
#in half of the trials a sequence of sounds will indicate when to press the key
#these trials are the Hardwick test
#-after the first block of test, it will follow a reward t block and another then another test


### Structure of the task ###
#1# Create stimuli. 4 different S which are different in colour
# Input (none), Output (4 different S which colours are determined pseudorand)

#2# Create the S-R maps, responses are the arrows

#3# List of trials for each block, randomize

#etc
