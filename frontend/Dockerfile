FROM node:latest  as builder

RUN apt-get update

ENV APP_ROOT /frontend
ENV HOST 0.0.0.0

RUN mkdir ${APP_ROOT}
WORKDIR ${APP_ROOT}
ENV PATH ${APP_ROOT}/node_modules/.bin:$PATH

# Copy the package.json and install dependencies
COPY package*.json .

RUN yarn install --silent
RUN yarn build
RUN yarn cache clean

# Copy all the app code
COPY . ${APP_ROOT}


# run entrypoint.sh
ENTRYPOINT ["/frontend/entrypoint.sh"]