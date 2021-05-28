import sys
import os
import glob
import re
import numpy as np

# Keras
from keras.models import load_model, model_from_json
from keras_preprocessing import image as kerasImage
from keras.applications.inception_v3 import preprocess_input

# Tensorflow
from tensorflow import Graph, Session

# Flask utils
from flask import Flask, redirect, url_for, request, render_template, send_from_directory, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer


app = Flask(__name__, template_folder='frontend', static_folder='frontend', static_url_path='')
CORS(app)

# constants
IMG_SIZE = 176
CLASSES = [ 'NonDemented',
            'VeryMildDemented',
            'MildDemented',
            'ModerateDemented']
MODEL_NAMES = ["alzheimer_inception_cnn_model"]
AMOUNT_OF_MODELS = len(MODEL_NAMES)
MODELS = []
GRAPHS = []
SESSIONS = []

def load_models():
    for i in range(AMOUNT_OF_MODELS):
        load_single_model("models/" + MODEL_NAMES[i] + ".h5")
        print("\nModel ", str(i+1), " of ",  AMOUNT_OF_MODELS, " loaded.")
    print('Ready to go! Visit -> http://127.0.0.1:5000/')   

# 
def load_single_model(path):
    graph = Graph()
    with graph.as_default():
        session = Session()
        with session.as_default():
            model = load_model(path)
            model._make_predict_function() 
            
            MODELS.append(model)
            GRAPHS.append(graph)
            SESSIONS.append(session)


def models_predict(file_path):
    
    # Beware to adapt the preprocessing to the input of your trained models
    img = kerasImage.load_img(file_path, target_size=(IMG_SIZE, IMG_SIZE))

    # Convert the image pixels to a numpy array
    image_array = kerasImage.img_to_array(img)

    # scale pixel values to [0, 1]
    image_array = image_array.astype(np.float32)
    image_array /= 255.0

    # add a dimension so that we have one sample
    image_array = np.expand_dims(image_array, axis=0)

    # Prepare the image for the CNN Model model
    image_array = preprocess_input(image_array)

    results = []

    for i in range(AMOUNT_OF_MODELS):
        with GRAPHS[i].as_default():
            with SESSIONS[i].as_default():
                
                # predict the classification
                predictions = MODELS[i].predict(image_array)

                # get the classified category
                selected_category = CLASSES[np.argmax(predictions[0])]


                results.append({"predictions": predictions, "category": selected_category})

    return results


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def upload():
    if request.method == 'POST':
        # Get the image from the POST request
        image_to_predict = request.files['image']

        # Save the image to ./uploads
        basepath = os.path.dirname(__file__)
        local_image_path = os.path.join(
            basepath, 'uploads', secure_filename(image_to_predict.filename))
        
        image_to_predict.save(local_image_path)

        predictions = models_predict(local_image_path)

        # Remove image after prediction is done
        os.remove(local_image_path)

        return jsonify(predictions)   


if __name__ == '__main__':
    load_models()
    wsgi_server = WSGIServer(('0.0.0.0', 5000), app)
    wsgi_server.serve_forever()
