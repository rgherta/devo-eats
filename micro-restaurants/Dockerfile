FROM python:3.9-slim-buster
LABEL project="micro-restaurants"


COPY ./src /app
WORKDIR /app

RUN pip install -U Flask firebase-admin

ENV FLASK_APP="app.py"
ENV FLASK_ENV="development"
ENV FLASK_DEBUG="0"

ENTRYPOINT ["python"]
CMD ["app.py"]