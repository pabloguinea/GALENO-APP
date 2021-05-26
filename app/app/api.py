"""
api.py: api views used by Flask server.
"""

__author__      = "pabloguinea"
__copyright__   = "Copyright 2021"


import os
from flask import Blueprint, jsonify, request

from skimage.io import imread
import io

from .model import *
from flask import current_app

from werkzeug.utils import secure_filename

api = Blueprint('api', __name__)

@api.route("/predict", methods=["POST"])
def predict():
    # result dictionary that will be returned from the view
    result = {"success": False}

    # ensure an image was properly uploaded to our endpoint
    if request.method == "POST":
        if request.files.get("file"):
            
            # read image in memory 
            """
            image_req = request.files["file"].read()
            request.files["file"].close()
            image = imread(io.BytesIO(image_req))
            """
            # Save the image to ./uploads
            image_req = request.files['file']
            basepath = os.path.dirname(__file__)
            local_image_path = os.path.join(
            basepath, 'uploads', secure_filename(image_req.filename))
            image_req.save(local_image_path)

            # preprocess the image for model
            preprocessed_image = preprocess_image(local_image_path, int(current_app.config["IMG_SIZE"]), int(current_app.config["IMG_SIZE"]))

            # classify the input image generating a list of predictions
            model = current_app.config["model"]
            predictions = model.predict(preprocessed_image)
            
             # get the classified category
            selected_category = current_app.config["CLASSES"][np.argmax(predictions[0])]

            # add generated predictions to result
            result["predictions"] = []

            for i in range(0, len(current_app.config["CLASSES"])):
                pred = {"category": current_app.config["CLASSES"][i], "probability": str(predictions[0][i])}
                result["predictions"].append(pred)

            result["most_probable_category"] = selected_category

            # indicate that the request was a success
            result["success"] = True

            # Remove image after prediction is done
            os.remove(local_image_path)

    # return result dictionary as JSON response to client
    return jsonify(result)