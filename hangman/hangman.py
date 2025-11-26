import random
import hangman_art
import words
word=random.choice(words.city_list)
correct_letters = []
placeholder=""
game_over= False
lives = 6
print('''
      
ŞEHİR BİLMECE OYUNUNA HOŞGELDİN...''')
word_length=len(word)
for position in range(word_length):
    placeholder += "_"

print(placeholder)


while not game_over:
    
    guess=input("Bir harf tahmin et: ").lower()
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
            print("Kaybettin")
            print(word)
    


    if "_" not in display:
        game_over = True
        print("Kazandın! Ve hala " + str(lives - 1) + " canın vardı...")
    

    if ("_" in display):
        print(display)

    
    elif ("_" not in display):
        print(word)

    
    print(hangman_art.HANGMANPICS[lives])