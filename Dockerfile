FROM python

WORKDIR /myapp

COPY ./app.py .

RUN pip install pymysql

CMD ["python", "app.py"]