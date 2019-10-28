#!/usr/bin/env python3

import user
import random
import time
import print_ascii

#===========================================

def attack_coon(user, weapon):

	#make response possibilities
	coon_injured = ['The raccoon dodges away but you still draw some blood.', "The raccoon hisses in anger after your blow. Hope it's not rabid.","You draw some blood but the raccoon hardly seems to notice."]
	coon_severe_inj = ["Ow. That raccoon isn't looking so good now.", "Wow! You hit that raccoon pretty hard.", "The raccoon staggers after the strength of your blow. Poor thing, I think it might have distemper."]
	user_miss = ['You swing, but are a little overenthusiastic, and miss the raccoon.', "The raccoon dodges away and your swing misses.", "You hit the ground instead of the raccoon. Maybe try to aim next time?"]

	if user.health < 26 and 'Healing Potion' in user.inventory['items']:
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
			print('Ahhh. How refreshing. Tastes like strawberries. Much better.')
			print('Your health is now ', user.health, '/100.', sep='')
			time.sleep(2)
			print('\n\n')

	if weapon == 'sword':
		hit = random.randint(5,150)
		try_points = random.randint(5,30)
	elif weapon == 'axe':
		hit = random.randint(5,150)
		try_points = random.randint(10,40)
	else: #otherwise dagger
		hit = random.randint(10,180)
		try_points = random.randint(5,25)

	if hit < 50: #coon hit class 50
		rand_user_miss = random.randint(0,2)
		print(user_miss[rand_user_miss])
		points = 0
	else: #you get a high number
		print('Nicely done! You hit it!')
		if try_points < 25: #good hit 
			rand_coon_inj = random.randint(0,2)
			print(coon_injured[rand_coon_inj]) #print one of the statements where you hit the coon
		elif hit > 145 or try_points > 29 and 'weapon master' not in user.status:
			print('Impressive hit! You have gained the status WEAPON MASTER.')
			user.add_status('weapon master')
		else: #you get a really good hit
			rand_coon_sev = random.randint(0,2)
			print(coon_severe_inj[rand_coon_sev])
		points = try_points
	
	return points

#============================================

def coon_attacks(user):

	#make some response options
	coon_miss = ["The raccoon swipes at you but misses.", "You feel its dagger claws pass over your head, but they don't hit. Lucky you!", "It seems like raccoon tried to take a swipe at you, but it looks more like it did a pirouette. Safe - for now."]
	coon_hit = ["Oh no! The raccoon catches you with his dagger claws.","Ow, that hurt. Watch out for those claws!","You stagger back from the raccoon's blow. Ouch."]

	hit = random.randint(10,120)
	if hit < user.armor: #if below armor class
		rand_miss = random.randint(0,2)
		print(coon_miss[rand_miss])
		points = 0
		print('Your health is still ', user.health, '/100.', sep='')
	else: #it hit, now determine damage
		points = random.randint(5,25)
		rand_hit = random.randint(0,2)
		print(coon_hit[rand_hit])
		print('Your health is now ', user.health-points, '/100.', sep='')
	return points

#==========================================

def choose_fight(user):
	choice = input('Yes or no? ')
	choice = choice.lower()
	while choice not in ['yes', 'no']:
		print('What did you say?')
		choice = input('Yes or no? ')
	if choice == 'yes':
		fight_choice = True
	elif choice == 'no':
		fight_choice = False
	return fight_choice

#==============================================

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

def raccoon_fight(player):
	print_ascii.raccoon_pic()
	print('That raccoon looks pretty intimidating. Are those wolverine claws? Damn. A formidable opponent for certain.')
	time.sleep(3)
	print('\n\n')

	#pick a weapon
	weapon = pick_weapon_fight(player)
	time.sleep(2)
	print('\n\n')

	#Initialize the raccoon
	coon_health = 40

	#Initialise tihe fight loop

	print('Okay! Time to fight!')
	print('Remember you have ', player.health,'/100 health.', sep='')
	time.sleep(2)
	print('\n\n')

	fight_choice = True
	while fight_choice == True:

		#fight the raccoon
		coon_damage = attack_coon(player, weapon)
		coon_health -= coon_damage
		if coon_health < 1:
			print_ascii.sleepy_raccoon_pic()
			print('That was too much for this raccoon. He passes out where he stands.')
			print("Huh. He looks much less scary when he's asleep.")
			time.sleep(3)
			print("\n\nBut wait! What's that behind the raccoon?\n\n")
			print('LINUX BOOK ASCII HERE')
			print("\n\nA Linux book, cool! That will come in handy later.")
			player.add_item('Linux Book')
			time.sleep(3)
			fight_choice = False
			break

		time.sleep(2)
		print('\n\n')
		coon_attack_say = ['Uh oh, looks like the raccoon is going to take a swipe at you now!', "You can't run away yet! The raccoon is angry...", "Wow that raccoon is pissed. It goes on the offensive."]
		rand_coon_say = random.randint(0,2)
		print(coon_attack_say[rand_coon_say])
		print('\n\n')
		time.sleep(2)
	
		#raccoon fights you
		player_damage = coon_attacks(player)
		player.injure(player_damage)

		print('\n\n')
		time.sleep(2)
	
		#do you want to keep fighting
		print('Do you want to attack the raccoon again?')
		fight_choice = choose_fight(player)

		print('\n\n')
		time.sleep(2)

	print('Now, on to the next adventure!')
