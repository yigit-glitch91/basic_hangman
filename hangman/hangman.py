import random
import hangman_art
import words
word=random.choice(words.city_list)
correct_letters = []
placeholder=""
game_over= False
lives = 6
print('''
      
WELCOME TO GUESS THE CİTY GAME WİTH HANGMAN...''')
word_length=len(word)
for position in range(word_length):
    placeholder += "_"

print(placeholder)


while not game_over:
    
    guess=input("GUESS A LETTER: ").lower()
    display=""

    for letter in word:
        if letter == guess:
            display+= letter
            correct_letters.append(letter)
        
        elif letter in correct_letters:
            display += letter

        else:
            display += "_"

    if(guess not in word):
        lives -= 1
        if lives == 0:
            game_over = True
            print("LOSE! :D HİHİHİHAHA")
            print(word)
    


    if "_" not in display:
        game_over = True
        print("YOU WİN! AND YOU STILL HAVE " + str(lives - 1) + " LIVES...")
    

    if ("_" in display):
        print(display)

    
    elif ("_" not in display):
        print(word)

    

    print(hangman_art.HANGMANPICS[lives])
