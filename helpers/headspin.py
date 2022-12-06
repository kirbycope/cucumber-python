import requests
from helpers.config import from_env


def devices():
    req = "devices"
    return send_request("get", req)


def device_hostname(devices, udid):
    device_list = devices['devices']
    for device in device_list:
        if device['serial'] == udid:
            return device['hostname']


def send_request(verb, req, data=None):
    # print('\u001b[36m' + verb + " | " + req + '\u001b[0m')  # DEBUGGING
    headspin_token = from_env("HEADSPIN_TOKEN")
    headers = {
        "Authorization": "Bearer {}".format(headspin_token)
    }
    req = "https://api-dev.headspin.io/v0/{}".format(req)
    if data == None:
        r = getattr(requests, verb)(req, headers=headers)
        return r.json()
    else:
        headers["content-type"] = "application/json"
        r = getattr(requests, verb)(req, headers=headers, data=data)
        return r.json()
