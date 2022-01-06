
import random
import animation
import words

choosen_word = random.choice(words.word)
print(choosen_word)
blank_word = []
for x in choosen_word:
    blank_word.append("_")
print(blank_word)
check_word = ""
lives = 6

game_stats = True
while check_word != choosen_word and game_stats == True:
    
   
    word_input = input("Choose any letter. ")
    x = 0
    for letter in choosen_word:
        if word_input == letter:
            blank_word[x] = word_input
        x += 1
    if word_input in choosen_word:
        print(animation.stages[lives])
    else :
        lives -= 1
        print(animation.stages[lives])
        if lives == 0:
            game_stats = False
    check_word = ''.join(blank_word)
    print(blank_word)
