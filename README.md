# GraphQL Playground

## First Project: complete-guide-to-building-a-graphql-api

Based on:

* Docker
* Express
* Express-GraphQL
* GraphQL
* GraphiQL
* Babel

How to use it:

* After cloning the repository, cd into "complete-guide-to-building-a-graphql-api/GRAPHQL/" and run 
	* `docker-compose build`
	* `docker-compose up -d`
	* Get into the running container by executing `docker exec -it graphql_graphiql_1 bash`. Your container name may be different.
	* Inside the container run `npm install && npm run serve`
	* Hit http://localhost:4000/graphql and play around with graphiql.
	* When you are done, exit your container and execute `docker-compose down`

* **Note:** You probably have to change the docker-compose.yml file in the root of the GRAPHQL folder with regards to the volumes. When you are on a windows machine, you probably have to define the current directory as an absolute path like I did. If you are one a linux or mac machine then you can just comment out the windows related line and uncomment the line above in the docker-compose.yml file.