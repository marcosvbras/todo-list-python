# coding=utf-8
from todo import app, tasks

def test_list_tasks_must_return_status_200():
    with app.test_client() as client:
        response = client.get('/tasks')
        assert response.status_code == 200


def test_list_tasks_must_have_json_format():
    with app.test_client() as client:
        response = client.get('/tasks')
        assert response.content_type == 'application/json'


def test_empty_todo_list_must_return_empty_list():
    with app.test_client() as client:
        response = client.get('/tasks')
        assert response.data == b'[]\n'


def test_non_empty_todo_list_must_return_content():
    tasks.append({'id': 1, 'titulo': 'tarefa 1',
                    'descricao': 'tarefa de numero 1', 'estado': False})
    with app.test_client() as client:
        response = client.get('/tasks')
        assert response.data == (b'[\n  {\n    "descricao": '
                                 b'"tarefa de numero 1", \n    '
                                 b'"estado": false, \n    '
                                 b'"id": 1, \n    '
                                 b'"titulo": "tarefa 1"\n  }\n]\n')
