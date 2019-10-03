#DofE Neural Network by Miles Burne 3/10/19

#imports
import numpy as np
import data_file_interpret as ext

#sigmoid function (used for feedforward)
def sigmoid(x):
    return(1/(1+np.exp(-x)))

#derivative of sigmoid function (used for back propagation)
def sigmoid_der(x):
    return(sigmoid(x)*(1-sigmoid(x)))

#main function
def main():
    
    #instant of file_management
    file = ext.file_management("data.csv")
    
    #gets layers
    input_layer = file.get_input_layer()
    output_layer = file.get_output_layer()
    
    #creates feature set
    feature_set = np.array(input_layer)
    labels = np.array(output_layer)
    labels = labels.reshape(3,1) #labels are answers we are trying to achieve
    
    #defines parameters of NN
    np.random.seed(42)
    weights = np.random.rand(4,1) #4 features therefore vector of 4 weights
    bias = np.random.rand(1)
    lr = 0.05 #learning rate is 0.05
        
    #-------------CODE-------------
    for epoch in range(20000):
        inpts = feature_set

        #feedforward step 1
        XW = np.dot(feature_set,weights) + bias

        #feedforward step 2
        z = sigmoid(XW)

        #backpropagation step 1
        cost = z - labels

        print(cost.sum())

        #backpropagation step 2
        dcost_dpred = cost
        dpred_dz = sigmoid_der(z)

        z_delta = dcost_dpred * dpred_dz

        inpts = feature_set.T
        weights -= lr * np.dot(inpts, z_delta)

        for num in z_delta:
            bias -= lr *num
            
    print("epoch complete for value 20000")
    
    testing = True
    while testing == True:
        #inputs for testing
        v1 = int(input("please input a value for weather: "))
        v2 = int(input("please input a value for sleep: "))
        v3 = int(input("please input a value for physical: "))
        v4 = int(input("please input a value for food: "))
        #testing values
        single_point = np.array([v1,v2,v3,v4])
        result = sigmoid(np.dot(single_point, weights) + bias)
        print("Overall moral at: "+str(result))
        
        

    
main()
    
           

