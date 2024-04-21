from fastapi import APIRouter, HTTPException
from open_dota_api_library import OpenDotaApi
import requests
from fastapi.responses import HTMLResponse

router = APIRouter()

# Initialize your API class with the base URL
api = OpenDotaApi()


@router.get("/", response_class=HTMLResponse)
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Welcome to My API</title>
        <style>
            body { font-family: 'Arial', sans-serif; margin: 20px; text-align: center; }
            h1 { color: #333; }
            a { color: #007BFF; text-decoration: none; }
            a:hover { text-decoration: underline; }
        </style>
    </head>
    <body>
        <h1>Welcome to My Game API</h1>
        <p><a href="/docs">Go to API Documentation</a></p>
    </body>
    </html>
    """


@router.get("/player/{player_id}")
def get_player(player_id: int):
    try:
        return api.get_player(player_id)
    except requests.RequestException as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/player/{player_id}/matches")
def get_player_matches(player_id: int):
    try:
        return api.get_player_matches(player_id)
    except requests.RequestException as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/match/{match_id}")
def get_match(match_id: int):
    try:
        return api.get_match(match_id)
    except requests.RequestException as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get(
    "/player/common_matches/{player1_id}/{player2_id}",
    description="Hello this is description.",
)
def get_common_matches(player1_id: int, player2_id: int) -> list[int]:
    try:
        player1_matches = api.get_player_matches(player1_id)
        player2_matches = api.get_player_matches(player2_id)

        player1_match_ids = {match["match_id"] for match in player1_matches}
        player2_match_ids = {match["match_id"] for match in player2_matches}

        common_match_ids = list(player1_match_ids.intersection(player2_match_ids))
        return common_match_ids
    except requests.RequestException as e:
        raise HTTPException(status_code=400, detail=f"Failed to fetch data: {str(e)}")
    except KeyError as e:
        raise HTTPException(status_code=500, detail=f"Key error in data: {str(e)}")
