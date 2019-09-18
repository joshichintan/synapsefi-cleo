FROM python:3.6-slim

USER root
WORKDIR /app
ADD . /app

#ENV LDFLAGS "-I/usr/local/opt/openssl/include -L/usr/local/opt/openssl/lib"
RUN pip install --trusted-host pypi.python.org -r requirements.txt
EXPOSE 5000
ENV FLASK_APP start.py
CMD ["python", "start.py"]