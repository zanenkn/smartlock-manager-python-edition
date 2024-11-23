import os
import requests


def json_rpc_request(method, params, token=None, url=""):
    headers = {
        "Content-Type": "application/json",
        "X-Company-Login": os.getenv("SIMPLYBOOK_COMPANY_LOGIN"),
    }

    if token:
        headers["X-Token"] = token

    request_data = {
        "jsonrpc": "2.0",
        "method": method,
        "params": params,
        "id": 1,
    }

    try:
        response = requests.post(
            f"{os.getenv('SIMPLYBOOK_BASE_URL')}{url}",
            json=request_data,
            headers=headers,
        )
        response.raise_for_status()

        print(f"SimplyBook: JSON-RPC request successful for method {method}")

        return response.json().get("result")
    except requests.RequestException as e:
        raise Exception(
            f"SimplyBook: JSON-RPC request for method {method} failed: {e}"
        ) from e
