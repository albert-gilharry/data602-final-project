FROM python:2.7

WORKDIR /home/ec2-user/insta

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

RUN git clone https://github.com/albert-gilharry/data602-assignment-3 /usr/src/app/insta

EXPOSE 5000

CMD [ "python", "/home/ec2-user/insta/app.py" ]