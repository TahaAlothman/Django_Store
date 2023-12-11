# start docker with linux kernal slim + install python 3.11
FROM python:3.11.6-slim-bullseye

# option linux : python
ENV PYTHONUNBUFFERED = 1

# update linux 
RUN apt-get update && apt-get -y install gcc libpq-dev 

# create folder ---> project
WORKDIR /app

# copy requirments.txt file
COPY requirements.txt /app/requirments.txt

# install all libraries 
RUN pip install -r /app/requirments.txt

# copy all project files 
COPY . /app/