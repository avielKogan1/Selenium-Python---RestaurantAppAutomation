import pytest
import json

from api_methods.dashboard_page_api import DashboardPageAPI
from pages.dashboard_page import DashboardPage


def pytest_addoption(parser):
    parser.addoption("--datafile", action="store", help="Path to the JSON data file")

@pytest.fixture(scope='session')
def datafile(request):
    filename = request.config.getoption("--datafile")
    if not filename:
        pytest.fail('Datafile not specified. Use --datafile to specify the path to the data file.')
    with open(filename, 'r') as f:
        data = json.load(f)
    return data

@pytest.fixture
def dashboard_page(driver):
    page = DashboardPage(driver)
    page.goto()
    yield page
    driver.quit()

@pytest.fixture
def dashboard_page_api():
    dashboard_page_api = DashboardPageAPI()
    yield dashboard_page_api
