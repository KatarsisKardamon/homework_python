import requests


base_url = 'https://ru.yougile.com/api-v2/'
TOKEN = "tqAALTbnXwIBRDFszTEPxDVkmEcImVwG2Cbr1x-cIhia+KP-6ZBvIKNPdLXKOLBZ"
HEADERS = {"Authorization": f"Bearer {TOKEN}"}


def test_create_project_positiv():
    body = {
        "title": "Мой проект для ДЗ",
        "users": {
            "82c600e6-9100-4ace-af3f-260a9a20363c": "admin"
        }
    }

    resp = requests.post(base_url + 'projects', json=body, headers=HEADERS)
    assert resp.status_code == 201


def test_create_project_negativ():
    body = {
        "title": "Мой проект для ДЗ",
        "users": {
            "82c600e6-9100-4ace-af3f-260a9a20363c": "admin"
        }
    }

    resp = requests.post(base_url + 'projects', json=body)
    assert resp.status_code == 401


def test_change_project_positiv():
    body = {
        "title": "Мой проект для ДЗ",
        "users": {
            "82c600e6-9100-4ace-af3f-260a9a20363c": "admin"
        }
    }
    body2 = {
        "title": "Мой измененный проект для ДЗ"
        }

    resp = requests.post(base_url + 'projects', json=body, headers=HEADERS)
    assert resp.status_code == 201
    id = resp.json()['id']
    resp2 = requests.put(base_url + f'projects/{id}',
                         json=body2, headers=HEADERS)
    assert resp2.status_code == 200


def test_change_project_negativ():
    body2 = {
        "title": "Мой измененный проект для ДЗ"
        }
    id = 123
    resp2 = requests.put(base_url + f'projects/{id}',
                         json=body2, headers=HEADERS)
    assert resp2.status_code == 404


def test_id_project_positiv():
    body = {
        "title": "Мой проект для ДЗ",
        "users": {
            "82c600e6-9100-4ace-af3f-260a9a20363c": "admin"
        }
    }

    resp = requests.post(base_url + 'projects', json=body, headers=HEADERS)
    assert resp.status_code == 201
    id = resp.json()['id']
    resp2 = requests.get(base_url + f'projects/{id}', headers=HEADERS)
    assert resp2.status_code == 200


def test_id_project_negativ():
    id = 123
    resp2 = requests.get(base_url + f'projects/{id}', headers=HEADERS)
    assert resp2.status_code == 404
