#!/bin/bash


./app.sh

echo "### Installing stack app for SSL support ... ($pwd)"
# run the generation of certs including the restarting of services in the SSL scope
. nginx/ssl/ssl-generator.sh
