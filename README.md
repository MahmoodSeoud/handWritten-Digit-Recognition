# Sketch Recognition

This project is aimed at recognizing hand-drawn sketches of digits using a trained machine learning model. By providing an input image of a digit sketch, the model predicts the corresponding digit and provides the confidence level of the prediction.

## Motivation
The motivation behind this project is to showcase the capabilities of machine learning in recognizing hand-drawn sketches. It demonstrates the practical application of deep learning algorithms in the field of image recognition.

## Project Details
- The project utilizes a trained TensorFlow model for recognizing hand-drawn digit sketches.
- The model is loaded from the file 'handwritten.model'.
- The input image is reshaped and normalized to fit the model's requirements.
- The model predicts the digit based on the input image and returns the digit along with the confidence level.
- The accuracy of the model has been evaluated using a separate test dataset, achieving a accuracy rate of approximately 97%.

## Features
- Sketchpad Input: Users can draw their digit sketches directly on the provided sketchpad interface.
- Real-time Prediction: The model predicts the digit as the user finishes sketching, providing immediate results.

## How to Use
1. Ensure that the necessary dependencies are installed. You can check the `requirements.txt` file for details.
2. Run the provided Python script to launch the interface.
    ```BASH
    python3 ./src/main.py
    ```
3. The app will open a port on your localhost. See the terminal for more information.
4. Use the sketchpad to draw a digit.
5. The model will process the sketch and display the predicted digit along with the confidence level.

## Requirements
The project requires the following dependencies:
- numpy
- tensorflow
- gradio

You can install the dependencies using the following command:
```BASH
pip install -r requirements.txt
```

## Future Improvements
This project can be extended and improved in several ways, including:
- Training the model with a larger dataset to improve accuracy.
- Expanding the recognition capabilities to include other types of sketches or images.
- Adding a feedback mechanism for users to provide input on the accuracy of predictions.

Feel free to contribute to this project by implementing these improvements or suggesting new features!

## Acknowledgments
This project was inspired by the desire to explore the potential of machine learning in recognizing hand-drawn sketches. Special thanks to the TensorFlow and Gradio communities for providing the necessary tools and resources.

If you have any questions or suggestions, please feel free to reach out. Happy sketch recognition!
