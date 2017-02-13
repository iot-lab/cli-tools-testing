#!/usr/bin/env python
# -*- coding:utf-8
import iotlabcli
from iotlabcli import experiment
from iotlabcli.parser.experiment import exp_resources_from_str
import os

USERNAME = os.environ['IOTLAB_USER']
PASSWORD = os.environ['IOTLAB_PASS']


def get_api():
    return iotlabcli.Api(USERNAME, PASSWORD)


def test_submit_experiment_a8_physical():
    """ Start experiment"""
    resources = exp_resources_from_str("grenoble,a8,1-2")
    name = "test_exp_A8"
    duration = 2
    api = get_api()
    exp = experiment.submit_experiment(api, name, duration, [resources])
    exp_id = exp['id']
    experiment.wait_experiment(api, exp_id)
    state = experiment.get_experiment(api, exp_id, 'state')
    assert state['state'] == "Running"


def test_submit_experiment_a8_logical():
    name = "test_exp_A8"
    duration = 2
    resources = exp_resources_from_str("2,archi=a8:at86rf231+site=grenoble")
    api = get_api()
    exp = experiment.submit_experiment(api, name, duration, [resources])
    exp_id = exp['id']
    experiment.wait_experiment(api, exp_id)
    state = experiment.get_experiment(api, exp_id, 'state')
    assert state['state'] == "Running"


def test_stop_experiment():
    # use previous experiment
    api = get_api()
    exp_ids = api.get_experiments()  # running experiments
    exp_id = exp_ids["items"][0]["id"]
    api.stop_experiment(exp_id)
