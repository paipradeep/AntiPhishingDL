# AntiPhishingDL

The aim of the project is to develop a safe browsing django web application that detects whether URL under browse is malicious or benign and then redirects the user accordingly. Here we have made an attempt to automate this task using Multilayer Perceptron Model with Backpropagation (using Gradient Descent ) as the learning algorithm for our network model.

### Experimental Overview

The dataset was collected from [here](https://www.phishtank.com) that consists of 7000 data samples with both positive and negative samples. This dataset was randomized for the sake of uniform distribution of both positive and negative samples. Since the dataset consisted of only URLs we extracted about 11 features from each data sample which were purely lexical. This was done with a help a python helper program with urlparse and tldextract packages. This extracted feature dataset is the actual dataset used for the experiment.

A generic model of Multilayer Perceptron Network with Backpropagation as the learning algorithm was built by hand-coding completely in Python (version Python 3.5.5) with several data science packages such as Numpy (for fast matrix calculations), Pandas (for constructing dataframes) and matplotlib ( to plot distribution of features across samples).

This model was experimented by varying hyper parameters like number of hidden layers, nodes in each hidden layer, batch size and the learning rate. The model worked well for 4 hidden layers resulting in an accuracy of 86.3 % for test data.

### Dataset

This dataset consisted of 2 columns : **<URL , label >**
1. ***URL*** :- The actual URL in string format
2. ***Class Label*** :- 1 denoting malicious and 0 denoting benign

Since we are focusing on the Lexical features of the URL a python helper program was written that extracted these Lexical features. This program made use of urlparse and tldextract python packages.

**Urlparse** - This helps in breaking down the URL into scheme (http/https etc), netloc(domain and subdomain), path( file path), params (GET parameters), query(set of arguments) and fragment. 
**Tldextract** - This helps in accurately extracting domain, subdomain and suffix ( .com, .in etc) from the URL.

![Dataset after preprocessing](https://github.com/paipradeep/AntiPhishingDL/blob/master/processed.png)


