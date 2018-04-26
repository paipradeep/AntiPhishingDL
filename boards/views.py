from django.shortcuts import render,redirect
from django.http import HttpResponse
#from django.contrib.auth import authenticate, login
''' views.py is for getting HTTP request and sending HTTP response'''
import boards.AntiPhishing as AP
import numpy as np
import pickle

def sigmoid(z):
    z = np.float64(z)
    return 1.0/(1.0+np.exp(-1.0 * z))

def home(request):
	if request.method == 'POST':
		inpURL = request.POST['url']
		print(inpURL)
		features = AP.extractFeatures(inpURL,0)
		features = features[1:-1]
		a = np.array(features)
		a = a.reshape(11,1)
		f = open('boards/trained.obj','rb')
		sizes = pickle.load(f)
		weights = pickle.load(f)
		biases = pickle.load(f)
		for b,w in zip(biases,weights):
		    a = sigmoid(np.dot(w, a)+b)
		result = np.argmax(a)

		if(result == 1):
			return render(request,'danger.html',{'url':inpURL})
		else:
			return redirect(inpURL)
	return render(request,'home.html')
