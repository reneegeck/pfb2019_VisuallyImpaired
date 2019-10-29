#!/usr/bin/env python3

import user, os, random, subprocess, time 
from print_wizard import decode, input1, input2, input3
from animate_dice import blinking_dice
from print_ascii import wizard_pic, swan_pic, mushroom_pic, pie_pic
#user = user.User('Horseshoe Crab', 100, 80, 50, 60, set(), dict())

	
def wizard_gift(user):
	print("Simon is getting a little tipsy! \n Simon is offering you a gift, do you want a mushroom from the Cold Spring Harbor forest or a cherry pie imported directly from Twedes Cafe")
	subprocess.run(["say","-v", "Daniel", "Simon is getting a little tipsy! Simon is offering you a gift, do you want a mushroom from the Cold Spring Harbor forest or a cherry pie imported directly from Twedes Cafe"])
	q2 = input1('')
	q2 = q2.lower()
	while q2.lower() not in ['a','b']:
		q2 = input2('')
	if q2.lower() == 'a':
		mushroom_pic()
		print("You are smart and you are tripping GOOOOOOOOOOOOD")
		subprocess.run(["say","-v","Daniel","you are smart and you are tripping GOOOOOOOOOOOOD"])		
		user.add_item('Third Eye')
		user.get_smarter(50)
		print('Wow, that mushroom made you:')
		user.print_health_bar() 
		user.print_intel_bar()
		user.list_items()
		print("And you aquired the key to the gate that leads to inner realms of higher consciousness, hope you have a great time in the next level")
		subprocess.run(["say","-v","Daniel","And you aquired the key to the gate that leads to inner realms of higher consciousness, hope you have a great time in the next level"])
	else:
		pie_pic()
		print("you had indigestion of cherry pie and will spend 50 minutes in the wizard's toilet.. and there is no toilet paper!")
		subprocess.run(["say","-v","Daniel","you had indigestion of cherry pie and will spend 50 minutes in the wizard's toilet.. and there is no toilet paper!"])
		user.injure(30)
		time.sleep( 10 )
		user.print_health_bar()
		user.print_intel_bar()
		print("Sorry there was no toilet paper, do you want a camomille?")
		subprocess.run(["say","-v", "Daniel", "Sorry there was no toilet paper, do you want a camomille?"])
		q3 = input3('')
		q3 = q3.lower()
		while q3.lower() not in ['yes']:
			print('What was that? Try again.')
			subprocess.run(["say","-v","Daniel","What was that? Try again."])
			q3 = input3('')
		if q3.lower()  == 'yes':
			user.heal(20)
			print("I see you feel way better now, you can go to the next level now")
			subprocess.run(["say","-v","Daniel","I see you feel way better now, you can go to the next level now"])
			user.print_health_bar()
			user.print_intel_bar()
	return user	
	
def wizard_fight(user):
	subprocess.run(["say","-v", "Daniel", "Getting rolling"])
	blinking_dice()
	success = random.randint(1, 10)
	print(success)
	if success in range(0,3):
		user.injure(30)
		print("You barely made it, no book thoough...")
		subprocess.run(["say","-v", "Daniel", "You barely made it, no book thoough..."])
		user.print_health_bar()
		user.print_intel_bar()
		print("Simon the wizard knocked you out, you are out of shape, less coding and more running")
		subprocess.run(["say", "-v", "Daniel", "Simon the wizard knocked you out, you are out of shape, less coding and more running"])
		if user.health < 26 and 'Healing Potion' in user.inventory['items']:
			print("Hmm looks like you aren't doing so great.Do you wan to drink your healing potion?")
			subprocess.run(["say","-v", "Daniel", "Hmm looks like you aren't doing so great.Do you wan to drink your healing potion?"])
			heal_choice = input3('')
			heal_choice = heal_choice.lower()
			while heal_choice.lower() not in ['yes']:
				print("What did you say? Let's try again.Do you wan to drink your healing potion?")
				subprocess.run(["say","-v","Daniel","What did you say? Let's try again.Do you wan to drink your healing potion?"])
				heal_choice = input3('')
			if heal_choice.lower() == 'yes':
				user.heal(30)
				subprocess.run(["say","-v","Daniel","Ahhh. How refreshing. Tastes like strawberries. Much better. You are ready for the next level"])
				user.print_health_bar()
				user.print_intel_bar()
		if user.health > 26:
			print("you loose few health points, do you fancy a restoring lavander tea?")
			subprocess.run(["say","-v", "Daniel", "you loose few health points, do you fancy a restoring lavander tea?"])
			heal_choice = input3('')
			heal_choice = heal_choice.lower()
			while heal_choice.lower() not in ['yes']:
				print("What did you say? Let's try again. Fancy a lavander tea?")
				subprocess.run(["say","-v", "Daniel", "What did you say? Let's try again. Fancy a lavander tea?"])
				heal_choice = input3('')
			if heal_choice.lower() == 'yes':
				user.heal(10)
				print("Ahhh. How refreshing. Tastes like flowers. Much better. You are ready for the next level")
				subprocess.run(["say","-v","Daniel","Ahhh. How refreshing. Tastes like flowers. Much better. You are ready for the next level"])
				user.print_health_bar()
				user.print_intel_bar()
	elif success in range(3,5):
		user.injure(10)
		print('You made it ok, no book though...Simon kicks you to the next level') 
		subprocess.run(["say", "-v", "Daniel", "You made it ok, no book though... Simon kicks you to the next level"])
		user.print_health_bar()
		user.print_intel_bar()
		if user.health < 26 and 'Healing Potion' in user.inventory['items']:
			print("Hmm looks like you aren't doing so great. Do you wan to drink your healing potion?")
			subprocess.run(["say","-v", "Daniel", "Hmm looks like you aren't doing so great. Do you wan to drink your healing potion?"])
			heal_choice = input3('')
			heal_choice = heal_choice.lower()
			while heal_choice.lower() not in ['yes']:
				print("What did you say? Let's try again.Do you wan to drink your healing potion?")
				subprocess.run(["say","-v", "Daniel", "What did you say? Let's try again.Do you wan to drink your healing potion?"])
				heal_choice = input3('')
			if heal_choice.lower() == 'yes':
				user.heal(10)
				print("Ahhh. How refreshing. Tastes like strawberries. Much better. Now you are ready for the next level")
				subprocess.run(["say","-v","Daniel","Ahhh. How refreshing. Tastes like strawberries. Much better. Now you are ready for the next level"])
	elif success in range(5,8):
		user.get_smarter(30)
		user.add_item('Python2')
		print("You are novice! That's embarassing. You stole the wrong book: the book of Python2")
		subprocess.run(["say","-v","Daniel","You are novice! That's embarassing.You stole the wrong book: the book of Python2"])
		print('You are:')
		user.print_health_bar()
		user.print_intel_bar()
		print('And you have:')
		print(user.inventory['items'])
		if 'Python2' in user.inventory['items']:
			print("Do you want to try to upgrade to Python3?")
			subprocess.run(["say","-v","Daniel","Do you want to try to upgrade to Python3?"])
			q4 = input3('')
			q4 = q4.lower()
			while q4.lower() not in ['yes', 'no']:
				print("Do you want to try to upgrade to Python3?")
				subprocess.run(["say","-v","Daniel","Do you want to try to upgrade to Python3?"])
			if q4.lower() == 'yes':
				subprocess.run(["say", "-v", "Daniel", "GET READY FOR THE ULTIMATE SWAN FIGHT!"])
				print("THE ULTIMATE SWAN FIGHT!")
				print("    THE ULTIMATE SWAN FIGHT!")
				print("        THE ULTIMATE SWAN FIGHT!")
				print("            THE ULTIMATE SWAN FIGHT!")
				print("                THE ULTIMATE SWAN FIGHT!")
				swan_pic()
				if 'Bread' in user.inventory['items']:
					print("I think swans like bread, do you want to feed it to the swan?")
					subprocess.run(["say","-v","Daniel","I think swans like bread, do you want to feed it to the swan?"])
					q5 = input3('')
					q5 = q5.lower()
					while q5.lower() not in ['yes', 'no']:
						print("I think swans like bread, do you want to feed it to the swan?")
						subprocess.run(["say","-v","Daniel","I think swans like bread, do you want to feed it to the swan?"])
					if q5.lower() == 'yes':
						print("The swan appreciates the bread. Now you have upgraded to the newest Python3, you are 50 point smarter and you are ready for the next level")
						subprocess.run(["say","-v","Daniel","the swan appreciates the bread. Now you have upgraded to the newest python3, you are 50 point smarter and you are ready for the next level "])
						user.get_smarter(50)
						user.add_item('Python3')
						user.print_health_bar()	
						user.print_intel_bar()
					else:
						print("The swan bite you and you are running away, go to the next level")
						subprocess.run(["say","-v","Daniel","the swan bite you and you are running away, go to the next level"])
						user.print_health_bar()
						user.print_intel_bar()
				else:
					blinking_dice()
					success = random.randint(1, 6)
					print(success)
					if success in range(0,3):
						print("You were unprepared, the swan bite you and you lost 30 health points. You are running away, go to the next level")
						subprocess.run(["say","-v","Daniel","You were unprepared, the swan bite and you lost 30 health points. You are running away, go to the next level"])
						user.injure(30)
						user.print_health_bar()
						user.print_intel_bar()
					else:
						print("You won the battle, you are 50 point smarter and you have upgraded to the newest Python3, good luck in the next level")	
						subprocess.run(["say","-v","Daniel","You won the battle, you are 50 point smarter and you have upgraded to the newest Python3, good luck in the next level"])
						user.get_smarter(50)
						user.add_item('Python3')
						user.print_health_bar()
						user.print_intel_bar()
			else:
				print("You are lazy, you loose 10 speed and 10 intelligence points, try harder next time! Goodbye, go to the next level")
				subprocess.run(["say", "-v", "Daniel", "you are lazy, you loose 10 speed and 10 intelligence points, try harder next time! Goodbye, go to the next level"])
				user.get_slower(10)
				user.get_dumber(10)
				user.print_health_bar()
				user.print_intel_bar()
				user.print_speed_bar()
	elif success in range(8,11):
		user.get_smarter(50)
		user.add_item('Python3')
		print("You are fine burglar! You have the mistic powers of Python3 scripting! Now you are 50 point smarter andyou are ready for the next level")
		subprocess.run(["say","-v","Daniel","You are fine burglar! You have the mistic powers of Python3 scripting! Now you are 50 point smarter andyou are ready for the next level"])
		print('Yayyyyyyyyy! You are:')
		user.print_health_bar()
		user.print_intel_bar()
		print('And you have:')
		print(user.inventory['items'])
	return user

def wizard_encounter(user):
	os.system('clear')
	print('You stumbled on Simon the Wizard of Cold Spring Harbor')
	subprocess.run(["say", "-v", "Samantha", "You stumbled on Simon the Wizard of Cold Spring Harbor"])
	print("\n")
	wizard_pic()
	print("Hi! My name is Simon the Wizard of Cold Spring Harbor, I'm the ward of the magic book of Python3, do you want to get a potato beer at the Eagle?")
	subprocess.run(["say","-v","Daniel","Hi! My name is Simon the Wizard of Cold Spring Harbor, I'm the ward of the magic book of Python3, do you want to get a potato beer at the Eagle?"])
	q1 = input3('')
	q1 = q1.lower()
	while q1.lower() not in ['yes','no']:
		print("What was that? Try again.")
		subprocess.run(["say","-v","Daniel","What was that? Try again."])
		q1 = input3('')
	if q1.lower() == 'yes':
		wizard_gift(user)
	else:
		print('Simon realized you are trying to steal his book dummy! Now roll a die to see if you can beat Simon!')
		subprocess.run(["say","-v","Daniel","Simon realized you are trying to steal his book dummy! Now roll a die to see if you can beat Simon!"])
		wizard_fight(user)
	return q1

#wizard_encounter(user)
