FROM python:3.8

WORKDIR /opt
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "./src/bot.py"]