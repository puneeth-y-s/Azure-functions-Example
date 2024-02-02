import azure.functions as func
import logging
import json
from sys import argv


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Hi there, HTTP Triggered function is triggered.")

    name = req.params.get("name")
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get("name")

    if name:
        return func.HttpResponse(
            f"Hello {name}, This HTTP triggered function executed successfully"
        )
    else:
        return func.HttpResponse(
            "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
            status_code=200,
        )


if __name__ == "__main__":
    print(f"called an azure function with args {argv[1]} {argv[2]}")
    body = {"name": "Punnet Y S"}
    body = json.dumps(body, indent=2).encode("utf-8")
    request = func.HttpRequest(method="POST", url="localhost", body=body)
    resp = main(request)
    print(f"body: {resp.get_body()}")
