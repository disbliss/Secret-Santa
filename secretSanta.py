### Secret Santa Generator
###  version 0.2
###  by Matthew Dunlap
###  26/11/2010
###############################################
### Operation:
###  Takes a return separated list of names and randomly assigns each one
###  to another name in the list (not their own). Creates a text file
###  for each name with the person they are giving to inside so that the 
###  generating person does not have the fun spoiled.
###############################################
### Future implementation:
###  - Take in email addresses as well and send the emails automatically.
###    ~ Probably best implemented by space separating name and email

import random		
import copy
import os

#asks for file path, opens file, creates lists and directory for text files		
peopleFile = open(raw_input("What is the path of the name file? (return separated, just names): "), "r")
peopleList = peopleFile.read().split("\n")
peopleMatchList = copy.deepcopy(peopleList)
usedIndexes = []
os.makedirs("Santa Files")

#Goes through each person in the list, finds the person they are giving a gift too, 
# and creates a text file with the giver as the filename, with the person they are giving to inside.
for person in peopleList:
	matchIndex = random.randint(0, len(peopleMatchList)-1)
	while ((matchIndex in usedIndexes) or (person == peopleMatchList[matchIndex])):
		matchIndex = random.randint(0, len(peopleMatchList)-1)	
	usedIndexes.append(matchIndex)
	
	#debug section. Only uncomment if you want to see who is giving and receiving!
	#print "---------------------"
	#print "Gives:		", person
	#print "Receives: 	", peopleMatchList[matchIndex]

	#Creates each text file
	filename = "Santa Files/"+ person + ".txt"
	file = open(filename, "w")
	file.write(peopleMatchList[matchIndex])
	file.close()