#### Scrape project ####
## Set up ##
1. Create an app in [Twitter develop console](https://developer.twitter.com/en)
2. Copy .env.template as .env
3. Fill in .env values
4. Run the code 
    ```
    docker-compose build
    docker-compose up -d
    ```

## Commend ##
1. Enter mongodb shell with your username and password: `docker-compose exec db mongosh -u "..." -p "..." `
2. Enter backend if you want to create a new spider: `docker-compose exec backend bash`
3. Check backend log: `docker-compose logs -f backend`

(Check my [medium](https://medium.com/@v0220225/backend-flask-mongodb-scrapy-5fccbdefb0ae) for detail records)
