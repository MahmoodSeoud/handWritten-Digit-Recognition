import os 
import cv2
import numpy as np
import tensorflow as tf
from flask import Flask, request
from flask_cors import CORS
import base64


app = Flask(__name__)
CORS(app)


@app.route('/api/process-image', methods=['POST'])
def process_image():

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

    try:
        image_data = request.json['image']
        print("IMAGE_DATA", image_data)
        encoded_data = image_data.split(',')[1]
        print("ENCODED_DATA", encoded_data)
        image_bytes = base64.b64decode(encoded_data)
        print("IMAGE_BYTES", image_data)
        image = np.frombuffer(image_bytes, np.uint8)
        print("IMAGE IS:", image)
        img = np.invert(np.array([image]))
        print("IMG IS:", img)

        predictions = model.predict(img)

       # prediction = np.argmax(predictions)
       # print(f'This digit is {prediction}')
    except Exception as e:
        print("ERROR", e)
        print('ERROR! IMG MAY NOT BE THE CORRECT RESOLUTION')
        image = None 
    
    return {"Res": "suic"}



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
