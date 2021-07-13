#!/bin/bash

echo "### Installing stack app "
sudo chmod +x backend/entrypoint.sh 
sudo docker-compose up --build -d