FROM continuumio/miniconda3

COPY . /app  
WORKDIR /app

RUN conda update --name base conda && conda env create --file envrionment.yaml
RUN pip install https://github.com/google-coral/pycoral/releases/download/release-frogfish/tflite_runtime-2.5.0-cp38-cp38-linux_x86_64.whl

SHELL ["conda", "run", "--name", "app", "/bin/bash", "-c"]

EXPOSE 5000
ENTRYPOINT ["conda", "run", "--name", "app", "python", "app.py"]
# ENTRYPOINT [ "python" ]
# CMD [ "app.py" ]