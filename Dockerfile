FROM python:3.9.13

COPY ./requirements.txt /code/

WORKDIR /code

RUN python -m pip install --upgrade pip

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . /code/

CMD ["python", "-m", "app.main"]

#CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]