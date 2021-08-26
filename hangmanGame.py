import random
from word_list import words

def replay():
    play_again = input("Would you like to start over? Yes or No").title().strip()
    if play_again == "Yes":
        main_game()
    elif play_again == "No":
        print("Thank you so much for playing my game. I hope you have had an enjoyable experience")
    else:
        print("Invalid input")

def get_word():
    word = random.choice(words)
    return word

def main_game():
    welcome = input("Welcome to my hangman game, are you ready? Yes or No").title().strip()
    if welcome == "Yes":
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        secret_word = get_word()
        guessed_letters = []
        tries = 10
        done = False # assign a False keyword to done 

        print(f"The secret word has {len(secret_word)} characters.")
        print(len(secret_word) * "_")
            
        while done == False and tries > 0: # while user has not found the word 
            user_guess = input(f"You have {tries} tries. Enter a letter or a word: ").lower().strip()
            if len(user_guess) == 1:  
                if user_guess in guessed_letters:
                    print("You already guessed that letter")
                elif user_guess in secret_word: 
                    print("Correct! This letter exists in the secret word") 
                    guessed_letters.append(user_guess)
                elif user_guess not in secret_word: 
                    print("The letter you entered is incorrect")
                    guessed_letters.append(user_guess)
                    tries -= 1
                else: 
                    print("Invalid input") 
                    tries -= 1 
                    
            elif len(user_guess) == len(secret_word):
                if user_guess == secret_word: 
                    print("Well done! You have found the word")
                    done = True    
                elif user_guess != secret_word: # check 
                    print("That is not the word you are looking for")
                    tries -= 1 
                
            else: 
                print("The word you enter does not match the length of the secret word")
                tries -= 1
                
            status = ""
            if done == False:
                for letter in secret_word:
                    if letter in guessed_letters:
                        status += letter
                    else:
                        status += "_"
                print(status)
                
            if status == secret_word:
                print("Well done! You have found the word")
                done = True
            elif tries == 0:
                print("Game over ! You have no tries left. The secret word is " + secret_word)
        
    elif welcome == "No":
        print("That's alright. You can come back once you are ready")
    else: 
        print("Invalid input")

    replay() 

main_game()