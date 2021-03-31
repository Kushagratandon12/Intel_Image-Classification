FROM python:3.8-slim-buster
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN pip install https://github.com/google-coral/pycoral/releases/download/release-frogfish/tflite_runtime-2.5.0-cp38-cp38-linux_x86_64.whl
EXPOSE 5000
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]