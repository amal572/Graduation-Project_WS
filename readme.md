# Watcher is an AI System that Helps Parents monitor children


### Problem statement
With life becoming busier and more complex, parents often find themselves spending more time at work, leaving them concerned about their kids' safety, especially when they're home alone. Our project, Watcher, aims to address this issue by creating a system that detects potential dangers and promptly alerts parents. The questions we sought to answer were:

1. What kinds of dangers could kids face?
2. How can we detect these dangers in real-time?
3. How can we make the system function with just a mobile phone and a laptop?
We developed a system with two main components: the backend, which receives video streams from a mobile phone camera and analyzes them, and a mobile app that parents use to manage the system and receive alerts.

### The application has four subsystem
1. Falls and fights detection system: Utilizes MoveNet to extract human
skeletons in video frames, handcrafting speed, and position features which are
then passed to an LSTM network for classifying.
2. Fire detection system: Employing YOLO v5 to detect fires.
3. Unusual sound detection: This system identifies sounds such as crying or
shooting through three steps: segmenting the sound into 2-second intervals,
extracting time and frequency features, and then passing them to a Boosting
classifier.
4. Face recognition system: to determine if children arrive home or if a stranger
enters the house through three steps: detecting faces using pre-trained SSD
model, extracting facial features, and performing face recognition using a
pre-trained VGGFace model with the ResNet50 architecture.

## Technologies and Tools
- Language - [**Python**](https://www.python.org)
- Django framework for the backend
- various image processing and machine learning libraries like OpenCV, NumPy, and TensorFlow
-  mobile application we used Flutter Framework and Firebase for the notifications

Our approach began with identifying the system requirements based on parental needs. We then researched similar projects, studying them to discover state-of-the-art techniques and models to implement in our system.

As a result, our system was accurate, successfully achieving the project's objectives. we accomplished this using only a mobile phone camera and a laptop with an
NVIDIA GeForce 1050 GPU, achieving a frame rate of 16 FPS with all subsystems working together, The novelty of our project lies in its affordability, user-friendliness, and
no need for additional equipment. It's a valuable tool for busy parents, ensuring the safety of their children at home with ease.

## Setup
```bash
python venv env
pip install -r requirements.txt
uvicorn main:app --reload
``` 
- run in http://localhost:8000

# Run APIs


```bash
cd mysite
python manage.py runserver

for connect mobile run this :
python manage.py runserver 0.0.0.0:8000
``` 
