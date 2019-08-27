#tokenise by Miles Burne 27/8/19

#class used to take raw data and convert it into a dictionary of integers with corresponding unique words, similar to dictionary encoding.
class Tokenise():
    #initilise
    def __init__(self, data):
        self.raw_data = str(data) #taken in and used as string
        self.word_list = [] #array of individual words
        self.token_dict = {} #final output dictionary
        self.filters = ["!",".",'"',"'",",","/","\n","[","?","]","(",")"] #filters for data set
        self.data_prepare() #prepares data

    #prepares raw data for tokenising by converting to individual words
    def data_prepare(self):
        raw_char = list(self.raw_data)
        current_filter = 0
        while current_filter != len(self.filters): #while still using filters
            try:
                removal = raw_char.index(self.filters[current_filter])
                raw_char.pop(removal)
            except ValueError:
                current_filter += 1
        #raw_char now removed special characters
        stripped_data = "".join(raw_char)
        self.word_list = stripped_data.split(" ") #turning into words by splitting on SPACE

    #creates dictionary from wordlist
    def tokenise(self):
        added_words = []
        token_number = 1
        for x in self.word_list: #iterate through array
            if x.lower() not in added_words: #if word is first appearance
                added_words.append(x.lower())
                self.token_dict[token_number] = x.lower() #add word to dict as lower
                token_number += 1
            else: #otherwise word in dict already
                pass
        return(self.token_dict) #returns dict

    #returns token_dict
    def get_tokens(self):
        return(self.token_dict)
    
        
        
if __name__ == "__main__":
    raw_data = ("According to all known laws of aviation, there is no way a bee should be able to fly. Its wings are too small to get its fat little body off the ground. The bee, of course, flies anyway because bees don't care what humans think is impossible. Yellow, black. Yellow, black. Yellow, black. Yellow, black. Ooh, black and yellow! Let's shake it up a little.")
    print("data:", raw_data,"\n")
    tokenise = Tokenise(raw_data)
    print("class:", tokenise,"\n")
    print("word list:", tokenise.word_list,"\n")
    token_dict = tokenise.tokenise()
    print("token dict:", token_dict,"\n")

    
