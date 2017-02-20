import pytest

from conftest import run, ssh
import time


site = "saclay"


def test_experiment_info_list():
    res = run("experiment-cli info -l --site " + site)

    assert len(res["items"]) > 0
    assert res["items"][0]["site"] == site


def test_experiment_info_list_a8():
    res = run("experiment-cli info -li --site " + site)

    alive_a8 = res["items"][0][site]["a8"]["Alive"]
    assert len(alive_a8.split('+')) > 4


def test_experiment_submit_a8_logical():
    args = "-d 4 -l 2,archi=a8:at86rf231+site=" + site
    run("experiment-cli submit " + args)
    run("experiment-cli wait")


def test_opena8_wait_for_boot():
    ret = run("open-a8-cli wait-for-boot")
    assert len(ret["wait-for-boot"]["0"]) == 2


def test_opena8_reset_m3():
    # uses previous experiment
    run("open-a8-cli reset-m3")


def test_opena8_run_script():
    # uses previous experiment
    nodes = run("experiment-cli get --resources")
    nb_nodes = len(nodes["items"])

    script = "tests/sample_script.sh"
    frontend = site + ".iot-lab.info"
    script_out = "A8/script_out.txt"
    ssh(frontend, "rm -f " + script_out)

    run("open-a8-cli run-script " + script)

    # script runs _async_ on A8 nodes. sample_script sleeps 3-4s. wait
    time.sleep(8)
    ret = ssh(frontend, "cat " + script_out)
    assert ret == "{}\n".format(time.strftime("%F")) * nb_nodes
