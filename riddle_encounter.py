#!/usr/bin/env python
import user, time, colorama, subprocess, print_ascii  #Personality_quiz, weapon_choice, little_vinnys
from colorama import Fore, Style

riddle_dict = { 'Question 1' : "\"Immature I am earthbound, but when I change, the sky I've found\"",  'Question 2' : '"Greatest man nor tallest tree, Begins as any more than me"', 'Question 3' : '"I grow larger the more you take and yet I shrink the more you add"', 'Question 4' : '"You can catch me, but never throw me. What am I?"', 'Question 5' : "\"What has one eye but can’t see?\"" }


class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def answer_riddles(user):
	correct_answers = 0
	print(color.BOLD + "\nPinecone in hand, you enter Hershey and spot Sofia dutifully guarding a bowl of candy. You reach for a piece, but she pulls the bowl away.\n\n"+ color.END)
	time.sleep(3)
	#subprocess.run(["say", "-v", "Daniel", "Pinecone in hand, you enter Hershey and spot Sophia dutifully guarding a bowl of candy. You reach for a piece, but she pulls the bowl away."])
	print(color.CYAN + "You will need to answer a few riddles before you can have any candy. Do you want to try?\n\n" + color.END)
	subprocess.run(["say", "-v", "Samantha", "You will need to answer a few riddles before you can have any candy. Do you want to try?"])
	response = input('Yes or No? ')
	response = response.lower()
	while response not in ['yes']:
		print(color.CYAN + "Don't be a coward" +color.END)
		subprocess.run(["say", "-v", "Samantha", "Don't be a coward"])
		response = input('Yes or No? ')
		response = response.lower()

#'No' returns the player to the top of the loop
#========================================================================

	if response == 'yes':
		print(color.CYAN + "\nGreat! Let's get started. If you can answer most of the riddles correctly, you will receive a special item. Let's see if you can answer the following riddle.\n" + color.END)
		subprocess.run(["say", "-v", "Samantha", "Great! Let's get started. If you can answer most of the riddles correctly, you will receive a special item. Let's see if you can answer the following riddle."])
		print(color.BOLD + riddle_dict['Question 1'] + color.END) #first question starts here
		time.sleep(2)
		answer1 = input('What is your answer? ')

#Player enters the game for the first time
#========================================================================
		
	if answer1.lower() == 'butterfly':
		print(color.CYAN + "\nExcellent! Don't get too excited though, I found that riddle on a children's website. Plus 10 to your speed.\n" + color.END)
		subprocess.run(["say", "-v", "Samantha", "excellent! Don't get too excited though, i found that riddle on a children's website. Plus 10 to your speed"])
		correct_answers += 1
		user.get_faster(10)
		print('\n\n')
		user.print_speed_bar()
		print('\n\n')
		print(color.BOLD + 'Number of correct answers:' + color.END, correct_answers)
		time.sleep(2)
	elif answer1.lower() != 'butterfly':
		print(color.CYAN + '\nSeriously? THAT was your answer? Are you feeling slow today? The correct answer was butterfly. Minus 10 speed points.\n' + color.END)
		subprocess.run(["say", "-v", "Samantha",  "Seriously? THAT was your answer? Are you feeling slow today? The correct answer was butterfly. Minus 10 speed points"])
		user.get_slower(10)
		print('\n\n')
		user.print_speed_bar()
		print('\n\n')
		print(color.BOLD + 'Number of correct answers:' + color.END, correct_answers)
		time.sleep(2)

#Question 1 finished
#========================================================================

	print(color.CYAN +  "\nOk, let's move on to the next question, ready?\n" + color.END)
	subprocess.run(["say", "-v", "Samantha", "Ok,let's move on to the next question, ready?"])
	response = input('Yes or No? ')
	response = response.lower()
	while response not in ['yes']:
		print(color.CYAN + "Don't be a coward" +color.END)
		subprocess.run(["say", "-v", "Samantha", "Don't be a coward"])
		response = input('Yes or No? ')
		response = response.lower()	
	if response == 'yes':
		print(color.CYAN + "\nOk, here's the next riddle.\n" + color.END)
		subprocess.run(["say", "-v", "Samantha", "Ok, here's the next riddle."])
		print(color.BOLD + riddle_dict['Question 2'] + color.END)
		time.sleep(2)
		answer2 = input('What is your answer? ')

	if answer2.lower() == 'seed':
		print(color.CYAN + "\nVery clever! Maybe you are pretty smart after all.  Plus 10 to your armor.\n"+ color.END)
		subprocess.run(["say", "-v", "Samantha", "Very clever! Maybe you are pretty smart after all.  Plus 10 to your armor."])
		correct_answers += 1
		user.get_armor(10)
		print('\n\n')
		user.print_armor_bar()
		print('\n\n')
		print(color.BOLD + 'Number of correct answers:' + color.END, correct_answers)
		time.sleep(2)
		if correct_answers == 2:
			print(color.CYAN + "That's two in a row, but even a broken clock is right twice a day. Let's continue." + color.END)
			subprocess.run(["say", "-v", "Samantha", "That's two in a row, but even a broken clock is right twice a day. Let's continue."])
	elif answer2.lower() != 'seed':
		print(color.CYAN + '\nWRONG!!! The answer was seed. Simon was right, you ARE useless. Minus 5 armor.\n' + color.END)
		subprocess.run(["say", "-v", "Samantha", "WRONG!!! The answer was seed. Simon was right, you ARE useless. Minus 5 armor."])
		user.lose_armor(5)
		print('\n\n')
		user.print_armor_bar()
		print('\n\n')
		print(color.BOLD + 'Number of correct answers:' + color.END, correct_answers)
		time.sleep(2)

#Question 2 finished
#========================================================================

	print(color.CYAN + '\nAre you ready for your third riddle?\n' + color.END)
	subprocess.run(["say", "-v", "Samantha", "Are you ready for your third riddle?"])
	response = input('Yes or No? ')
	response = response.lower()
	while response not in ['yes']:
		print(color.CYAN + "Don't be a coward" +color.END)
		subprocess.run(["say", "-v", "Samantha", "Don't be a coward"])
		response = input('Yes or No? ')
		response = response.lower()
	if response == 'yes':
		print(color.CYAN + "\nOk, Just a few more to go.\n" + color.END)
		subprocess.run(["say", "-v", "Samantha", "Ok, Just a few more to go."])
		print(color.BOLD + riddle_dict['Question 3'] + color.END)
		time.sleep(2)
		answer3 = input('What is your answer? ')

	if answer3.lower() == 'hole':
		print(color.CYAN + "\nHole-y crap! Very good answer. You've gained 15 intelligence points.\n" + color.END)
		subprocess.run(["say", "-v", "Samantha", "Wholly crap! Very good answer. You've gained 15 intelligence points."])
		correct_answers += 1
		user.get_smarter(15)
		print('\n\n')
		user.print_intel_bar()
		print('\n\n')
		print(color.BOLD + 'Number of correct answers:' + color.END, correct_answers)
		time.sleep(2)
		#if correct_answers == 2:
			#print(color.CYAN + "That's two in a row, but even a broken clock is right twice a day. Let's continue." + color.END)
		#subprocess.run(["say", "-v", "Samantha", "That's two in a row, but even a broken clock is right twice a day. Let's continue."])
		if correct_answers == 3:
			print(color.CYAN +"That's three in a row, your mother must be so proud of you!" + color.END)
			subprocess.run(["say", "-v", "Samantha", "That's three in a row, your mother must be so proud of you!"])
	elif answer2.lower() != 'hole':
		print(color.CYAN + '\nNo, the answer is "hole". Do you have a hole in your head? Minus 10 intelligence.\n' + color.END)
		subprocess.run(["say", "-v", "Samantha", "No, the answer is 'hole'. Do you have a hole in your head? Minus 10 intelligence."])
		user.get_dumber(10)
		print('\n\n')
		user.print_intel_bar()
		print('\n\n')
		print(color.BOLD + 'Number of correct answers:' + color.END, correct_answers)
		time.sleep(2)

#Question 3 ends
#========================================================================

	print(color.CYAN + "\nTime for the fourth question. Notice how I didn't ask if you were ready? It's because you don't have a choice. I still need you to type yes though.\n" + color.END)
	subprocess.run(["say", "-v", "Samantha", "Time for the fourth question. Notice how I didn't ask if you were ready? It's because you don't have a choice. I still need you to type yes, though."])
	response = input('Yes or No? ')
	response = response.lower()
	while response not in ['yes']:
		print(color.CYAN + "Don't be a coward" +color.END)
		subprocess.run(["say", "-v", "Samantha", "Don't be a coward"])
		response = input('Yes or No? ')
		response = response.lower()
	if response == 'yes':
		print(color.CYAN + "\nThanks!\n" + color.END)
		subprocess.run(["say", "-v", "Samantha", "Thanks!"])
		print(color.BOLD + riddle_dict['Question 4'] + color.END)
		time.sleep(2)
		answer4 = input('What is your answer? ')
		
	if answer4.lower() in ['cold', 'a cold']:
		print(color.CYAN + "\nThat's correct! Here's some extra health points. I don't want you getting the rest of us sick. 20 health points restored.\n" + color.END)
		subprocess.run(["say", "-v", "Samantha", "That's correct! Here's some extra health points. I don't want you getting the rest of us sick. 20 health points restored."])
		correct_answers += 1
		user.heal(20)
		print('\n\n')
		user.print_health_bar()
		print('\n\n')
		print(color.BOLD + 'Number of correct answers:' + color.END, correct_answers)
		time.sleep(2)
		if correct_answers == 4:
			print(color.CYAN +"Four in a row? I'm starting to worry about you. Maybe you should go outside. " + color.END)
			subprocess.run(["say", "-v", "Samantha", "Four in a row? I'm starting to worry about you. Maybe you should go outside."])
	elif answer4.lower() not in ['cold', 'a cold']:
		print(color.CYAN + "\nHa ha ha ha ha ha ha ha. That's so wrong. The answer was 'a cold'. Are you feeling sick? Maybe you should go lay down. Minus 10 health points.\n" + color.END)
		subprocess.run(["say", "-v", "Samantha", "Ha ha ha ha ha ha ha ha. That's so wrong. The answer was 'a cold'. Are you feeling sick? Maybe you should go lay down. Minus 10 health points."])
		user.injure(10)
		print('\n\n')
		user.print_health_bar()
		print('\n\n')
		print(color.BOLD + 'Number of correct answers:' + color.END, correct_answers)
		time.sleep(2)

#Question 4 ends
#========================================================================

	print(color.CYAN + "\nFinally, the last question. Let's hurry this up. I am supposed to be at the bar in 20 minutes. Type yes already!\n" + color.END)
	subprocess.run(["say", "-v", "Samantha", "Finally, the last question. Let's hurry this up. I am supposed to be at the bar in 20 minutes. Type yes already!"])
	response = input('Yes or No? ')
	response = response.lower()
	while response not in ['yes']:
		print(color.CYAN + "Don't be a coward" +color.END)
		subprocess.run(["say", "-v", "Samantha", "Don't be a coward"])
		response = input('Yes or No? ')
		response = response.lower()
	if response == 'yes':
		print(color.CYAN + "\nQuickly now, my beer is getting warm.\n" + color.END)
		subprocess.run(["say", "-v", "Samantha", "Quickly now, my beer is getting warm"])
		print(color.BOLD + riddle_dict['Question 5'] + color.END)
		time.sleep(2)
		answer5 = input('What is your answer? ')
		
	if answer5.lower() in ['needle', 'hurricane']:
		print(color.CYAN + "\nVery good! You should join us for a beer later. First drink is on me. Here's a healing potion.\n" + color.END)
		subprocess.run(["say", "-v", "Samantha", "Very good! You should join us for a beer later. First drink is on me. Here's a healing potion."])
		correct_answers += 1
		print_ascii.healthpotion_pic()
		print('\n\n')
		user.add_item('Healing Potion')
		print(color.BOLD + 'Number of correct answers:' + color.END, correct_answers)
		time.sleep(2)
		if correct_answers == 5:
			print(color.CYAN +"All five in a row? That's as impressive as it is sad! Congratulations anyway!" + color.END)
			subprocess.run(["say", "-v", "Samantha", "All five in a row? That's as impressive as it is sad! Congratulations anyway!"])
	elif answer5.lower() not in ['needle', 'hurricane']:
		print(color.CYAN + "\nThat was supposed to be a freebie. If there was one you were supposed to get right, this was it. Bless your heart child." + color.END)
		subprocess.run(["say", "-v", "Samantha", "That was supposed to be a freebie. If there was one you were supposed to get right, this was it. Bless your heart child."])
		print(color.BOLD + 'Number of correct answers:' + color.END, correct_answers)
		time.sleep(2)

#Question 5 ends
#========================================================================

	if correct_answers > 2:
		print(color.CYAN + "\nWow, you answered most of the riddles correctly! What an incredible achievement. Maybe you can put this on your résumé. As a reward for your intellectual cunning, I award you with a rare candy. Don't ask me what it does, Cedar found it under the couch." + color.END)
		subprocess.run(["say", "-v", "Samantha", "Wow, you answered most of the riddles correctly! What an incredible achievement. Maybe you can put this on your résumé. As a reward for your intellectual cunning, I award you with a rare candy. Don't ask me what it does, cedar found it under the couch"])
		print(color.BOLD + 'Plus 1 Rare Candy' + color.END)
		user.add_item('Rare Candy')
	elif correct_answers < 3:
		print(color.CYAN + "\nWell, you tried your best. I was going to give you a piece of rare candy, but I'll give it to Cedar instead. At least he got some of the questions right." + color.END)
		subprocess.run(["say", "-v", "Samantha", "Well, you tried your best. I was going to give you a piece of rare candy, but I'll give it to Cedar instead. At least he got some of the questions right"])
		time.sleep(2)
	print(color.CYAN + "\nBy the way, there was a weird man dressed in a wizard's robe staggering around on campus. I think he might be drunk. Anyway, you should go and talk to him." + color.END)
	subprocess.run(["say", "-v", "Samantha", "By the way, there was a weird man dressed in a wizard's robe staggering around on campus. I think he might be drunk. Anyway, you should go and talk to him"])

	input('Press enter to continue ')
