FROM python:3

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY /app/requirements.txt /code/

RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install -r requirements.txt

COPY /app/ /code/

RUN chmod 755 entrypoint.sh
