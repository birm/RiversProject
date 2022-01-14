FROM node:16-alpine as build
WORKDIR /usr/app
COPY ./ /usr/app
RUN npm install
RUN npm run build
RUN ls dist/


FROM nginx:alpine
COPY ./nginx/nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=build /usr/app/dist/Frontend /usr/share/nginx/html
EXPOSE 80
