FROM python:3.7-alpine
RUN apk add mariadb-dev build-base py3-scikit-learn
WORKDIR /src
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["python3", "getData.py"]
