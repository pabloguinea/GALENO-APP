#!/bin/bash

./app.sh

# run the generation of certs including the restarting of services in the SSL scope
. nginx/ssl/ssl-generator.sh
