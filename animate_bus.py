#!/usr/bin/env python3

def moving_bus():
	import os, time

	os.system('clear')
	filenames = ['bus7.txt','bus6.txt','bus5.txt','bus4.txt','bus3.txt','bus2.txt','bus1.5.txt','bus1.4.txt','bus1.3.txt','bus1.2.txt', 'bus1.txt', 'bus.txt']

	frames = []

	for name in filenames:
		with open(name,'r') as f:
			frames.append(f.readlines())

	for frame in frames:
		print('\n\n\n\n\n')
		print("".join(frame))
		time.sleep(0.8)
		os.system('clear')
