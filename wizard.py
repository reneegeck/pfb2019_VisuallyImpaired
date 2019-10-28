#!/usr/bin/env python3

import user 
import random 
import subprocess
import time

player = user.User('Horseshoe Crab', 100, 80, 50, 60, set(), dict())

def wizard_encounter(user):
	print('You stumbled on Simon the Wizard of Cold Spring Harbor')
	subprocess.run(["say","-v","Daniel","Hi! My name is Simon the Wizard of Cold Spring Harbor, I'm the ward of the magic book of Python3, do you want to get a potato beer at the Eagle?"]) 
	q1 = input('Yes or no?')
	while q1 not in ['yes','no']:
		print('What was that? Try again.')
		q1 = input('Yes or no?')	
	if q1.lower() == 'yes':
		print('Simon is getting a little tipsy')
		wizard_gift(user)
	else:
		print('Simon realized you are trying to steal his book dummy! Now roll a die to see if you can beat Simon!')
		wizard_gift(user)
	return q1

	
def wizard_gift(user):
	q2_ans_dict = {'room':0, 'pie':0}
	subprocess.run(["say","-v", "Daniel", "Simon is offering you a gift, do you want a mushroom from the Cold Spring Harbor forest or a cherry pie imported directly from Twedes Cafe"])
	q2 = input("A) MUSHROOM, B) CHERRY PIE")
	if q2.lower() == 'a':
		subprocess.run(["say","-v","Daniel","you are smart"])		
		q2_ans_dict['room'] +=1 
		print('You are tripping GOOOOOOOOOOOOD')
		if 'items' not in user.inventory.keys():
			user.inventory['items'] = list()
		user.add_item('Third Eye')
		user.get_smarter(50)
		print('Wow, that mushroom made you:') 
		user.print_user_stats() 
		user.list_items()
		print('And you aquired the key to the gate that leads to inner realms of higher consciousness')
	else:
		q2_ans_dict['pie'] +=1
		subprocess.run(["say","-v","Daniel","you had indigestion of cherry pie and will spend 50 minutes in the wizard's toilet.. and there is no toilet paper!"])
		user.injure(10)
		time.sleep( 10 ) 
		print('blinking toilet')
		
def wizard_fight(user):
	success = 0
	for i in range(10):
		print(success.random.sample(range(10), 1))
		if success == range(0,2):
			user.injure(30)
			print('You barely made it, no book thoough...')
			print(user.print_user_stats())
			subprocess.run(["say", "-v", "Daniel", "Simon knocked you out, you are out of shape, less coding and more running"])
			if user.health < 26 and 'healing potion' in user.inventory['items']:
				print("Hmm looks like you aren't doing so great.")
				heal_choice = input('Do you wan to drink your healing potion? ')
				heal_choice = heal_choice.lower()
				while heal_choice not in ['yes', 'no']:
					print("What did you say? Let's try again.")
					heal_choice = input('Do you wan to drink your healing potion? ')
				if heal_choice == 'yes':
					user.health =+ 30
					print('Ahhh. How refreshing. Tastes like strawberries. Much better.')
					subprocess.run(["say","-v","Daniel","Much better"])
		elif success == range(3,5):
			user.injure(10)
			print('You made it ok, no book though...') 
			print(user.print_user_stats())
			if user.health < 26 and 'healing potion' in user.inventory['items']:
				print("Hmm looks like you aren't doing so great.")
				heal_choice = input('Do you wan to drink your healing potion? ')
				heal_choice = heal_choice.lower()
				while heal_choice not in ['yes', 'no']:
					print("What did you say? Let's try again.")
					heal_choice = input('Do you wan to drink your healing potion? ')
				if heal_choice == 'yes':
					user.health =+ 10
					print('Ahhh. How refreshing. Tastes like strawberries. Much better.')	
					subprocess.run(["say","-v","Daniel","Much better"])
		elif success == range(6,8):
			user.get_smarter(30)
			if 'items' not in user.inventory.keys():
				user.inventory['items'] = list()
			user.add_item('Python2')
			subprocess.run(["say","-v","Daniel","You are novice! That's embarassing"])
			print('You are novice! You stole the wrong book: the book of Python2! You are:')
			print(user.print_user_stats())
			print('And you have:')
			print(user.inventory['items'])
			if 'Python2' in self.inventory['items']:
				input('Do you want to try to upgrade to Python3? A) Yes B) No')
				if q1.lower() == 'yes':
					subprocess.run(["say", "-v", "Daniel", "GET READY FOR THE ULTIMATE SWAN FIGHT!"])
					print("THE ULTIMATE SWAN FIGHT!") 
				else:
					subprocess.run(["say", "-v", "Daniel", "you are lazy"])
		elif success == range(9,10):
			user.get_smarter(50)
			if 'items' not in user.inventory.keys():
				user.inventory['items'] = list()
			user.add_item('Python3')
			subprocess.run(["say","-v","Daniel","You are fine burglar! Yayyyyyyyyy"])
			print('You have the mistic powers of Python3 scripting! You are:')
			print(user.print_user_stats())
			print('And you have:')
			print(user.inventory['items'])

wizard_encounter(user)
