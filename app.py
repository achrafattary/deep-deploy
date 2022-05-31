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


# Load your trained model







@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')





if __name__ == '__main__':
    app.run(debug=True)

