import os
from datetime import datetime
import pytest
import Utils
from Utils import  utils
from Utils.constants import common
from Utils.csv_utils import CSV

"""
    For addoption actions, see: https://docs.python.org/3/library/argparse.html
    For fixture scopes, see: https://docs.pytest.org/en/latest/reference/reference.html?highlight=fixture#pytest.fixture
    parser.addoption('--flagname', default='default_value', action='store_variable', help='help_text')
"""


def pytest_addoption(parser):
    parser.addoption('--env', action='store', help='--env dev/qa/stage', default='stage')
    parser.addoption('--no-cleanup', action='store_true', default=False)
    parser.addoption('--csv', action='store_true', default=False)
    parser.addoption('--jenkins', action='store_true', default=False)



def pytest_sessionfinish():
    """
        Pytest automatically calls this function once test run completes.
        If common.jenkins_flag is True, it will exit w/ a '0' code no matter what.
            (This is so the Jenkins job doesn't fail if there are test failures)
    """
    if common.jenkins_flag:
        pytest.exit('0', returncode=0)



@pytest.fixture(scope='session')
def params(request):
    env = request.config.getoption('--env').lower()
    csv_debug = request.config.getoption('--csv')
    ff_browser = request.config.getoption('--ff')
    common.jenkins_flag = request.config.getoption('--jenkins')
    #browser = request.config.getoption('--browser').lower()

    if request.config.getoption('--no-cleanup'):
        cleanup = False
    else:
        cleanup = True

    if env == 'stg' or env == 'test':
        env = 'stage'

    yield {
        'env': env,
        'cleanup': cleanup,
        'debug': csv_debug,
        'ff_browser': ff_browser
    }


@pytest.fixture(scope='session')
def apic(params):
    from Clients import api_client
    api_client = api_client.apic(params['env'])
    yield api_client


@pytest.fixture(scope='session')
def webc(params):
    from Clients import web_client
    web_client = web_client.wc(params['env'],params['ff_browser'])
    yield web_client










