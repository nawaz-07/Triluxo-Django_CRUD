# Triluxo-Django_CRUD

A Python-based RESTful API for managing a simple task list. This API allows users to perform CRUD (Create, Read, Update, Delete) operations on tasks and uses Django as the web framework with an SQLite database for data storage.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/task-list-api.git
   cd task-list-api
   

2. Create and activate a virtual environment (recommended):
   ```
   python -m venv venv
   source venv/bin/activate
   

3. Install project dependencies:
   ```
   pip install -r requirements.txt
   

4. Apply database migrations:
   ```
   python manage.py migrate
   

5. Run the development server:
   ```
   python manage.py runserver

   

## Usage

This API provides endpoints to manage tasks. You can interact with the API using HTTP requests. Below are the available endpoints:

## Endpoints

POST /tasks: Create a new task with a title and description.

GET /tasks: Retrieve a list of all tasks.

GET /tasks/{id}: Retrieve a specific task by its ID.

PUT /tasks/{id}: Update an existing task by providing the task's ID.

DELETE /tasks/{id}: Delete a task by providing the task's ID


## Example Requests and Responses

1. Create a new task:
```
POST /tasks
Content-Type: application/json

{
  "title": "Task 1",
  "description": "Description of Task 1"
}
```


2. Retrieve all tasks:

```
GET /tasks
```


3. Retrieve a specific task by ID:
```
GET /tasks/1
```


4. Update an existing task:

```
PUT /tasks/1
Content-Type: application/json

{
  "title": "Updated Task",
  "description": "Updated Description"
}
```


5. Delete a task:

```
DELETE /tasks/1
```


## Testing

Unit tests for the API endpoints are provided to ensure they function correctly. You can run the tests using the following command:

```
python manage.py test tasklist_app.tests
or
python manage.py test
```


## Explanation of Design Choices and Challenges:

- **Django Framework**: I chose to use Django as the web framework for its robustness, built-in features and tools, and extensive documentation.

- **SQLite Database**: SQLite was selected for its simplicity and ease of use, making it suitable for this small-scale project.

- **Django Rest Framework**: Django Rest Framework was used to simplify API development, providing serializers, views, and exception handling.

- **Challenges**: Challenges faced during test.py creation and handling different types of exceptions.





