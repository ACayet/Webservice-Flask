FROM python:3.7.6
ADD . /docker
WORKDIR /docker
RUN pip install -r requirements.txt