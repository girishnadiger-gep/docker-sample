FROM ubuntu

WORKDIR /app

ADD . /app

RUN apt-get update
RUN apt-get install python3 -y
RUN apt-get update
RUN apt-get install python3-pip -y
RUN pip3 install -r requirements.txt

EXPOSE 4000

CMD ["python3", "main.py"]
