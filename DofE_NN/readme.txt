OVERVIEW:
The idea here is to create a neural network which estimates our group moral while on the Duke of Edinburgh Award expedition. This is based off of previous data which we gathered while on expedition, including measures for the weather, sleep quality, hunger and physical feeling. The program interprets this data and fine tunes weights and a bias to accuratley estimate moral.

HOW TO USE:
Download the repositry and run the 'neural_network.py' file, this will then load the data using the 'data_interpreter.py' file and create a neural network. From here you can then input the value of 1 or 0 into each factor, and the neural network will estimate the likelyhood that moral is good or bad, and estimate a moral rating from 0 to 10. 

DRAWBACKS:
Unfortunately to accurately estimate using machine learning you need a large data set, as we were only in the field for 4 days, we do not have this resource. Additionally this program was meant to estimate the accuracy of a true or false reading, whereas I have used the decimal accuracy to estimate our overall moral on a scale of 1 to 10. This may make the estimates inaccurate. Further testing is needed.

FILE EXPLANATION:
The file 'data.csv' holds the current data from the expedition.
The file 'data_interpreter.py' is used to interpret data from the csv file into a useful format.
The file 'neural network.py' imports the data from 'data_interpreter.py' and uses it to create a neural network, the user can then input values to estimate outcomes. 

DEPENDANCIES:
This program is dependant on the 'numpy' module in Python, and was written in Python version 3.6. The program has not been tested with any other version of Python.

RESOURCES:
The file 'neural network', and the entire idea, is heavily based off of the guide here (https://stackabuse.com/creating-a-neural-network-from-scratch-in-python/), and I can claim no originality for the underlying neural network in the code.
