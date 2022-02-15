'''
Rules :
    * In the "keyword.txt" file is a word that the user has to guess (hidden word)
    * In order to guess it, the user must input a word of the same length as the chosen word in the file
    * The user will be given a word made of characters with the following meaning :
        - "*" means that the letter in this position is placed correctly in the hidden word
        _ "+" means that the letter in this position exists is the hidden word
        - "?" means that the letter in this position doesn't exist in the hidden word
    * The goal is to find the word in as few tries as possible.
'''
try:
    file = open("keyword.txt", "r")
except:
    print("Error opening file")
keyword = file.readline().lower()
file.close()

finish = False
count = 0


def exists(letter, keyword):
    return letter in keyword


def is_placed_correctly(letter, keyword, position):
    return keyword[position] == letter

while finish == False:
    user_guess = input("Please input a word of length " + str(len(keyword)) + " :").lower()
    help_word = ""
    i = 0
    if len(user_guess) != len(keyword):
        continue
    if user_guess == keyword:
        finish = True
    else:
        for letter in user_guess:
            if exists(letter, keyword) and is_placed_correctly(letter, keyword, i):
                help_word = help_word + "*"
            elif exists(letter, keyword):
                help_word = help_word + "+"
            else:
                help_word = help_word + "?"
            i += 1
    print(help_word)
    count += 1
print("you guessed the word after " + str(count) + " guesses !")

