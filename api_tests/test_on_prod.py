import pytest


def test_on_prod(api):
    assert api.url == "https://www.iot-lab.info/rest/"


def test_exp_resources_from_str_on_dev():
    from iotlabcli.parser.experiment import exp_resources_from_str
    exp_resources_from_str("2,archi=a8:at86rf231+site=grenoble")


def test_get_sites(api):
    sites = api.get_sites()
    sites = sites["items"]
    assert {"site": "grenoble"} in sites
