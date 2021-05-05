FROM python:3.7-buster

# Set a docker label to advertise multi-model support on the container
LABEL com.amazonaws.sagemaker.capabilities.multi-models=false
# Set a docker label to enable container to use SAGEMAKER_BIND_TO_PORT environment variable if present
LABEL com.amazonaws.sagemaker.capabilities.accept-bind-to-port=true

RUN apt-get update -y && apt-get -y install --no-install-recommends default-jdk
RUN rm -rf /var/lib/apt/lists/*

COPY container/req.txt /opt/ml/req.txt
RUN pip install --upgrade pip
RUN pip --no-cache-dir install -r opt/ml/req.txt

ENV PYTHONUNBUFFERED=TRUE
ENV PYTHONDONTWRITEBYTECODE=TRUE
ENV PYTHONPATH="/opt/ml/code:${PATH}"

COPY container/main.py /opt/ml/code/main.py
COPY container/train.py /opt/ml/code/train.py
COPY container/handler.py /opt/ml/code/serving/handler.py

ENTRYPOINT ["python", "/opt/ml/code/main.py"]