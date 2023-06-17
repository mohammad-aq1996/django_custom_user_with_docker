FROM python:3.10-alpine


WORKDIR /urs/src/code


RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt


COPY . .
