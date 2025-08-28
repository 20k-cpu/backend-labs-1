FROM node:20

WORKDIR /var/www/node

COPY package*.json ./
RUN npm install

COPY . .

CMD ["npm", "start"]
