import pickle
import numpy as np
from PIL import Image
from sklearn import datasets, svm
from sklearn.model_selection import train_test_split

def read():
    with open('mnist.pickle', 'rb') as file:
        clf = pickle.load(file)
    return clf