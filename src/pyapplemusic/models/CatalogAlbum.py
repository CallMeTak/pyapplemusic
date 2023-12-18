from typing import List

from pydantic import BaseModel, Field

from CatalogSongResponse import PlayParams
from .common import Artwork, ResourceTypes, EditorialNotes


class Attributes(BaseModel):
    artistName: str
    artistUrl: str = None
    artwork: Artwork
    audioVariants: List[str] = None
    contentRating: str = None
    copyright: str = None
    editorialNotes: EditorialNotes
    genreNames: List[str]
    isCompilation: bool
    isComplete: bool
    isMasteredForItunes: bool
    isSingle: bool
    name: str
    playParams: PlayParams = PlayParams()
    recordLabel: str = None
    releaseDate: str = None
    trackCount: int
    upc: str = None
    url: str


class AlbumsResponse(BaseModel):
    id: str
    type: str = ResourceTypes.ALBUMS
    href: str
    attributes: Attributes = None


class AlbumsList(BaseModel):
    albums: List[AlbumsResponse] = Field(validation_alias="data")
