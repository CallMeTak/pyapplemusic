from typing import List

from pydantic import BaseModel, Field

from .CatalogSongResponse import PlayParams, Preview
from .common import Artwork, EditorialNotes, ContentRating, ResourceTypes


class Attributes(BaseModel):
    albumName: str = None
    artistName: str
    artistUrl: str = None
    artwork: Artwork
    contentRating: ContentRating = None
    durationInMillis: int
    editorialNotes: EditorialNotes = None
    genreNames: List[str] = None
    has4K: bool
    hasHDR: bool
    isrc: str = None
    name: str
    playParams: PlayParams = PlayParams()
    previews: List[Preview] = None
    releaseDate: str = None
    trackNumber: int = None
    url: str
    videoSubType: str = None
    workId: str = None
    workName: str = None


class MusicVideo(BaseModel):
    id: str
    type: ResourceTypes = ResourceTypes.MUSIC_VIDEOS
    href: str
    attributes: Attributes = None


class MusicVideoList(BaseModel):
    music_videos: List[MusicVideo] = Field(validation_alias="data")
