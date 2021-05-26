"""
model.py: Functions related to Deep Learning model based on Keras.
"""

__author__      = "pabloguinea"
__copyright__   = "Copyright 2021"


# Keras
from keras.models import load_model
from keras_preprocessing import image as kerasImage
from keras.applications.inception_v3 import preprocess_input
import tensorflow as tf
from tensorflow_addons.metrics import F1Score
from skimage import transform, util
import numpy as np

def f1_score_macro():
    return tf.metrics.F1Score(num_classes = 7, average = 'macro', name = 'f1_score_macro', threshold = 0.5)

def f1_score_micro():
    return tf.metrics.F1Score(num_classes = 7, average = 'micro', name = 'f1_score_micro', threshold = 0.5)


def init_model(model_path):
    """Function that loads Deep Learning model.
    Returns:
        model: Loaded Deep Learning model.
    """
    model = tf.keras.models.load_model(model_path,
                            custom_objects={ 
                               'F1Score': f1_score_macro,
                               'F1Score': f1_score_micro,
                            }
                        )
    #model = load_model(model_path)
    model.make_predict_function()

    return model

def preprocess_image(image, size_w, size_h):
    """Function that preprocess image.
    Returns:
        image: Preprocessed image.
    """

    # Beware to adapt the preprocessing to the input of your trained models
    img = kerasImage.load_img(image, target_size=(size_w, size_h))
    
    # Convert the image pixels to a numpy array
    image_array = kerasImage.img_to_array(img)

    # invert grayscale image
    #image = util.invert(image)

    # resize and reshape image for model
    #image_array = transform.resize(image, (size_w, size_h), anti_aliasing=True, mode="constant")
    
    #image_array = np.array(image)

    # scale pixel values to [0, 1]
    image_array = image_array.astype(np.float32)
    image_array /= 255.0

    # add a dimension so that we have one sample
    image_array = np.expand_dims(image_array, axis=0)

    # Prepare the image for the CNN Model model
    image_array = preprocess_input(image_array)


    return image_array