FROM python:3

ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR  /code
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt
ADD . /code/



#COPY . /usr/src/app/
EXPOSE 8000

CMD ["python3", "./manage.py"]
#RUN mkdir -p /usr/src/app/