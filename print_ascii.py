#!/usr/bin/env python3

def vinnys_sign():
	frames = []

	with open('vinnys_sign.txt','r') as f:
		frames.append(f.readlines())

	for frame in frames:
		print("".join(frame))


def pizza_pic():
	frames = []
	with open('pizza_pic.txt','r') as f:
		frames.append(f.readlines())
	for frame in frames:
		print("".join(frame))

def soup_pic():
	frames = []
	with open('soups.txt','r') as f:
		frames.append(f.readlines())
	for frame in frames:
		print("".join(frame))
