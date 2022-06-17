from typing import Optional

import pylast
from lastfmcollagegenerator.collage_generator import CollageGenerator
from pydantic import BaseModel


class CollageParams(BaseModel):
    entity: Optional[str] = CollageGenerator.ENTITY_ALBUM
    username: str
    rows: Optional[int] = 5
    cols: Optional[int] = 5
    period: Optional[str] = pylast.PERIOD_7DAYS
