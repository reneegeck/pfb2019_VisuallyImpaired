#!/usr/bin/env python3

def blinking_dice():
	frames = []

	with open('dice.txt','r') as f:
		lines = f.readlines()

	for line in lines:	
		line = line.rstrip()
		print('\033[5m' + line + '\033[0m')
