"""Word Finder: finds random words from a dictionary."""
import random
word_txt = open('words.txt', 'r')
class WordFinder:
    def __init__(self,path):
    
        word_txt = open(path)

        self.words = self.parse(word_txt)
    
        print(f"{len(self.words)} words read")
    
    def parse(self, word_txt):

        return [w.strip() for w in word_txt]
    
    def random(self):

        return random.choice(self.words)
    
class SpecialWordFinder(WordFinder):

    def parse(self, word_txt):

        return [w.strip() for w in word_txt if w.strip() and not w.startswith('#')]