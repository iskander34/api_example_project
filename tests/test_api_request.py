import allure

from lib.api_routes import APIRoutes
from http import HTTPStatus

from lib.http_client_request import HTTPClient


@allure.epic("API Tests")
@allure.feature("Request from library Request")
@allure.story("Mashine story")
@allure.severity(allure.severity_level.CRITICAL)
class TestAPIRequest:
    """GET запрос"""

    @allure.title("Request from API with GET method")
    @allure.description("Проверка ответа при обращении к API")
    def test_local(self, app):
        self._action(app)

    @staticmethod
    def _action(app):
        with allure.step("Формируем ссылку для обращения"):
            url = app.config["web"]["base_url"] + APIRoutes.LIST_USERS_GET
        with allure.step("Читаем в переменную ответ от сервера"):
            resp = HTTPClient.get(url=url, headers={"Connection": "close", "User-Agent": "Test"})

        with allure.step("Проверяем status code"):
            assert resp.status_code == HTTPStatus.OK, f"Expected status code - {HTTPStatus.OK}," \
                                                      f" but status in response - {resp.status_code}"
