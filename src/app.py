# Import necessary libraries
import tensorflow as tf
import numpy as np
import keras
import os
import time
import shutil
# Keras
from keras.models import load_model, model_from_json
from keras.preprocessing import image
from PIL import Image
from keras.preprocessing.image import img_to_array, load_img
from keras import applications
import uvicorn
from fastapi import FastAPI, Request
from fastapi import File, UploadFile
from pydantic import BaseModel
from typing import List
import pandas as pd
import numpy as np
import sklearn.externals
import joblib
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles


# Loading model

vgg16 = applications.VGG16(include_top=False, weights="imagenet")

# Loading VGG16 trained model for inference on single image
model = load_model("../models/pneumonia_detection.h5")


# Parent app
app = FastAPI()

app.mount("/static", StaticFiles(directory="../static"), name="static")

templates = Jinja2Templates(directory="../templates")

# Root route
@app.get("/")
async def root_route(req: Request):
    return "Welcome to API"

@app.get("/prediction", response_class=HTMLResponse)
async def prediction_route(request: Request):
    return templates.TemplateResponse("index.html", {'request': request})

# Endpoint for prediciton
@app.post("/prediction", response_class=HTMLResponse)
async def prediction_route(request: Request, sample: UploadFile = File(...)):

    # Saving image
    with open("../test/xray.jpeg", "wb") as buffer:    
        shutil.copyfileobj(sample.file, buffer)

    # preprocessing image
    img1 = load_img("../test/xray.jpeg", target_size=(224, 224))
    image = img_to_array(img1)
    image = np.expand_dims(image, axis=0)
    image /= 255.

    # Feature extraction using vgg16 model
    bt_prediction = vgg16.predict(image)

    #extracting max probability value
    prediction = np.argmax(model.predict(bt_prediction), axis=-1)

    # If class probability is atleast 0.5 then it is positive class
    if prediction > 0.5:
        prediction = "Pneumonia Detected"
    else:
        prediction = "Normal"

    return templates.TemplateResponse("index.html", context={'request': request, 'result': prediction})

