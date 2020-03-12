FROM python:3.6.1-alpine

# Update image
RUN apk update \
  && apk add \
  build-base

# Copy requirements
COPY ./requirements.txt /app/
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# COPY ./install-hcltojson.sh /app/
# RUN './app/install-hcltojson.sh'

# Copy all files to Docker container
COPY . /app

# Argument to python command
ENTRYPOINT ["python", "./app.py"]
