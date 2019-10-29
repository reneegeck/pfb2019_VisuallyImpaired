#!/usr/bin/env python3

def moving_bus():
	import os, time

	os.system('clear')
	filenames = ['ascii_art/bus7.txt','ascii_art/bus6.txt','ascii_art/bus5.txt','ascii_art/bus4.txt','ascii_art/bus3.txt','ascii_art/bus2.txt','ascii_art/bus1.5.txt','ascii_art/bus1.4.txt','ascii_art/bus1.3.txt','ascii_art/bus1.2.txt', 'ascii_art/bus1.txt', 'ascii_art/bus.txt']

	frames = []

	for name in filenames:
		with open(name,'r') as f:
			frames.append(f.readlines())

	for frame in frames:
		print('\n\n\n\n\n')
		print("".join(frame))
		time.sleep(0.6)
		os.system('clear')
