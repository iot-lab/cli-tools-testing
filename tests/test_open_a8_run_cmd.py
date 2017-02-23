import pytest

from conftest import run, open_a8, a8_nodes_list


def test_start_experiment(exp):
    args = ["-d 3",
            "-l 2,archi=a8:at86rf231+site=grenoble",
            "-l 2,archi=a8:at86rf231+site=saclay",
    ]
    ret = run("experiment-cli submit " + " ".join(args))
    exp.id = str(ret["id"])
    run("experiment-cli wait -i " + exp.id)


def test_run_cmd_on_frontend(exp):
    open_a8(exp, "run-cmd --frontend 'uname -a'")
    # note: no need to wait for boot


@pytest.mark.skip(reason="fails in run-cmd if some nodes are not booted")
def test_run_cmd_naive(exp):
    open_a8(exp, "wait-for-boot")
    open_a8(exp, "run-cmd 'uname -a'")


def test_run_cmd(exp):
    ret = open_a8(exp, "wait-for-boot --max-wait 70")
    booted_nodes = ret["wait-for-boot"]["0"]
    open_a8(exp, "run-cmd 'uname -a' " + a8_nodes_list(booted_nodes))
