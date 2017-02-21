import pytest

import iotlabcli
import os

@pytest.fixture(scope="module")
def api(auth):
    username, password = auth
    return iotlabcli.Api(username, password)

@pytest.fixture(scope="module")
def auth():
    try:
      return (os.environ['IOTLAB_USER'], os.environ['IOTLAB_PASS'])
    except:
      return iotlabcli.auth.get_user_credentials()

@pytest.fixture(scope="module")
def run_on_dev():
    iotlabcli.rest.Api.url = "https://devwww.iot-lab.info/rest/"
    iotlabcli.rest.Api._cache = {}
    yield True
    iotlabcli.rest.Api.url = "https://www.iot-lab.info/rest/"
    iotlabcli.rest.Api._cache = {}


from iotlabcli import experiment
from iotlabcli.parser.experiment import exp_resources_from_str

@pytest.fixture(scope="module")
def exp_a8(api):
    duration = 2
    nb_nodes = 2
    site = "grenoble"
    name = "test_exp_A8"

    if "dev" in api.url:
        site = "dev" + site
    resources = exp_resources_from_str(
        "{},archi=a8:at86rf231+site={}".format(nb_nodes, site))
    exp = experiment.submit_experiment(api, name, duration, [resources])
    exp_id = exp['id']
    experiment.wait_experiment(api, exp_id)

    yield exp_id

    api.stop_experiment(exp_id)
