import numpy as np
import matplotlib.pyplot as plt
# import tflite_runtime.interpreter as tflite
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
    # print(type(image))
    image.save(os.path.join(app.config["IMAGE_UPLOADS"], image.filename))
    image = plt.imread(''+image.filename)
    # # LOAD THE TENSORFLOW LITE MODEL
    # interpreter = tflite.Interpreter(model_path='tflite_model')
    # interpreter.allocate_tensors()
    # # Get input and output tensors.
    # input_details = interpreter.get_input_details()
    # output_details = interpreter.get_output_details()
    # # Test model on random input data.
    # input_shape = input_details[0]['shape']
    # input_data = np.array(np.expand_dims(img, 0), dtype=np.float32)
    # interpreter.set_tensor(input_details[0]['index'], input_data)
    # # print(input_data)
    # interpreter.invoke()
    # output_details = interpreter.get_output_details()
    # output_data = interpreter.get_tensor(output_details[0]['index'])
    # results = np.squeeze(output_data)
    # # print(results)
    # pred = np.argmax(results)
    return 'Image Received With Size {}'.format(image.shape), 200


if __name__ == '__main__':
    app.run(debug=True)
