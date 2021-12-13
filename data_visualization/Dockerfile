FROM node:alpine

ENV NEXT_TELEMETRY_DISABLED 1
ENV PORT 3000

WORKDIR ${ROOT}

COPY . .

RUN npm install

RUN npm run build

EXPOSE 3000

ENTRYPOINT ["npm", "start"]