Disease Detection Using Deep Learning
 ==============================

Building Rest API for Disease Detection using Deep Learning for classification and FastAPI for serving.

Problem:-

Traditional diagnosis system for pneumonia detection is very slow process. There should be specialist doctor for diagnosing X-ray diagnosis.
But Using this Web service one can simply upload their X-ray and get result within seconds.

Here I am using Deep Learning models for Image processing and classification tasks which are very sophisticated in distinguish between normal and affeacted X-ray by analysing image features and upto very minute detail in image.

Workflow:-

Normal workflow of the project is We have to train our Deep learning model using as much X-ray data as possible so that it can learn to classify them more robustly
If we can automate the process of traning and deployment part of this then this will work as expected.

The components i have used in this project are:-

VGG16 model for image classification
Kears with tensorflow backend for efficient computation and prediction.

Deployment :-

Using Heroku free tier services we can easily deploy our model for demonstration.

Interface:-

![demo](demo.png)


