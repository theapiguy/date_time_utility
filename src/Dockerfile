FROM python:alpine
RUN pip install --upgrade pip
WORKDIR /app
ADD . /app
RUN pip install -r requirements.txt
CMD ["python", "src/main.py"]
