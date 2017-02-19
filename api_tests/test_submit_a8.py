import pytest

from iotlabcli import experiment
from iotlabcli.parser.experiment import exp_resources_from_str

# see conftest.py for api def.


def test_submit_experiment_a8_physical(api):
    resources = exp_resources_from_str("grenoble,a8,1-2")
    name = "test_exp_A8"
    duration = 2
    exp = experiment.submit_experiment(api, name, duration, [resources])
    exp_id = exp['id']
    experiment.wait_experiment(api, exp_id)
    state = experiment.get_experiment(api, exp_id, 'state')
    assert state['state'] == "Running"


def test_submit_experiment_a8_logical(api):
    name = "test_exp_A8"
    duration = 2
    resources = exp_resources_from_str("2,archi=a8:at86rf231+site=grenoble")
    exp = experiment.submit_experiment(api, name, duration, [resources])
    exp_id = exp['id']
    experiment.wait_experiment(api, exp_id)
    state = experiment.get_experiment(api, exp_id, 'state')
    assert state['state'] == "Running"


def test_stop_experiment(api):
    # use previous experiment
    exp_ids = api.get_experiments()  # running experiments
    exp_id = exp_ids["items"][0]["id"]
    api.stop_experiment(exp_id)
