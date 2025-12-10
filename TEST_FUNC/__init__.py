import json
import math
import logging
import azure.functions as func
from data_service import DataService
from package_installer import install_package

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        req_body = req.get_json()
    except Exception:
        return func.HttpResponse(
            json.dumps({ "name": "BadRequest", "message": "Request body is required." }),
            status_code=400,
            mimetype="application/json"
        )

    try:
        output = execute(req_body)
        return func.HttpResponse(
            json.dumps(output),
            status_code=200,
            mimetype="application/json"
        )

    except Exception as err:
        return func.HttpResponse(
            json.dumps({ "name": "InternalError", "message": str(err) }),
            status_code=500,
            mimetype="application/json"
        )

def execute(input):
    return "Random stuff"








