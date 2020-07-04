#!/usr/bin/python3
#Iterators

class iterDemo:
	def __init__(self):
		self.alphabet = "abcdefghijklmnopqrstuvwxyz"
		self.i = 0


	def __iter__(self):
		return self

	def __next__(self):
		if self.i == 26:
			raise StopIteration
		letter = self.alphabet[self.i]
		self.i = self.i + 1
		return letter


ID = iterDemo()

for i in ID:
	print (i)

