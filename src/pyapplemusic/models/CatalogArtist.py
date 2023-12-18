from typing import List

from pydantic import BaseModel, Field
from .common import Artwork, EditorialNotes, ResourceTypes


class Attributes(BaseModel):
    artwork: Artwork = Artwork()
    editorialNotes: EditorialNotes = EditorialNotes()
    genreNames: List[str]
    name: str
    url: str


class Artist(BaseModel):
    id: str
    type: ResourceTypes = ResourceTypes.ARTISTS
    href: str
    attributes: Attributes = None


class ArtistList(BaseModel):
    artists: List[Artist] = Field(validation_alias="data")
