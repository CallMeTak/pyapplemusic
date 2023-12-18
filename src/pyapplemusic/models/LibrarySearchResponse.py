from typing import Dict

from .LibraryMusicVideo import LibraryMusicVideos
from .LibraryPlaylist import LibraryPlaylists
from .LibraryAlbum import LibraryAlbums
from .LibraryArtist import LibraryArtists
from .LibrarySong import LibrarySongs
from pydantic import BaseModel, Field


class Results(BaseModel):
    library_albums: LibraryAlbums = Field(validation_alias="library-albums", default=None)
    library_artists: LibraryArtists = Field(validation_alias="library-artists", default=None)
    library_music_videos: LibraryMusicVideos = Field(validation_alias="library-music-videos", default=None)
    library_playlists: LibraryPlaylists = Field(validation_alias="library-playlists", default=None)
    library_songs: LibrarySongs = Field(validation_alias="library-songs", default=None)


# Todo
class Meta(BaseModel):
    results: Dict


class LibrarySearchResponse(BaseModel):
    results: Results = None
    meta: Meta = None

