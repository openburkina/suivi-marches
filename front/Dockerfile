FROM node:lts

WORKDIR /app

COPY . .

RUN yarn install \
  --prefer-offline \
  --frozen-lockfile \
  --non-interactive \
  --production=false

ENV HOST 0.0.0.0
EXPOSE 80

CMD [ "yarn", "dev" ]
