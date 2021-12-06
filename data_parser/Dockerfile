FROM python:3.7-slim

WORKDIR ${ROOT}

COPY . .

RUN apt-get update && rm -rf /var/cache/apt

RUN pip install --no-cache-dir -U pip
RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python", "/app/main.py"]
