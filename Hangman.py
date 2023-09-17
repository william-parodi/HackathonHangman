import pygame
from button import Button
import time
import Words 
import random
import sys

pygame.init()

#Sets the display of the screen and the Title of the first scene
SCREEN = pygame.display.set_mode((1408, 792))
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
BACKGROUND_MUSIC1.set_volume(0.2)
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
HANGMAN_ORIGIN = [745, 400]   

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
result = ""
def play(word):
    result = word
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

    active = False

    while not(guessed) and tries > 0:

        PLAY_MOUSE_POS = pygame.mouse.get_pos() #Gets the position of the mouse 

        SCREEN.blit(BG, (0, 0))

        PLAY_TEXT = get_font(45).render("Hello Hangman", True, "White") #Title of the playing screen
        PLAY_RECT = PLAY_TEXT.get_rect(center=(700, 50))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        #sets the back and quit buttons
        PLAY_BACK = Button(image=None, pos=(120, 690), 
                            text_input="BACK", font=get_font(40), base_color="White", hovering_color="Green")
        PLAY_QUIT = Button(image=None, pos=(1250, 690), 
                            text_input="QUIT", font=get_font(40), base_color="White", hovering_color="Green")
        
        
        
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        PLAY_QUIT.changeColor(PLAY_MOUSE_POS)
        PLAY_QUIT.update(SCREEN)

        draw_noose(700, 500)        #Draws the noose for the hangman

        
        hangman_animation(tries) 
        
       

        WORD_TEXT = get_font(20).render(word_completion, True, "Black")
        WORD_RECT = WORD_TEXT.get_rect(center=(700, 180))
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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    iguess = 'a'
                    active = True
                    print("a")
                if event.key == pygame.K_b:
                    iguess = 'b'
                    active = True
                if event.key == pygame.K_c:
                    iguess = 'c' 
                    active = True
                if event.key == pygame.K_d:
                    iguess = 'd'
                    active = True
                if event.key == pygame.K_e:
                    iguess = 'e'
                    active = True
                if event.key == pygame.K_f:
                    iguess = 'f'
                    active = True
                if event.key == pygame.K_g:
                    iguess = 'g'
                    active = True
                if event.key == pygame.K_h:
                    iguess = 'h'
                    active = True
                if event.key == pygame.K_i:
                    iguess = 'i'
                    active = True
                if event.key == pygame.K_j:
                    iguess = 'j'
                    active = True
                if event.key == pygame.K_k:
                    iguess = 'k'
                    active = True
                if event.key == pygame.K_l:
                    iguess = 'l'
                    active = True
                if event.key == pygame.K_m:
                    iguess = 'm'
                    active = True
                if event.key == pygame.K_n:
                    iguess = 'n'
                    active = True
                if event.key == pygame.K_o:
                    iguess = 'o'
                    active = True
                if event.key == pygame.K_p:
                    iguess = 'p'
                    active = True
                if event.key == pygame.K_q:
                    iguess = 'q'
                    active = True
                if event.key == pygame.K_r:
                    iguess = 'r'
                    active = True
                if event.key == pygame.K_s:
                    iguess = 's'
                    active = True
                if event.key == pygame.K_t:
                    iguess = 't'
                    active = True
                if event.key == pygame.K_u:
                    iguess = 'u'
                    active = True
                if event.key == pygame.K_v:
                    iguess = 'v'
                    active = True
                if event.key == pygame.K_w:
                    iguess = 'w'
                    active = True
                if event.key == pygame.K_x:
                    iguess = 'x'
                    active = True
                if event.key == pygame.K_y:
                    iguess = 'y'
                    active = True
                if event.key == pygame.K_z:
                    iguess = 'z'
                    active = True
               


        pygame.display.update()
        if active:
         answer_key = list(word)                #creates a list of words to call when the program wants to replace the underscores with the uncovered letters
         # converts user input to uppercase
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
         elif (len(guess) == 1 and guess.isalpha()):                    # user guesses a valid letter in the alphabet
               if guess in guessed_letters:                             # user repeats a guess
                  print("You already guessed this letter:", guess)
               elif guess not in word:                                  # user guesses a wrong letter
                  print("Oops! The letter you guessed is not in the word :(")
                  tries -= 1                                           # no. of tries decreased
                  guessed_letters.append(guess)                        # the guess is added to the list of guessed letters
               else:
                  guessed = True
                  word_completion = word
         else:                                                        # if user gives an invalid input
             print("Not a valid guess.")
             hangman_animation(tries)                                     # displays state of the hangman after each guess             
             print(word_completion)                                       # displays current status of the word being guessedprint("\n")
        if guessed:
            print("WOHOOO! You guessed the word!")
            win()
               #activate_guess = False

        elif tries <= 0:
            print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")
            lose()
               #activate_guess = False
        
def win():
    while True:
        WIN_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG, (0, 0))

        WIN_TEXT = get_font(35).render("WOHOOO! You guessed the word!", True, "Green")
        WIN_RECT = WIN_TEXT.get_rect(center=(700, 350))
        SCREEN.blit(WIN_TEXT, WIN_RECT)

        WIN_BACK = Button(image=None, pos=(120, 690), 
                            text_input="BACK", font=get_font(40), base_color="White", hovering_color="Green")
        WIN_QUIT = Button(image=None, pos=(1250, 690), 
                            text_input="QUIT", font=get_font(40), base_color="White", hovering_color="Green")

        WIN_BACK.changeColor(WIN_MOUSE_POS)
        WIN_BACK.update(SCREEN)
        WIN_QUIT.changeColor(WIN_MOUSE_POS)
        WIN_QUIT.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if WIN_BACK.checkForInput(WIN_MOUSE_POS):
                    BUTTON_SOUND.play()
                    options()
            if event.type == pygame.MOUSEBUTTONDOWN:
            	if WIN_QUIT.checkForInput(WIN_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
        pygame.display.update()

def lose():
    while True:
        LOSE_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG, (0, 0))
        print (result)

        LOSE_TEXT = get_font(35).render("Sorry! You're out of tries!", True, "Red")

        LOSE_RECT = LOSE_TEXT.get_rect(center=(700, 350))
        SCREEN.blit(LOSE_TEXT, LOSE_RECT)

        LOSE_BACK = Button(image=None, pos=(120, 690), 
                            text_input="BACK", font=get_font(40), base_color="White", hovering_color="Green")
        LOSE_QUIT = Button(image=None, pos=(1250, 690), 
                            text_input="QUIT", font=get_font(40), base_color="White", hovering_color="Green")

        LOSE_BACK.changeColor(LOSE_MOUSE_POS)
        LOSE_BACK.update(SCREEN)
        LOSE_QUIT.changeColor(LOSE_MOUSE_POS)
        LOSE_QUIT.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if LOSE_BACK.checkForInput(LOSE_MOUSE_POS):
                    BUTTON_SOUND.play()
                    options()
            if event.type == pygame.MOUSEBUTTONDOWN:
            	if LOSE_QUIT.checkForInput(LOSE_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
        pygame.display.update()

#options screen that allows user to select the category of their game
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG, (0, 0))

        OPTION1_BUTTON = Button(image=pygame.image.load("assets/Options_Rect.png"), pos=(700, 200), 
                            text_input="Purdue", font=get_font(55), base_color="White", hovering_color="#d7fcd4")
        OPTION2_BUTTON = Button(image=pygame.image.load("assets/Options_Rect.png"), pos=(700, 400), 
                            text_input="Halloween", font=get_font(55), base_color="White", hovering_color="#d7fcd4")
        OPTION3_BUTTON = Button(image=pygame.image.load("assets/Options_Rect.png"), pos=(700, 600), 
                            text_input="Christmas", font=get_font(55), base_color="White", hovering_color="#d7fcd4")

        for button in [OPTION1_BUTTON, OPTION2_BUTTON, OPTION3_BUTTON]:
            button.changeColor(OPTIONS_MOUSE_POS)
            button.update(SCREEN)

        OPTIONS_TEXT = get_font(45).render("Pick your category!", True, "White")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(700, 50))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(120, 690), 
                            text_input="BACK", font=get_font(40), base_color="White", hovering_color="Green")
        OPTIONS_QUIT = Button(image=None, pos=(1250, 690), 
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
                  BACKGROUND_MUSIC1.set_volume(0.2)
                  BACKGROUND_MUSIC2.set_volume(0)
                  BACKGROUND_MUSIC3.set_volume(0)
                  play(get_word(category))
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTION2_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    category = "Halloween"
                    BUTTON_SOUND.play()
                    BACKGROUND_MUSIC1.set_volume(0)
                    BACKGROUND_MUSIC2.set_volume(0.2)
                    BACKGROUND_MUSIC3.set_volume(0)
                    play(get_word(category))
            if event.type == pygame.MOUSEBUTTONDOWN:
            	if OPTION3_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                  category = "Christmas"
                  BUTTON_SOUND.play()
                  BACKGROUND_MUSIC1.set_volume(0)
                  BACKGROUND_MUSIC2.set_volume(0)
                  BACKGROUND_MUSIC3.set_volume(0.2)
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
        MENU_RECT = MENU_TEXT.get_rect(center=(690, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play_Rect.png"), pos=(690, 350), 
                            text_input="PLAY", font=get_font(75), base_color="White", hovering_color="#d7fcd4")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit_Rect.png"), pos=(690, 550), 
                            text_input="QUIT", font=get_font(75), base_color="White", hovering_color="#d7fcd4")

        #sets images
        image = pygame.image.load('assets/PurdueP.png')
        image = pygame.transform.scale(image, (275,275))
        image2 = pygame.image.load('assets/PurdueLogo.png')
        image2 = pygame.transform.scale(image2, (300,300))

        SCREEN.blit(MENU_TEXT, MENU_RECT)
        SCREEN.blit(image2,(950, 300))
        SCREEN.blit(image,(100, 300))

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