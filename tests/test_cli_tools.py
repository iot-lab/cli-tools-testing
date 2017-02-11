# import pytest

import subprocess
import json


def test_experiment_info_list():
    res = run("experiment-cli info -l --site grenoble")

    assert len(res["items"]) > 0
    assert res["items"][0]["site"] == "grenoble"


def test_experiment_info_list_a8():
    res = run("experiment-cli info -li --site grenoble")

    alive_a8 = res["items"][0]["grenoble"]["a8"]["Alive"]
    assert len(alive_a8.split('+')) > 4


def test_opena8_wait_for_boot():
    args = "-d 4 -l 2,archi=a8:at86rf231+site=grenoble"
    run("experiment-cli submit " + args)
    run("experiment-cli wait")
    run("open-a8-cli wait-for-boot")


def test_opena8_reset_m3():
    # uses previous experiment
    run("open-a8-cli reset-m3")


def run(cmd, raw=False):
    cmd = cmd.split()
    ret = subprocess.check_output(cmd)
    return ret if raw else json.loads(ret)
