#!/usr/bin/env python3

import user, time

def choose_weapon(player):
				#initialize weapon set if not present already
				if 'weapons' not in player.inventory.keys():
					player.inventory['weapons'] = set()

				#count current number of weapons
				weaponCount = len(player.inventory['weapons'])

				#start the choice
				print('You see a dagger, a sword, and an axe.')

				#if you already have all 3 weapons
				if weaponCount == 3:
					print('Too bad, you have them all already! Fierce!')

				#if you still don't have all 3 weapons, you get to pick one
				else:
					while len(player.inventory['weapons']) == weaponCount: #while you still have that number of weapons
						weaponChoices = ['sword', 'axe', 'dagger']	
						try:
							chosenWeapon = input('Which do you choose? The: ')
							chosenWeapon = chosenWeapon.lower() #make lowercase for consistencty
							if chosenWeapon not in weaponChoices:
								raise ValueError("That wasn't one of the choices, dummy!!") #to catch typos
							if chosenWeapon in player.inventory['weapons']:
								raise ValueError('You already have that weapon! Pick something else!') #to catch repeats
						except ValueError:
							print("Try again!")
							continue #you get to go back to the top of the while loop and try again
						player.add_weapon(chosenWeapon) #add to set of weapons
					print('\n\nGreat! You are now armed with a ', chosenWeapon, '.', sep='')
					time.sleep(3)
					return player

