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


@pytest.fixture(scope="module")
def exp():
    """ a popo for storing experiment id across tests """
    class _exp: id = None
    return _exp()
