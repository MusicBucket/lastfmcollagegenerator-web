import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from views import home, collage

load_dotenv()

app = FastAPI()


def configure():
    configure_routing()
    configure_apikeys()


def configure_apikeys():
    pass


def configure_routing():
    app.mount("/static", StaticFiles(directory="static"), name="static")
    app.include_router(home.router)
    app.include_router(collage.router)


if __name__ == "__main__":
    configure()
    uvicorn.run(app, port=8000, host="127.0.0.1")
else:
    configure()
