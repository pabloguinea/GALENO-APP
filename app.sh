#!/bin/bash

echo "### Installing stack app "
sudo chmod -R 777 *
sudo docker-compose up --build -d
make deploy-frontend