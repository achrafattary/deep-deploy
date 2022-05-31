from __future__ import division, print_function
import os


# Keras


from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
# Flask utils
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename

# Define a flask app
app = Flask(__name__)

# Model saved with Keras model.save()
MODEL_PATH = 'pre_final_model.h5'

# Load your trained model
model = load_model(MODEL_PATH)
print('Model loaded. Check http://127.0.0.1:5000/')


def model_predict(img_path):
    img = image.load_img(img_path, target_size=(200, 200))
    img = img_to_array(img)
    img = img.reshape(1, 200, 200, 3)
    img = img.astype('float32')
    img = img - [123.68, 116.779, 103.939]
    
    preds = model.predict(img)
    return preds


@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')





if __name__ == '__main__':
    app.run(debug=True)

