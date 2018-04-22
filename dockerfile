FROM python:3.6.5

RUN mkdir /src
COPY *.py /src/

# RUN pip install <>
EXPOSE 4000
CMD [ "python", "./src/server.py" ]
