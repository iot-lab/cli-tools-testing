import pytest

import subprocess
import json
import time


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


def test_opena8_run_script():
    # uses previous experiment
    nodes = run("experiment-cli get --resources")
    nb_nodes = len(nodes["items"])

    script = "tests/sample_script.sh"
    frontend = "grenoble.iot-lab.info"
    script_out = "A8/script_out.txt"
    ssh(frontend, "rm -f " + script_out)

    run("open-a8-cli run-script " + script)

    # script runs _async_ on A8 nodes. sample_script sleeps 3-4s. wait
    time.sleep(5)
    ret = ssh(frontend, "cat " + script_out)
    assert ret == "{}\n".format(time.strftime("%F")) * nb_nodes


def ssh(host, cmd):
    opt = "-o StrictHostKeyChecking=no"
    return run("ssh " + host + " " + opt + " " + cmd, raw=True)


def run(cmd, raw=False):
    cmd = cmd.split()
    try:
        ret = subprocess.check_output(cmd)
    except Exception as e:
        pytest.fail(e)
    return ret if raw else json.loads(ret)
