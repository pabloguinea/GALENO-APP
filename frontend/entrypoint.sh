#!/bin/sh

ls -la node_modules
ls -la node_modules/.bin/
yarn deploy

exec "$@"