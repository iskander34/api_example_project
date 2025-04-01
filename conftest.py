import pytest

from settings.application_json import Application


@pytest.fixture
def app(pytestconfig):
    return Application(config_file="config.json")
