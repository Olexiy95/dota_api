from typing import Union, List, Optional
import requests
import os

BASE_URL = os.getenv("OPEN_DOTA_API_BASE_URL", "https://api.opendota.com/api")


class OpenDotaApi:
    def __init__(self):
        self.base_url = BASE_URL
        self.headers = {"Content-Type": "application/json"}

    def get_player(self, player_id: int):
        return requests.get(f"{self.base_url}/players/{player_id}").json()

    # Generic GET, POST, PUT, DELETE methods

    def get(self, endpoint: str):
        response = requests.get(f"{self.base_url}/{endpoint}", headers=self.headers)
        if response.status_code not in (200, 201):
            print(response.text)
        response.raise_for_status()
        return response.json()

    def post(self, endpoint: str, data: dict):
        response = requests.post(
            f"{self.base_url}/{endpoint}", json=data, headers=self.headers
        )
        response.raise_for_status()
        return response.json()

    def put(self, endpoint: str, data: dict):
        response = requests.put(
            f"{self.base_url}/{endpoint}", json=data, headers=self.headers
        )
        response.raise_for_status()
        return response.json()

    def delete(self, endpoint: str):
        response = requests.delete(f"{self.base_url}/{endpoint}", headers=self.headers)
        response.raise_for_status()
        return response.json()
