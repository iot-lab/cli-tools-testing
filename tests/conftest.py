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


@pytest.fixture(scope="module")
def exp_a8():
    args = "-d 4 -l 2,archi=a8:at86rf231+site=grenoble"
    ret = run("experiment-cli submit " + args)
    exp_id = ret["id"]
    run("experiment-cli wait -i {}".format(exp_id))
    yield "-i {}".format(exp_id)

    run("experiment-cli stop -i {}".format(exp_id))


@pytest.fixture(scope="module")
def exp():
    """ a popo for storing experiment id across tests """
    class _exp: id = None
    return _exp()
