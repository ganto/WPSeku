# WPSeku - Wordpress Security Scanner 
# https://github.com/m4ll0k/WPSeku
#
# VERSION v0.4.0
#
# Docker Implementation

FROM python:3.7-alpine

WORKDIR /usr/src/app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

ENTRYPOINT [ "python", "wpseku.py" ]
