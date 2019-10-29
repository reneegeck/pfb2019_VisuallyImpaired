#!/usr/bin/env python3
import user
import random
import time
import sys
from print_quiz import re_input_easy, re_input_med, re_input_hard
import print_ascii
import os
import subprocess

def random_en1(user):
	os.system("clear")
	#find sketch food, do you eat it?
	#if you choose to eat the apple, there's a 50% chance it will injure you and a 50% chance it will heal you
	#print apple art
	print_ascii.apple_pic()
	time.sleep(1.5)
	print("You found an apple, just sitting there on the ground. It looks very appetizing, but it's kind of strange that someone left it here. What do you do?")
	time.sleep(1.5)
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
			time.sleep(1)
			user.print_health_bar()
			time.sleep(2)
			input("Press enter to continue")
		else:
			print("Yum, a crisp and juicy apple. You gain 10 health.")
			user.heal(10)
			time.sleep(1)
			user.print_health_bar()
			time.sleep(2)
			input("Press enter to continue")
	else:
		print("You leave the apple alone and walk away")
		time.sleep(2)
		input("Press enter to continue")

def random_en2(user):
  os.system("clear")
  time.sleep(2)
  #useless item encouter
  print_ascii.mysteryman_pic()
  time.sleep(2)
  print("A mysterious man approaches you.")
  time.sleep(2)
  #print man image
  print("He hands you an ordinary-looking dirty pinecone.")
  time.sleep(2)
  print_ascii.pinecone_pic()
  time.sleep(1.5)
  #print pinecone image
  print("'It's dangerous to go alone! Take this!'") 
  time.sleep(2)
  print(".......")
  time.sleep(2)
  print("Okay...It's probably a good idea not to argue with him. You put the pinecone in your inventory and walk away.")
  user.add_item('Useless Pinecone')
  input("Press enter to continue ")

def random_en3(user):
  os.system("clear")
  print_ascii.sphinx_pic()
  time.sleep(2)
  print("You encouter Shasta the Sphinx. She says she has a quiz for you!")
  #text color change
  time.sleep(1.5)
  print("\033[32mAnswer my questions and I will give you a prize!\033[m")
  subprocess.run(["say","-v","Samantha","Answer my questions and I will give you a prize!"])
  time.sleep(2)
  if user.intel >= 65:
    print("\033[32mYou're a smart cookie, this one will be easy!\033[33m")
    subprocess.run(["say","-v","Samantha","You're a smart cookie, this one will be easy!"])
    re_e = re_input_easy('')
    #easy regular expression quiz
    while re_e.lower() not in ['a','b','c','d']:
      print("\033[32mThat makes no sense. What did you say?\033[33m")
      subprocess.run(["say","-v","Samantha","That makes no sense. What did you say?"])
      re_e = re_input_easy('')
    if re_e.lower() == 'b':
      print("\033[32mCongrats! You chose the correct answer. All that studying is paying off.\033[33m")
      subprocess.run(["say","-v","Samantha","Congrats! You chose the correct answer. All that studying is paying off"])
      time.sleep(2)
      print("Shasta hands you a healing potion. Sweet!")
      time.sleep(2)
      print_ascii.healthpotion_pic()
      time.sleep(2)
      user.add_item('Healing Potion')
      input("Press enter to continue")
    else:
      print("\033[32mYikes...that's not right. Were you asleep during that module?\033[33m")
      subprocess.run(["say","-v","Samantha","Yikes...that's not right. Were you asleep during that module?"])
      time.sleep(2)
      print("You walk away empty-handed")
      time.sleep(2)
      input("Press enter to continue")
  elif user.intel >= 50:
    #medium regex quiz
    print("\033[32mYour intelligence is okay, but you'll have to think a little on this one...\033[33m")
    re_m = re_input_med('')
    while re_m.lower() not in ['a','b','c','d']:
      print("\033[32mThat makes no sense. What did you say?\033[33m")
      subprocess.run(["say","-v","Samantha","That makes no sense. What did you say?"])
      re_m = re_input_med('')
    if re_m.lower() == 'b':
      print("\033[32mCongrats! You chose the correct answer. All that studying is paying off.\033[33m")
      subprocess.run(["say","-v","Samantha","Congrats! You chose the correct answer. All that studying is paying off"])
      time.sleep(2)
      print("Shasta hands you a healing potion. Sweet!")
      time.sleep(2)
      print_ascii.healthpotion_pic()
      time.sleep(2)
      user.add_item('Healing Potion')
      input("Press enter to continue")
    else:
      print("\033[32mYikes...that's not right. Were you asleep during that module?\033[33m")
      subprocess.run(["say","-v","Samantha","Yikes...that's not right. Were you asleep during that module?"])
      time.sleep(2)
      print("You walk away empty-handed")
      time.sleep(2)
      input("Press enter to continue")
  else:
    #hard regex quiz
    print("\033[32mWhew, you're not exactly the sharpest crayon in the box, are you? This is going to be a tough one.\033[33m")
    subprocess.run(["say","-v","Samantha","Whew, you're not exactly the sharpest crayon in the box, are you? This is going to be a tough one"])
    re_h = re_input_hard('')
    while re_h.lower() not in ['a','b','c','d']:
      print("\033[32mThat makes no sense. What did you say?\033[33m")
      subprocess.run(["say","-v","Samantha","That makes no sense. What did you say?"])
      re_h = re_input_hard('')
    if re_h.lower() == 'b':
      print("\033[32mCongrats! You chose the correct answer. All that studying is paying off.\033[33m")
      subprocess.run(["say","-v","Samantha","Congrats! You chose the correct answer. All that studying is paying     off"])
      time.sleep(2)
      print("Shasta hands you a healing potion. Sweet!")
      time.sleep(2)
      print_ascii.healthpotion_pic()
      time.sleep(2)
      user.add_item('Healing Potion')
      input("Press enter to continue")
    else:
      print("\033[32mYikes...that's not right. Were you asleep during that module?\033[33m")
      subprocess.run(["say","-v","Samantha","Yikes...that's not right. Were you asleep during that module?"])
      time.sleep(2)
      print("You walk away empty-handed")
      time.sleep(2)
      input("Press enter to continue")

#make mini-encounter before swan fight, yields "Bread"
def random_en4(user):
  os.system("clear")
  time.sleep(1)
  print("Joe walks by and offers you some bread from the cafeteria. It looks like normal bread, but why is he giggling? Do you take the bread? \n\n")
  time.sleep(3)
  print_ascii.bread_pic()
  time.sleep(1)
  print("A) Yes or  B) No")
  en4_ans = input(">>> ")
  while en4_ans.lower() not in ['a','b']:
    print("You have two options, A or B, it's not that hard. Try again.")
    print("Joe walks by and offers you some bread from the cafeteria. It looks like normal bread, but why is he giggling? Do you take the bread?")
    print("A) Take the bread or B) Just walk away")
    en4_ans = input(">>> ")
  if en4_ans.lower() == 'a':
    user.add_item("Bread")
    time.sleep(1)
    print("It seems like totally normal bread. This could be a nice snack in a little while...")
    time.sleep(1.5)
    print("Do you:  A) eat the bread now or B) save it for later?")
    bread_eat = input(">>> ")
    while bread_eat.lower() not in ['a','b']:
      print("You only have two choices, it's not that hard. Try again.")
      print("It seems like totally normal bread. This could be a nice snack in a little while...")
      print("Do you:  A) eat the bread now or B) save it for later?")
      bread_eat = input(">>> ")
    if bread_eat.lower() == 'a':
        user.heal(10)
        time.sleep(1)
        print("Yummy! The bread has restored 10 of your health points.")
        time.sleep(1)
        user.print_health_bar()
        time.sleep(2)
        input("Press enter to continue")
    else:
        print("You keep the bread in your pocket for later, just in case.")
        time.sleep(2)
        input("Press enter to continue")
  else:
    print("Mom said never to take candy from strangers. You walk away from Joe.")
    time.sleep(2)
    input("Press enter to continue")



