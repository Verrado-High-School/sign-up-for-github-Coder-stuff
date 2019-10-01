#name
#rock paper scissors
#VARIABLES
import random
psc = 0
scs = 0
tz = 0
computerChoices = ["r", "p", "s"]


#welcome message
# print the message
print("ROCK PAPER SCISSORS!!!")
#prompt for player name
pn = input("EE NAME>>..?")



#final score
def printScore():
	# write message
	print("Da skore be: ")
#write player score
	print(pn + ": " + str(psc))
#write computer score
	print("DA cumpoter: " + str(scs))
#write how many ties
	print("Ties: urghhm about... " + str(tz))

#gamemloop
#make a forever loop
while True:
	#print current score
	printScore()
	#prompt for a choice (r (rock), P (paper), s(scissors), q (quit))
	pch = input("Enter r (rock), p (paper), s (scissors) or q (to quit): ")
	#deal wit q entering!
	if pch == "q":
		break
	#get computers choice (random)
	cHoice = random.choice(computerChoices)
	# compare for for plaer enter r
	if pch == "r":
		print(pn + " picketh rock")
		#if computer is r
		if cHoice == "r":
			print("computer picketh rock!")
			print("TIE TIE!!")
			tz = tz + 1
		#if computer is p
	elif cHoice =="p":
		print(" PAPER!! PAPE R the computer has picket!")
		print(" rock > scissors bruh u lose bruh bruh")
		psc = psc + 1
		#if computer is s
	#compare for player entering p
	elif pch == "p":
		pass

	#compare for player entering s
	elif pch == "s":
		pass
