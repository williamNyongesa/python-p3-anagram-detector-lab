# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, word_list):
        return[w for w in word_list if sorted(w) == sorted(self.word) ]
