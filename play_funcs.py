import pygame
pygame.init()

import Words 
import random
from Hangman import white, black, red, green, blue, category, SCREEN
#Origin point of the Hangman, MOVE THIS TO MOVE HIM

def get_word(category):                              # generates word and changes it to uppercase
    if category=="Purdue":
        random_index = random.randint(0,12)
        word = Words.purdue_words[random_index]
    elif category=="Halloween":
        random_index = random.randint(0,12)
        word = Words.halloween_words[random_index]
    elif category=="Christmas":
        random_index = random.randint(0,12)
        word = Words.christmas_words[random_index]
    return word.upper()

def play(word):                              # method to play the game
	print (word)
	wordLength = len(word)                   
	word_completion = "_ " * wordLength      # displays _ for the number of letters in the word
	guessed = False
	guessed_letters = []
	guessed_words = []
	tries = 6
	print("Let's play Hangman!")
	hangman_animation(tries)                # display initial hangman

	word_completion_list =  list(word)
	word_as_list = list(word)                #Makes a letter equivalent of word_completion_list to allow us to compare word_completion to the actual word
	for i in range (len(word_completion_list)):
		if not(word_completion_list[i] == " "):
			word_completion_list[i] = ' _ '		
	for i in range (len(word_as_list)):
		if not(word_as_list[i] == " "): word_as_list[i] = " " + word_as_list[i] + " "
	word_completion = "".join(word_completion_list)
	word_compare = "".join(word_as_list)
	print ("Your word is")
	print(word_completion)
	print("\n")
	while (not guessed) and (tries > 0):      # loop runs until user guesses the word or runs out of tries 
		answer_key = list(word)                #creates a list of words to call when the program wants to replace the underscores with the uncovered letters
		iguess = input("Guess a letter or a word: ")        # converts user input to uppercase
		guess = iguess.upper()
		if (len(guess) == 1 and guess.isalpha()):                    # user guesses a valid letter in the alphabet
			if guess in guessed_letters:                             # user repeats a guess
				print("You already guessed this letter:", guess)
			elif guess not in word:                                  # user guesses a wrong letter
				print("Oops! The letter you guessed is not in the word :(")
				tries -= 1                                           # no. of tries decreased
				guessed_letters.append(guess)                        # the guess is added to the list of guessed letters
			else:                                                    # user guesses a correct letter
				print("Yay! The letter you guessed is in the word :)")
				guessed_letters.append(guess)                        # the guess is added to the list of guessed letters
				word_completion_as_list = list(word_completion)     # update word_completion to reveal all occurences of the guessed letter. convert word_completion from a string to a list so we can index into it
				word_as_list = list(word_compare)
				for i in range (len(word_completion_as_list)-1):                #reveals all instances of the guessed letter
					if guess == word_as_list[i]:
						word_completion_as_list[i] = guess
				word_completion = "".join(word_completion_as_list)
            
				if "_" not in word_completion:                       # to check if the guessed letter completes the word
					guessed = True
		elif len(guess) == len(word) and guess.isalpha():            # if user guesses a word that is the same size as the answer word and is made of only letters
			if guess in guessed_words:
				print("You already guessed this word:", guess)
			elif guess != word:
				print("Oops! Your guess is incorrect :(")
				tries -= 1
				guessed_words.append(guess)
			else:
				guessed = True
				word_completion = word
		else:                                                        # if user gives an invalid input
			print("Not a valid guess.")
		hangman_animation(tries)                                     # displays state of the hangman after each guess             
		print(word_completion)                                       # displays current status of the word being guessed
		print("\n")
		if guessed:
			print("WOHOOO! You guessed the word!")
		elif tries <= 0:
			print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")
			




# def main():                    # main method
#     word = get_word()          # generate a word
#     play(word)                 # start the game
#     while input("Play Again? (Y/N) ").upper() == "Y":        # to restart the game
#         word = get_word()
#         play(word)

# if __name__ == "__main__":
# 	main()