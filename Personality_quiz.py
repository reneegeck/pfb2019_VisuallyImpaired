#!/usr/bin/env python3
import user, weapon_choice, little_vinnys

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
elif animal_name == 'Horseshoe Crab':
	player = user.User('Horseshoe Crab', 100, 80, 50, 60, set(), dict())
elif animal_name == 'Banana Slug':
	player = user.User('Banana Slug', 100, 40, 30, 80, set(), dict())
else: #otherwise squirrel
	player = user.User('Squirrel', 100, 50, 60, 60, set(), dict())

player.print_user_stats()

#===================================================

print('You find yourself on the Cold Spring Harbor Laboratories Campus')

#call the weapon choice script
weapon_choice.choose_weapon(player)

#===================================================

#call little vinny's encounter
little_vinnys.foraging(player)

#==================================================

#call riddles encounter
#riddle_encounter.answer_riddles(player)
