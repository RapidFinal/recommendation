FROM python:2.7.15
EXPOSE 5000
ADD requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
ADD . .
VOLUME [ "/app" ]
CMD python server.py
