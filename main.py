from fastapi import FastAPI
from datetime import datetime
from pydantic import BaseModel
import json

app = FastAPI()


class InfoResponse(BaseModel):
    email: str
    current_datetime: str
    github_url: str


def load_config():
    with open("config.json") as config_file:
        return json.load(config_file)


config = load_config()


@app.get("/info", response_model=InfoResponse)
def get_info():
    return InfoResponse(
        email=config["email"],
        current_datetime=datetime.now().isoformat(),
        github_url=config["github_url"],
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=10000)
