# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 00:28:47 2023

@author: hemal nakrani
"""
import numpy as np
from fastapi import FastAPI, File, UploadFile
import uvicorn
from io import BytesIO
from PIL import Image
import tensorflow as tf

MODEL = tf.keras.models.load_model('saved_models/1.h5')

#MODEL = tf.keras.models.load_model(model_file)
CLASS_NAMES = ['Bacterial spot',
 'Early blight',
 'Late blight',
 'Leaf Mold',
 'Septoria leaf spot',
 'Spider mites Two spotted spider mite',
 'Target Spot',
 'YellowLeaf Curl Virus',
 'mosaic virus',
 'healthy']

app = FastAPI()

@app.get('/')
async def ping():
    return 'hello world'

def read_file_as_image(data) -> np.ndarray:
    image = np.array(Image.open(BytesIO(data)))
    return image

@app.post('/predict')
async def predict(
    file: UploadFile = File(...)
):
    image = read_file_as_image(await file.read())
    image_batch = np.expand_dims(image,0)

    predictions = MODEL.predict(image_batch)
    predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
    confidence = np.max(predictions[0])

    return {
        'class': predicted_class,
        'confidence': float(confidence)
    }


    
if __name__ == '__main__':
   uvicorn.run(app,host = '0.0.0.0' ,port = 8000, log_level="info")