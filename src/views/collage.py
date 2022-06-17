import io
import os

import fastapi
from fastapi import Form
from lastfmcollagegenerator.collage_generator import CollageGenerator
from starlette.responses import StreamingResponse
from starlette.templating import Jinja2Templates


router = fastapi.APIRouter()
templates = Jinja2Templates(directory="templates")


@router.post("/collage")
async def collage(
        username: str = Form(),
        entity: str = Form(),
        rows: int = Form(),
        cols: int = Form(),
        period: str = Form()
):
    collage_generator = CollageGenerator(
        lastfm_api_key=os.getenv("LASTFM_API_KEY"),
        lastfm_api_secret=os.getenv("LASTFM_API_SECRET")
    )
    img = collage_generator.generate(
        entity=entity,
        username=username,
        rows=rows,
        cols=cols,
        period=period
    )
    img_array = io.BytesIO()
    img.save(img_array, format="JPEG")
    img_array.seek(0)
    return StreamingResponse(img_array, media_type="image/jpeg")
