from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input
from tensorflow.keras.preprocessing import image
import numpy as np
import cv2

# Load pre-trained MobileNetV2 model for scene classification
indoor_outdoor_model = MobileNetV2(weights='imagenet')

def classify_scene(frame):
    img = cv2.resize(frame, (224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    preds = indoor_outdoor_model.predict(x)
    return 'indoor' if preds[0][0] > preds[0][1] else 'outdoor'
