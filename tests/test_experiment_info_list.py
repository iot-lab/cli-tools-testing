import pytest

from conftest import run

SITES = ["saclay", "grenoble"]


@pytest.mark.parametrize(("site"), SITES)
def test_experiment_info_list(site):
    res = run("experiment-cli info -l --site " + site)

    assert len(res["items"]) > 0
    assert res["items"][0]["site"] == site


@pytest.mark.parametrize(("site"), SITES)
def test_experiment_info_list_a8(site):
    res = run("experiment-cli info -li --site " + site)

    alive_a8 = res["items"][0][site]["a8"]["Alive"]
    assert len(alive_a8.split('+')) > 4
