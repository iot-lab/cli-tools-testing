import pytest

from conftest import run, open_a8


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


def test_run_cmd(exp):
    open_a8(exp, "wait-for-boot")
    open_a8(exp, "run-cmd 'uname -a'")
