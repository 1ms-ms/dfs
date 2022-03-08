FROM python:3.8-slim-buster

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY notes.py db.py ./
ENV FLASK_APP=notes.py
EXPOSE 5000/tcp
RUN python3 db.py
ENTRYPOINT [ "flask", "run", "--host=0.0.0.0" ]
