# ------------------------------------------------------------------------------
# Name:        reusables.py
# Purpose:     Store of useful re-usable code
# Author:      srattigan
# Created:     27/09/2019
# Revision:    1.00
# ------------------------------------------------------------------------------

# -- IMPORTS --


# -- GLOBALS/CONSTANTS --


# -- FUNCTIONS/CLASSES --

def get_int(prompt="Enter number: "):
	'''
	(str) -> int
	Prompts for a number and returns a valid int.
	Code will loop until a valid int is entered by the user.
	This function takes an optional str argument as a prompt.
	'''
	while True:
		num = input(prompt)  # use a try/except here
		try:
			num = int(num)
			return num
		except:
			print("Invalid number! Please try again")
			
def get_menu(prompt="Choose an option: "):
	'''
	(str) -> int
	Prompts for a number and returns a valid int.
	Code will loop until a valid int is entered by the user.
	This function takes an optional str argument as a prompt.
	'''
	print("1. Easy")
	print("2. Medium")
	print("3. Hard")
	while True:
		num = input(prompt)  # use a try/except here
		try:
			num = int(num)
			return num
		except:
			print("Invalid number! Please try again")


			

def get_float(prompt="Enter number: "):
	'''
	(str) -> float
	Prompts for a number and returns a valid float
	Code will loop until a valid num is entered by the user.
	This function takes an optional str argument as a prompt.
	'''
	while True:
		num = input(prompt)  # use a try/except here
		try:
			num = float(num)
			return num
		except:
			print("Invalid number")			

def cls():
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')
def main():
	"""
	The main code for this module
	"""
	pass

def title_gen():
	title = "Hangman Game"
	print("*" * 60)
	print(" " * 25 + title + " " *25)
	print("*" * 60)	
	
	
	
# -- MAIN BODY --
if __name__ == '__main__':
	main()
