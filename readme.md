# Watcher an AI System that Helps Parents monitor children


### Problem statement
With life becoming busier and more complex, parents often find themselves spending more time at work, leaving them concerned about their kids' safety, especially when they're home alone. Our project, Watcher, aims to address this issue by creating a system that detects potential dangers and promptly alerts parents. The questions we sought to answer were:

1. What kinds of dangers could kids face?
2. How can we detect these dangers in real-time?
3. How can we make the system function with just a mobile phone and a laptop?
We developed a system with two main components: the backend, which receives video streams from a mobile phone camera and analyzes them, and a mobile app that parents use to manage the system and receive alerts.

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
