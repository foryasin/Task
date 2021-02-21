FROM python:3.8

WORKDIR /usr/src/app

COPY utils.py .
COPY worker.py .
COPY requirements.txt .

RUN pip install -r requirements.txt

CMD ["python3", "./app.py"]

