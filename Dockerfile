FROM python:3
WORKDIR /proj
COPY requirments.txt /proj
RUN pip install -r requirments.txt
COPY . .
EXPOSE 5000
CMD gunicorn --bind 0.0.0.0:5000 main:app

