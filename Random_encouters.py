#!/usr/bin/env python3
import user
import random

player = user.User('Horseshoe Crab', 100, 80, 50, 60, set(), dict())

def random_en1(user):
	#find sketch food, do you eat it?
	#print apple art
	print("You found an apple, just sitting there on the ground. It looks very appetizing, but it's kind of strange that someone left it here. What do you do?")
	print("A) Eat the apple or B) Don't eat the apple")
	en1_ans = input('>>>')
	if en1_ans.lower() == 'a':
		randomnum = random.randint(1,3)
		if randomnum == 1:
			print("Nasty! Why would you eat something you found on the ground? You lose 10 health")
			user.injure(10)
		else:
			print("Yum, a crisp and juicy apple. You gain 10 health.")
			user.heal(10)
	elif en1_ans.lower() == 'b':
		print("You leave the apple alone and walk away")
	else:
		print("What? Try again.")
	#there's a 50% chance it was rotten, you lose health
	#there's a 50% chance it was delicious, you gain health
random_en1(player)
player.print_user_stats()

def random_en2(user):
	#useless item encouter
	print("A mysterious man approaches you."
	time.sleep(1)
	print("He hands you an ordinary-looking dirty pinecone.") 
	print("'It's dangerous to go alone! Take this!'")
	if 'items' not in user.inventory.keys():
		user.inventory['items'] = list()
		print("It's probably a good idea not to argue with him. You put the pinecone in your inventory and walk away.")
		user.add_item('Useless Pinecone')
		print(user.inventory['items']) 
	elif 'Useless Pinecone' in user.inventory['items']:
		print("Yikes...this guy again. You take the pinecone and discreetly throw it out.")
	else:
		print("It's probably a good idea not to argue with him. You put the pinecone in your inventory and walk away.") 
		user.add_item('Useless Pinecone')
		print("Inventory:", user.inventory['items']) 
random_en2(player)  




#make mini-encounter before racoon fight, yields healing potion
def random_en3(self):
	print("Someone walks up to you.")
	#text color change
	print("You'll probably need this.")
	print("She hands you a free health potion. Sweet!")
	player.add_item("Health Potion")







#this is redundant, take it out or re-skin it
#Matty 2-soups encounter
def random_en4(self):
	print("A sudden fog descends. From the mist, MATTY 2-SOUPS emerges")
	print("He offers you one of his soups. Which do you take?")
	print("A) Chicken Noodle or B) Tomato bisque")
	answer = input('>>>')
	if en4_ans.lower() == 'a':
		print("Delicious! So much soup, a naps seems nice right now... +10 health -5 speed")
		player.speed(-5)
		player.heal(10)
	elif en4_ans.lower() == 'b':
		print("Hey, this wasn't tomato bisque! It was some sort of magic sludge... +5 intelligence -5 health")
	else:
		print("Don't mess around with MATTY 2-SOUPS....which do you want?")
	print(".")
	time.sleep(1) 
	print(".")
	time.sleep(1)
	print(".")
	time.sleep(1)
	print("Hmmm... MATTY 1-SOUP still has his remaining soup. He seems kinda attached to it though. Should you try to take it from him?")
	





#coffee encounter +speed, repeat






