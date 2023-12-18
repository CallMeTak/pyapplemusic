from typing import List

from pydantic import BaseModel, Field
from .common import ResourceTypes


class Attributes(BaseModel):
    name: str


class LibraryArtist(BaseModel):
    id: str
    type: ResourceTypes = ResourceTypes.LIBRARY_ARTISTS
    href: str
    attributes: Attributes = None


class LibraryArtists(BaseModel):
    next: str = None
    artists: List[LibraryArtist] = Field(validation_alias="data")
