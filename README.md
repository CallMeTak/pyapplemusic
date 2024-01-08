# PyAppleMusic
PyAppleMusic is an API wrapper for the Apple Music API. Unlike most other API wrappers, this one supports Library Resources (as long as you have a Media-User-Token)! Additionally, raw JSON responses are serialized into classes with Pydantic making it easier for developers to work with the API. This project is currently a work-in-progress so only a small subset of endpoints and resources are implemented, but more will come soon.

## Usage

```python
from pyapplemusic.AppleMusic import AppleMusicClient

music = AppleMusicClient(dev_token="YOUR APPLE DEVELOPER TOKEN", media_token="YOUR MEDIA USER TOKEN")

# Prints every song in a user's library
all_songs = music.library.get_all_songs()
    has_next = all_songs.next
    while has_next is not None:
        songs = music.library.get_next_songs(has_next)
        has_next = songs.next
        for song in songs.songs:
            print(f"Name: {song.attributes.name}")
            print(f"Artist: {song.attributes.artistName}")
            print("==============================================")

```
## Output
```commandline
Name: Human Nature
Artist: Michael Jackson
==============================================
Name: HURTWORLD '99
Artist: City Morgue, ZillaKami & SosMula
==============================================
Name: HYFR (Hell Ya F*****g Right) [feat. Lil Wayne]
Artist: Drake
==============================================
Name: Hype Boy
Artist: NewJeans
==============================================
Name: i
Artist: Kendrick Lamar
==============================================
Name: I
Artist: Lil Skies
==============================================
Name: I Can
Artist: Nas
==============================================
Name: I Can't Decide
Artist: Hopsin
==============================================

```