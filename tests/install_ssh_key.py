#!/usr/bin/env python

import os
import requests

URL = "https://www.iot-lab.info/rest/users/{login}/sshkeys"
USER = os.environ["IOTLAB_USER"]
PASS = os.environ["IOTLAB_PASS"]

KEY_FILE = os.environ["HOME"] + "/.ssh/id_rsa.pub"


def get_ssh_keys():
    res = requests.get(
        URL.format(login=USER),
        auth=(USER, PASS),
    )
    res.raise_for_status()
    return res.json()


def set_ssh_keys(keys_json):
    res = requests.put(
        URL.format(login=USER),
        auth=(USER, PASS),
        headers={"content-type": "application/json"},
        json=keys_json,
    )
    res.raise_for_status()


def delete_ssh_keys():
    set_ssh_keys({"sshkeys": []})


def fixup_ssh_keys(ssh_keys):
    if "" in ssh_keys:  # handle server peculiarity
        ssh_keys.remove("")

    if len(ssh_keys) > 5:  # round-robin on last 2 keys
        ssh_keys.pop(3)


def main():
    keys_json = get_ssh_keys()
    the_key = open(KEY_FILE).read()

    ssh_keys = keys_json["sshkeys"]
    if the_key in ssh_keys:
        print("key already registered, not re-registering")
        return

    ssh_keys.append(the_key)
    fixup_ssh_keys(ssh_keys)

    set_ssh_keys(keys_json)
    print(keys_json)

if __name__ == "__main__":
    main()
