import tensorflow as tf
import numpy as np
from tensorflow import keras
from keras.preprocessing import image
from keras.models import load_model
# ------------------Intel-Classification-Model-Classes-------------------
classes = ['buildings', 'forest', 'glacier', 'mountain', 'sea', 'street']
# -----------------------------------------------------------------------


saved_model = load_model('F:\Intel_Image-Classification\intel_model')
shape=(256,256)

def decode_img(image_path,shape):
    img = tf.keras.preprocessing.image.load_img(image_path,target_size=(shape))
    img = tf.keras.preprocessing.image.img_to_array(img) # converted to ndarray 
    img = img.astype(np.float32)/255.0
    img = np.expand_dims(img,axis=0)
    return img


def model_pred(image_path):
    img = decode_img(image_path,shape)
    pred = saved_model.predict(img)
    idx = np.argmax(pred)
    print(classes[idx])
    predictions = classes[idx]
    return predictions
