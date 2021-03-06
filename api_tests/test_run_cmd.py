import pytest

from iotlabsshcli.sshlib import OpenA8Ssh
from iotlabsshcli.open_a8 import _nodes_grouped
from tests.test_open_a8_run_cmd import test_start_experiment as start_experiment

#pytestmark = pytest.mark.usefixtures("run_on_dev")


def test_start_experiment(exp):
    start_experiment(exp)


def test_run_cmd_on_frontends(ssh_api):
    ret = ssh_api.run("uname -a", with_proxy=False)

    assert ret["0"] is not []
    # command result is not (yet) available in return
    #assert "Debian" in ret[...]


def test_run_cmd(ssh_api):
    ret = ssh_api.wait(max_wait=70)
    booted = ret["0"]
    ssh_api.groups = _nodes_grouped(booted)
    
    ssh_api.run("uname -a")
    #assert "armv7l" in ret["0"][0]["result"]


@pytest.fixture
def ssh_api(exp, api):
    user = api.auth.username
    info = api.get_experiment_info(exp.id)
    deployed_nodes = info["deploymentresults"]["0"]
    deployed_a8 = ["node-" + n for n in deployed_nodes if "a8" in n]
    ssh_api = OpenA8Ssh({"user": user}, _nodes_grouped(deployed_a8))
    return ssh_api
