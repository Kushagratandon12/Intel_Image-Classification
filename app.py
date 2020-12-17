import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
import tensorflow.keras.models as Models
from flask import Flask, request
from flask_cors import CORS, cross_origin
import json
import os

app=Flask(__name__)
app.config["IMAGE_UPLOADS"] = "pred_images/"
cors = CORS(app)
@cross_origin()
@app.route('/',methods=['POST','GET'])
def image_process():
    if request.method == 'GET':
        return 'Send Post Request Here'
    image = request.files['image']
    #print(type(image))
    image.save(os.path.join(app.config["IMAGE_UPLOADS"], image.filename))
    # img = tf.keras.preprocessing.image.load_img('pred_images/'+image.filename)
    #image =plt.imread('pred_images/'+image.filename)
    #plt.imshow(image)
    classes = ['buildings', 'forest', 'glacier', 'mountain', 'sea', 'street']
    img = tf.keras.preprocessing.image.load_img('pred_images/'+image.filename, target_size=(150,150))
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0) # Create a batch
    model = Models.load_model('intel_weights.h5')
    predictions = model.predict(img_array)
    score = tf.nn.softmax(predictions[0])
    print(predictions)
    print("This image most likely belongs to {}".format(classes[np.argmax(score)]))
    return 'Image Saved',200

if __name__ == '__main__':
  app.run(debug=True)