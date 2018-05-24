FROM python:2.7

RUN apt-get -y update
RUN apt-get -y install git

WORKDIR /home/ec2-user

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

RUN pip install --upgrade --no-cache-dir https://get.graphlab.com/GraphLab-Create/2.1/Harpreet.Shoker87@spsmail.cuny.edu/3E6D-7FB4-971D-81F5-D440-CF9B-1D17-BA6F/GraphLab-Create-License.tar.gz

RUN git clone https://github.com/albert-gilharry/data602-final-project /home/ec2-user/insta

EXPOSE 5000

CMD [ "python", "/home/ec2-user/insta/app.py" ]