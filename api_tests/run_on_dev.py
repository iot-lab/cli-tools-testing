#!/usr/bin/env python

import iotlabcli

iotlabcli.rest.Api.url = "https://devwww.iot-lab.info/rest/"


def test_get_sites(api):
    sites = api.get_sites()
    sites = sites["items"]
    assert {"site": "devgrenoble"} in sites


def api():
    username, password = iotlabcli.auth.get_user_credentials()
    return iotlabcli.Api(username, password)


def test_exp_resources_from_str_on_dev():
    from iotlabcli.parser.experiment import exp_resources_from_str
    exp_resources_from_str("2,archi=a8:at86rf231+site=devgrenoble")


def test_exp_resources_from_str_on_prod_fails():
    try:
        exp_resources_from_str("2,archi=a8:at86rf231+site=grenoble")
        assert False  # will raise if running on the dev platform
    except:
        pass


def main():
    test_exp_resources_from_str_on_dev()
    test_get_sites(api())


if __name__ == "__main__":
    main()
