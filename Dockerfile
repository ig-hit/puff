FROM python:3.8-buster

WORKDIR /home/app
COPY . .

RUN pip3 install virtualenv
RUN . venv/bin/activate
RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["./manage.py"]
