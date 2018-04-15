# coding=utf-8
from todo import app

def test_list_tasks_must_return_status_200():
    with app.test_client() as client:
        response = client.get('/tasks')
        assert response.status_code == 200


def test_list_tasks_must_have_json_format():
    with app.test_client() as client:
        response = client.get('/tasks')
        assert response.content_type == 'application/json'


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
                    'title': 'The Incredible Title',
                    'description': 'The Incredible Description'
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
