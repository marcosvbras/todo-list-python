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


def test_create_task_accepts_method_post():
    with app.test_client() as client:
        response = client.post('/tasks')
        assert response.status_code != 405


def test_create_task_returns_created_task():
    with app.test_client() as client:
        import json
        response = client.post(
            '/tasks',
            data=json.dumps(
                {
                    'title': 'The Best Title',
                    'description': 'The Best Description'
                }
            ),
            content_type='application/json'
        )

        data = json.loads(response.data.decode('utf-8'))
        assert data['id'] == 1
        assert data['title'] == 'The Best Title'
        assert data['description'] == 'The Best Description'
        assert data['done'] == False


def test_create_task_must_returns_201_status_code():
    with app.test_client() as client:
        import json
        response = client.post(
            '/tasks',
            data=json.dumps(
                {
                    'title': 'The Best Title',
                    'description': 'The Best Description'
                }
            ),
            content_type='application/json'
        )

        assert response.status_code == 201


def test_create_task_without_description_must_returns_400():
    with app.test_client() as client:
        import json
        response = client.post(
            '/tasks',
            data=json.dumps(
                {
                    'title': 'The Best Title',
                    'description': None
                }
            ),
            content_type='application/json'
        )
        assert response.status_code == 400


def test_create_task_without_title_must_returns_400():
    with app.test_client() as client:
        import json
        response = client.post(
            '/tasks',
            data=json.dumps(
                {
                    'title': None,
                    'description': 'The Best Description'
                }
            ),
            content_type='application/json'
        )
        assert response.status_code == 400
