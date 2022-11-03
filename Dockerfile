FROM python:3.9

RUN pip install nltk textblob

ADD ts.py .

CMD ["python3", "./ts.py"]