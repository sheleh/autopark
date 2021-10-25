# pull official base image
FROM python:3

#make and set work directory
RUN mkdir /code
WORKDIR  /code

# set enviroment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

#RUN apk update \
#    && apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# copy project
ADD . /code/

# set port
EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

