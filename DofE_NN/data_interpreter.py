#Data File Interpret by Miles Burne 3/10/19

class file_management():
    #init
    def __init__(self, filename):
        self.filename = filename
        self.raw_data = self.import_file()
        self.array = self.interpret_data()
        self.fur_array = self.further_interpret()
        self.input_layer = []
        self.output_layer = []
        self.create_layers()
        
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
        correspond = {"0":0,"1":0,"2":0,"3":0,"4":0,"5":1,"6":1,"7":1,"8":1,"9":1,"10":1} #dictionary to correspond with
        
        #removes day and time from array
        for a in fur_array:
            for b in range(0,2):
                fur_array[fur_array.index(a)].pop(0) #day is pos 0, once day removed time is pos 0
        
        #per 1d
        for x in fur_array:
            depth = fur_array.index(x)
            #2d
            for y in x:
                fur_array[depth][x.index(y)] = correspond[y]

        return(fur_array)

    #creates both input and output layers
    def create_layers(self):
        input_l = []
        output_l = []
        #iterate through 2d array
        for x in self.fur_array:
            output_l.append(x.pop(4))
            input_l.append(x)
        self.input_layer = input_l
        self.output_layer = output_l
        
    #returns the array (has to recreate as fur_array overwrites
    def get_array(self):
        return(self.interpret_data())

    #returns raw data
    def get_data(self):
        return(self.raw_data)

    def get_input_layer(self):
        return(self.input_layer)
    
    def get_output_layer(self):
        return(self.output_layer)


if __name__ == "__main__":
    file = file_management("data.csv")
    print(file.get_data())
    print(file.get_array())
    print(file.get_input_layer())
    print(file.get_output_layer())

        

    
        
