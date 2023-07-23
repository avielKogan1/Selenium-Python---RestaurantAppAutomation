import pytest
import json


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