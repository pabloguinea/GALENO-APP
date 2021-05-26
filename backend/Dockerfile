FROM python:3.8.10-slim-buster

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install SO dependencies and update repositories
RUN apt-get update \
    && apt-get install -y make gcc netcat \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get update \
    && apt-get remove libpq5 \
    && apt-get install -y libpq-dev python3-dev

# create the app user
#RUN addgroup -S app && adduser -S app -G app

# set work directory
ENV APP_HOME=/backend
RUN mkdir -p $APP_HOME
RUN mkdir $APP_HOME/static
RUN mkdir $APP_HOME/media
WORKDIR $APP_HOME

# install dependencies
COPY requirements.txt $APP_HOME
RUN python3 -m venv .
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install setuptools
RUN python3 -m pip install psycopg2-binary
RUN python3 -m pip install --no-cache-dir -r requirements.txt

# copy source code to virtual
COPY ./entrypoint.sh $APP_HOME
RUN chmod +x $APP_HOME/entrypoint.sh
COPY . $APP_HOME

RUN ls -la $APP_HOME

# chown all the files to the app user
#RUN chown -R app:app $APP_HOME

# change to the app user
#USER app

# open port
EXPOSE 8000

# run entrypoint.sh
ENTRYPOINT ["/backend/entrypoint.sh"]
