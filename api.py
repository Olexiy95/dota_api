from fastapi import APIRouter, HTTPException
from open_dota_api_library import OpenDotaApi
import requests

router = APIRouter()

# Initialize your API class with the base URL
api = OpenDotaApi()


@router.get("/")
def get_root():
    return {"message": "Hello World"}


@router.get("/players/{player_id}")
def get_player(player_id: int):
    try:
        return api.get_player(player_id)
    except requests.RequestException as e:
        raise HTTPException(status_code=400, detail=str(e))
