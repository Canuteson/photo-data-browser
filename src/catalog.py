import requests
from munch import DefaultMunch


class PhotoCatalog(object):
    def __init__(self):
        self.client = requests
        self.base_url = 'https://jsonplaceholder.typicode.com'

    def get(self, uri, params=None):
        url = self.base_url + uri
        r = self.client.get(url, params=params)
        r.raise_for_status()
        return r.json()

    def get_all_photos(self):
        for photo in self.get('/photos'):
            yield Photo(photo)

    def get_photo(self, photo_id):
        return Photo(next((photo for photo in self.get('/photos', params={'id': str(photo_id)})), {}))

    def get_all_albums(self):
        for album in self.get('/albums'):
            yield Album(album)

    def get_album(self, album_id):
        return Album(next((album for album in self.get('/albums', params={'id': str(album_id)})), {}))

    def get_photos_for_album(self, album_id):
        for photo in self.get('/photos', params={'albumId': album_id}):
            yield Photo(photo)


class Photo(DefaultMunch):
    def __init__(self, kwargs):
        super(Photo, self).__init__(None, kwargs)


class Album(DefaultMunch):
    def __init__(self, kwargs):
        super(Album, self).__init__(None, kwargs)
