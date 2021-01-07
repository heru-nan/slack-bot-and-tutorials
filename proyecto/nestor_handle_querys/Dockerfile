FROM python:3.6.3

ENV MYSQL_PORT 3306

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

ENV PYTHONUNBUFFERED=1

WORKDIR /nestor_handle_querys


COPY ./connection.py /connection.py
COPY ./nestor_handle_querys.py /nestor_handle_querys.py

CMD [ "python", "/nestor_handle_querys.py" ]
