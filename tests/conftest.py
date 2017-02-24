import pytest

import subprocess
import shlex
import json


def ssh(host, cmd):
    opt = "-o StrictHostKeyChecking=no"
    return run("ssh " + host + " " + opt + " " + cmd, raw=True)


def run(cmd, raw=False):
    cmd = shlex.split(cmd)
    try:
        ret = subprocess.check_output(cmd)
    except Exception as e:
        pytest.fail(e)
    return ret if raw else json.loads(ret)


def open_a8(exp, cmd):
    return run("open-a8-cli -i " + exp.id + " " + cmd)


# utility

def a8_nodes_list(nodes):
    def node_id(node): return node.split(".")[0].split("-")[-1]
    def str_list(nodes): return "+".join([node_id(n) for n in nodes])
    from iotlabsshcli.open_a8 import _nodes_grouped

    groups = _nodes_grouped(nodes or [])
    specs = [ site + ",a8," + str_list(groups[site]) for site in groups ]

    return " -l ".join([""] + specs)
