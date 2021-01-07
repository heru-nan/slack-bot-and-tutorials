FROM python:3.6.3

ENV MYSQL_PORT 3306

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

ENV PYTHONUNBUFFERED=1

WORKDIR /nestor_save_msgs


COPY ./connection.py /connection.py
COPY ./nestor_save_msgs.py /nestor_save_msgs.py

CMD [ "python", "/nestor_save_msgs.py" ]
