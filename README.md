# Meduzzen-internship

First you need to install requirements with command:
pip install -r requirements.txt

For start the app you need write this in console:
uvicorn main:app --reload

For running tests you need to do:
python -m pytest

First you need from my Dockerfile make build:
docker build -t fastapiapp:lts .

Then you need to start the docker container
docker run -p 8000:8000 -d --rm --name fastapiapp fastapiapp:lts

And now you need to run command:
docker exec -it Id_of_your_container bash

And then run tests with command:
python -m pytest