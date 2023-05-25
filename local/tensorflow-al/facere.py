import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model

# Define the custom layer
class L1Dist(tf.keras.layers.Layer):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def call(self, input_embedding, validation_embedding):
        return tf.math.abs(input_embedding - validation_embedding)

# Register the custom layer
tf.keras.utils.get_custom_objects()['L1Dist'] = L1Dist

# Load the trained siamese model
siamese_model = load_model('siamesemodelv2.h5')

# Function to preprocess input images
def preprocess_input(image):
    image = cv2.resize(image, (100, 100))
    image = image.astype("float32") / 255.0
    return image

# Function to perform face recognition using the loaded model
def recognize_face(image):
    # Preprocess input image
    preprocessed_image = preprocess_input(image)

    # Expand dimensions to match model input shape
    preprocessed_image = np.expand_dims(preprocessed_image, axis=0)

    # Perform face recognition using the model
    prediction = siamese_model.predict([preprocessed_image, preprocessed_image])

    # Print the prediction
    print("Prediction:", prediction)

# Example usage: Perform face recognition on a webcam feed
cap = cv2.VideoCapture(0)  # Open the webcam

while True:
    ret, frame = cap.read()  # Read a frame from the webcam

    if not ret:
        break

    # Perform face recognition on the frame
    recognize_face(frame)

    # Display the frame
    cv2.imshow("Face Recognition", frame)

    # Exit the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close any open windows
cap.release()
cv2.destroyAllWindows()
