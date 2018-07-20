FROM python:2.7.15
EXPOSE 5000
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt
VOLUME [ "/app" ]
CMD python server.py
