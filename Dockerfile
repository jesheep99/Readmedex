FROM python:3.11.10-alpine3.20

RUN mkdir /app 

COPY requirements.txt /app/requirements.txt

COPY main.py /app/main.py

#RUN pwd
RUN cd /app && pip install -r requirements.txt

COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
