from fastapi import FastAPI
from api import router

app = FastAPI(title="Dota 2 API", version="0.1")

app.include_router(router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
