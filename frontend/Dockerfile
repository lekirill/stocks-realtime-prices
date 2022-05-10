FROM node:lts-alpine

WORKDIR /stocks

COPY ./stocks/package.json /stocks/package.json
COPY ./stocks/package-lock.json /stocks/package-lock.json
RUN npm install

COPY ./stocks /stocks

CMD npm run serve