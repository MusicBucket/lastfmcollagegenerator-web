import fastapi
from lastfmcollagegenerator.collage_generator import CollageGenerator
from starlette.requests import Request
from starlette.templating import Jinja2Templates

from templatetags.tags import GATag

router = fastapi.APIRouter()
templates = Jinja2Templates(directory="templates", extensions=[GATag])


@router.get("/")
async def root(request: Request):
    context = {
        "request": request,
        "entities": CollageGenerator.ENTITIES,
        "rows": list(range(2, 6)),
        "cols": list(range(2, 6)),
        "periods": CollageGenerator.PERIODS
    }
    context["rows"].reverse()
    context["cols"].reverse()
    return templates.TemplateResponse("home/index.html", context)
