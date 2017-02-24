import pytest

from conftest import run, ssh, a8_nodes_list
import time


site = "saclay"


def test_start_experiment(exp):
    args = "-d 4 -l 2,archi=a8:at86rf231+site=" + site
    ret = run("experiment-cli submit " + args)
    exp.id = str(ret["id"])
    run("experiment-cli wait -i " + exp.id)


def test_run_script(exp):
    ret = run("open-a8-cli -i " + exp.id + " wait-for-boot")
    booted_nodes = ret["wait-for-boot"]["0"]
    do_run_script(exp, booted_nodes)


def do_run_script(exp, nodes):
    script = "tests/sample_script.sh"
    frontend = site + ".iot-lab.info"
    script_out = "A8/script_out.txt"
    ssh(frontend, "rm -f " + script_out)

    run("open-a8-cli -i " + exp.id + " run-script " + script + a8_nodes_list(nodes))

    # script runs _async_ on A8 nodes. sample_script sleeps 3-4s. wait
    time.sleep(10)
    ret = ssh(frontend, "cat " + script_out)
    assert ret == "{}\n".format(time.strftime("%F")) * len(nodes)


@pytest.mark.skip(reason="fails if some nodes are not booted")
def test_run_script_naive(exp):
    run("open-a8-cli -i " + exp.id + " wait-for-boot")
    do_run_script(exp, None)
