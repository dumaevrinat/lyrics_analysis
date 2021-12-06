FROM python:3.7-slim

ARG SCRIPT_TO_RUN="lyrics.py"
ENV SCRIPT_TO_RUN=$SCRIPT_TO_RUN

WORKDIR ${ROOT}

COPY . .

RUN apt-get update && rm -rf /var/cache/apt

RUN pip install --no-cache-dir -U pip
RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python", "/app/$APP"]
