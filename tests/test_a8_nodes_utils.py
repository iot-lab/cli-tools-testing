import pytest

from conftest import a8_nodes_list


def test_a8_nodes_list_expected_usage():
    nodes = [ "node-a8-2.grenoble.iot-lab.info", "node-a8-10.saclay.iot-lab.info" ]
    ret = a8_nodes_list(nodes)
    assert ret == ' -l grenoble,a8,2 -l saclay,a8,10'


def test_a8_nodes_list_does_not_filter_out_m3():
    nodes = [ "m3-2.grenoble.iot-lab.info", "node-a8-10.saclay.iot-lab.info" ]
    ret = a8_nodes_list(nodes)
    assert ret == ' -l grenoble,a8,2 -l saclay,a8,10'


def test_a8_nodes_list_dont_care_about_full_fqdn():
    nodes = [ "node-a8-10.saclay", "node-a8-3.saclay", "node-a8-4.grenoble" ]
    ret = a8_nodes_list(nodes)
    assert ret == ' -l saclay,a8,10+3 -l grenoble,a8,4'


def test_a8_nodes_list_dont_care_about_node_a8_name():
    nodes = [ "a8-10.saclay", "a8-3.saclay", "a8-4.grenoble" ]
    ret = a8_nodes_list(nodes)
    assert ret == ' -l saclay,a8,10+3 -l grenoble,a8,4'


def test_a8_nodes_list_eat_none():
    nodes = None
    ret = a8_nodes_list(nodes)
    assert ret == ""
