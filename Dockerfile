FROM python:2.7.15
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD python server.py