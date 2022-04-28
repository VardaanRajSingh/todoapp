FROM python:alpine

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

ENTRYPOINT [ "uvicorn", "main:app", "--host=0.0.0.0", "--port=5000" ]
