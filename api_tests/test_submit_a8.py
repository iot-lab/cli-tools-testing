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


def test_submit_experiment_a8_logical(api, exp):
    name = "test_exp_A8"
    duration = 2
    resources = exp_resources_from_str("2,archi=a8:at86rf231+site=grenoble")
    ret = experiment.submit_experiment(api, name, duration, [resources])
    exp.id = ret['id']
    exp_id = exp.id
    experiment.wait_experiment(api, exp_id)
    state = experiment.get_experiment(api, exp_id, 'state')
    assert state['state'] == "Running"


def test_get_experiments(api, exp):
    exps_info = api.get_experiments(state='Running')
    exps_ids = [ info["id"] for info in exps_info["items"] ]
    assert exp.id in exps_ids


def test_stop_experiment(api, exp):
    api.stop_experiment(exp.id)

    # stopped experiments eventually report as Error
    experiment.wait_experiment(api, exp.id, states="Error")
