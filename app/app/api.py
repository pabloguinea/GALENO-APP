"""
api.py: api views used by Flask server.
"""

__author__      = "pabloguinea"
__copyright__   = "Copyright 2021"


import os
from flask import Blueprint, abort, jsonify, request
from flask_cors import cross_origin
from flask import json

from skimage.io import imread
import io

from .model import *
from flask import current_app

from werkzeug.utils import secure_filename
from werkzeug.exceptions import HTTPException

api = Blueprint('model', __name__)

@api.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    response = e.get_response()
    # replace the body with JSON
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response

@api.errorhandler(400)
def invalid_request(e):
    return jsonify(error=str(e)), 400

@api.route("/clasify", methods=["DELETE"])
@cross_origin()
def remove():
    return jsonify(1)

@api.route("/clasify", methods=["POST"])
@cross_origin()
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

    if result["success"] is False:
        abort(400, description="Parameters not valid")

    # return result dictionary as JSON response to client
    return jsonify(result)