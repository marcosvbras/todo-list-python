# TODO List in Python

[![Build Status](https://travis-ci.org/marcosvbras/todo-list-python.svg?branch=master)](https://travis-ci.org/marcosvbras/todo-list-python)

<p align="center">
  <img src="https://raw.github.com/marcosvbras/todo-list-python/master/images/to-do-list.jpg" alt="Custom image"/>
</p>

**TO DO List** is a simple API project created with everything that I learned on course [Do Zero ao Deploy](https://github.com/cassiobotaro/do_zero_ao_deploy) by [Cássio Botaro](https://github.com/cassiobotaro/).

This project covers the following concepts:
- Python environments with [Pipenv](https://github.com/pypa/pipenv)
- Test Driven Development with [PyTest](https://docs.pytest.org/en/latest/)
- Starting with [Flask](http://flask.pocoo.org/) framework
- Continuous Integration with [Travis](https://travis-ci.org/)
- Continuous Deployment with [Heroku](https://www.heroku.com/)

Starting from what has been taught, I improved the API with **MongoDB** persistence.

## How To Run

This project was developed with **Python version 3.6**, so, for a correct running, it is recommended to install this one.

First, it is required to install all project dependencies. You can use [Pipenv](https://github.com/pypa/pipenv) or [Virtualenv](https://virtualenv.pypa.io/en/stable/). If you are using **Pipenv**, use the following command to install from **Pipfile**:

```bash
$ pipenv install
```

...and active the environment:
```bash
$ pipenv shell
```

However, if you are using **Virtualenv**, you need to activate the environment and install from **requirements.pip** file with the following commands:

```bash
$ source YOUR_ENVIRONMENT_DIRECTORY/bin/activate
$ pip install -r requirements.pip
```

Run the project:

```bash
$ pipenv run python -m flask run
Loading .env environment variables…
 * Serving Flask app "todo"
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

API Endpoints:
- `/tasks` **POST** and **GET**

## Testing (Optional)

You can test the application using the development dependencies.

Install all development dependencies from **Pipfile**:
```bash
$ pipenv install --dev
```

Or from **dev-requirements.pip** file if you are using **VirtualEnv**:
```bash
$ pip install -r dev-requirements.pip
```

To debug endpoints, you can use [HTTPie](https://httpie.org/) as following:
```bash
$ http http://127.0.0.1:5000/tasks
[
  {
    "_id": {
      "$oid": "5ad3d924e3bdea6ccf9d9d3e"
    },
    "description": "The Best Description",
    "done": false,
    "title": "The Best Title"
  },
  {
    "_id": {
      "$oid": "5ad3d8fae3bdea6c41d571f4"
    },
    "description": "The Incredible Description",
    "done": false,
    "title": "The Incredible Title"
  }
]
```

```bash
$ http POST http://127.0.0.1:5000/tasks title=Test description=Title
HTTP/1.0 201 CREATED
Content-Length: 123
Content-Type: application/json
Date: Mon, 16 Apr 2018 00:23:45 GMT
Server: Werkzeug/0.14.1 Python/3.6.2

{
  "_id": {
    "$oid": "5ad3ed11e3bdea06aa7afa06"
  },
  "description": "Title",
  "done": false,
  "title": "Test"
}
```

To run the tests, you can use [PyTest](https://docs.pytest.org/en/latest/) as following:
```bash
$ python -m pytest
...
collected 7 items

test_todo.py .......                                                    [100%]
========================== 7 passed in 1.32 seconds ==========================
```
