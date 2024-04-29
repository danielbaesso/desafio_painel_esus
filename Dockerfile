FROM ubuntu:latest

RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    apt-get clean

ENV PATH="/usr/bin/python3:${PATH}"
ENV PATH="/usr/bin/pip3:${PATH}"

WORKDIR /project

COPY . /project

RUN pip3 install -r requirements.txt --no-cache-dir --break-system-packages

EXPOSE 5000

CMD ["python3", "run.py"]
