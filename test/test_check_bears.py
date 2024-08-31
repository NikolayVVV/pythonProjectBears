import json
from requests import Response

from utills.http_methods import Http_methods

base_url = "http://localhost:8080/"


class Test_check_bears():

    def test_get_info(self):
        url = base_url + "/info"
        response = Http_methods.get(url)
        assert response.content == b'Welcome to Alaska!\nThis is CRUD service for bears in alaska.\nCRUD routes presented with REST naming notation:\n\nPOST\t\t\t/bear - create\nGET\t\t\t/bear - read all bears\nGET\t\t\t/bear/:id - read specific bear\nPUT\t\t\t/bear/:id - update specific bear\nDELETE\t\t\t/bear - delete all bears\nDELETE\t\t\t/bear/:id - delete specific bear\n\nExample of ber json: {"bear_type":"BLACK","bear_name":"mikhail","bear_age":17.5}.\nAvailable types for bears are: POLAR, BROWN, BLACK and GUMMY.'

    def test_create_bear_polar(self):
        url = base_url + "/bear"
        data = {
            "bear_type": "POLAR",
            "bear_name": "Dima",
            "bear_age": 2
        }

        response = Http_methods.post(url, data)
        assert response.json() == 1
        assert response.status_code == 200

    def test_create_bear_brown(self):
        url = base_url + "/bear"
        data = {
            "bear_type": "BROWN",
            "bear_name": "Vasya",
            "bear_age": 10.5
        }

        response = Http_methods.post(url, data)
        assert response.json() == 2
        assert response.status_code == 200

    def test_create_bear_black(self):
        url = base_url + "/bear"
        data = {
            "bear_type": "BLACK",
            "bear_name": "mikhail",
            "bear_age": 17.5
        }

        response = Http_methods.post(url, data)
        assert response.json() == 3
        assert response.status_code == 200

    def test_create_bear_gummy(self):
        url = base_url + "/bear"
        data = {
            "bear_type": "GUMMY",
            "bear_name": "anton",
            "bear_age": 5.1
        }

        response = Http_methods.post(url, data)
        assert response.json() == 4
        assert response.status_code == 200

    def test_get_all_bears(self):
        url = base_url + "/bear"

        response = Http_methods.get(url)
        assert response.json() == [{'bear_id': 1, 'bear_type': 'POLAR', 'bear_name': 'DIMA', 'bear_age': 2.0},
                                   {'bear_id': 2, 'bear_type': 'BROWN', 'bear_name': 'VASYA', 'bear_age': 10.5},
                                   {'bear_id': 3, 'bear_type': 'BLACK', 'bear_name': 'MIKHAIL', 'bear_age': 17.5},
                                   {'bear_id': 4, 'bear_type': 'UNKNOWN', 'bear_name': 'EMPTY_NAME', 'bear_age': 0.0}]
        assert response.status_code == 200

    def test_get_polar_bear(self):
        url = base_url + "/bear/1"
        response = Http_methods.get(url)
        assert response.json() == {'bear_id': 1, 'bear_type': 'POLAR', 'bear_name': 'DIMA', 'bear_age': 2.0}
        assert response.status_code == 200

    def test_get_brown_bear(self):
        url = base_url + "/bear/2"

        response = Http_methods.get(url)
        assert response.json() == {'bear_id': 2, 'bear_type': 'BROWN', 'bear_name': 'VASYA', 'bear_age': 10.5}
        assert response.status_code == 200

    def test_get_black_bear(self):
        url = base_url + "/bear/3"

        response = Http_methods.get(url)
        assert response.json() == {'bear_id': 3, 'bear_type': 'BLACK', 'bear_name': 'MIKHAIL', 'bear_age': 17.5}
        assert response.status_code == 200

    def test_get_gummy_bear(self):
        url = base_url + "/bear/4"
        response = Http_methods.get(url)
        assert response.text == 'null'

    def test_change_polar_bear(self):
        url = base_url + "/bear/1"
        data = {
            "bear_type": "POLAR",
            "bear_name": "kolya",
            "bear_age": 17.5
        }
        response_change_bear = Http_methods.put(url, data)
        response_get_update_bear = Http_methods.get(url)
        assert response_change_bear.text == 'OK'
        assert response_change_bear.status_code == 200
        assert response_get_update_bear.json()['bear_name'] == 'kolya'
        assert response_get_update_bear.status_code == 200

    def test_delete_polar_bear(self):
        url = base_url + "/bear/1"
        response = Http_methods.delete_without_body(url)
        assert response.text == 'OK'
        assert response.status_code == 200

    def test_delete_all_bears(self):
        url = base_url + "/bear"
        response = Http_methods.delete_without_body(url)
        assert response.text == 'OK'
        assert response.status_code == 200
