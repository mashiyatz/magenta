FROM python:3.6-stretch
FROM tensorflow/tensorflow:latest-gpu-py3

RUN apt-get update && apt-get install -y \
    libev-dev

RUN pip install --upgrade pip && \
    pip install \
    numpy==1.15.4 \
    magenta \
    pyFluidSynth \
    pretty_midi

WORKDIR /work/

COPY work .
ENV PYTHONPATH /work