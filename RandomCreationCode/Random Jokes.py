#Random Jokes by Miles Burne
import random

#creates random jokes
class RandomJoke():
    #init
    def __init__(self):
        self.dict_length = 0
        self.english_dict = self.get_dict()
        self.format_string = ("Knock knock! Who's there? {firstWord}. {firstWord} who? {firstWord} {secondWord}")
        #words
        self.word_dict = {}
        
    #unpacking data
    def get_dict(self):
        #getting file
        f = open("English_Dictionary.txt","r")
        file = f.read()
        f.close()
        #turning into dict
        words = file.split("\n")
        english_dict = {i : words[i] for i in range(0, len(words))}
        #getting len
        self.dict_length = len(words)
        #returning
        return(english_dict)
    
    #picking random
    def get_words(self):
        #getting numbers
        first_word_number = random.randint(0, self.dict_length-1)
        second_word_number = random.randint(0, self.dict_length-1)
        #getting words
        first_word = self.english_dict[first_word_number]
        second_word = self.english_dict[second_word_number]
        #word dict
        self.word_dict = {"firstWord": first_word, "secondWord": second_word}

    #creates new jokes and returns to the user
    def create_joke(self):
        #getting words
        self.get_words()
        #printing string
        print(self.format_string.format(**self.word_dict))

if __name__ == "__main__":
    #instance
    jokeMaker = RandomJoke()
    while True:
        #new joke
        jokeMaker.create_joke()
        #input to exit
        user = input()
        if user == "x":
            break
        
