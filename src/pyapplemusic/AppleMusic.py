import sys
import traceback
from typing import List, Any, Union

import requests
from requests import Session, Response

from .models.CatalogSongResponse import CatalogSong, CatalogSongs
from .models.LibraryArtist import LibraryArtist, LibraryArtists
from .models.LibraryPlaylist import LibraryPlaylist, LibraryPlaylists, LibraryPlaylistTracks
from .models.LibrarySearchResponse import LibrarySearchResponse
from .models.LibrarySong import LibrarySongs
from .models.common import ResourceTypes


class Service:
    def __init__(self, dev_token: str, media_token: str):
        self.developer_token: str = dev_token
        self.media_token: str = media_token
        self.base_url: str = "https://api.music.apple.com/v1/"
        self.__client = Session()
        self.__configure_session()

    def __configure_session(self):
        self.__client.headers = {
            'Authorization': 'Bearer ' + self.developer_token,
            'Media-User-Token': self.media_token,
            'Origin': 'https://music.apple.com'
        }

    def perform_request(self, url: str, query_params: dict[str, Any] = {}) -> Union[None, Response]:
        try:
            response = self.__client.get(url, params=query_params)
        except requests.RequestException as err:
            print("Error performing request.")
            print(err)
            traceback.print_exc()
            sys.exit(1)
        else:
            status = response.status_code
            if status != 200:
                response.raise_for_status()
            return response
            # if status == 404:
            #    print(f"404 Not Found: {response.request.url}")
            # elif status == 401:
            #    print("401 Unauthorized. Please check your developer and user tokens.")
            # elif status == 403:
            #    print("403 Forbidden. Please check your developer and user tokens.")
            # else:
            #    print(f"HTTP Error: {status}")
            # return False, response


class LibraryService(Service):
    def __init__(self, dev_token: str, media_token: str):
        super().__init__(dev_token, media_token)

    def get_next_songs(self, url) -> LibrarySongs:
        response = self.perform_request("https://api.music.apple.com" + url)
        return LibrarySongs.model_validate_json(response.text)

    def get_playlist(self):
        pass

    # Fetch one or more playlists by ids. Max fetch limit is 25
    def get_playlists_by_ids(self, ids: List[str]) -> List[LibraryPlaylist]:
        query_params = {
            "ids": ids
        }
        url = f"me/library/playlists"
        response = self.perform_request(url, query_params)

        # Using the LibraryPlaylists model because it already has a List[Playlists] for validation,
        # The next and href will always be None for this endpoint, so they are unneeded. This is also done for
        # other endpoints further down in this file
        data = LibraryPlaylists.model_validate_json(response.text)
        return data.playlists

    # A playlist can also have a MusicVideo, should rework later
    def get_playlist_tracks(self, playlist_id: str, offset: int = 0, limit: int = 25) -> LibraryPlaylistTracks:
        """
        Note: May result in 404 not found if the playlist is empty

        @param playlist_id: Library id of playlist
        @param offset: Start index of returned results
        @param limit: Number of results to return (max: 100)
        @return: List of Songs
        """
        query_params = {
            "offset": offset,
            "limit": limit
        }
        response = self.perform_request(self.base_url + f"me/library/playlists/{playlist_id}/tracks",
                                        query_params)
        return LibraryPlaylistTracks.model_validate_json(response.text)

    def get_all_playlists(self, offset: int = 1, limit: int = 10) -> LibraryPlaylists:
        """
        Gets all the user's playlists in their library

        @param offset: Start index of the returned results
        @param limit: Number of results to return
        @return: List of LibraryPlaylists
        """
        query_params = {
            "offset": offset,
            "limit": limit
        }
        response = self.perform_request(self.base_url + "me/library/playlists", query_params)
        return LibraryPlaylists.model_validate_json(response.text)

    def get_song(self) -> CatalogSong:
        pass

    def get_songs_by_ids(self, track_ids: List[str]) -> LibrarySongs:
        """
        Gets library information of 1 - 300 songs.
        @param track_ids: List of song ids
        @return: List of Songs
        """
        url = self.base_url + "me/library/songs"
        query_params = {"ids": track_ids}
        response = self.perform_request(url, query_params)
        return LibrarySongs.model_validate_json(response.text)

    def get_song_relationship(self):
        pass

    def get_all_songs(self, offset: int = 0, limit: int = 25) -> LibrarySongs:
        """
        Gets all songs in the library.
        Max limit of 100.
        Used get_next() to continue going through all results
        @param offset:
        @param limit:
        @return:
        """
        query_params = {
            "offset": offset,
            "limit": limit
        }
        response = super().perform_request(self.base_url + "me/library/songs", query_params)
        return LibrarySongs.model_validate_json(response.text)

    def get_artist(self, artist_id: str) -> LibraryArtist:
        """
        Note: Due to an API limitation, it is not possible to use an artist's library id to retrieve their catalog info
        Instead, you must perform a search using the artist's name
        @param artist_id: Library id of artist
        @return: LibraryArtist
        """
        response = self.perform_request(self.base_url + f"me/library/artists/{artist_id}", {})
        return LibraryArtist.model_validate_json(response.text)

    def get_artist_relationship(self):
        pass

    def get_artists_by_ids(self, artist_ids: List[str]) -> List[LibraryArtist]:
        query_params = {"ids": artist_ids}
        response = self.perform_request(self.base_url + "me/library/artists", query_params)
        data = LibraryArtists.model_validate_json(response.text)
        return data.artists

    def get_all_artists(self) -> LibraryArtists:
        response = self.perform_request(self.base_url + "me/library/artists")
        return LibraryArtists.model_validate_json(response.text)

    def search(self, search_term: str, types: List[ResourceTypes], limit: int = 25,
               offset: int = 0) -> LibrarySearchResponse:
        search_term = search_term.replace(" ", "+")
        query_params = {
            "term": search_term,
            "types": types,
            "limit": limit,
            "offset": offset
        }
        response = self.perform_request(self.base_url + "me/library/search", query_params)
        print(response.json())
        return LibrarySearchResponse.model_validate_json(response.text)


class CatalogService(Service):
    def __init__(self, dev_token: str, media_token: str):
        super().__init__(dev_token, media_token)

    def get_song(self) -> CatalogSong:
        pass

    def get_songs(self) -> List[CatalogSong]:
        pass

    def get_songs_by_ids(self, track_ids: List[str]) -> List[CatalogSong]:
        """
        Gets catalog information of 1 - 300 songs

        @param track_ids: List of song ids
        @return: List of Songs
        """
        query_params = {"ids": track_ids}
        response = self.perform_request(self.base_url + "catalog/us/songs", query_params)
        data = CatalogSongs.model_validate_json(response.text)
        return data.songs

    def search(self, search_term: str, types: [ResourceTypes], offset: int = 0, limit: int = 25):
        query_params = {
            "offset": offset,
            "limit": limit,
            "types": types,
            "term": search_term
        }
        response = self.perform_request(self.base_url + "catalog/us/search", query_params)


class StorefrontService:
    pass


class AppleMusicClient:
    def __init__(self, dev_token: str, media_token: str) -> None:
        self.library = LibraryService(dev_token, media_token)
        self.catalog = CatalogService(dev_token, media_token)
        # self.storefront = StorefrontService(dev_token, media_token)


"""
    # Should use generics (or 2 separate functions) later so this works for playlists too
    def get_next(self, url: str):
        
        Retrieves the next set of data given the "next" url from a previous request
        @param url:
        @return:
        
        response = self.__perform_request("https://api.music.apple.com" + url, {})
        if not success:
            return None
        songs = SongsList.model_validate_json(response.text)
        return songs
"""
