import tensorflow as tf
import numpy as np
from tensorflow import keras
from keras.preprocessing import image
from keras.models import load_model
# ------------------Intel-Classification-Model-Classes-------------------
classes = ['buildings', 'forest', 'glacier', 'mountain', 'sea', 'street']
# -----------------------------------------------------------------------


saved_model = load_model('model_weights\model.h5')


def model_pred(image_path):
    image.load_img(image_path, target_size=(160, 160))
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    idx = np.argmax(saved_model.predict(img, batch_size=5))
    print(idx)
