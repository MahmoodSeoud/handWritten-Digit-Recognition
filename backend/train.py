
import numpy as np
import tensorflow as tf

# Importing the data for tf.keras
mnist = tf.keras.datasets.mnist

# Splitting the data into traning and testing sets.
(X_train, t_train), (X_test, t_test) = mnist.load_data()

# Normalizing the training sets (0-255 -> 0-1)
X_train = tf.keras.utils.normalize(X_train, axis= 1)
X_test = tf.keras.utils.normalize(X_test, axis= 1)

# defining the model
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten(input_shape=(28, 28)))
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(10, activation=tf.nn.softmax))

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy', 
              metrics=['accuracy'])

#    fitting the data. epochs is how many times the model sees the same data.
model.fit(X_train, t_train, epochs=10)

# Saving the model, so that we do not have to fit it again.
model.save('handwritten.model') 