# Realtime Facial Emotion Recognition

# Introduction
This repo includes simple implementation of realtime facial emotion recognition.

Service       | Realization
------------- | -------------
Frontend  | React.js
Backend | Fastapi
Protocol | WebSocket
Emotion Recognition | FER (tensorflow)

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

## Sample output
```json
{
    "box": [
        425,
        209,
        346,
        346
    ],
    "emotions": {
        "angry": 0.0,
        "disgust": 0.0,
        "fear": 0.0,
        "happy": 0.97,
        "sad": 0.0,
        "surprise": 0.0,
        "neutral": 0.03
    },
    "emotion": "happy"
}
```