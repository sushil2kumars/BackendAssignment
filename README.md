# Assignment Project

This README provides documentation for the Predixtions Assinment Project.

## Table of Contents



- [Endpoints](#endpoints)
  - [User Management](#user-management)
    - [User Registration](#user-registration)
    - [User Authentication](#user-authentication)
    - [User Profile](#user-profile)
    - [User Deletion](#user-deletion)
  - [Posts Management](#posts-management)
    - [Create, Retrieve, Update, and Delete Posts](#create-retrieve-update-and-delete-posts)
    - [Posts list](#post-list)

  - [List and Create Posts](#Post-List)
  - [Retrieve, Update, and Delete Posts](#retrieve-update-and-delete-posts)
- [Installation](#installation)

## Code file structure
```
├───api
│   │   admin.py
│   │   apps.py
│   │   tests.py
│   │   urls.py
│   │   __init__.py
│   │
│   ├───migrations
│   │       0001_initial.py
│   │       __init__.py
│   │
│   ├───models
│   │       post.py
│   │       user.py
│   │       __init__.py
│   │
│   ├───serializers
│   │       post.py
│   │       user.py
│   │       __init__.py
│   │
│   └───views
│           post.py
│           user.py
│           __init__.py
│
└───BackendAssignment
        asgi.py
        settings.py
        urls.py
        wsgi.py
        __init__.py
```

## Endpoints

### User Management

#### User Registration

- **URL**: `/api/user/`
- **Method**: POST
- **Description**: Register a new user.

  **Parameters**:
  - JSON data with user details.
  - **Example data**
   ```json
       {"email": "sushil@test.com",  "password": "passw5ord123", "first_name": "Sushil", "last_name": "Kumar"}
    ```

#### User Authentication

- **URL**: `/api/login/`
- **Method**: POST
- **Description**: Authenticate a user and return a JWT token.

  **Parameters**:
  - `username`: User's username.
  - `password`: User's password.
  - - **Example data**
  - ```json
       {
        "email": "sushil@test.com",
        "password": "passw5ord123",
    }
    ```

#### User Profile

- **URL**: `/api/user/`
- **Method**: GET
- **Authorization**: "JWT token"
- **Description**: Retrieve the user's profile if authenticated.

- **URL**: `/api/user/`
- **Method**: PUT
- **Authorization**: "JWT token"
- **Description**: Update the user's profile if authenticated.

  **Parameters**:
  - JSON data with updated user details.

#### User Deletion

- **URL**: `/api/user/`
- **Method**: DELETE
- **Authorization**: "JWT token"
- **Description**: Delete the user's account if authenticated.

### Posts Management

#### Create, Retrieve, Update, and Delete Posts
 **Create a new post**
- **URL**: `/api/post/`
- **Method**: POST
- **Authorization**: "JWT token"
- **Description**: Create a new post.
- ```json
       {
        "title": "test title",
        "content": "test content ",
    }
    ```

  **Parameters**:
  - `Title`: "Post title".
  - `Post`: "Post data"

**Retrieve post by id**
- **URL**: `/api/post/{post_id}/`
- **Method**: GET
- **Authorization**: "JWT token"
- **Description**: Retrieve a post by ID.

  **Parameters**:
  - `post_id`: Post ID.


** Update Post**
- **URL**: `/api/posts/{post_id}/`
- **Method**: PUT
- **Authorization**: "JWT token"
- **Description**: Update an existing post.

  **Parameters**:
  - `post_id`: Post ID.
  - JSON data with updated post details.
 

**Delete post**

- **URL**: `/api/posts/{post_id}/`
- **Method**: DELETE
- **Authorization**: "JWT token"
- **Description**: Delete an existing post.

  **Parameters**:
  - `post_id`: Post ID.
 
    
#### Post List

- **URL**: `/api/posts/`
- **Method**: GET
- **Authorization**: "JWT token"
- **Description**: List posts with optional search and sorting.

  **Parameters**:
  - `query` (optional): Search query string.
  - `sort_by` (optional): Sorting field ('name', 'created', or default 'created_at').
- **Method**: POST
- **Description**: Create a new post.

  **Parameters**:
  - JSON data with post details.



## Installation

1. Clone the repository:
    ```git clone https://github.com/sushil2kumars/BackendAssignment.git ```
2. Crete vertualenv
    
3.  pip3 install requirements.txt
4.  update database configuration
5.  python3 manage.py makemigrations
6.  python3 manage.py migrate
7.  python3 manage.py runserver
