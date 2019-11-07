# ------------------------------------------------------------------------------
# Name:        Hangman
# Purpose:     project
# Author:      N.DEE
# Created:     07/11/2019
# Revision:    2.00
# ------------------------------------------------------------------------------
# -- IMPORTS --
import winsound
import random
import reusables as r
import words as w
from stages import steps, free
# -- GLOBALS/CONSTANTS --
options = ("simple", "medium", "hard")
# -- FUNCTIONS/CLASSES --
def title_menu():
	"""
	show title of game and menu of choices , easy, medium, hard.
	"""
	print("test")

def menuu():
	if menu == 1:
		print("easy level")
		word = w.easy[random.randint(0,len(w.easy)-1)]
		return word
	elif menu == 2:
		print("medium level")
		word = w.medium[random.randint(0,len(w.medium)-1)]
		return word
	elif menu == 3:
		print("hard level")
		word = w.hard[random.randint(0,len(w.hard)-1)]
		return word

def rungame():
	"""while turn != maxturns:
		
		asterix = len(word)
		print("_" * asterix)
		for char in word:
			if char in guesses:
				print (char)
			else:
				print ("_")
				turn += 1
		if maxturns == turn:
			print("You lost!")
			break"""
	turns = 7
	guesses = ''
	word = menuu()
	x = 0
	print(steps[x])
	while turns > 0:
		failed = 0
		for char in word:      
			if char in guesses:    
				print (char, end=" ")    
			else:
				print ("_", end=" ")     
				failed +=1
		if failed == 0:        
			print("You won")
			print(free[0])
			break              
		print
		guess = input("guess a character:") 
		guesses += guess                    
		if guess not in word:  
			turns -= 1        
			print("Wrong") 
			x +=1
			print(steps[x])
			print("You have", + turns, 'more guesses')
			if turns == 0:           
				print("You Loose") 
# -- MAIN BODY --
if __name__ == '__main__':
	r.title_gen()
	menu = r.get_menu()
	menuu()
	rungame()