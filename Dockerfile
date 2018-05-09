FROM python:3.6

RUN apt-get -y update
RUN apt-get -y install git

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

RUN git clone https://github.com/albert-gilharry/data602-assignment-3 /usr/src/app/trader3

EXPOSE 5000

CMD [ "python", "/usr/src/app/trader3/app.py" ]