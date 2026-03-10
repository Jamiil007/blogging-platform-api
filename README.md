Welcome to the 007 james beyond blogging platform 

Here's the project structure :

````bash

blogging-platform-api
│
├── app.py
├── config.py
├── database.py
├── models.py
├── requirements.txt
├── README.md
│
├── routes
│   ├── users.py
│   ├── posts.py
│   └── comments.py
│
├── instance
│   └── blog.db
│
└── __pycache__
````


````bash

| File             | Purpose                              |
| ---------------- | ------------------------------------ |
| app.py           | Main application entry point         |
| config.py        | Application configuration            |
| database.py      | Database initialization              |
| models.py        | Data models (Users, Posts, Comments) |
| routes           | API endpoint definitions             |
| instance/blog.db | SQLite database file                 |

````


git clone and make virtual env and pip install the requirements should be good . 

then simply run through 

````bash

python3 app.py
````



The endpoints are for post : /users , /posts , /comments
		      get : /users , /users/<id> , /posts , /posts/<id> , /comments , /comments/<post_id> ,  
		      delete ; /users/id , /posts/id , /comments/post_id 

content-type is application/json 
