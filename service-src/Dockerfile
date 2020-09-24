FROM python:3.6
COPY . /code
WORKDIR /code
EXPOSE 5000
RUN python3.6 -m pip install -r requirements.txt
CMD python3.6 app.py