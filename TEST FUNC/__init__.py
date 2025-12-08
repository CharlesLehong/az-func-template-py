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

    headers = req.headers
    org_id = headers.get("bootsure-organization-id")
    api_id = headers.get("bootsure-api-id")
    env_id = headers.get("bootsure-environment-id")

    if not org_id or not api_id or not env_id:
        return func.HttpResponse(
            json.dumps({ "name": "BadRequest", "message": "Could not set appropriate headers." }),
            status_code=400,
            mimetype="application/json"
        )

    master_data_url = req_body.get("masterDataLookupEndpoint")
    effective = req_body.get("effectiveDate")

    try:
        data_service = DataService(org_id, api_id, env_id, master_data_url, effective)
        output = execute(req_body.get("input", {}), data_service)

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

def execute(input, data_service):
    print("Your code goes here")








