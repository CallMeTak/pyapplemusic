from typing import List

from pydantic import BaseModel, Field

from .common import Artwork, ContentRating, ResourceTypes


class PlayParams(BaseModel):
    pass


class Attributes(BaseModel):
    albumName: str = None
    artistName: str
    artwork: Artwork
    contentRating: ContentRating = None
    durationInMillis: int
    genreNames: List[str]
    name: str
    playParams: PlayParams = PlayParams()
    releaseDate: str = None
    trackNumber: int = None


class LibraryMusicVideo(BaseModel):
    id: str
    type: ResourceTypes = ResourceTypes.MUSIC_VIDEOS
    href: str
    attributes: Attributes = None


class LibraryMusicVideos(BaseModel):
    next: str = None
    href: str = None
    videos: List[LibraryMusicVideo] = Field(validation_alias="data")
