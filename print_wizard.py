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

def input1(text):
  print(decode('+-------------%' + '+---------------%'))
  print(decode('| A) MUSHROOM |' + '| B) CHERRY PIE |'))
  print(decode('\\-------------/' + '\\---------------/'))
  answer = input('>>>')
  return(answer)

def input2(text):
  print('What was that? Try again!')
  print(decode('+-----%' + '+----%'))
  print(decode('| A)  |' + '| B) |'))
  print(decode('\\-----/' + '\\----/'))
  answer = input('>>>')
  return(answer)

def input3(text):
  print('Yes or No?')
  print(decode('+-----%' + '+----%'))
  print(decode('| Yes |' + '| No |'))
  print(decode('\\-----/' + '\\----/'))
  answer = input('>>>')
  return(answer)













