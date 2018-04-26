# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 19:27:54 2018

@author: paipradeep
"""

import pandas as pd
import numpy as np
import backprop1
import pickle

def myLoader(datasetFile,trainSize,crossSize,testSize):
    df = pd.read_csv(datasetFile)
    train_input =[]
    train_output = []
    for i in range(trainSize):
        train_input.append(np.array(df.iloc[i,1:-1]).reshape(11,1))
        #train_output.append(np.array(df.iloc[i,-1:]).reshape(1,1))
        train_output.append(vectorized(df.iloc[i,-1]))
    train_data = zip(train_input,train_output)
    validation_input = []
    validation_output = []
    for i in range(trainSize,trainSize+crossSize):
        validation_input.append(np.array(df.iloc[i,1:-1]).reshape(11,1))
        validation_output.append(df.iloc[i,-1])
    validation_data = zip(validation_input,validation_output)
    test_input = []
    test_output = []
    for i in range(trainSize+crossSize,trainSize+crossSize+testSize):
        test_input.append(np.array(df.iloc[i,1:-1]).reshape(11,1))
        test_output.append(df.iloc[i,-1])
    test_data = zip(test_input,test_output)
    return (train_data,validation_data,test_data)

def vectorized(ele):
    res = np.zeros((2,1),dtype="float64")
    res[ele] = 1.0
    return res

a,b,c = myLoader("finalDataset.csv",5000,1000,1000)
net = backprop1.Network([11,9,5,7,8,2])
#net = backprop1.Network([11,5,2])
net.SGD(a,30,15,0.05,test_data=b)
print(net.evaluate(c))
f = open("trained.obj","wb")
pickle.dump(net.sizes,f)
pickle.dump(net.weights,f)
pickle.dump(net.biases,f)
f.close()
