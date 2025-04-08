import allure
import requests
import urllib3

from lib.logger import Logger


class HTTPClient:

    @allure.step("Making DELETE request to URL '{url}'")
    def delete(url: str, auth: str = None, data: dict = None, headers: dict = None, cookies: dict = None):
        return HTTPClient._send(url, data, headers, cookies, auth, "DELETE")

    @allure.step("Making GET request to URL '{url}'")
    def get(url: str, auth: str = None, data: dict = None, headers: dict = None, cookies: dict = None):
        return HTTPClient._send(url, data, headers, cookies, auth, "GET")

    @allure.step("Making POST request to URL '{url}'")
    def post(url: str, auth: str = None, data: dict = None, files: dict = None, headers: dict = None,
             cookies: dict = None):
        return HTTPClient._send(url, data, headers, cookies, auth, "POST", files)

    @allure.step("Making PUT request to URL '{url}'")
    def put(url: str, auth: str = None, data: dict = None, headers: dict = None, cookies: dict = None):
        return HTTPClient._send(url, data, headers, cookies, auth, "PUT")

    @staticmethod
    def _send(url: str, data: dict, headers: dict, cookies: dict, auth: str, method: str, files: dict = None):

        urllib3.disable_warnings()

        if headers is None:
            headers = {}
        if cookies is None:
            cookies = {}

        Logger.add_request(url, data, headers, cookies, method)

        if method == 'DELETE':
            response = requests.delete(url, data=data, headers=headers, cookies=cookies, auth=auth, verify=False)
        elif method == 'GET':
            response = requests.get(url, params=data, headers=headers, cookies=cookies, auth=auth, verify=False)
        elif method == 'POST':
            response = requests.post(url, data=data, headers=headers, cookies=cookies, auth=auth, verify=False)
        elif method == 'PUT':
            response = requests.put(url, data=data, headers=headers, cookies=cookies, auth=auth, verify=False)

        else:
            raise Exception(f"Bad HTTP method '{method}' was received")

        Logger.add_response(response)

        return response
