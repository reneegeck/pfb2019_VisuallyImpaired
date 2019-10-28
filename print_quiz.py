#!/usr/bin/env python3

dic = {
'\\' : b'\xe2\x95\x9a',
'-'  : b'\xe2\x95\x90',
'/'  : b'\xe2\x95\x9d',
'|'  : b'\xe2\x95\x91',
'+'  : b'\xe2\x95\x94',
'%'  : b'\xe2\x95\x97',
}

def decode(x):
	return (''.join(dic.get(i, i.encode('utf-8')).decode('utf-8') for i in x))

def quiz_input1(text):	
	print('What is your favorite game?')
	print(decode('+-------------%' + '+---------%' + '+-------------%' + '+-----------------%'))
	print(decode('| A) Monopoly |' + '| B) Clue |' + '|   C) Apex   |' + '| D) Super Mario  |'))
	print(decode('\\-------------/' + '\\---------/' + '\\-------------/' + '\\-----------------/'))
	answer = input('>>>')
	return(answer)

def quiz_input2(text):
	print('What is the best breakfast meat?')
	print(decode('+-------------%' + '+----------%' + '+------------%' + '+----------------%'))
	print(decode('| A) Sausage  |' + '| B) Bacon |' + '|   C) Ham   |' + '|  D) Pancakes   |'))
	print(decode('\\-------------/' + '\\----------/' + '\\------------/' + '\\----------------/'))
	answer = input('>>>')
	return(answer)

def quiz_input3(text):  
  print('What is your ideal vacation?')
  print(decode('+-------------%' + '+-----------%' + '+-------------%' + '+-----------------%'))
  print(decode('| A)   Spa    |' + '| B) Beach  |' + '|   C) City   |' + '| D)  Mountains   |'))
  print(decode('\\-------------/' + '\\-----------/' + '\\-------------/' + '\\-----------------/'))
  answer = input('>>>')
  return(answer)

def quiz_input4(text): 
  print('Your boss calls you into their office and commands you to dance.' + '\n' + 'What dance move do you do?')
  print(decode('+-------------------%' + '+--------------%' + '+------------%' + '+-----------------------%'))
  print(decode("| A) Chicken dance  |" + '| B) Macarena  |' + '|  C) Floss  |' + "| D) 'the sprinkler'    |"))
  print(decode('\\-------------------/' + '\\--------------/' + '\\------------/' + '\\-----------------------/'))
  answer = input('>>>')
  return(answer)

def quiz_input5(text):
  print("What's a tasty food?")
  print(decode('+---------------%' + '+--------------%' + '+------------%' + '+-------------%'))
  print(decode('| A) Bananas    |' + '| B)  Seaweed  |' + '|  C)  Corn  |' + '| D)  Nuts    |'))
  print(decode('\\---------------/' + '\\--------------/' + '\\------------/' + '\\-------------/'))
  answer = input('>>>')
  return(answer)

def quiz_input6(variable1,variable2):
  print('Choose which you would most like to be:')
  print(decode('+-----------------------%' + '+-----------------------%'))
  print(decode('|A)'+ variable1 + ' |' + '|B)' + variable2 + ' |'))
  print(decode('\\-----------------------/' + '\\-----------------------/'))
  answer = input('>>>')
  return(answer)

def re_input_easy(text):
  print("What will match the following EASY regular expression?")
  print("[Regular expression]")
  print(decode('+---------------%' + '+--------------%' + '+------------%' + '+-------------%'))
  print(decode('| A) Bananas    |' + '| B)  Seaweed  |' + '|  C)  Corn  |' + '| D)  Nuts    |'))
  print(decode('\\---------------/' + '\\--------------/' + '\\------------/' + '\\-------------/'))
  answer = input('>>> ')
  return(answer)	

def re_input_med(text):
  print("What will match the following MEDIUM regular expression?")
  print("[regular expression]")
  print(decode('+---------------%' + '+--------------%' + '+------------%' + '+-------------%'))
  print(decode('| A) Bananas    |' + '| B)  Seaweed  |' + '|  C)  Corn  |' + '| D)  Nuts    |'))
  print(decode('\\---------------/' + '\\--------------/' + '\\------------/' + '\\-------------/'))
  answer = input('>>> ')
  return(answer)

def re_input_hard(text):
  print("What will match the following DIFFICULT` regular expression?")
  print("[regular expression]")
  print(decode('+---------------%' + '+--------------%' + '+------------%' + '+-------------%'))
  print(decode('| A) Bananas    |' + '| B)  Seaweed  |' + '|  C)  Corn  |' + '| D)  Nuts    |'))
  print(decode('\\---------------/' + '\\--------------/' + '\\------------/' + '\\-------------/'))
  answer = input('>>> ')
  return(answer)







