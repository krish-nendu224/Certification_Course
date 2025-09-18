import tensorflow as tf
from tensorflow.keras import layers,models
import matplotlib.pyplot as plt

# Load dataset (MNIST is built in)
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

#Normalise data
x_train = x_train.astype('float32') / 255.0
x_test = x_test.astype('float32') / 255.0
print("hello")

# Reshape data 
x_train = x_train.reshape(-1,18,18,1)
x_test = x_test.reshape(-1,18,18,1)