FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY cfg.py cfg.py
COPY main.py main.py

CMD python ./main.py