import numpy as np
import tensorflow as tf
from tensorflow import keras
import tensorflow.keras.preprocessing.image as preprocessing
from flask import Flask, request, send_file
import os

app = Flask(__name__)
app.config[""] = " "


@app.route('/', methods=['POST', 'GET'])
def image_process():
    if request.method == 'GET':
        return 'Send Post Request Here'

    # Request Image Form The Postman
    image = request.files['image']
    image.save(os.path.join(app.config["IMAGE_UPLOADS"], image.filename))

    # Pre-Process The Image Using Tensorflow->Keras->Image->Preprocessing_Function
    img = preprocessing.load_img(image.filename)
    print(type(img))

    # predictions = model_pred(img)
    # return 'The Image Predicted By Model Is Of {}'.format(predictions), 200
    return 'Tensorflow Working', 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
