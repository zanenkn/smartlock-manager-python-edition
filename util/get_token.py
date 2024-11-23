import os
from util.json_rpc_request import json_rpc_request


def get_token():
    params = {
        "company_login": os.getenv("SIMPLYBOOK_COMPANY_LOGIN"),
        "api_key": os.getenv("SIMPLYBOOK_API_KEY"),
    }

    return json_rpc_request(method="getToken", params=params, url="/login")
