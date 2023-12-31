import numpy as np
import tensorflow as tf
import gradio as gr

from train import Digit_recognizer

def sketch_recognition(img):

    model = tf.keras.models.load_model('handwritten.model')
     
    (_,_), (X_test, t_test) = Digit_recognizer.load_data()
    # Computing loss and accuraccy
    loss, accuracy = model.evaluate(X_test, t_test)
    # print(loss, accuracy) # loss=0.087, accuracy=97%

    # Reshaping to fit into a 28 X 28 resolution array
    img_3d = img.reshape(-1, 28, 28)
    # Normalizing the set (0-255 -> 0-1)
    img_norm = tf.keras.utils.normalize(img_3d, axis= 1)
    predictions = model.predict(img_norm)
    # Getting the number with the highest value
    prediction = np.argmax(predictions)
    
    return (f'I am {round(accuracy*100)}% sure that the digit is {prediction}.')

css = """
footer {visibility: hidden;}
.gradio-container {background-color: #101820FF;}
.wrap {background-color: #101820FF;}
button#component-8 {background: #FEE715FF; border-color: #101820FF; color: #101820FF;}
button#component-7 {background: #101820FF; border-color: #FEE715FF; color: #FEE715FF;}
"""

demo = gr.Interface(fn=sketch_recognition, 
                    inputs="sketchpad",
                      outputs="label",
                      css=css,
                      allow_flagging="never"
                   )


if __name__ == "__main__":
    demo.launch(share=True, debug='True')    