#!/usr/bin/env python3

#make a name insert
print("Hello - what is your name?")
name = input("Name: ")
print("Hello " + str(name) + ", now do the personality quiz")


#creating counts for each of the personality types
#make a dictionary
answer_dict = {'A_count': 0, 'B_count': 0, 'C_count': 0, 'D_count': 0}

#making first questio
#mess around with the input formatting so the question input looks nice
#textwrapping, etc
q1 = input("choose a letter A) A, B) B, C) C, D) D \n")

if q1.lower() == 'a':
	answer_dict['A_count'] += 1
elif q1.lower() == 'b':
	answer_dict['B_count'] += 1
elif q1.lower() == 'c':
	answer_dict['C_count'] += 1
elif q1.lower() == 'd':
	answer_dict['D_count'] += 1
else:
	print("sorry I don't understand, try a different response")
print(answer_dict)
#print("response count:", "As=", A_count, "Bs=", B_count, "Cs=", C_count, "Ds=", D_count)

q2 = input("choose a letter A) A, B) B, C) C, D) D \n")
if q2.lower() == 'a':
	answer_dict['A_count'] += 1
elif q2.lower() == 'b':
	answer_dict['B_count'] += 1
elif q2.lower() == 'c':
	answer_dict['C_count'] += 1
elif q2.lower() == 'd':
	answer_dict['D_count'] += 1
else:
	print("sorry I don't understand, try a different response")
print(answer_dict)


q3 = input("choose a letter A) A, B) B, C) C, D) D \n")
if q3.lower() == 'a':
  answer_dict['A_count'] += 1
elif q3.lower() == 'b':
  answer_dict['B_count'] += 1
elif q3.lower() == 'c':
  answer_dict['C_count'] += 1
elif q3.lower() == 'd':
  answer_dict['D_count'] += 1
else:
  print("sorry I don't understand, try a different response")

q4 = input("choose a letter A) A, B) B, C) C, D) D \n")
if q4.lower() == 'a':
  answer_dict['A_count'] += 1
elif q4.lower() == 'b':
  answer_dict['B_count'] += 1
elif q4.lower() == 'c':
  answer_dict['C_count'] += 1
elif q4.lower() == 'd':
  answer_dict['D_count'] += 1
else:
  print("sorry I don't understand, try a different response")

#figure out how to break ties
sorted_dict = sorted(answer_dict.items(), key=lambda x:x[1], reverse=True)
print(sorted_dict)

if sorted_dict[0][1] == sorted_dict[1][1]:
	print (sorted_dict[0][0])
	print (sorted_dict[1][0])
	variable1 = ''
	variable2 = ''
	#this is the tiebreaker question
	TieBreak_Dict = {'A_count': 'squirrel', 'B_count': 'horseshoe crab', 'C_count': 'pigeon', 'D_count': 'banana slug'}
	for key in TieBreak_Dict.keys():
		if key == sorted_dict[0][0]: 
			variable1= TieBreak_Dict[key]
		elif key == sorted_dict[1][0]:
			variable2= TieBreak_Dict[key]
	print(variable1, variable2)

	#q4 = input("choose a letter A) A, B) B, C) C, D) D \n")
	#if q4.lower() == 'a':
  #answer_dict['A_count'] += 1
	#elif q4.lower() == 'b':
  #answer_dict['B_count'] += 1
	#elif q4.lower() == 'c':
  #answer_dict['C_count'] += 1
	#elif q4.lower() == 'd':
  #answer_dict['D_count'] += 1
	#else:
	#print("buh")
else:
	print("Congrats, you are a",sorted_dict[0][0])






