FROM python:3.10-alpine
RUN pip3 install --upgrade pip
RUN pip3 install psycopg2-binary
ENV PYTHONUNBUFFERED=1
WORKDIR /django
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
