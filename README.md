# Todo API

Simple Todo API built with FastAPI.

## Features

* Pydantic BaseModel
* Get all tasks
* Get task by ID
* Create task
* Put task by ID
* Delete task

## Technologies

* Python 3
* FastAPI
* Pydantic

## Endpoints

### Get all tasks

GET /tasks

### Get task by ID

GET /tasks/{id}

### Create task

POST /tasks

### Put task

PUT /tasks/{id}

### Delete task

DELETE /tasks/{id}

## Run project

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

## API Documentation

After starting the server:

* /docs
* /tasks
