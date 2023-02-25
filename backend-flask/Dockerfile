FROM python:3.10-slim-buster

# Inside Container
#make a new folder inside tcontainer
WORKDIR /backend-flask

# Outside container -> Inside container
#this contains the libraries we want to install to run the app
COPY requirements.txt requirements.txt

#Inside container
#Install the python libraries used for the app
RUN pip3 install -r requirements.txt

#Otside container -> inside container
#. means everything in the current directory
# first period .  /backend-flask outside 
# second perod  . /backend-flask inside
COPY . .
COPY scriptToStart.sh /scriptToStart.sh
RUN chmod +x /scriptToStart.sh


#Set env vars
#Inside the container and will remain set when the container is running
ENV FLASK_ENV=development

EXPOSE ${PORT}

# CMD (command)
# python3 -m flask run --host=0.0.0.0 --port=4567
CMD /scriptToStart.sh