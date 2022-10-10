import requests

"""Список http запросов"""


class Http_metods():

    headers = {'Content-Type': 'application/json'}
    cookie = ''

    @staticmethod
    def get(url):

        result = requests.get(url, headers=Http_metods.headers, cookies=Http_metods.cookie)
        return result

    @staticmethod
    def post(url, body):

        result = requests.post(url, json=body, headers=Http_metods.headers, cookies=Http_metods.cookie)
        return result

    @staticmethod
    def put(url, body):

        result = requests.put(url, json=body, headers=Http_metods.headers, cookies=Http_metods.cookie)
        return result

    @staticmethod
    def delete(url, body):

        result = requests.delete(url, json=body, headers=Http_metods.headers, cookies=Http_metods.cookie)
        return result
