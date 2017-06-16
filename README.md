# titanic

This repository we will attempt to predict survivors of the Titanic using machine learning algorithms, per the Kaggle competition [Titanic: Machine Learning from Disaster](https://www.kaggle.com/c/titanic).

## Multi-Layer Perceptron (MLP) Approach

In this approach, we attempt to classify survivors of the Titanic by training an artificial neural network.  An artifical neural network is a model inspired by neuroscience.  In this model, `neurons` are arranged in multiple `layers`.  The first layer is known as the `input layer`, with one neuron per input, and an additional `bias` neuron.  These neurons transform the input data, and propagate that information to some number of `hidden layers` of neurons.  The process repeats, until the data reaches the `output layer`, which will predict whether or not an individual survived the Titanic disaster.

## Installation

This installation is assumed for Python version 3.6.1.  For information on how to install Python, visit [the python website](https://www.python.org).  To install, first click "clone or download", and download to your local machine.  Then, open the command line, and cd to the new directory.  Run the following commands:

`>>> python3 -m pip install virtualenv`

`>>> python3 -m virtualenv venv`

`>>> source venv\bin\activate` or (for Windows) `>>> venv\Scripts\activate`

`>>> pip install -r requirements.txt`
