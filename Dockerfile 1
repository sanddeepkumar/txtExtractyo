FROM python:3.10.8-slim-buster
RUN apt-get update -y && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends gcc libffi-dev musl-dev ffmpeg aria2 python3-pip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY . /app/
WORKDIR /app/

RUN apk add --no-cache gcc libffi-dev musl-dev ffmpeg aria2 \
    && pip install --no-cache-dir -r requirements.txt
CMD [ "python", "./main.py" ]
# RUN pip3 install --no-cache-dir --upgrade --requirement requirements.txt
# CMD gunicorn app:app & python3 main.py
