import requests

from Framework.configurations.config_file import BASE_URL


class BaseAPI:
    def __init__(self):
        self.__base_url = BASE_URL
        self.header = {'Content-Type': 'application/json'}
        self.__request = requests
        self.__body = {}

    def get(self, url, headers=None):
        if headers is None:
            headers = self.header
        response = self.__request.get(f'{self.__base_url}{url}', headers=headers)
        return response

    def post(self, url, headers=None, body=None):
        if headers is not None:
            headers = self.header
        if body is not None:
            body = self.__body
        response = self.__request.post(f'{self.__base_url}{url}', headers=headers, data=body)
        return response

    def delete(self, url):
        response = self.__request.delete(f'{self.__base_url}{url}')
        return response

    def put(self, url, body=None):
        if body is None:
            body = self.__body.update()
        response = self.__request.put(f'{self.__base_url}{url}', data=body)
        return response
