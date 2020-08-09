FROM python:3.7
USER root
ENV PYTHONUNBUFFERED 1
WORKDIR /home/app/
COPY requirements.txt /home/app/
RUN pip install -r requirements.txt
ENV PYTHONPATH=/usr/local/lib/python3.7
COPY . .
EXPOSE 8000
EXPOSE 6800
# COPY scrapyd.conf ~/
