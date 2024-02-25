# Realtime Facial Emotion Recognition

# Introduction
This repository demonstrates an end-to-end pipeline for real-time Facial emotion recognition application through full-stack development.
The frontend is developed in react.js and the backend is developed in FastAPI. The emotion prediction model is built with Tensorflow Keras, and for real-time face detection with animation on the frontend, Tensorflow.js have been used.

# Implementation
Implementation of the full-stack end-to-end face emotion recognition pipeline.

## setup
```sh
$ pip install -r requirements.txt
$ cd frontend
$ npm install
```
## Starting the API server 
```sh
$ cd server
$ uvicorn main:app --reload
```

## Starting the React Fronted
```sh
$ cd frontend
$ npm start
```