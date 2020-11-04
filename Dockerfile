FROM python:3.6

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

COPY ./app.py /nestorbot_app.py
COPY ./nestorbot.py /nestorbot.py

CMD [ "python3", "/nestorbot_app.py" ]


