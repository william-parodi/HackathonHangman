import pygame
from button import Button
import time
import Words 
import random
import sys

pygame.init()

#Sets the display of the screen and the Title of the first scene
SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

#Sets the backkground for all the scenes
BG = pygame.image.load("assets/PurdueBackground.png")

#Sets the category 
category = "Standard"

#sets sounds for clicking the buttons 
BUTTON_SOUND = pygame.mixer.Sound('assets/buttonSound.wav')
BUTTON_SOUND.set_volume(0.2)

#sets music
BACKGROUND_MUSIC1 = pygame.mixer.Sound('assets/BeepBox-HailPurdue(MusicBox2).wav')
BACKGROUND_MUSIC2 = pygame.mixer.Sound('assets/BeepBox-HailPurdue(Creepy).wav')
BACKGROUND_MUSIC3 = pygame.mixer.Sound('assets/BeepBox-HailPurdue(Christmas).wav')
BACKGROUND_MUSIC1.set_volume(0.1)
BACKGROUND_MUSIC2.set_volume(0)
BACKGROUND_MUSIC3.set_volume(0)
BACKGROUND_MUSIC1.play(-1)
BACKGROUND_MUSIC2.play(-1)
BACKGROUND_MUSIC3.play(-1)

#establish variables for the colors
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
HANGMAN_ORIGIN = [645, 300]

#load the image files for the buttons
A_img = pygame.image.load('assets/A.png').convert_alpha()
B_img = pygame.image.load('assets/B.png').convert_alpha()
C_img = pygame.image.load('assets/C.png').convert_alpha()
D_img = pygame.image.load('assets/D.png').convert_alpha()
E_img = pygame.image.load('assets/E.png').convert_alpha()
F_img = pygame.image.load('assets/F.png').convert_alpha()
G_img = pygame.image.load('assets/G.png').convert_alpha()
H_img = pygame.image.load('assets/H.png').convert_alpha()
I_img = pygame.image.load('assets/I.png').convert_alpha()
J_img = pygame.image.load('assets/J.png').convert_alpha()
K_img = pygame.image.load('assets/K.png').convert_alpha()
L_img = pygame.image.load('assets/L.png').convert_alpha()
M_img = pygame.image.load('assets/M.png').convert_alpha()
N_img = pygame.image.load('assets/N.png').convert_alpha()
O_img = pygame.image.load('assets/O.png').convert_alpha()
P_img = pygame.image.load('assets/P.png').convert_alpha()
Q_img = pygame.image.load('assets/Q.png').convert_alpha()
R_img = pygame.image.load('assets/R.png').convert_alpha()
S_img = pygame.image.load('assets/S.png').convert_alpha()
T_img = pygame.image.load('assets/T.png').convert_alpha()
U_img = pygame.image.load('assets/U.png').convert_alpha()
V_img = pygame.image.load('assets/V.png').convert_alpha()
W_img = pygame.image.load('assets/W.png').convert_alpha()
X_img = pygame.image.load('assets/X.png').convert_alpha()
Y_img = pygame.image.load('assets/Y.png').convert_alpha()
Z_img = pygame.image.load('assets/Z.png').convert_alpha()

class Button2():
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

        SCREEN.blit(self.image, (self.rect.x, self.rect.y))
        return movement

A_button = Button2(200, 600, A_img, 0.05)
B_button = Button2(275, 600, B_img, 0.05)
C_button = Button2(350, 600, C_img, 0.05)
D_button = Button2(425, 600, D_img, 0.05)
E_button = Button2(500, 600, E_img, 0.05)
F_button = Button2(575, 600, F_img, 0.05)
G_button = Button2(650, 600, G_img, 0.05)
H_button = Button2(725, 600, H_img, 0.05)
I_button = Button2(800, 600, I_img, 0.05)
J_button = Button2(875, 600, J_img, 0.05)
K_button = Button2(950, 600, K_img, 0.05)
L_button = Button2(1025, 600, L_img, 0.05)
M_button = Button2(1100, 600, M_img, 0.05)
N_button = Button2(200, 700, N_img, 0.05)
O_button = Button2(275, 700, O_img, 0.05)
P_button = Button2(350, 700, P_img, 0.05)
Q_button = Button2(425, 700, Q_img, 0.05)
R_button = Button2(500, 700, R_img, 0.05)
S_button = Button2(575, 700, S_img, 0.05)
T_button = Button2(650, 700, T_img, 0.05)
U_button = Button2(725, 700, U_img, 0.05)
V_button = Button2(800, 700, V_img, 0.05)
W_button = Button2(875, 700, W_img, 0.05)
X_button = Button2(950, 700, X_img, 0.05)
Y_button = Button2(1025, 700, Y_img, 0.05)
Z_button = Button2(1100, 700, Z_img, 0.05)


    

def get_word(category):                              # generates word and changes it to uppercase
    if category=="Purdue":
        random_index = random.randint(0,32)
        word = Words.purdue_words[random_index]
    elif category=="Halloween":
        random_index = random.randint(0,32)
        word = Words.halloween_words[random_index]
    elif category=="Christmas":
        random_index = random.randint(0,32)
        word = Words.christmas_words[random_index]
    return word.upper()

#animates the hangman based on the number of tries left 
def hangman_animation(tries):
   if tries <= 5: 
      pygame.draw.circle(SCREEN, red, (HANGMAN_ORIGIN[0], HANGMAN_ORIGIN[1]-50), 25) #draws the head: 1st miss
      if tries <= 4:
         pygame.draw.line(SCREEN, red, (HANGMAN_ORIGIN[0], HANGMAN_ORIGIN[1]-50), (HANGMAN_ORIGIN[0], HANGMAN_ORIGIN[1]+50), 5) #draws the body: 2nd miss
         if tries <= 3:
            pygame.draw.line(SCREEN, red, (HANGMAN_ORIGIN[0]-50, HANGMAN_ORIGIN[1]), (HANGMAN_ORIGIN[0], HANGMAN_ORIGIN[1]), 5) #draws the left arm: 3rd miss
            if tries <= 2:
               pygame.draw.line(SCREEN, red, (HANGMAN_ORIGIN[0], HANGMAN_ORIGIN[1]), (HANGMAN_ORIGIN[0]+50, HANGMAN_ORIGIN[1]), 5) #draws the right arm: 4th miss 
               if tries <= 1:
                  pygame.draw.line(SCREEN, red, (HANGMAN_ORIGIN[0]-25, HANGMAN_ORIGIN[1]+75), (HANGMAN_ORIGIN[0], HANGMAN_ORIGIN[1]+50), 5) #draws left leg: 5th miss
                  if tries <= 0:
                     pygame.draw.line(SCREEN, red, (HANGMAN_ORIGIN[0], HANGMAN_ORIGIN[1]+50), (HANGMAN_ORIGIN[0]+25, HANGMAN_ORIGIN[1]+75), 5) #draws right leg
                     pygame.draw.circle(SCREEN, black, (HANGMAN_ORIGIN[0]+10, HANGMAN_ORIGIN[1]-60), 3) #draws eyes
                     pygame.draw.circle(SCREEN, black, (HANGMAN_ORIGIN[0]-10, HANGMAN_ORIGIN[1]-60), 3) #draws eyes
                     pygame.draw.line(SCREEN, black, (HANGMAN_ORIGIN[0]-10, HANGMAN_ORIGIN[1]-50), (HANGMAN_ORIGIN[0]+10, HANGMAN_ORIGIN[1]-50), 5) #Draws mouth


#Draws the noose to hang the hangman 
def draw_noose(x, y):
    pygame.draw.line(SCREEN, black, (x-50, y), (x+50, y), 7)
    pygame.draw.line(SCREEN, black, (x, y), (x, y-200), 5)
    pygame.draw.line(SCREEN, black, (x, y-200), (x+45, y-200), 5)
    pygame.draw.line(SCREEN, black, (x+45, y-200), (x+45, y-175), 5)

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

#The main scene where the gameplay takes place
def play(word):
    
    tries = 6
    wordLength = len(word)                   
    word_completion = "_ " * wordLength      # displays _ for the number of letters in the word
    guessed = False
    guessed_letters = []
    guessed_words = []
    word_completion_list =  list(word)
    word_as_list = list(word)                #Makes a letter equivalent of word_completion_list to allow us to compare word_completion to the actual word
    for i in range (len(word_completion_list)):
      if not(word_completion_list[i] == " "):word_completion_list[i] = ' _ '
    for i in range (len(word_as_list)):
      if not(word_as_list[i] == " "): word_as_list[i] = " " + word_as_list[i] + " "
    word_completion = "".join(word_completion_list)
    word_compare = "".join(word_as_list)



    while not(guessed) and tries > 0:
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

        PLAY_MOUSE_POS = pygame.mouse.get_pos() #Gets the position of the mouse 

        SCREEN.blit(BG, (0, 0))

        PLAY_TEXT = get_font(45).render("Hello Hangman", True, "White") #Title of the playing screen
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 50))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        #sets the back and quit buttons
        PLAY_BACK = Button(image=None, pos=(120, 690), 
                            text_input="BACK", font=get_font(40), base_color="White", hovering_color="Green")
        PLAY_QUIT = Button(image=None, pos=(1150, 690), 
                            text_input="QUIT", font=get_font(40), base_color="White", hovering_color="Green")
        
        
        
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        PLAY_QUIT.changeColor(PLAY_MOUSE_POS)
        PLAY_QUIT.update(SCREEN)

        draw_noose(600, 400)        #Draws the noose for the hangman

        
        hangman_animation(tries) 
        
       

        WORD_TEXT = get_font(30).render(word_completion, True, "Black")
        WORD_RECT = WORD_TEXT.get_rect(center=(640, 150))
        SCREEN.blit(WORD_TEXT, WORD_RECT)

        #Handles events in the hangman game
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN: 
               if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                  BUTTON_SOUND.play()
                  options()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_QUIT.checkForInput(PLAY_MOUSE_POS):
                  pygame.quit()
                  sys.exit()

            
               


        pygame.display.update()
      #   answer_key = list(word)                #creates a list of words to call when the program wants to replace the underscores with the uncovered letters
      #   iguess = input("Guess a letter or a word: ")        # converts user input to uppercase
      #   guess = iguess.upper()
      #   if (len(guess) == 1 and guess.isalpha()):                    # user guesses a valid letter in the alphabet
      #         if guess in guessed_letters:                             # user repeats a guess
      #             print("You already guessed this letter:", guess)
      #         elif guess not in word:                                  # user guesses a wrong letter
      #             print("Oops! The letter you guessed is not in the word :(")
      #             tries -= 1                                           # no. of tries decreased
      #             guessed_letters.append(guess)                        # the guess is added to the list of guessed letters
      #         else:                                                    # user guesses a correct letter
      #             print("Yay! The letter you guessed is in the word :)")
      #             guessed_letters.append(guess)                        # the guess is added to the list of guessed letters
      #             word_completion_as_list = list(word_completion)     # update word_completion to reveal all occurences of the guessed letter. convert word_completion from a string to a list so we can index into it
      #             word_as_list = list(word_compare)
      #             for i in range (len(word_completion_as_list)-1):                #reveals all instances of the guessed letter
      #                if guess == word_as_list[i]:
      #                   word_completion_as_list[i] = guess
      #                word_completion = "".join(word_completion_as_list)
      #             if "_" not in word_completion:                       # to check if the guessed letter completes the word
      #                guessed = True
      #   elif (len(guess) == 1 and guess.isalpha()):                    # user guesses a valid letter in the alphabet
      #         if guess in guessed_letters:                             # user repeats a guess
      #            print("You already guessed this letter:", guess)
      #         elif guess not in word:                                  # user guesses a wrong letter
      #            print("Oops! The letter you guessed is not in the word :(")
      #            tries -= 1                                           # no. of tries decreased
      #            guessed_letters.append(guess)                        # the guess is added to the list of guessed letters
      #         else:
      #            guessed = True
      #            word_completion = word
      #   else:                                                        # if user gives an invalid input
      #         print("Not a valid guess.")
      #   hangman_animation(tries)                                     # displays state of the hangman after each guess             
      #   print(word_completion)                                       # displays current status of the word being guessedprint("\n")
      #   if guessed:
      #         print("WOHOOO! You guessed the word!")
      #         activate_guess = False

      #   elif tries <= 0:
      #         print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")
      #         activate_guess = False

            
        



#options screen that allows user to select the category of their game
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG, (0, 0))

        OPTION1_BUTTON = Button(image=pygame.image.load("assets/Options_Rect.png"), pos=(640, 200), 
                            text_input="Purdue", font=get_font(75), base_color="White", hovering_color="#d7fcd4")
        OPTION2_BUTTON = Button(image=pygame.image.load("assets/Options_Rect.png"), pos=(640, 400), 
                            text_input="Halloween", font=get_font(75), base_color="White", hovering_color="#d7fcd4")
        OPTION3_BUTTON = Button(image=pygame.image.load("assets/Options_Rect.png"), pos=(640, 600), 
                            text_input="Christmas", font=get_font(75), base_color="White", hovering_color="#d7fcd4")

        for button in [OPTION1_BUTTON, OPTION2_BUTTON, OPTION3_BUTTON]:
            button.changeColor(OPTIONS_MOUSE_POS)
            button.update(SCREEN)

        OPTIONS_TEXT = get_font(45).render("Pick your theme!", True, "White")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 50))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(120, 690), 
                            text_input="BACK", font=get_font(40), base_color="White", hovering_color="Green")
        OPTIONS_QUIT = Button(image=None, pos=(1150, 690), 
                            text_input="QUIT", font=get_font(40), base_color="White", hovering_color="Green")


        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)
        OPTIONS_QUIT.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_QUIT.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    BUTTON_SOUND.play()
                    main_menu()
            if event.type == pygame.MOUSEBUTTONDOWN:
            	if OPTION1_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                  category = "Purdue"
                  BUTTON_SOUND.play()
                  BACKGROUND_MUSIC1.set_volume(0.1)
                  BACKGROUND_MUSIC2.set_volume(0)
                  BACKGROUND_MUSIC3.set_volume(0)
                  play(get_word(category))
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTION2_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    category = "Halloween"
                    BUTTON_SOUND.play()
                    BACKGROUND_MUSIC1.set_volume(0)
                    BACKGROUND_MUSIC2.set_volume(0.1)
                    BACKGROUND_MUSIC3.set_volume(0)
                    play(get_word(category))
            if event.type == pygame.MOUSEBUTTONDOWN:
            	if OPTION3_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                  category = "Christmas"
                  BUTTON_SOUND.play()
                  BACKGROUND_MUSIC1.set_volume(0)
                  BACKGROUND_MUSIC2.set_volume(0)
                  BACKGROUND_MUSIC3.set_volume(0.1)
                  play(get_word(category))
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_QUIT.checkForInput(OPTIONS_MOUSE_POS):
                    pygame.quit()
                    sys.exit()            		

        pygame.display.update()

#start menu
def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(90).render("Hello Hangman", True, "White")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play_Rect.png"), pos=(640, 300), 
                            text_input="PLAY", font=get_font(75), base_color="White", hovering_color="#d7fcd4")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit_Rect.png"), pos=(640, 500), 
                            text_input="QUIT", font=get_font(75), base_color="White", hovering_color="#d7fcd4")

        #sets images
        image = pygame.image.load('assets/PurdueP.png')
        image = pygame.transform.scale(image, (275,275))
        image2 = pygame.image.load('assets/PurdueLogo.png')
        image2 = pygame.transform.scale(image2, (300,300))

        SCREEN.blit(MENU_TEXT, MENU_RECT)
        SCREEN.blit(image2,(900, 250))
        SCREEN.blit(image,(50, 260))

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    BUTTON_SOUND.play()
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()