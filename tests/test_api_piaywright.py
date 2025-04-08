import allure

from lib.api_routes import APIRoutes
from http import HTTPStatus

from playwright.sync_api import sync_playwright


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
        with sync_playwright() as playwright:
            with allure.step("Формируем ссылку для обращения"):
                url = app.config["web"]["base_url"] + APIRoutes.LIST_USERS_GET
                with allure.step(f"{url}"):
                    pass
            request = playwright.request.new_context(base_url=url)
            with allure.step("Читаем в переменную ответ от сервера"):
                resp = request.get(url=url, headers={"Connection": "close", "User-Agent": "Test"})
                with allure.step(f"{resp}"):
                    pass
            with allure.step("Проверяем status code"):
                with allure.step(f"{resp.status}"):
                    pass
                assert resp.status == HTTPStatus.OK, f"Expected status code - {HTTPStatus.OK}," \
                                                     f" but status in response - {resp.status_code}"
