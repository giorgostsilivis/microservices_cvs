FROM python:3.8
#FROM python:3.9-buster

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


#Change working directory
#RUN mkdir /nrv

#WORKDIR /nrv
# COPY requirements.txt
COPY ./requirements.txt ./
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
# Copy main.py file
COPY nrv/ .

#WORKDIR /nrv/


EXPOSE 4001

#RUN python app3.py
CMD ["python","app3.py"]
