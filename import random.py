import random 

def get_num():
	num = random.randint(0,20)
	return num


def play(num):
	guessed = False 
	guessed_nums = []
	print("LETS PLAY GUESS THE NUMBER")
	print("I AM THINKING OF A NUMBER BETWEEN 0 AND 20")
	print("YOU HAVE INFINITE CHANCES ")


	while not guessed:
		guess = input("NOW , GUESS THE NUMBER")
		if guess.isapla() or guess not in range(0,20):
			print("THIS IS NOT A VALID ANSWER ")
		elif guess not in guessed_nums:
			guessed_nums.append(guess)
			if guessed_nums[0] = guess:
				print("HOT")
			else:
				if num[len(num)] >= guess :
					print("HOTTER")
				else:
					print("COLDER")
			elif guess == num:
				guessed = True 
				print("YOU HAVE GUESSED THE NUMBER")
		else:
			print("YOU HAVE ALREADY GUESSED THIS NUMBER")



def main():
	num = get_num()
	play(num)
	while input("Play Again? (Y/N) ").upper() == "Y":
		num = get_num()
		play(num)


if __name__ = "__main__" :
	main()