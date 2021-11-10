FROM python:3.7-alpine
RUN apk add mariadb-dev build-base
WORKDIR /src
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["python3", "getData.py"]
