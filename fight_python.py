#!/usr/bin/env python3

import user
import random
import time
import print_ascii
import os
import subprocess

#===========================================

def attack_python(user, weapon):

	#make response possibilities
	pyth_injured = ['The PYTHON dodges away but you still draw some blood.', "The PYTHON hisses in anger after your blow. Hope it's not venomous.","You draw some blood but the PYTHON hardly seems to notice."]
	pyth_severe_inj = ["Ow. That PYTHON isn't looking so good now.", "Wow! You hit that PYTHON pretty hard.", "The PYTHON sways back after the strength of your blow."]
	user_miss = ["You swing, but it bounces right off the PYTHON's scales.", "The PYTHON sways away and your swing misses.", "You hit the ground instead of the PYTHON. Maybe try to aim next time?"]

	#optional healing
	if user.health < 26 and 'Healing Potion' in user.inventory['items']: #if you still have some
		print("Hmm looks like you aren't doing so great.")
		print('Do you want to drink your healing potion?')
		heal_choice = input('Yes or no? ')
		heal_choice = heal_choice.lower()
		while heal_choice not in ['yes', 'no']:
			print("What did you say? Let's try again.")
			heal_choice = input('Do you want to drink your healing potion? ')
		if heal_choice == 'yes':
			user.heal(50)
			user.remove_item('Healing Potion')
			print('Ack that tasted worse than the free coffee. At least you feel more alert now.')
			user.print_health_bar()
			time.sleep(2)
			print('\n\n')
	if user.health < 26 and "Rare Candy" in user.inventory['items']: #if you got Rare candy from riddles
		print("Hmm looks like you aren't doing so great.")
		print('Do you want to eat your rare candy?')
		candy_choice = input('Yes or no? ')
		candy_choice = candy_choice.lower()
		while candy_choice not in ['yes', 'no']:
			print("What did you say? Let's try again.\nDo you want to eat your rare candy?")
			candy_choice = input('Yes or no? ')
		if candy_choice == 'yes':
			user.heal(30)
			user.remove_item('Rare Candy')
			print('Wow that was declicious and magical. You feel rejuvenated.')
			user.print_health_bar()
			time.sleep(2)
			print('\n\n')

	#weapons determine hit scores
	if weapon == 'sword':
		hit = random.randint(5,150)
		try_points = random.randint(5,30)
	elif weapon == 'axe':
		hit = random.randint(5,150)
		try_points = random.randint(10,40)
	else: #otherwise dagger
		hit = random.randint(10,180)
		try_points = random.randint(5,25)
	
	#account for things gained in previous modules
	if 'weapon master' in user.status:
		hit_bonus = 5 
	else:
		hit_bonus = 0
	if 'Python3' in user.inventory['items']:
		dmg_bonus = 5
	elif 'Python2' in user.inventory['items']:
		dmg_bonus = 2
	else:
		dmg_bonus = 0
	hit += hit_bonus
	try_points += dmg_bonus

	#now attack the python
	if hit < 70: #python hit class 70
		rand_user_miss = random.randint(0,2)
		print('\n\n')
		print(user_miss[rand_user_miss])
		points = 0
	else: #you get a high number
		print('\n\nNicely done! You hit it!\n\n')
		if try_points < 28: #good hit 
			rand_pyth_inj = random.randint(0,2)
			print(pyth_injured[rand_pyth_inj])
		else: #you get a really good hit
			rand_pyth_sev = random.randint(0,2)
			print(pyth_severe_inj[rand_pyth_sev])
		points = try_points
	
	return points

#============================================

def pyth_attacks(user):

	#make some response options
	pyth_miss = ["The PYTHON darts towards you but misses.", "You feel its fangs pass over your head, but they don't hit. Lucky you!", "Its fangs graze you, but don't draw blood. Safe - for now. Unless it's poisonous..."]
	pyth_hit = ["Oh no! The PYTHON stabs you with its fangs!","Ow, that hurt. Watch out for those fangs!","The python squeezes you, crushing the breath out of your fragile body. Ouch."]

	hit = random.randint(10,120)
	protect_bonus = 0
	if 'Third Eye' in user.inventory['items']:
		protect_bonus += 5
	if user.speed > 80:
		protect_bonus += 3
	if hit < user.armor: #if below armor class
		rand_miss = random.randint(0,2)
		print(pyth_miss[rand_miss])
		points = 0
	else: #it hit, now determine damage
		points = random.randint(5,25) - protect_bonus
		if points in range(1,25):
			rand_hit = random.randint(0,2)
			print(pyth_hit[rand_hit])
		else: #otherwise there was no damage
			points = 0
			print('Nice! Your special powers protected you from the blow!')
	return points

#==========================================

def pick_weapon_fight(user):
	if len(user.inventory['weapons']) < 2:
		for item in user.inventory['weapons']:
			weapon_used = item
		print('You have a', weapon_used, 'so you will fight with that.')
	else:
		print('Time to choose a weapon! You have:')
		weapons_string = ', '.join(str(set_item) for set_item in user.inventory['weapons'])
		print(weapons_string)
		weapon_used = input('Which do you want to use? ')
		weapon_used = weapon_used.lower()
		while weapon_used not in user.inventory['weapons']:
			print("Hmm that doesn't seem to be a weapon you have...Let's try again.")
			weapon_used = input('Which weapon do you want to use? ')
		print('Okay! You will fight with your', weapon_used +'.')
	return weapon_used

#===============================================
#ACTUAL FIGHT

def python_fight(player):
	os.system('clear')
	print("And then you see it\n\n")
	time.sleep(2)
	print("What you've been looking for this whole time\n\n")
	time.sleep(2)
	print_ascii.scary_python_pic()
	time.sleep(2)
	print("\n\nTHE PYTHON\n\n")
	time.sleep(3)
	print("You both know that there is only one reason you are here.\n\n")
	time.sleep(2)
	print("To battle and prove your worth to the PYTHON.\n\n")
	time.sleep(4)
	
	input('Press any key to continue.\n\n')
	
	#Go through inventory and repot what helpful things you have
	print("First, you recall what you have learned.\n\n")
	time.sleep(2)
	item_list = ["Python3", "Python2", "Linux Book", "Third Eye"]
	if 'Python3' in player.inventory['items']:
		print('You received training in Python3 from Simon the Wizard, so you get bonus damage points again the PYTHON!\n\n')
		time.sleep(4)
	elif 'Python2' in player.inventory['items']:
		print('You received training in Python2, which is a bit out of date but you still get some bonus damage points against the PYTHON.\n\n')
		time.sleep(4)
		print("At least you're not trying to use Perl.\n\n")
		time.sleep(2)
	elif any(item in player.inventory['items'] for item in item_list):	
		print("Wait you never even installed Python?\n\n")
		time.sleep(2)
		print("You're still using Perl?\n\n")
		time.sleep(2)
		print("Too late to back out now. Give it your best effort!\n\n")
		time.sleep(3)
	else:
		print('Unfortunately, not much.\n\n')
		time.sleep(2)
		print("Too late to back out now! Give it your best effort!\n\n")
		time.sleep(2)
	
	if 'weapon master' in player.status:
		print("You received the status of Weapon Master for your impressive hit against the raccoon!\n\n")
		time.sleep(3)
		print("You get bonus hit points against the PYTHON!\n\n")
		time.sleep(2)

	if 'Third Eye' in player.inventory['items']:
		print("You received a Third Eye that gives you exceptional perception.\n\n")
		time.sleep(3)
		print("It protects you from some of the damage the PYTHON may inflict!\n\n")
		time.sleep(3)

	if 'Linux Book' in player.inventory['items']:
		print("You learned Linux from the book you got from the raccoon!\n\n")
		time.sleep(2)
		print("Now you know how to start, and get to begin your battle with the PYTHON!\n\n")
		time.sleep(3)

	#pick a weapon
	weapon = pick_weapon_fight(player)
	print('\n\n')
	if weapon == 'sword':
		print_ascii.sword_pic()
	elif weapon == 'axe':
		print_ascii.axe_pic()
	else:
		print_ascii.dagger_pic()
	time.sleep(2)
	print('\n\n')

	#start the fight
	pyth_health = 100

	print('Are you ready to fight the PYTHON?')
	fight_yes = input('Say yes! ')
	fight_yes = fight_yes.lower()
	while fight_yes not in ['yes']: #too bad you have to fight it!
		print("Kind of late for second thoughts.")
		print("You really don't have a choice at this point.")
		fight_yes = input('Are you ready to fight the PYTHON? Say yes! ')
		fight_yes = fight_yes.lower()

	print('\n\n')
	player.print_health_bar()
	print('\n\n')
	time.sleep(2)

	#if you have Linux book you go first	
	if 'Linux Book' in player.inventory['items']:
		print("Since you won the Linux book from the raccoon, you are prepared for this fight!\n\n")
		time.sleep(1)
		print("You get to attack first!")
		time.sleep(2)
		attack_python(player, weapon)
		time.sleep(2)
		print("\n\nNow it is the PYTHON'S turn to attack!\n\n")
		time.sleep(2)
	else:
		print("The PYTHON is prepared and strikes first!\n\n")
		time.sleep(2)

	#Initialize the fight loop
	while pyth_health > 0 and player.health > 0:

		#python attacks
		injure_points = pyth_attacks(player)
		player.injure(injure_points)
		time.sleep(2)
		if player.health < 1:
			break
		print('\n\n')
		player.print_health_bar()		
		print('\n\n')

		time.sleep(2)
		go_on = input("Okay, now it's your turn! Are you ready? Say yes! ")
		while go_on.lower() not in ['yes']:
			print("You're committed now. Keep going!\n\n")
			go_on = input("Are you ready? Say yes! ")
		time.sleep(1)

		pyth_damage = attack_python(player, weapon)
		pyth_health -= pyth_damage
		if pyth_health < 1:
			break
		time.sleep(2)
		print("\n\nNow it is the PYTHON'S turn to attack!\n\n")
		time.sleep(2)

	if pyth_health <= 0:
		#print about winning
		time.sleep(2)
		print('\n\nCongratulations! The PYTHON concedes and bows to you.\n\n')
		time.sleep(2)
		print_ascii.cute_python_pic()
		time.sleep(4)
		print("Simon and Sofia look on respectfully.\n\n")
		time.sleep(1)
		subprocess.run(['say', '-v', 'Daniel', 'Well done!'])
		subprocess.run(['say', '-v', 'Samantha', 'Great job!'])
		print("Maybe they will ask you to TA next year...\n\n")
		time.sleep(3)
		print("Triumphant, you saunter off to the bar. You deserve a beer.\n\n")
		time.sleep(2)
		print_ascii.beer_pic()
		time.sleep(3)
		os.system('clear')
		print('\n\n\n\n')
		print_ascii.end_pic()
	else: #otherwise you died
		print("\n\nSo close, yet so far.\n\n")
		time.sleep(1)
		print("Better luck next time!")
