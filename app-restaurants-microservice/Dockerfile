FROM python:3.9-slim-buster
LABEL project="micro-restaurants"


COPY ./src /app
WORKDIR /app

RUN pip install -U Flask

ENV FLASK_APP="app.py"
ENV FLASK_ENV="development"

CMD ["python3", "-m", "flask", "run"]