FROM tensorflow/tensorflow
RUN apt-get update
RUN apt-get install -y libmariadb3 libmariadb-dev
WORKDIR /src
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . .
CMD ["python3", "getData.py"]
