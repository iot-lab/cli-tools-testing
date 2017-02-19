import pytest

import requests

SITE = "https://devwww.iot-lab.info"

API_URL  = SITE + "/rest/admin/users"

ADMIN_AUTH = ("admin_user", "admin_passwd")


TEST_LOGIN = "somelogin"  # no exotic chars


pytestmark = pytest.mark.skip("requires admin user login")

def test_create_user():

    create_payload = {
        "firstName":   "First name",
        "lastName":    "Last name",
        "login":       TEST_LOGIN,
        "city":        "City",
        "country":     "Country",
        "email":       "e.mail@some.place",
        "motivations": "Doing things\nwith IoT-LAB",
        "password":    "SOME PASSWORD HERE",
        "sshPublicKey": "",  # single key allowed
        "structure":   "Hosting structure",
        "type":        "sa",
    }

    ret = requests.post(API_URL, json=create_payload, auth=ADMIN_AUTH)
    ret.raise_for_status()


def test_delete_user():

    login = TEST_LOGIN

    ret = requests.delete(API_URL+"/"+login, auth=ADMIN_AUTH)
    ret.raise_for_status()


@pytest.mark.skip(reason="un-official api, test does not work (yet) ?")
def test_send_email():

    email_payload = {
        "to": "olivier.fambon@inria.fr",
        "subject": "subject",
        "message": "message",
    }
    
    MAIL_URL = SITE + "/testbed/scripts/send_mail.php"
    ret = requests.post(MAIL_URL, data=email_payload, auth=ADMIN_AUTH)
    ret.raise_for_status()
