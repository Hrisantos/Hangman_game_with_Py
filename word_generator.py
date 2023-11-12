import random

with open(file="words.txt", mode="w") as f:
    w = f.writelines([
        "python\n",
        "mangusta\n",
        "arici\n",
        "viezure"
    ])

class WorldGenerator:

    def __init__(self, filename="words.txt"):
        self.filename = filename
        self.words = self.get_all_words(filename)

    def get_all_words(self, filename):
        try:
            with open(file=filename, mode="r") as f:
                words = f.read().splitlines()
                return words
        except FileNotFoundError:
            print(f"Error: {filename} not found.")
            return []

    def get_random_words(self):
        if self.words:
            secret_word = random.choice(self.words)
            return secret_word
        else:
            return "Random"
