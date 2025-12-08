import json
import requests

from custom_error import CustomError

class DataService:
    def __init__(self, bootSureOrganisationId, bootSureApiId, bootSureEnvironmentId, bootSureApiUrl, effectiveDate):
        if not bootSureOrganisationId:
            raise CustomError("Header Error", "bootSURE-organization-id is required")
        
        if not bootSureApiId:
            raise CustomError("Header Error", "bootSURE-api-id is required")
        
        if not bootSureEnvironmentId:
            raise CustomError("Header Error", "bootSURE-environment-id is required")

        self._bootSureOrganisationId = bootSureOrganisationId
        self._bootSureApiId = bootSureApiId
        self._bootSureEnvironmentId = bootSureEnvironmentId
        self._bootSureApiUrl = bootSureApiUrl
        self._effectiveDate = effectiveDate
        self._lookupDict = {}

    def get(self, table_name):
        return self._lookupDict.get(table_name)

    def add(self, table_name, data):
        self._lookupDict[table_name] = data

    def load(self, table_name):
        if table_name in self._lookupDict:
            return  

        data = {
            "code": table_name,
            "effectiveDate": self._effectiveDate,
        }

        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "bootSURE-organization-id": self._bootSureOrganisationId,
            "bootSURE-environment-id": self._bootSureEnvironmentId,
            "bootSURE-api-id": self._bootSureApiId,
        }

        response = requests.post(
            f"{self._bootSureApiUrl}/api/rating/lookup",
            headers=headers,
            json=data,
            verify=False  
        )

        response.raise_for_status()
        lookup_response = json.loads(response.json().get("data", "{}"))
        self.add(table_name, lookup_response)
