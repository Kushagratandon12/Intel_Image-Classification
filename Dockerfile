FROM python:3.8-slim-buster

COPY . /app  
WORKDIR /app

#Docker - Linux System Dependencies Install -- 
RUN apt-get update

RUN pip install -r requirements.txt

EXPOSE 5000
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]