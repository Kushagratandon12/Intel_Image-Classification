# Docker System Setup

## Create A File Named As Dockerfile without an extension

```docker
FROM python:3.8-slim-buster

COPY . /app  
WORKDIR /app

#Docker - Linux System Dependencies Install -- 
RUN apt-get update

RUN pip install -r requirements.txt

EXPOSE 5000
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]
```

## Build The Image For Docker

```docker
sudo docker build --tag <docker_name>
```

After The Build Is Complete Start The Docker Container 

```docker
sudo docker run -p 5000:5000 --detach <docker_name>
```

Push The Docker Container To Docker Hub

```docker
docker login
docker container ls -a #will show the docker container with the tag 
```

![Docker%20System%20Setup%200848c02415484e869b341156965daa3c/Untitled.png](Docker%20System%20Setup%200848c02415484e869b341156965daa3c/Untitled.png)

```docker
docker tag ceciphillip:awesomeapp <your_dockerhub_id>/<docker_hub_repo_name>
docker images ls 
docker push <your_dockerhub_id>/<docker_hub_repo_name>
```
