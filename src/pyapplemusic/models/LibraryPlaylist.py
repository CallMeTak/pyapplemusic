from __future__ import annotations

from enum import Enum

from .LibraryMusicVideo import LibraryMusicVideo
from .common import Artwork, ResourceTypes
from pydantic import BaseModel, Field
from typing import List, Optional, Union
from .LibrarySong import LibrarySong


class LibraryTrackTypes(Enum):
    LIBRARY_MUSIC_VIDEOS = "library-music-videos"
    LIBRARY_SONGS = "library-songs"


class Description(BaseModel):
    description: str = None
    standard: str = None


# No official documentation for PlayParams
class PlayParams(BaseModel):
    id: str = None
    kind: str = None
    isLibrary: bool = None

    # Undocumented
    versionHash: str = None
    globalId: str = None


# https://developer.apple.com/documentation/applemusicapi/libraryplaylists/attributes
class Attributes(BaseModel):
    playParams: PlayParams = PlayParams()
    canEdit: bool = None
    name: str = None
    description: Description = Description()
    dateAdded: str = None
    artwork: Optional[Artwork] = Artwork()
    isPublic: bool = None
    hasCatalog: bool
    trackTypes: List[LibraryTrackTypes] = None
    """Extended Attribute"""


# https://developer.apple.com/documentation/applemusicapi/libraryplaylists
class LibraryPlaylist(BaseModel):
    id: str
    type: ResourceTypes = ResourceTypes.LIBRARY_PLAYLISTS
    href: str
    attributes: Attributes = None


# https://developer.apple.com/documentation/applemusicapi/get_all_library_playlists
class LibraryPlaylists(BaseModel):
    playlists: List[LibraryPlaylist] = Field(validation_alias="data")


# https://developer.apple.com/documentation/applemusicapi/libraryplaylists/relationships/libraryplayliststracksrelationship
class LibraryPlaylistTracks(BaseModel):
    tracks: List[Union[LibrarySong, LibraryMusicVideo]] = Field(validation_alias="data")
    meta: LibraryPlaylistTracks.Meta = None
    next: str = None

    class Meta(BaseModel):
        total: int
