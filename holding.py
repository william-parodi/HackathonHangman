import pygame
pygame.init()

import Words 
import random
import Hangman 

def get_word():                              # generates word and changes it to uppercase
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
	print(display_hangman(tries))            # display initial hangman

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
		print(display_hangman(tries))                                # displays state of the hangman after each guess             
		print(word_completion)                                       # displays current status of the word being guessed
		print("\n")
		if guessed:
			print("WOHOOO! You guessed the word!")
		elif tries <= 0:
			print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")
			


def display_hangman(tries):             # method to display hangman animation
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]


def main():                    # main method
    word = get_word()          # generate a word
    play(word)                 # start the game
    while input("Play Again? (Y/N) ").upper() == "Y":        # to restart the game
        word = get_word()
        play(word)

if __name__ == "__main__":
	main()


import pygame

pygame.init()
pygame.font.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

display_surface = pygame.display.set_mode()

pygame.display.set_caption('Hangman game')

A_img = pygame.image.load('A.png').convert_alpha()
B_img = pygame.image.load('B.png').convert_alpha()
C_img = pygame.image.load('C.png').convert_alpha()
D_img = pygame.image.load('D.png').convert_alpha()
E_img = pygame.image.load('E.png').convert_alpha()
F_img = pygame.image.load('F.png').convert_alpha()
G_img = pygame.image.load('G.png').convert_alpha()
H_img = pygame.image.load('H.png').convert_alpha()
I_img = pygame.image.load('I.png').convert_alpha()
J_img = pygame.image.load('J.png').convert_alpha()
K_img = pygame.image.load('K.png').convert_alpha()
L_img = pygame.image.load('L.png').convert_alpha()
M_img = pygame.image.load('M.png').convert_alpha()
N_img = pygame.image.load('N.png').convert_alpha()
O_img = pygame.image.load('O.png').convert_alpha()
P_img = pygame.image.load('P.png').convert_alpha()
Q_img = pygame.image.load('Q.png')
R_img = pygame.image.load('R.png')
S_img = pygame.image.load('S.png')
T_img = pygame.image.load('T.png')
U_img = pygame.image.load('U.png')
V_img = pygame.image.load('V.png')
W_img = pygame.image.load('W.png')
X_img = pygame.image.load('X.png')
Y_img = pygame.image.load('Y.png')
Z_img = pygame.image.load('Z.png')

class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        movement = False

        position = pygame.mouse.get_pos()

        if self.rect.collidepoint(position):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                movement = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        screen.blit(self.image, (self.rect.x, self.rect.y))
        return movement

A_button = Button(200, 600, A_img, 0.05)
B_button = Button(275, 600, B_img, 0.05)
C_button = Button(350, 600, C_img, 0.05)
D_button = Button(425, 600, D_img, 0.05)
E_button = Button(500, 600, E_img, 0.05)
F_button = Button(575, 600, F_img, 0.05)
G_button = Button(650, 600, G_img, 0.05)
H_button = Button(725, 600, H_img, 0.05)
I_button = Button(800, 600, I_img, 0.05)
J_button = Button(875, 600, J_img, 0.05)
K_button = Button(950, 600, K_img, 0.05)
L_button = Button(1025, 600, L_img, 0.05)
M_button = Button(1100, 600, M_img, 0.05)
N_button = Button(200, 700, N_img, 0.05)
O_button = Button(275, 700, O_img, 0.05)
P_button = Button(350, 700, P_img, 0.05)
Q_button = Button(425, 700, Q_img, 0.05)
R_button = Button(500, 700, R_img, 0.05)
S_button = Button(575, 700, S_img, 0.05)
T_button = Button(650, 700, T_img, 0.05)
U_button = Button(725, 700, U_img, 0.05)
V_button = Button(800, 700, V_img, 0.05)
W_button = Button(875, 700, W_img, 0.05)
X_button = Button(950, 700, X_img, 0.05)
Y_button = Button(1025, 700, Y_img, 0.05)
Z_button = Button(1100, 700, Z_img, 0.05)

running = True
while running:
    screen.fill((202, 228, 241))

    if A_button.draw() == True:
        print('A')
    if B_button.draw() == True:
        print('B')
    if C_button.draw() == True:
        print('C')
    if D_button.draw() == True:
        print('D')
    if E_button.draw() == True:
        print('E')
    if F_button.draw() == True:
        print('F')
    if G_button.draw() == True:
        print('G')
    if H_button.draw() == True:
        print('H')
    if I_button.draw() == True:
        print('I')
    if J_button.draw() == True:
        print('J')
    if K_button.draw() == True:
        print('K')
    if L_button.draw() == True:
        print('L')
    if M_button.draw() == True:
        print('M')
    if N_button.draw() == True:
        print('N')
    if O_button.draw() == True:
        print('O')
    if P_button.draw() == True:
        print('P')
    if Q_button.draw() == True:
        print('Q')
    if R_button.draw() == True:
        print('R')
    if S_button.draw() == True:
        print('S')
    if T_button.draw() == True:
        print('T')
    if U_button.draw() == True:
        print('U')
    if V_button.draw() == True:
        print('V')
    if W_button.draw() == True:
        print('W')
    if X_button.draw() == True:
        print('X')
    if Y_button.draw() == True:
        print('Y')
    if Z_button.draw() == True:
        print('Z')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()

pygame.quit()


import pygame

pygame.init()
pygame.font.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

display_surface = pygame.display.set_mode()

pygame.display.set_caption('Hangman game')

A_img = pygame.image.load('A.png').convert_alpha()
B_img = pygame.image.load('B.png').convert_alpha()
C_img = pygame.image.load('C.png').convert_alpha()
D_img = pygame.image.load('D.png').convert_alpha()
E_img = pygame.image.load('E.png').convert_alpha()
F_img = pygame.image.load('F.png').convert_alpha()
G_img = pygame.image.load('G.png').convert_alpha()
H_img = pygame.image.load('H.png').convert_alpha()
I_img = pygame.image.load('I.png').convert_alpha()
J_img = pygame.image.load('J.png').convert_alpha()
K_img = pygame.image.load('K.png').convert_alpha()
L_img = pygame.image.load('L.png').convert_alpha()
M_img = pygame.image.load('M.png').convert_alpha()
N_img = pygame.image.load('N.png').convert_alpha()
O_img = pygame.image.load('O.png').convert_alpha()
P_img = pygame.image.load('P.png').convert_alpha()
Q_img = pygame.image.load('Q.png').convert_alpha()
R_img = pygame.image.load('R.png').convert_alpha()
S_img = pygame.image.load('S.png').convert_alpha()
T_img = pygame.image.load('T.png').convert_alpha()
U_img = pygame.image.load('U.png').convert_alpha()
V_img = pygame.image.load('V.png').convert_alpha()
W_img = pygame.image.load('W.png').convert_alpha()
X_img = pygame.image.load('X.png').convert_alpha()
Y_img = pygame.image.load('Y.png').convert_alpha()
Z_img = pygame.image.load('Z.png').convert_alpha()

class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        movement = False

        position = pygame.mouse.get_pos()

        if self.rect.collidepoint(position):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                movement = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        screen.blit(self.image, (self.rect.x, self.rect.y))
        return movement

A_button = Button(200, 600, A_img, 0.05)
B_button = Button(275, 600, B_img, 0.05)
C_button = Button(350, 600, C_img, 0.05)
D_button = Button(425, 600, D_img, 0.05)
E_button = Button(500, 600, E_img, 0.05)
F_button = Button(575, 600, F_img, 0.05)
G_button = Button(650, 600, G_img, 0.05)
H_button = Button(725, 600, H_img, 0.05)
I_button = Button(800, 600, I_img, 0.05)
J_button = Button(875, 600, J_img, 0.05)
K_button = Button(950, 600, K_img, 0.05)
L_button = Button(1025, 600, L_img, 0.05)
M_button = Button(1100, 600, M_img, 0.05)
N_button = Button(200, 700, N_img, 0.05)
O_button = Button(275, 700, O_img, 0.05)
P_button = Button(350, 700, P_img, 0.05)
Q_button = Button(425, 700, Q_img, 0.05)
R_button = Button(500, 700, R_img, 0.05)
S_button = Button(575, 700, S_img, 0.05)
T_button = Button(650, 700, T_img, 0.05)
U_button = Button(725, 700, U_img, 0.05)
V_button = Button(800, 700, V_img, 0.05)
W_button = Button(875, 700, W_img, 0.05)
X_button = Button(950, 700, X_img, 0.05)
Y_button = Button(1025, 700, Y_img, 0.05)
Z_button = Button(1100, 700, Z_img, 0.05)

running = True
while running:
    screen.fill((202, 228, 241))

    if A_button.draw() == True:
        print('A')
    if B_button.draw() == True:
        print('B')
    if C_button.draw() == True:
        print('C')
    if D_button.draw() == True:
        print('D')
    if E_button.draw() == True:
        print('E')
    if F_button.draw() == True:
        print('F')
    if G_button.draw() == True:
        print('G')
    if H_button.draw() == True:
        print('H')
    if I_button.draw() == True:
        print('I')
    if J_button.draw() == True:
        print('J')
    if K_button.draw() == True:
        print('K')
    if L_button.draw() == True:
        print('L')
    if M_button.draw() == True:
        print('M')
    if N_button.draw() == True:
        print('N')
    if O_button.draw() == True:
        print('O')
    if P_button.draw() == True:
        print('P')
    if Q_button.draw() == True:
        print('Q')
    if R_button.draw() == True:
        print('R')
    if S_button.draw() == True:
        print('S')
    if T_button.draw() == True:
        print('T')
    if U_button.draw() == True:
        print('U')
    if V_button.draw() == True:
        print('V')
    if W_button.draw() == True:
        print('W')
    if X_button.draw() == True:
        print('X')
    if Y_button.draw() == True:
        print('Y')
    if Z_button.draw() == True:
        print('Z')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()

pygame.quit()


#retyped code
import pygame
SCREEN_HEIGHT = 720
SCREEN_WIDTH = 1280
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('HackathonHangman')

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

