import numpy as np
import pickle
import AntiPhishing as AP
def sigmoid(z):
    z = np.float64(z)
    return 1.0/(1.0+np.exp(-1.0 * z))

b = AP.extractFeatures('http://www.texrenfest.com/',0)

b = b[1:-1]

a = np.array(b)
a = a.reshape(11,1)

f = open('trained.obj','rb')
sizes = pickle.load(f)
weights = pickle.load(f)
biases = pickle.load(f)

for b,w in zip(biases,weights):
    a = sigmoid(np.dot(w, a)+b)


print(np.argmax(a))
