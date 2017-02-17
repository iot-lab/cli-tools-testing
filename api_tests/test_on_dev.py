import pytest

from iotlabcli.parser.experiment import exp_resources_from_str

pytestmark = pytest.mark.usefixtures("run_on_dev")


def test_exp_resources_from_str_on_dev():
    exp_resources_from_str("2,archi=a8:at86rf231+site=devgrenoble")


def test_exp_resources_from_str_on_prod_fails():
    with pytest.raises(Exception):
        exp_resources_from_str("2,archi=a8:at86rf231+site=grenoble")


def test_get_sites(api):
    sites = api.get_sites()
    sites = sites["items"]
    assert {"site": "devgrenoble"} in sites
