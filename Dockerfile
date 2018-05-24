FROM python:2.7

RUN apt-get -y update
RUN apt-get -y install git

WORKDIR /home/ec2-user

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

RUN git clone https://github.com/albert-gilharry/data602-final-project /home/ec2-user/insta

EXPOSE 5000

CMD [ "python", "/home/ec2-user/insta/app.py" ]