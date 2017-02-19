import pytest

from iotlabcli import experiment
from iotlabcli.parser.experiment import exp_resources_from_str


def submit_experiment_a8(api, duration, nb_nodes,
                         site="grenoble",
                         name="test_exp_A8"):
    resources = exp_resources_from_str(
                 "{},archi=a8:at86rf231+site={}".format(nb_nodes, site))
    exp = experiment.submit_experiment(api, name, duration, [resources])
    exp_id = exp['id']
    return exp_id


def wait_for_running(api, exp_id):
    experiment.wait_experiment(api, exp_id)
    state = experiment.get_experiment(api, exp_id, 'state')
    assert state['state'] == "Running"


def test_get_experiment_info(api):
    exp_id = submit_experiment_a8(api, duration=2, nb_nodes=3)
    info = api.get_experiment_info(exp_id)
    assert info["name"] == "test_exp_A8"
    assert info["type"] == "alias"  # aka "logical"

    # checking deployment results requires state "Running"
    wait_for_running(api, exp_id)

    info = api.get_experiment_info(exp_id)
    assert info["state"] == "Running"
    reserved_nodes = info["nodes"]
    deployed_nodes = info["deploymentresults"]["0"]
    assert len(reserved_nodes) == len(deployed_nodes)
