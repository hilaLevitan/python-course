import random
class Game:
    def __init__(self, words_list):
        self.words_list = words_list
        self.word_to_guess = ""
        self.max_turns = 10
        self.current_turn = 0
        self.mismatched_letters = []
        self.worng_letters = []
        self.not_done = True
        pass

    def generate_random_word(self):
        idx = random.randint(0,len(self.words_list)-1)
        self.word_to_guess = self.words_list[idx]

    def play_turn(self):
        self.current_turn+=1
        guess = self.get_valid_input()
        guess = guess.lower()
        if guess == self.word_to_guess:
            self.not_done = False
        else:
            self.compare_chars(guess)
            print(f"mismatched: {', '.join(self.mismatched_letters)}") # [print(ch, ", ",end="") for ch in mismatch_letters]
            print(f"worng: {(', '.join(self.worng_letters))}")
            print(f"you have {self.max_turns - self.current_turn} turns left")


    def play(self):
        self.generate_random_word()
        while self.not_done and self.max_turns > self.current_turn:
            self.play_turn()
        if self.max_turns == self.current_turn:
            print('''
 __   _____  _   _   _     ___  ____ _____ 
 \ \ / / _ \| | | | | |   / _ \/ ___|_   _|
  \ V / | | | | | | | |  | | | \___ \ | |  
   | || |_| | |_| | | |__| |_| |___) || |  
   |_| \___/ \___/  |_____\___/|____/ |_|  
                                           ''')
        else:
            print('''
__     __  ____   _    _        __        __   ___   _   _    _   _ 
\ \   / / / __ \ | |  | |       \ \      / /  / _ \ | \ | |  | | | |
 \ \_/ / | |  | || |  | |        \ \ /\ / /  | | | ||  \| |  | | | |
  \   /  | |  | || |  | |         \ V  V /   | | | || . ` |  | | | |
   | |   | |__| || |__| |          | | | |   | |_| || |\  |  |_| |_|
   |_|    \____/  \____/           |_| |_|    \___/ |_| \_|  (_) (_)''')

    def get_valid_input(self):
        guess = input(f"enter your guess (should be {len(self.word_to_guess)} length)")
        while not self.is_valid_guess(guess):
            guess = input("please enter a valid guess")
        return guess

    def is_valid_guess(self, guess:str):
        return len(self.word_to_guess) == len(guess) and guess.isalpha()
    
    def compare_chars(self, guess:str):
        for idx, char in enumerate(self.word_to_guess):
            if char == guess[idx]:
                print(char, end="")
                if char in self.mismatched_letters: 
                    self.mismatched_letters.remove(char)
            elif guess[idx] in self.word_to_guess:
                print("_", end="")
                if guess[idx] not in self.mismatched_letters:
                    self.mismatched_letters.append(guess[idx])
            else:
                print("_", end="")
                if guess[idx] not in self.worng_letters:
                    self.worng_letters.append(guess[idx])
        print()
    
    def reset(self):
        self.word_to_guess = ""
        self.max_turns = 10
        self.current_turn = 0
        self.mismatched_letters = []
        self.worng_letters = []
        self.not_done = True