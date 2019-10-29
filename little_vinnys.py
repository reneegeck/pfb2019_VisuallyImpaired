#!/usr/bin/env python3

import time, user, animate_bus, print_ascii, os

#encounter to take trip to Little Vinny's 
def foraging(player):
	os.system('clear')
	print("\n\n\nYou see a shuttle in the parking lot. Do you want to get on it?\n")
	answer = ''

	while answer.lower() not in ['yes','no']:
		answer = input("Yes or No? ")
		if answer.lower() == 'yes':
			print("Great! Welcome on board")
			time.sleep(1.5)
			animate_bus.moving_bus()
			print('\n\n'+"The shuttle stops in Huntington. Do you want to get out?"+'\n\n')
			get_off_bus = input("Yes or No? ")

			if get_off_bus.lower() == 'yes':
				print('\n\n'+"You get off the bus and find yourself in front of Little Vinny's"+'\n')
				print_ascii.vinnys_sign()
				vinnys = 'No'			

				while vinnys.lower() != 'yes':
					vinnys = input("Do you want to get a slice? Yes or no? ")

					if vinnys.lower() == 'yes':
						print("\nOf course you want a slice!")
						print('\n\n\n')
						time.sleep(1)
						print_ascii.pizza_pic()
						time.sleep(2)
						player.heal(20) 
						print("The pizza gives you life."+'\n')
						player.print_health_bar()					
						time.sleep(3)
						print('\n\nTime to head back to CSHL!\n')
						input('Press enter to get on the shuttle. ')
						animate_bus.moving_bus()						

					elif vinnys.lower() == 'no':
						print("I think you're mistaken. Try again.")
						continue

			elif get_off_bus.lower() == 'no':
				print('\n'+"Alright, back to CSHL!"+'\n')
				time.sleep(2)
				animate_bus.moving_bus()
				print('\n'+"You're back on campus and go to the Clarkson dining hall."+'\n')
				time.sleep(1.5)
				print("At the dining hall you run into Matty Two Soups.\n")
				time.sleep(1.5)
				print("What a pleasure!\n")
				time.sleep(2)
				print("He offers you one of his soups.")
				time.sleep(1.5)
				print_ascii.soup_pic()
				soup_answer = 'No'
	
				while soup_answer.lower() != 'yes':
					soup_answer = input("Do you want to accept Matty Two Soups kind offer and have some soup? Yes or no? ")	

					if soup_answer.lower() == 'yes':
						print("\nOf course you want to share some soup with Matty Two Soups!\n")
						time.sleep(1)
						print("The soup has healing powers and makes you feel refreshed.\n")
						time.sleep(1.5)	
						player.heal(20)
						player.print_health_bar()

					elif soup_answer.lower() == 'no':
						print("\nMatty Two Soups doesn't take no for an answer! Try again.\n")
						continue			
	
		elif answer.lower() == 'no':
			print("\nAlright! You go to the Clarkson dining hall instead.\n")
			time.sleep(1.5)
			print("At the dining hall you run into Matty Two Soups.\n")
			time.sleep(1.5)
			print("What a pleasure!\n")
			time.sleep(2)
			print("He offers you one of his soups.")
			time.sleep(1.5)
			print_ascii.soup_pic()
			soup_answer = 'No'

			while soup_answer.lower() != 'yes':
				soup_answer = input("Do you want to accept Matty Two Soups kind offer and have some soup? Yes or no? ")
				if soup_answer.lower() == 'yes':
					print("\nOf course you want to share some soup with Matty Two Soups!\n")
					time.sleep(1)
					print("The soup has healing powers and makes you feel refreshed.\n")
					time.sleep(1.5)
					player.heal(20)
					player.print_health_bar()	

				elif soup_answer.lower() == 'no':
					print("\nMatty Two Soups doesn't take no for an answer! Try again.\n")
					continue
		else:
			continue

	input('Press enter to continue\n')
