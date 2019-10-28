#!/usr/bin/env python3

import random

class User(object):
	#attributes:
	def __init__(self, name, health, armor, speed, intel, status, inventory):
		#health = health points, integer
		#armor = armor points, integer
		#speed = how fast are you?, integer
		#intel = intelligence, how smart are you?, integer
		#status = are you poisoned, invincible, etc?, set because you can't have same status multiple times
		#inventory = weapons/items you pick up, list or dictionary of lists (e.g. weapons, potions)
		self.name = name
		self.health = health
		self.armor = armor
		self.speed = speed
		self.intel = intel
		self.status = set()

		self.inventory = {}
	
	def heal(self,health_points):    #look into defining max efficiently. Ask group about setting MAX for other attributes.	
		if self.health in range(0,100-health_points):	
			self.health += health_points
		else:
			self.health = 100			

	def injure(self,damage_points):
		self.health -= damage_points

	def get_faster(self, speed_points):
		if self.speed in range(0,100-speed_points):
			self.speed += speed_points
		else: 
			self.speed = 100

	def get_slower(self, slow_points): #can never be less than 10
		if self.speed in range(10+slow_points,100):
			self.speed -= slow_points
		else:
			self.speed = 10

	def get_armor(self, protection_points):
		if self.armor in range(0,100-protection_points):
			self.armor += protection_points
		else:
			self.armor = 100

	def lose_armor(self, weak_points): #can never be less than 10
		if self.armor in range(10+weak_points,100):
			self.armor -= weak_points
		else:
			self.armor = 10	

	def get_smarter(self, intel_points):
		if self.intel in range(0,100-intel_points):
			self.intel += intel_points
		else:
			self.intel = 100

	def get_dumber(self, dumb_points): #can never be less than 10
		if self.intel in range(10+dumb_points,100):
			self.intel -= intel_points
		else: 
			self.intel = 10

	def add_status(self, new_status):
		self.status.add(new_status)

	def lose_status(self, current_status):
		self.status.remove(current_status)

	def list_status(self):
		if self.status == False:
			print('You have no statuses that affect your play')
		else:
			print(self.status)
		return self.status

	def add_weapon(self,weapon):
		self.inventory['weapons'].add(weapon)

	def remove_weapon(self, weapon):
		self.inventory['weapons'].remove(weapon)

	def lose_weapon(self, weapon):   #this is random
		lost_weapon = self.inventory['weapons'].pop()

	def list_weapons(self):
		return self.inventory['weapons']

	def list_items(self):
		unique_items = set(self.inventory['items'])
		for item in unique_items:
			num_item = self.inventory['items'].count(item)
			print(num_item, item)

	def add_item(self, item):
		self.inventory['items'].append(item)

	def remove_item(self, item):
		self.inventory['items'].remove(item)

	def lose_item(self):   #this is random
		random.shuffle(self.inventory['items'])
		lost_item = self.inventory['items'].pop() 

	def count_item(self, specific_item):
		return self.inventory['items'].count(specific_item)

	def print_user_stats(self):
		print(self.name)
		print('Health: ', self.health, '/100', sep='')
		print('Armor hit class:', self.armor)
		print('Intelligence:', self.intel)
		print('Speed:', self.speed)

	def print_health_bar(self, decimals = 1, length = 100, fill = '█'):
		color_dict = {'purple' : '\033[95m', 'blue' : '\033[94m', 'green' : '\033[92m', 'yellow' : '\033[93m', 'red' : '\033[91m', 'end' : '\033[0m', 'bold' : '\033[1m', 'underline' : '\033[4m', 'blink' : '\033[5m', 'dim' : '\033[2m',}
		percent = ("{0:." + str(decimals) + "f}").format(100 * (self.health / 100))
		filledLength = int(length * self.health // 100)
		if self.health < 5:
			bar = color_dict['blink'] + color_dict['red'] + fill * filledLength + color_dict['end'] + color_dict['blink'] + color_dict['dim'] + fill * (length - filledLength) + color_dict['end'] + color_dict['green']
			bar_out = '{}hp|{}| {}%'.format(self.health, bar, percent)
		else:
			bar = fill * filledLength + color_dict['end'] + color_dict['dim'] + fill * (length - filledLength) + color_dict['end'] + color_dict['green']
			bar_out = '{}hp|{}| {}%'.format(self.health, bar, percent)
		print(bar_out)


#Move to trait quiz (or maybe backbone script?)
#pigeon has ok armor and speed and is not very intelligent
#pigeon  = User('Pigeon', 100, 60, 60, 40, set(), dict()) 

#banana slug has not good armor and is slow but weirdly intelligent
#banana_slug = User('Banana Slug', 100, 40, 30, 80, set(), dict())

#squirrel is ok for armor and is faster, and has ok intelligence
#squirrel = User('Squirrel', 100, 50, 60, 60, set(), dict())

#crab is good for armor and ok for speed and intelligence
#horseshoe_crab = User('Horseshoe Crab', 100, 80, 50, 60, set(), dict())

