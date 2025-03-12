FROM python:3.12.7-alpine3.20

RUN apk add --no-cache git

COPY . ./ScalarBot

WORKDIR /ScalarBot

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "__main__.py"]
