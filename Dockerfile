FROM python:3

COPY ./src /src
COPY ./output /output
COPY ./data /data

ADD ./requirements.txt /requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt
