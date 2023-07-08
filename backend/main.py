import os 
import cv2
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from flask import Flask, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route('/api/process-image', methods=['POST'])
def process_image():
    image_data = request.json['image']
    # Importing the data for tf.keras
    mnist = tf.keras.datasets.mnist

    # Splitting the data into traning and testing sets.
    (X_train, t_train), (X_test, t_test) = mnist.load_data()

    # Normalizing the training sets (0-255 -> 0-1)
    X_train = tf.keras.utils.normalize(X_train, axis= 1)
    X_test = tf.keras.utils.normalize(X_test, axis= 1)


    # defining the model
    # model = tf.keras.models.Sequential()
    # model.add(tf.keras.layers.Flatten(input_shape=(28, 28)))
    # model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
    # model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
    # model.add(tf.keras.layers.Dense(10, activation=tf.nn.softmax))
    # 
    # model.compile(optimizer='adam',
    #               loss='sparse_categorical_crossentropy', 
    #               metrics=['accuracy'])
    # 
    # # fitting the data. epochs is how many times the model sees the same data.
    # model.fit(X_train, t_train, epochs=3)
    # 
    # # Saving the model, so that we do not have to fit it again.
    # model.save('handwritten.model') 
    # 
    # 
    model = tf.keras.models.load_model('handwritten.model')
    # 
    # # Computing loss and accuraccy
    # loss, accuracy = model.evaluate(X_test, t_test)
    # print(loss, accuracy) # loss=0.087, accuracy=97%

    image_number = 1
    while os.path.isfile(f'digit-samples/digit_{image_number}.png'):  # Path to the imgs
        try:
            img = cv2.imread(f'digit-samples/digit_{image_number}.png')[:, :, 0]
            img = np.invert(np.array([img]))
            predictions = model.predict(img)
            prediction = np.argmax(predictions)
            print(f'This digit is {prediction}')
            plt.imshow(img[0], cmap=plt.cm.binary)
            plt.show()
        except:
            print('Error! Img may not be the correct resolution')
        finally: 
            image_number += 1
    return {'result': 'success'}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
