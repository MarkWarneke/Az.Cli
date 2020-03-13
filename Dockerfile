FROM python:3.7-alpine

COPY REQUIREMENTS.txt /

RUN apk --update add python py-pip openssl ca-certificates py-openssl wget
RUN apk --update add --virtual build-dependencies libffi-dev openssl-dev python-dev py-pip build-base \
  && pip install --upgrade pip \
  && pip install -r REQUIREMENTS.txt \
  && apk del build-dependencies


COPY src/ /app
WORKDIR /app

# Argument to python command
ENTRYPOINT ["python"]
