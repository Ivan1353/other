'''
The hangman game is a word guessing game where the player is given a word and has to guess the letters that make up the word. 
The player is given a certain number of tries (no more than 6 wrong guesses are allowed) to guess the correct letters before the game is over.
'''

# Output
'''
You have 6 tries left.                                                                                                                                           
Used letters:                                                                                                                                                    
Word: _ _ _ _                                                                                                                                                    
Guess a letter: a 

You have 6 tries left.                                                                                                                                           
Used letters: a                                                                                                                                                  
Word: _ a _ a                                                                                                                                                    
Guess a letter: j    

You have 6 tries left.                                                                                                                                           
Used letters: j a                                                                                                                                                
Word: j a _ a                                                                                                                                                    
Guess a letter: v                                                                                                                                                
You guessed the word java !
'''

from random_word import RandomWords
word_generator = RandomWords()

word = word_generator.get_random_word()
tries = 6
guessword = ["_ " for x in range (len(word))]
used_letters = []

while word != "".join(guessword):
    print(f"\nYou have {tries} tries left")
    print("".join(guessword))
    print(f"Used letters: {', '.join(used_letters)}")
    letter = input("What letter would you guess?")
    if letter in used_letters:
        print("Letter already used.")
        continue
    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                guessword[i] = letter
    else:
        print("You guessed wrong.")
        tries -= 1

    used_letters.append(letter)

    if tries <=0:
        print("You have been hanged.")
        break

