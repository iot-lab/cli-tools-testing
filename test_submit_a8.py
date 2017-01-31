#!/usr/bin/env python
# -*- coding:utf-8
import iotlabcli
from iotlabcli import experiment
from iotlabcli.parser.experiment import exp_resources_from_str
import os

def get_api():
    user = os.environ['IOTLAB_USER']
    passwd = os.environ['IOTLAB_PASS']
    api = iotlabcli.Api(user, passwd)
    return api


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
