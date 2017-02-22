import pytest

from conftest import run


def test_start_experiment(exp):
    args = "-d 1 -l 2,archi=m3:at86rf231+site=grenoble"
    ret = run("experiment-cli submit " + args)
    exp.id = str(ret["id"])


def test_wait_for_running(exp):
    run("experiment-cli wait -i " + exp.id, raw=True)

    ret = run("experiment-cli get -s -i " + exp.id)
    assert ret["state"] == "Running"


def test_stop_experiment(exp):
    ret = run("experiment-cli stop -i " + exp.id)
    assert ret["id"] == exp.id
    assert ret["status"] == "Delete request registered"


def test_wait_for_stopped(exp):
    # stopped experiments eventually report as "Error"
    run("experiment-cli wait --state Error -i " + exp.id, raw=True)


def test_start_and_wait(exp):
    test_start_experiment(exp)
    test_wait_for_running(exp)


def test_let_die(exp):
    run("experiment-cli wait --state Terminated -i " + exp.id, raw=True)



@pytest.fixture(scope="module")
def exp():
    """ a popo for storing experiment id across tests """
    class _exp: id = None
    return _exp()
