FROM python:3.9.6-alpine3.14

ENV PYTHONWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

WORKDIR /src
# RUN apk add build-base

RUN python -m pip install --upgrade pip
COPY requirements.txt .

RUN pip install -r requirements.txt


COPY src .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--reload"]
# CMD ["hypercorn", "main:app", "--bind", "0.0.0.0:8000"]
EXPOSE 8000
