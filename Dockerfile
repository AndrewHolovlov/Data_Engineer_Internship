FROM python:3.8

#MAINTAINER AndrewHolovlov 'holovlovandrii@gmail.com'

RUN apt-get update -y && \
    apt-get install -y python-pip python3-dev


#RUN mkdir -p /app
WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY . /app

EXPOSE 80

ENTRYPOINT [ "python" ]
CMD [ "app.py" ]
