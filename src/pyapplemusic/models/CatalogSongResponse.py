from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field

from .common import Artwork, ContentRating, EditorialNotes, ResourceTypes


class Preview(BaseModel):
    artwork: Artwork = None
    hashValue: int = None
    hlsURL: str = None
    url: str = None


class PlayParams(BaseModel):
    id: str = None
    kind: str = None
    isLibrary: bool = None
    reporting: bool = None
    catalogId: int = None
    reportingId: int = None


class AudioVariants(Enum):
    DOLBY_ATMOS = "dolby-atmos"
    DOLBY_AUDIO = "dolby-audio"
    HI_RES_LOSSLESS = "hi-res-lossless"
    LOSSLESS = "lossless"
    LOSSY_STEREO = "lossy-stereo"


# https://developer.apple.com/documentation/applemusicapi/songs/attributes
class Attributes(BaseModel):
    albumName: str
    artistName: str
    artistUrl: str = None
    """Extended"""
    artwork: Artwork
    attribution: str = None
    audioVariants: List[AudioVariants] = None
    """Extended"""
    composerName: str = None
    contentRating: ContentRating = None
    discNumber: int = None
    durationInMillis: int
    editorialNotes: EditorialNotes = None
    genreNames: List[str]
    hasLyrics: bool
    isAppleDigitalMaster: bool
    isrc: str = None
    movementCount: int = None
    movementName: str = None
    movementNumber: int = None
    name: str
    playParams: PlayParams = PlayParams()
    previews: List[Preview]
    releaseDate: str = None
    trackNumber: int = None
    url: str
    workName: str = None


# https://developer.apple.com/documentation/applemusicapi/get_a_catalog_song
class CatalogSong(BaseModel):
    id: str
    type: ResourceTypes = ResourceTypes.SONGS
    href: str
    attributes: Attributes = None


class CatalogSongs(BaseModel):
    songs: List[CatalogSong] = Field(validation_alias="data")
