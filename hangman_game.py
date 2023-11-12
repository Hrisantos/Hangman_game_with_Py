from word_generator import WorldGenerator

class HangmanGame:

    def __init__(self, max_lives=6):
        self.max_lives = max_lives
        self.word_generator = WorldGenerator()
        self.__secret_word = self.word_generator.get_random_words().upper()
        self.display_word = '_' * len(self.__secret_word)
        self.guesses = []
        self.lives_left = self.max_lives

    def display_game_status(self):
        print(f"Word: {self.display_word}")
        print(f"Lives left: {self.lives_left}")
        print(f"Guessed letters: {', '.join(self.guesses)}")


    def guess_letter(self, letter):
        letter = letter.upper()

        if letter in self.guesses:
            print(f"You've already guessed the letter {letter}. Try again.")
        else:
            self.guesses.append(letter)

            if letter not in self.__secret_word:
                self.lives_left -= 1
                print("Incorrect guess")
            else:
                for i in range(len(self.__secret_word)):
                    if self.__secret_word[i] == letter:
                        self.display_word = self.display_word[:i] + letter + self.display_word[i + 1:]
                print("Good guess!")

    def is_game_over(self):
        return self.lives_left == 0 or '_' not in self.display_word

    def play(self):
        print("Welcome to Hangman!")
        while not self.is_game_over():
            self.display_game_status()
            guess = input("Guess a letter: ")
            self.guess_letter(guess)

        if '_' not in self.display_word:
            print(f"Congratulations! You guessed the word: {self.__secret_word}")
        else:
            print(f"Game over! The word was: {self.__secret_word}")
