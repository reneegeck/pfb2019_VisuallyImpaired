#!/usr/bin/env python3
import user
import random
from print_quiz import re_input_easy, re_input_med, re_input_hard 
player = user.User('Horseshoe Crab', 100, 80, 50, 60, set(), dict())

#make mini-encounter before racoon fight, yields healing potion
#regular expressions quiz, depends on intelligence level
def random_en3(user):
	print("Shasta walks up to you.")
	#text color change
	print("Answer my questions and I will give you a prize!")
	if user.intel >= 65:
		print("You're a smart cookie, this one will be easy!")
		re_e = re_input_easy('')
		#easy regular expression quiz
		if re_e.lower() == 'c':
			print("Congrats! You chose the correct answer. All that studying is paying off.")
			print("Shasta hands you a health potion. Sweet!")
			if 'items' not in user.inventory.keys():
				user.inventory['items'] = list()
				user.add_item('Health Potion')
			else:
				user.add_item('Health Potion')
		elif re_e.lower() == ('a' or 'b' or 'd'):
			print("Yikes...that's not right. Were you asleep during that module?")
			print("You walk away empty-handed")
		else:
			print("That makes no sense. What did you say?")
	elif user.intel >= 50:
		#medium regex quiz
		print("Your intelligence is okay, but you'll have to think a little on this one...")
		re_m = re_input_med('')
		if re_m.lower() == 'b':
			print("Congrats! You chose the correct answer. All that studying is paying off.")
			print("Shasta hands you a health potion. Sweet!")
			if 'items' not in user.inventory.keys():
				user.inventory['items'] = list()
				user.add_item('Health Potion')
			else:
				user.add_item('Health Potion')
		elif re_m.lower() == ('a' or 'c' or 'd'):
			print("Yikes...that's not right. Were you asleep during that module?")
			print("You walk away empty-handed")
		else:
			print("That makes no sense. What did you say?")
	else:
		#hard regex quiz
		print("Whew, you're not feeling so smart right now. This is going to be a tough one.")
		re_h = re_input_hard('')
		if re_h.lower() == 'c':
			print("Congrats! You chose the correct answer. All that studying is paying off.")
			print("Shasta hands you a health potion. Sweet!")
			if 'items' not in user.inventory.keys():
				user.inventory['items'] = list()
				user.add_item('Health Potion')
			else:
				user.add_item('Health Potion')
		elif re_m.lower() == ('a' or 'c' or 'd'):
			print("Yikes...that's not right. Were you asleep during that module?")
			print("You walk away empty-handed")
		else:
			print("That makes no sense. What did you say?")
