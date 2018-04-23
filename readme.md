This is just a simple Server application. I used Python 3.6.5 to build this application.

To run this application from commandline:
```bash
python server.py
python testClient.py
```

This application has also been dockerized. It listens on port 4000. You can build and run the application like so (if Docker is installed):

```bash
docker build -t my-python .
docker run --name my-running-app -p 4000:4000 my-python
```