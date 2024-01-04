# PyAppleMusic
PyAppleMusic is an API wrapper for the Apple Music API. Unlike most other API wrappers, this one supports Library Resources (as long as you have a Media-User-Token)! Additionally, raw JSON responses are serialized into classes with Pydantic making it easier for developers to work with the API. This project is currently a work-in-progress so only a small subset of endpoints and resources are implemented, but more will come soon.

# Usage
```python
from pyapplemusic import AppleMusic

music = AppleMusic(dev_token="YOUR APPLE DEVELOPER TOKEN", media_token="YOUR MEDIA USER TOKEN")
```
