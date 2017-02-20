import pytest

from conftest import run


def test_run_cmd_on_frontend(exp_a8):
    run("open-a8-cli run-cmd --frontend 'uname -a'")
    # note: no need to wait for boot


def test_run_cmd(exp_a8):
    run("open-a8-cli wait-for-boot")
    run("open-a8-cli run-cmd 'uname -a'")
