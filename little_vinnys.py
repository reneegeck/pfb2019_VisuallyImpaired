#!/usr/bin/env python3

import time
import user


#encounter to take trip to Little Vinny's 

print("You see a shuttle in the parking lot. Do you want to get on it?")

answer = input("Yes or No? ")

if answer.lower() == 'yes':
	print("Great! Welcome on board")
	time.sleep(4)   #INCLUDE BUS ART HERE?
	print('\n\n'+"The shuttle stops in Huntington. Do you want to get out?"+'\n\n')
	get_off_bus = input("Yes or No? ")
	if get_off_bus.lower() == 'yes':
		print('\n\n'+"You get off the bus and find yourself in front of Little Vinny's"+'\n')
		print('vinny ascii art here')
		vinnys = 'No'			
		while vinnys.lower() == 'no':
			vinnys = input("Do you want to get a slice? Yes or no? ")
			if vinnys.lower() == 'yes':
				print("Of course you want a slice!")
				print('pizza ascii art here')
				#user.player.heal(20) #Add health points, check if this works tomorrow
				print("The pizza gives you life.")
			elif vinnys.lower() == 'no':
				print("I think you're mistaken. Try again. Do you want a slice?")
				continue
	
	elif get_off_bus.lower() == 'no':
		print('\n'+"Alright, back to CSHL!"+'\n')
		time.sleep(4)
		print('\n'+"You're back on campus and go to the Clarkson dining hall."+'\n')



elif answer.lower() == 'no':
	print("Alright! You go somewhere else instead.")
