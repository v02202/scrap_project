#### Scrape project ####
### Set up (Docker-compos) ###
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

### Set up (K8s) ###
If ypu are using Mac M1 as same as me, please try to use the commend under.
1. Initalize minikube with docker engine
    `minikube start --driver=docker --alsologtostderr`
2. Mount local storage to minikube VM
    `minikube mount <source directory>:<target directory>`
3. Deploy all the mechines
    ```
    kubectl apply -f backend-claim0-persistentvolumeclaim.yaml , backend-deployment.yaml , backend-service.yaml , db-claim0-persistentvolumeclaim.yaml , db-claim1-persistentvolumeclaim.yaml , db-deployment.yaml , db-service.yaml
    ```
4. Open the backend service
    `minikube service backend-db-service`

## Commend ##
1. List all pod: `kubectl get pod`
2. Enter backend shell: `kubectl exec -it <backend pod name> bash`
3. Enter db shell with username and password
    ```
    kubectl exec -it <db pod name> bash
    mongosh "mongodb://<username>:<password>@localhost:27017"
    ```
4. Check logs: `kubectl logs -f <backend pod name>`
(Check my [medium](https://medium.com/@v0220225/backend-flask-mongodb-scrapy-5fccbdefb0ae) for detail records)
