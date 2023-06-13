# ------------------------- BASKETBALL GAME --------------------------
import random
from basketball_art import logo
from basketball_words import word_list

#Randomly choose a word from the word_list and assign it to a varible word
chosen_word = random.choice(word_list)
# get word length
word_length = len(chosen_word)
# print logo
print(logo)    
             
#set end of game varaible to flase
end_of_game = False

# set game life count, 6 lives
lives = 5

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create an empty List called display.
# this will keep track of your empty spaces for the user during the game
display = []

#For each letter in the word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
for _ in range(word_length):
    display += "_"


end_of_game = False

# while the game is not over

while not end_of_game:
    
    #Ask the user to guess a letter and assign their answer to a variable called guess. make guess lowercase 
    guess = input("Please guess a letter: ").lower()
    
    # if the user has already guessed an entry, print the letter and let them know 
    if guess in display:
        print(f"You've already guessed {guess}")

    #Loop through each position in the chosen_word;
    #If the letter at that position matches 'guess' then reveal that letter in the display at that position.
    #e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
    '''Check guessed letter'''
    for position in range(word_length):
        # letter is the letter obtained from the word at this iteration of the loop
        letter = chosen_word[position]
        # if the user guesses correctly -------------------------------------------- CORRECT
        # The letter found in the random word selected should match the letter given by the user 
        if letter == guess :
            # update the display list with the user input for that exact position
            display[position] = letter
            # let them know they guessed right
            print("CORRECT!")
            #print(f"Current position: {position}\n Current letter:{letter}\n Guessed letter: {guess}")
        
    # if user guesses incorrectly -------------------------------------------- INCORRECT
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. you lose a life.")
        # subtract 1 from lives list
        lives = lives - 1
        # let the user know 
        # print("INCORRECT!")
        # check life count, if 0 then terminate game
        if lives == 0:
            end_of_game = True
            print("you lose.")
    
    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")        

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")
                 
    from basketball_art import stages 
    # print the basketball stage the user is in 
    print(stages[lives])