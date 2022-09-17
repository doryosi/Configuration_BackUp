FROM python:latest

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY devices_details .

COPY Main.py .

RUN mkdir -p /var/lib/jenkins/Switch_BackUp/

CMD [ "python3", "Main.py"]
