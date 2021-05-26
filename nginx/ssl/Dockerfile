FROM nginx:1.20.0-alpine

RUN mkdir /app
RUN rm /etc/nginx/conf.d/default.conf
COPY conf.d/nginx.conf /etc/nginx/conf.d/
WORKDIR /app