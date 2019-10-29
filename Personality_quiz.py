#!/usr/bin/env python3
import user, weapon_choice, little_vinnys, time, random, print_ascii, fight_raccoon

#======================================================
from print_quiz import decode
from print_quiz import quiz_input1, quiz_input2, quiz_input3, quiz_input4, quiz_input5, quiz_input6


print("Hello - what is your name?")
name = input("Name: ")
print("Hello " + str(name) + ", now do the personality quiz")


#creating counts for each of the personality types
answer_dict = {'Banana Slug': 0, 'Horseshoe Crab': 0, 'Pigeon': 0, 'Squirrel': 0}

q1 = quiz_input1('')

if q1.lower() == 'a':
	answer_dict['Banana Slug'] += 1
elif q1.lower() == 'b':
	answer_dict['Horseshoe Crab'] += 1
elif q1.lower() == 'c':
	answer_dict['Pigeon'] += 1
elif q1.lower() == 'd':
	answer_dict['Squirrel'] += 1
else:
	print("What? Try again!")

q2 = quiz_input2('')
if q2.lower() == 'a':
	answer_dict['Banana Slug'] += 1
elif q2.lower() == 'b':
	answer_dict['Horseshoe Crab'] += 1
elif q2.lower() == 'c':
	answer_dict['Pigeon'] += 1
elif q2.lower() == 'd':
	answer_dict['Squirrel'] += 1
else:
	print("What? Try again!")

q3 = quiz_input3('')
if q3.lower() == 'a':
  answer_dict['Banana Slug'] += 1
elif q3.lower() == 'b':
  answer_dict['Horseshoe Crab'] += 1
elif q3.lower() == 'c':
  answer_dict['Pigeon'] += 1
elif q3.lower() == 'd':
  answer_dict['Squirrel'] += 1
else:
  print("What? Try again!")

q4 = quiz_input4('')
if q4.lower() == 'a':
  answer_dict['Banana Slug'] += 1
elif q4.lower() == 'b':
  answer_dict['Horseshoe Crab'] += 1
elif q4.lower() == 'c':
  answer_dict['Pigeon'] += 1
elif q4.lower() == 'd':
  answer_dict['Squirrel'] += 1
else:
  print("What? Try again!")

q5 = quiz_input5('')
if q5.lower() == 'a':
  answer_dict['Banana Slug'] += 1
elif q5.lower() == 'b':
  answer_dict['Horseshoe Crab'] += 1
elif q5.lower() == 'c':
  answer_dict['Pigeon'] += 1
elif q5.lower() == 'd':
  answer_dict['Squirrel'] += 1
else:
  print("What? Try again!")

sorted_dict = sorted(answer_dict.items(), key=lambda x:x[1], reverse=True)

if sorted_dict[0][1] == sorted_dict[1][1]:
	variable1 = ''
	variable2 = ''
	#this is the tiebreaker question
	TieBreak_Dict = {'Banana Slug': '    Damp and cold   ', 'Horseshoe Crab': '   Sandy and cold   ', 'Pigeon': ' Covered in garbage ', 'Squirrel': 'Being chased by dogs'}
	for key in TieBreak_Dict.keys():
		if key == sorted_dict[0][0]: 
			variable1= TieBreak_Dict[key]
		elif key == sorted_dict[1][0]:
			variable2= TieBreak_Dict[key]
	q6 = quiz_input6(variable1,variable2)
	if q6.lower() == "a":
		for key, value in TieBreak_Dict.items():
			if value == variable1:
				animal_name = key
				print("Congrats, you are a", animal_name)
	elif q6.lower() == "b":
		for key, value in TieBreak_Dict.items():
			if value == variable2:
				animal_name = key
				print("Congrats, you are a", animal_name)
	else:
		print("Sorry I don't understand, try a different response")
else:
	animal_name = sorted_dict[0][0]
	print("Congrats, you are a",animal_name)

#==================================================
#Assign player based on quiz outcome
if animal_name == 'Pigeon':
	player = user.User('Pigeon', 100, 60, 60, 40, set(), dict())
	print_ascii.pigeon_pic()
elif animal_name == 'Horseshoe Crab':
	player = user.User('Horseshoe Crab', 100, 80, 50, 60, set(), dict())
	print_ascii.horseshoecrab_pic()
elif animal_name == 'Banana Slug':
	player = user.User('Banana Slug', 100, 40, 30, 80, set(), dict())
	print_ascii.bananaslug_pic()
else: #otherwise squirrel
	player = user.User('Squirrel', 100, 50, 60, 60, set(), dict())
	print_ascii.squirrel_pic()

time.sleep(2)
player.print_user_stats()
time.sleep(5)
print('\n\n\n')

#test
player.print_health_bar()
player.print_speed_bar()
player.print_intel_bar()
player.print_armor_bar()

#===================================================

print('You heft your suitcase out of your Uber and find yourself on the Cold Spring Harbor Laboratories Campus')
time.sleep(1)
print_ascii.CSHL_logo()			#ASCII CSHL ART
print('Mmm so lovely, it smells like fall.')
print('\n\n')
time.sleep(3)

print("But you don't let all that nature distract you from your mission.\n")
time.sleep(2)
print("You have traveled by plane, train, and car to come here to gain the skills needed to... \n\n")
time.sleep(1.5)
print_ascii.master_the_python_pic()
time.sleep(2.5)
print("You and your village have been plagued with inefficient data analysis and server error messages.\n\n")
time.sleep(2)
print("You have come seeking the wisdom of CSHL to be worthy of the art of the PYTHON.")
time.sleep(4)
print("\n\nBut first, you will need some equipment.\n\n")
time.sleep(2)
print("On the lawn in front of you you see some very useful supplies. \n\n")
time.sleep(2)

#call the weapon choice script
weapon_choice.choose_weapon(player)

while player.health > 0: #so long as you aren't dead yet...
#==============================================
	#Encounter with person who asks you questions to get a healing potion

#================================================
	#RACCOON FIGHT
	time.sleep(2)
	print("You're starting to feel kind of hungry and are about to head off to find some food")
	time.sleep(2)
	print("When a giant RACCOON steps out to block your path!")
	time.sleep(2)

	#call the raccoon fight functions
	fight_raccoon.raccoon_fight(player)

#===================================================

	#call little vinny's encounter
	little_vinnys.foraging(player)

#==================================================

#call riddles encounter
#riddle_encounter.answer_riddles(player)
#=================================================
#Die for now to get out of loop
	player.health = 0
#============================================================
player.print_health_bar()
print('Too bad. So long, friend.')
