FROM python:3.11.10-alpine3.20

RUN mkdir /app 

COPY requirement.txt /app/requirement.txt

COPY main.py /app/main.py

RUN pip install -r requirements.txt

COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
