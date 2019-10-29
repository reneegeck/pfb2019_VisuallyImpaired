#!/usr/bin/env python3
import user
import random
import time
import sys
from print_quiz import re_input_easy, re_input_med, re_input_hard
import print_ascii

def random_en1(user):
	#find sketch food, do you eat it?
	#if you choose to eat the apple, there's a 50% chance it will injure you and a 50% chance it will heal you
	#print apple art
	print_ascii.apple_pic()
	print("You found an apple, just sitting there on the ground. It looks very appetizing, but it's kind of strange that someone left it here. What do you do?")
	print("A) Eat the apple or B) Don't eat the apple")
	en1_ans = input('>>> ')
	while en1_ans not in ['a','b']:
		print("There's only two choices, it's not that hard. Don't hurt yourself, try again.")
		en1_ans = input('>>> ')
	if en1_ans.lower() == 'a':
		randomnum = random.randint(1,3)
		if randomnum == 1:
			print("Nasty! Why would you eat something you found on the ground? You lose 10 health")
			user.injure(10)
			user.print_health_bar()
		else:
			print("Yum, a crisp and juicy apple. You gain 10 health.")
			user.heal(10)
			user.print_health_bar()
	else:
		print("You leave the apple alone and walk away")
random_en1(player)
player.print_user_stats()

def random_en2(user):
  #useless item encouter
  print_ascii.mysteryman_pic()
  print("A mysterious man approaches you.")
  time.sleep(2)
  #print man image
	print_ascii.pinecone_pic()
  print("He hands you an ordinary-looking dirty pinecone.")
  time.sleep(2)
  #print pinecone image
  print("'It's dangerous to go alone! Take this!'")
  if 'Useless Pinecone' in user.inventory['items']:
    print("Yikes...this guy again. You take the pinecone and discreetly throw it out.")
  else: 
    time.sleep(1)
    delay_string = ("...")
    for char in delay_string:
      sys.stdout.write(char)
      sys.stdout.flush()
      time.sleep(1)
    time.sleep(2)
    print("\n""Okay...It's probably a good idea not to argue with him. You put the pinecone in your inventory and walk away.")
    user.add_item('Useless Pinecone')
random_en2(player)

def random_en3(user):
	print_ascii.sphnix_pic()
  print("Shasta the Sphinx walks up to you.")
  #text color change
  print("\033[32mAnswer my questions and I will give you a prize!\033[m")
  if user.intel >= 65:
    print("You're a smart cookie, this one will be easy!")
    re_e = re_input_easy('')
    #easy regular expression quiz
    while re_e.lower() not in ['a','b','c','d']:
      print("That makes no sense. What did you say?")
      re_e = re_input_easy('')
    if re_e.lower() == 'b':
      print("Congrats! You chose the correct answer. All that studying is paying off.")
      print("Shasta hands you a health potion. Sweet!")
      user.add_item('Health Potion')
    else:
      re_e.lower() == ('a' or 'c' or 'd')
      print("Yikes...that's not right. Were you asleep during that module?")
      print("You walk away empty-handed")
	elif user.intel >= 50:
    #medium regex quiz
    print("Your intelligence is okay, but you'll have to think a little on this one...")
    re_m = re_input_med('')
    while re_m.lower() not in ['a','b','c','d']:
      print("That makes no sense. What did you say?")
      re_m = re_input_med('')
    if re_m.lower() == 'b':
      print("Congrats! You chose the correct answer. All that studying is paying off.")
      print("Shasta hands you a health potion. Sweet!")
      user.add_item('Health Potion')
    else:
      print("Yikes...that's not right. Were you asleep during that module?")
      print("You walk away empty-handed")
	else:
    #hard regex quiz
    print("Whew, you're not feeling so smart right now. This is going to be a tough one.")
    re_h = re_input_hard('')
    while re_h.lower() not in ['a','b','c','d']:
      print("That makes no sense. What did you say?")
      re_h = re_input_hard('')
    if re_h.lower() == 'b':
      print_ascii.healthpotion()
      print("Congrats! You chose the correct answer. All that studying is paying off.")
      print("Shasta hands you a health potion. Sweet!")
      user.add_item('Health Potion')
    else:
      print("Yikes...that's not right. Were you asleep during that module?")
      print("You walk away empty-handed")
random_en3(player)

#make mini-encounter before swan fight, yields "Bread"
def random_en4(user):
   print_ascii.bread_pic()
	 print("Joe walks by and offers you some bread from the cafeteria. It looks like normal bread, but why is he giggling? Do you take the bread?")
  print("A) Yes or  B) No")
  en4_ans = input(">>> ")
  print(en4_ans)
  while en4_ans.lower() not in ['a','b']:
    print("You have two options, A or B, it's not that hard. Try again.")
    print("Joe walks by and offers you some bread from the cafeteria. It looks like normal bread, but why is he giggling? Do you take the bread?")
    print("A) Take the bread or B) Just walk away")
    en4_ans = input(">>> ")
  if en4_ans.lower() == 'a':
    user.add_item("Bread")
    print("It seems like totally normal bread. This could be a nice snack in a little while...")
    print("Do you:  A) eat the bread now or B) save it for later?")
    bread_eat = input(">>> ")
    while bread_eat.lower() not in ['a','b']:
      print("You only have two choices, it's not that hard. Try again.")
      print("It seems like totally normal bread. This could be a nice snack in a little while...")
      print("Do you:  A) eat the bread now or B) save it for later?")
      bread_eat = input(">>> ")
    if bread_eat.lower() == 'a':
        user.heal(10)
        print("Yummy! The bread has restored 10 of your health points.")
        user.print_health_bar()
    else:
        print("You keep the bread in your pocket for later, just in case.")
  else:
    print("Mom said never to take candy from strangers. You walk away from Joe.")
random_en4(player)




