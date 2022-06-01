import tensorflow 

MODEL_PATH = 'pre_final_model.h5'

# Load your trained model
model = tensorflow.keras.models.load_model(MODEL_PATH)
print('Model loaded. Check http://127.0.0.1:5000/')


def model_predict(img_path):
    img = tensorflow.keras.preprocessing.image.load_img(img_path, target_size=(200, 200))
    img = tensorflow.keras.preprocessing.image.img_to_array(img)
    img = img.reshape(1, 200, 200, 3)
    img = img.astype('float32')
    img = img - [123.68, 116.779, 103.939]
    
    preds = model.predict(img)
    return preds
