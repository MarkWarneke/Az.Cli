FROM python:3.7-alpine

# Update image
RUN apk update \
  && apk add \
  build-base

# Copy requirements
COPY ./requirements.txt /app/
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


# Copy all files to Docker container
COPY . /app

# Argument to python command
ENTRYPOINT ["python", "./app"]
