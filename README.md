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


## Second Project: hackernews-clone

Based on:

* Docker
* Django
* Graphene
* Graphene-Django
* Django-Filter
* Django-Graphql-Jwt

This project is based on the tutorial you can find on [https://www.howtographql.com/graphql-python/0-introduction/](https://www.howtographql.com/graphql-python/0-introduction/)

How to use it:

* After cloning the repository, cd into "hackernews-clone" and run 
	* `docker-compose build`
	* `docker-compose up -d`
	* Get into the running container by executing `docker exec -it hackernewsclone_web_1 bash`. Your container name may be different.
	* Inside the container just execute `start_server.sh`.
	* Hit http://localhost:8000/graphql and play around with graphiql.
	* If you want to test the authentication part then you probably need a tool like Postman or Insomnia where you can put your auth token into the Authorization header with a JWT prefix
	* When you are done, exit your container and execute `docker-compose down`

Note: According to the howtographql.com tutorial you should create a virtual environment by invoking the following commands

```
python3.6 -m venv venv
source venv/bin/activate
```

Because we already use docker as an isolated environment for one application this step is probably not necessary. Furthermore they state that with the activated environment you should run the following commands:

```
pip install django==2.0.2 graphene==2.0.1 graphene-django==2.0.0 django-filter==1.1.0 django-graphql-jwt==0.1.5
django-admin startproject hackernews
cd hackernews
python manage.py migrate
python manage.py runserver
```

The first four lines are already executed either by the Dockerfile or by docker-compose.yml. The last command is integrated and tweaked into the `start_server.sh` file.

Mutations to try out:

```
mutation {
  createLink(
    url: "http://github.com",
    description: "Lots of code"
  ){
    id
    url
    description
  }
}

mutation {
  createUser(
    username: "christoph", email: "christoph@awesomecompany.com", password: "123"
  ){
    user {
      id
      username
      email
    }
    
  }
}

mutation {
  tokenAuth(username: "christoph", password: "123"){
    token
  }
}

mutation {
  verifyToken(token: "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6IkNocmlzdG9waCIsImV4cCI6MTUyNTcyMDkyNiwib3JpZ19pYXQiOjE1MjU3MjA2MjZ9.pk2fC6CsQItTm--YbQgFqMzVyO060HM4dSztAGiAZUg"){
    payload
  }
}

// This one only works with properly set HTTP headers like Content-Type: application/json
// and Authorization: JWT <token>
mutation {
	createLink(
		url: "https://github.com/christophschmidl",
		description: "Christoph Github"
	) {
		id
		url
		description
		postedBy {
			id
			username
			email
		}
		
	}
}

// This one only works with properly set HTTP headers like Content-Type: application/json
// and Authorization: JWT <token>
mutation {
	createVote(linkId: 1) {
		user {
			id
			username
			email
		}
		link {
			id
			description
			url
		}
	}
}

// Relay specific mutation.
// This one only works with properly set HTTP headers like Content-Type: application/json
// and Authorization: JWT <token>
mutation {
  relayCreateLink(input: {
    url: "http://deployeveryday.com",
    description: "Author's Blog"
  }) {
    link {
      id
      url
      description
    }
  }
}

```


Queries to try out:

```
// If you want to see what's available
query {
  __schema {
    types {
      name
    }
  }
}

{
  __type(name: "User") {
    name
    description
  }
}


query {
  links {
    id
    description
    url
  }
}

query {
  users {
    id
    username
    email
  }
}

// This one only works with properly set HTTP headers like Content-Type: application/json
// and Authorization: JWT <token>
query {
	me {
		id
		username
	}
}

query {
	votes {
		id
		user {
			id
			username
		}
		link {
			id
			url
		}
	}
}

query {
	links {
		id
		url
		votes {
			id
			user {
				id
				username
			}
		}
	}
}

// Relay specific query
query {
  relayLinks {
    edges {
      node {
        id
        url
        description
        votes {
          edges {
            node {
              id
              user {
                id
              }
            }
          }
        }
      }
    }
  }
}


query {
  relayLinks(first: 1) {
    edges {
      node {
        id
        url
        description
      }
    }
     pageInfo {
      startCursor
      endCursor
    }
  }
}
```






