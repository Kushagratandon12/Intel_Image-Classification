import numpy as np
import matplotlib.pyplot as plt
from flask import Flask, request, send_file
from flask_cors import CORS
import os

#  Tensorflow Model Classes
classes = ['buildings', 'forest', 'glacier', 'mountain', 'sea', 'street']
#

app = Flask(__name__)
app.config["IMAGE_UPLOADS"] = ""
cors = CORS(app)


@app.route('/', methods=['POST', 'GET'])
def image_process():
    if request.method == 'GET':
        return 'Send Post Request Here'

    # Request Image Form The Postman
    image = request.files['image']
    image.save(os.path.join(app.config["IMAGE_UPLOADS"], image.filename))
    image = plt.imread(''+image.filename)
    return 'Image Received With Size {}'.format(image.shape), 200


if __name__ == '__main__':
    app.run(debug=True)
