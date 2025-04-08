# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word
    
    def match(self, my_anagrams):
        matches =[]
        sorted_word = sorted(self.word)

        for match in my_anagrams:
            if sorted(match.lower())== sorted_word:

                matches.append(match)

        return matches

