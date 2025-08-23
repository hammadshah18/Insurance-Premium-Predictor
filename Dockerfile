#use base image 
FROM python:3.13-slim


# set Working directory

WORKDIR /app

#COPY REQUIREMENTS AND INSTALL DEPENDENCIES
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#COPY rest of application code

COPY . .

#EXPOSE THE APPLICATION PORT

EXPOSE  8000

#COMMAND TO START FASTAPI APPLICATION

CMD [ "uvicorn","main:app","--host","0.0.0.0","--port","8000" ]

# CMD ['uvicorn','main:app',"--host","0.0.0.0","--port","8000"]



