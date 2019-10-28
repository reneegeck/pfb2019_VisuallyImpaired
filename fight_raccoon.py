#!/usr/bin/env python3

import user
import random

#===========================================

def attack_coon(weapon):

	if player.health < 26 and 'healing potion' in player.inventory['items']:
		print("Hmm looks like you aren't doing so great.")
		heal_choice = input('Do you wan to drink your healing potion? ')
		heal_choice = heal_choice.lower()
		while heal_choice not in ['yes', 'no']
			print("What did you say? Let's try again.")
			heal_choice = input('Do you wan to drink your healing potion? ')
		if heal_choice == 'yes':
			player.health =+ 50
			print('Ahhh. How refreshing. Tastes like strawberries. Much better.')

	if weapon == 'sword':
		hit = random.randint(5,150)
		try_points = random.randint(5,30)
	elif weapon = 'axe':
		hit = random.randint(5,150)
		try_points = random.randint(10,40)
	else: #otherwise dagger
		hit = random.randint(10,180)
		try_points = random.randint(5,25)

	if hit < 50: #coon hit class 50
		print('You swing, but are a little overenthusiastic, and miss the raccoon.')
		points = 0
	else: #you get a high number
		print('Nicely done! You hit it!')
		if try_points < 25: #good hit 
			print('The raccoon dodges away but you still draw some blood.')
		elif hit > 145 or try_points > 29 and 'weapon master' not in player.status
			print('Impressive hit! You have gained the status WEAPON MASTER.'
			player.status.add('weapon master')
		else: #you get a really good hit
			print('Wow! You hit that raccoon pretty hard.')
	
	points = try_points
	
	return points

#============================================

def coon_attacks():
	hit = random.randint(10-120)
	if hit < player.armor: #if below armor class
		print('The raccoon swipes at you but misses.')
		points = 0
	else: #it hit, now determine damage
		points = random.randint(5-25)
		print('Oh no! The raccoon catches you with his dagger claws')
	return points

#==========================================

def choose_fight():
	choice = input('Yes or no? ')
	choice = choice.lower()
	while choice not in ['yes', 'no']:
		print('What did you say?')
		choice = input('Yes or no? ')
	if choice == 'yes':
		True
	elif choise == 'no':
		False
	return

#==============================================

def pick_weapon_fight():
	if len(player.inventory[weapons]) < 2:
		weapon_used = player.inventory[weapons] #WILL THIS REFERENCE ONLY ITEM IN SET??
		print('You have a', weapon_used, 'so you will fight with that.')
	else:
		print('Time to choose a weapon! You have:')
		weapons_string = ','.join(str(set_item) for set_item in player.inventory[weapons])
		print(weapons_string)
		weapon_used = input('Which do you want to use? ')
		weapon_used = weapon_used.lower()
		while weapon_used not in player.inventory['weapons']:
			print("Hmm that doesn't seem to be a weapon you have...Let's try again.")
			weapon_used = input('Which weapon do you want to use? ')
	return weapon_choice

#================================================

#text about the encounter

print('That raccoon looks pretty intimidating. Are those wolverine claws? Damn. A formidable opponent for certain.')
#PRINT THE RACCOON ASCII IMAGE

#pick a weapon
weapon = pick_weapon_fight()

#Initialize the raccoon
coon_health = 50

#Initialise the fight loop
fight_choice = True
while fight_choice == True:
	
	#fight the raccoon
	coon_damage = attack_coon(weapon)
	coon_health -= coon_damage
	if coon_health < 1:
		print('That was too much for this raccoon. He passes out where he stands.')
		print("Huh. He looks much less scary when he's asleep.")
		#PRINT SLEEPING RACCOON ASCII ART
	
	#raccoon fights you
	player_damage = coon_attacks()
	player.health -= player_damage
	
	#do you want to keep fighting
	print('Do you want to attack the raccoon again?'
	fight_choice = choose_fight()
	continue #DO I NEED TO TELL IT TO KEEP GOING THROUGH WHILE LOOP?






