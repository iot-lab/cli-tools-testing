import pytest

import iotlabcli
import os

@pytest.fixture
def api(auth):
    username, password = auth
    return iotlabcli.Api(username, password)

@pytest.fixture
def auth():
    try:
      return (os.environ['IOTLAB_USER'], os.environ['IOTLAB_PASS'])
    except:
      return iotlabcli.auth.get_user_credentials()

@pytest.fixture
def run_on_dev():
    iotlabcli.rest.Api.url = "https://devwww.iot-lab.info/rest/"
    iotlabcli.rest.Api._cache = {}
    yield True
    iotlabcli.rest.Api.url = "https://www.iot-lab.info/rest/"
    iotlabcli.rest.Api._cache = {}
