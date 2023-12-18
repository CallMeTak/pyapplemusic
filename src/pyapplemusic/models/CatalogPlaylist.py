from enum import Enum
from typing import List, Union

from pydantic import BaseModel, Field
from .common import Artwork, ResourceTypes


class PlayListType(Enum):
    EDITORIAL = "editorial"
    EXTERNAL = "external"
    PERSONAL_MIX = "personal-mix"
    REPLAY = "replay"
    USER_SHARED = "user-shared"


class PlayParams(BaseModel):
    id: str = None
    kind: str = None
    versionHash: str = None


class Attributes(BaseModel):
    artwork: Artwork = None
    curatorName: str
    description: str = None
    isChart: bool
    lastModifiedDate: str = None
    name: str
    playlistType: PlayListType = None
    url: str
    playParams: PlayParams = PlayParams()
    trackTypes: List[Union[ResourceTypes.MUSIC_VIDEOS, ResourceTypes.SONGS]] = None
    """Extended attribute"""


class CatalogPlaylist(BaseModel):
    id: str
    type: ResourceTypes
    href: str
    attributes: Attributes = None


class PlaylistList(BaseModel):
    artists: List[CatalogPlaylist] = Field(validation_alias="data")


class CatalogPlaylists(BaseModel):
    playlists: List[CatalogPlaylist] = Field(validation_alias="data")
    href: str = None
    next: str = None
