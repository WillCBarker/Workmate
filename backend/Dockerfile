FROM python:3

# Move into directory of manage.py
WORKDIR /config

COPY . /config

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000