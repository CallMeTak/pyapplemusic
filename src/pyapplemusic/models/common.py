from pydantic import BaseModel
from enum import Enum
from typing import Optional


class Artwork(BaseModel):
    width: Optional[int] = None
    height: Optional[int] = None
    url: Optional[str] = None
    bgColor: str = None
    textColor1: str = None
    textColor2: str = None
    textColor3: str = None
    textColor4: str = None


class ResourceTypes(str, Enum):
    ACTIVITIES = "activities"
    ALBUMS = "albums"
    APPLE_CURATORS = "apple-curators"
    ARTISTS = "artists"
    CURATORS = "curators"
    MUSIC_VIDEOS = "music-videos"
    PLAYLISTS = "playlists"
    RECORD_LABELS = "record-labels"
    SONGS = "songs"
    STATIONS = "stations"
    LIBRARY_ALBUMS = "library-albums"
    LIBRARY_ARTISTS = "library-artists"
    LIBRARY_MUSIC_VIDEOS = "library-music-videos"
    LIBRARY_SONGS = "library-songs"
    LIBRARY_PLAYLISTS = "library-playlists"


class ContentRating(Enum):
    CLEAN = "clean"
    EXPLICIT = "explicit"


class EditorialNotes(BaseModel):
    name: str = None
    short: str = None
    standard: str = None
    tagline: str = None

