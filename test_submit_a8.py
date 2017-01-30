#!/usr/bin/env python
# -*- coding:utf-8
import iotlabcli
from iotlabcli import experiment
from iotlabcli.parser.experiment import exp_resources_from_str
import os

def test_submit_experiment_a8():
    """ Start experiment"""
    user = os.environ['IOTLAB_USER']
    passwd = os.environ['IOTLAB_PASS']
    resources = exp_resources_from_str("grenoble,a8,1-2")
    name = "test_exp_A8"
    duration = 2
    api = iotlabcli.Api(user, passwd)
    exp = experiment.submit_experiment(api, name, duration, [resources])
    exp_id = exp['id']
    experiment.wait_experiment(api, exp_id)
    state = experiment.get_experiment(api, exp_id, 'state')
    assert state['state'] == "Running"
