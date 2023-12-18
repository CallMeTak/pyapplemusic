from typing import List

from pydantic import BaseModel, Field
from .common import Artwork, ResourceTypes


class PlayParameters(BaseModel):
    id: str = None
    kind: str = None
    isLibrary: bool = None
    reporting: bool = None
    catalogId: str = None
    reportingId: str = None


class Attributes(BaseModel):
    # Define the Pydantic model for the Song
    albumName: str
    artistName: str
    artwork: Artwork = Artwork()
    contentRating: str = None
    discNumber: int = None
    durationInMillis: int
    genreNames: List[str]
    hasLyrics: bool
    name: str
    playParams: PlayParameters = PlayParameters()
    releaseDate: str = None
    trackNumber: int = None


# https://developer.apple.com/documentation/applemusicapi/librarysongs
class LibrarySong(BaseModel):
    id: str
    type: ResourceTypes = ResourceTypes.LIBRARY_SONGS
    href: str
    attributes: Attributes = None


class LibrarySongs(BaseModel):
    next: str = None
    href: str = None
    songs: List[LibrarySong] = Field(validation_alias="data")
