#Data File Interpret by Miles Burne 3/10/19

class file_management():
    #init
    def __init__(self, filename):
        self.filename = filename
        self.raw_data = self.import_file()
        self.array = self.interpret_data()
        self.fur_array = self.further_interpret()

        
    #handles the import of the file to raw data
    def import_file(self):
        #try and except
        try: #tries to read file
            f = open(self.filename,"r")
            file = f.read()
            f.close()
        except FileNotFoundError: #if file does not exist
            print("Error: File", self.filename,"does not exist.")
            quit()
        #returns raw file data
        return(file)

    #changes the data into a useful 2d array format
    def interpret_data(self):
        #trims data down in a series of passes
        first_pass = self.raw_data
        second_pass = first_pass.split("\n")
        second_pass.pop(0) #removing headers to data
        array = []
        #splitting
        for x in second_pass:
            y = x.split(",")
            array.append(y) #split into 2d array [day,time,weather,sleep,physical,food,overall]
        return(array)
    
    #simplifies integer data down to booleans
    def further_interpret(self):
        fur_array = self.array
        correspond = {"0":False,"1":False,"2":False,"3":False,"4":False,"5":True,"6":True,"7":True,"8":True,"9":True,"10":True} #dictionary to correspond with 
        #per 1d
        for x in fur_array:
            depth = fur_array.index(x)
            #2d
            for y in x:
                #if day or time
                if x.index(y) == 0 or x.index(y) == 1:
                    pass
                else:
                    fur_array[depth][x.index(y)] = correspond[y]

        return(fur_array)
        
    #returns the array (has to recreate as fur_array overwrites
    def get_array(self):
        return(self.interpret_data())

    #returns raw data
    def get_data(self):
        return(self.raw_data)

    #returns fur_array
    def get_fur(self):
        return(self.fur_array)



if __name__ == "__main__":
    file = file_management("data.csv")
    print(file.get_data())
    print(file.get_array())
    print(file.get_fur())

        

    
        
