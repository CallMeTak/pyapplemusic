from typing import List

from pydantic import BaseModel, Field
from .common import Artwork, ContentRating, ResourceTypes


class PlayParams(BaseModel):
    catalogId: str = None


class Attributes(BaseModel):
    artistName: str
    artwork: Artwork
    contentRating: ContentRating = None
    dateAdded: str = None
    name: str
    playParams: PlayParams = PlayParams()
    releaseDate: str = None
    trackCount: int
    genreNames: List[str]


# https://developer.apple.com/documentation/applemusicapi/get_a_library_album
class LibraryAlbum(BaseModel):
    id: str
    type: ResourceTypes = ResourceTypes.LIBRARY_ALBUMS
    href: str


class LibraryAlbums(BaseModel):
    albums: List[LibraryAlbum] = Field(validation_alias="data")
    href: str = None
    next: str = None
