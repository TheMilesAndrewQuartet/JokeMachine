OVERVIEW:
The idea here is to create a neural network which estimates our group moral while on the Duke of Edinburgh Award expedition. This is based off of previous data which we gathered while on expedition, including measures for the weather, sleep quality, hunger and physical feeling. The program interprets this data and fine tunes weights and a bias to accuratley estimate moral.

DRAWBACKS:
Unfortunately to accurately estimate using machine learning you need a large data set, as we were only in the field for 4 days, we do not have this resource. Additionally this program was meant to estimate the accuracy of a true or false reading, whereas I have used the decimal accuracy to estimate our overall moral on a scale of 1 to 10. This may make the estimates inaccurate. Further testing is needed.

FILE EXPLANATION:
Use file 'neural network' to run and estimate new values based off of previous data. 
File 'data_file_interpret' is used to interpret data from the csv file.
File 'data' hold the current partial data from the expedition.

DEPENDANCIES:
This program is dependant on the 'numpy' module in python.

RESOURCES:
The file 'neural network', and the entire idea, is heavily based off of the guide here (https://stackabuse.com/creating-a-neural-network-from-scratch-in-python/), and I can claim little originality for the code.
