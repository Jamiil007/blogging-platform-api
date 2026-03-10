# Blogging Platform API
# 007

A lightweight Flask API for managing users, posts, and comments with SQLite database support.  

---

## Features

- User registration and management
- Create, read, and delete posts
- Add and retrieve comments
- JSON-based REST API
- SQLite database with SQLAlchemy ORM

---

## Tech Stack

- Python 3.12
- Flask
- Flask-SQLAlchemy
- Flask-JWT-Extended (optional for authentication)
- SQLite

---

## Project Structure


blogging-platform-api
│
├── app.py # Main application entry point
├── config.py # App configuration
├── database.py # Database initialization
├── models.py # SQLAlchemy models (User, Post, Comment)
├── requirements.txt # Python dependencies
├── README.md # Project documentation
│
├── routes # API endpoints
│ ├── users.py
│ ├── posts.py
│ └── comments.py
│
├── instance # Local database
│ └── blog.db
└── pycache # Python cache



---

## Installation

Clone the repository:

```bash

git clone https://github.com/Jamiil007/blogging-platform-api.git
cd blogging-platform-api
````


Create a virtual environment and activate it:

````bash 

python3 -m venv venv
source venv/bin/activate   # macOS / Linux
venv\Scripts\activate      # Windows
````

then install dependencies through :

````bash

python3 -m venv venv
source venv/bin/activate   # macOS / Linux
venv\Scripts\activate      # Windows
````

## API ENDPOINTS

````bash

#### Users

| Method | Endpoint    | Description     |
| ------ | ----------- | --------------- |
| POST   | /users      | Create new user |
| GET    | /users      | Get all users   |
| GET    | /users/<id> | Get user by ID  |
| DELETE | /users/<id> | Delete user     |


#### Posts

| Method | Endpoint    | Description     |
| ------ | ----------- | --------------- |
| POST   | /posts      | Create new post |
| GET    | /posts      | Get all posts   |
| GET    | /posts/<id> | Get post by ID  |
| DELETE | /posts/<id> | Delete post     |


#### Comments

| Method | Endpoint            | Description             |
| ------ | ------------------- | ----------------------- |
| POST   | /comments           | Create comment          |
| GET    | /comments           | Get all comments        |
| GET    | /comments/<post_id> | Get comments by post    |
| DELETE | /comments/<post_id> | Delete comments by post |

````


## Database

SQLite database located at instance/blog.db

Models defined in models.py:

User: id, username, email, password

Post: id, title, content, author_id

Comment: id, text, user_id, post_id
