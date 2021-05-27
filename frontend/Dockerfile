FROM node:14.17.0  as builder

RUN apt-get update

ENV APP_ROOT /frontend
ENV HOST 0.0.0.0

RUN mkdir ${APP_ROOT}
WORKDIR ${APP_ROOT}
ENV PATH ${APP_ROOT}/node_modules/.bin:$PATH

# Copy the package.json and install dependencies
COPY package*.json .

#RUN yarn 
#RUN yarn build
RUN yarn cache clean

# Copy all the app code
COPY . ${APP_ROOT}

#RUN yarn generate

#RUN ./entrypoint.sh

# run entrypoint.sh
CMD ["yarn", "deploy"]