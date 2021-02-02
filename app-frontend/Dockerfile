FROM nginx:latest
LABEL project="FriendlyEatsRG"

COPY ./src /usr/share/nginx/html 
COPY ./certs /etc/nginx/certs

COPY default.conf /etc/nginx/conf.d/default.conf