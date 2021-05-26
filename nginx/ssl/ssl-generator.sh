#################
## Este script genera los certificados SSL (autofirmados) para asegurar la comunicación a través del protocolo HTTPS
## Para esto se utiliza la herramienta Certbot que a su vez hace uso del servicio Letsencrypt
## Mas información de Certbot: https://certbot.eff.org/
## Mas información de Letsencrypt: https://letsencrypt.org/es/
## Los certificados seran renovados automaticamente cada 5 dias por Certbot
#################

#!/bin/bash

domains=(galenoapp.teamcloud.com.co)
rsa_key_size=4096
root_dir="./nginx/ssl"
data_path="./$root_dir/data/certbot"
email="pabloguineabenito@hotmail.com" 
staging=0
current_path=$(pwd)

if [ -d "$data_path" ]; then
    read -p "Existing data found for $domains. Continue and replace existing certificate? (y/N) " decision
    if [ "$decision" != "Y" ] && [ "$decision" != "y" ]; then
        # start the service with ssl
        docker-compose down
        docker-compose -f docker-compose-ssl.yml up -d 
        exit
    fi
fi

if [ ! -e "$data_path/conf/options-ssl-nginx.conf" ] || [ ! -e "$data_path/conf/ssl-dhparams.pem" ]; then
    echo "### Downloading recommended TLS parameters ..."
    mkdir -p "$data_path/conf"
    cp "$root_dir/options-ssl-nginx.conf" "$data_path/conf/options-ssl-nginx.conf"
    cp "$root_dir/ssl-dhparams.pem" "$data_path/conf/ssl-dhparams.pem"
    #curl -s https://raw.githubusercontent.com/certbot/certbot/master/certbot-nginx/certbot_nginx/_internal/tls_configs/options-ssl-nginx.conf >"$data_path/conf/options-ssl-nginx.conf"
    #curl -s https://raw.githubusercontent.com/certbot/certbot/master/certbot/certbot/ssl-dhparams.pem >"$data_path/conf/ssl-dhparams.pem"
    echo
fi

for domain in "${domains[@]}"; do
    echo "### Removing old certificate for $domain ..."
    docker-compose run --rm --entrypoint "\
    rm -Rf /etc/letsencrypt/live/$domain && \
    rm -Rf /etc/letsencrypt/archive/$domain && \
    rm -Rf /etc/letsencrypt/renewal/$domain.conf" certbot
    echo
done

for domain in "${domains[@]}"; do
    echo "### Creating dummy certificate for $domain ..."
    path="/etc/letsencrypt/live/$domain"
    mkdir -p "$data_path/conf/live/$domain"
    docker-compose run --rm --entrypoint "\
    openssl req -x509 -nodes -newkey rsa:1024 -days 1\
      -keyout "$path/privkey.pem" \
      -out "$path/fullchain.pem" \
      -subj '/CN=localhost'" certbot
    echo
done

echo "### Starting nginx ... "
docker-compose down
docker-compose -f docker-compose-ssl.yml up -d
echo

for domain in "${domains[@]}"; do
    echo "### Removing dummy certificate for $domain ..."
    docker-compose run --rm --entrypoint "\
    rm -Rf /etc/letsencrypt/live/$domain" certbot
    echo
done

echo "### Requesting Let's Encrypt certificates ..."

# Select appropriate email arg
case "$email" in
"") email_arg="--register-unsafely-without-email" ;;
*) email_arg="--email $email" ;;
esac

# Enable staging mode if needed
if [ $staging != "0" ]; then staging_arg="--staging"; fi

for domain in "${domains[@]}"; do
    docker-compose run --rm --entrypoint "\
    certbot certonly --webroot -w /var/www/certbot \
      $staging_arg \
      $email_arg \
      -d $domain \
      --rsa-key-size $rsa_key_size \
      --agree-tos \
      --force-renewal" certbot
    echo
done

echo "### Reloading server ..."
docker-compose exec server nginx -s reload
