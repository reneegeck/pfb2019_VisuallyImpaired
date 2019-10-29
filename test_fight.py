#!/usr/bin/env python3

import user
import random
import fight_python
import time
import print_ascii

player = user.User('HorseshoeCrab', 100, 40, 50, 60, set(), {})
player.inventory['weapons'] = set()
player.add_weapon('axe')
player.add_weapon('sword')
player.inventory['items'] = ['Linux Book']
player.status = set()

fight_python.python_fight(player)

print('OK we are out of the fight function now.')
'''
print_ascii.raccoon_pic()
print('That raccoon looks pretty intimidating. Are those wolverine claws? Damn. A formidable opponent for certain.')
time.sleep(3)
print('\n\n')

#pick a weapon
weapon = fight_raccoon.pick_weapon_fight(player)
time.sleep(3)
print('\n\n')

#Initialize the raccoon
coon_health = 70

#Initialise tihe fight loop

print('Okay! Time to fight!')
print('Remember you have ', player.health,'/100 health.', sep='')
time.sleep(3)
print('\n\n')

fight_choice = True
while fight_choice == True:

  #fight the raccoon
	coon_damage = fight_raccoon.attack_coon(player, weapon)
	coon_health -= coon_damage
	if coon_health < 1:
		sleepy_raccoon_pic()
		print('That was too much for this raccoon. He passes out where he stands.')
		print("Huh. He looks much less scary when he's asleep.")
		time.sleep(3)
		print("\n\nBut wait! What's that behind the raccoon?")
		#print Linux book art
		print("A Linux book, cool! That will come in handy later.")
		player.add_item('Linux Book')
		fight_choice = False
		break

	time.sleep(3)
	print('\n\n')
	coon_attack_say = ['Uh oh, looks like the raccoon is going to take a swipe at you now!', "You can't run away yet! The raccoon is angry...", "Wow that raccoon is pissed. It goes on the offensive."]
	rand_coon_say = random.randint(0,2)
	print(coon_attack_say[rand_coon_say])
	print('\n\n')
	time.sleep(3)

	#raccoon fights you
	player_damage = fight_raccoon.coon_attacks(player)
	player.injure(player_damage)

	print('\n\n')
	time.sleep(2)

	#do you want to keep fighting
	print('Do you want to attack the raccoon again?')
	fight_choice = fight_raccoon.choose_fight(player)

	print('\n\n')
	time.sleep(3)
print('Now, on to the next adventure!')
'''
