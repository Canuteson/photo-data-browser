from unittest import TestCase
import requests_mock
from robber import expect

from src.catalog import PhotoCatalog


requests_mock.mock.case_sensitive = True


class PhotoCatalogTest(TestCase):
    def __init__(self, methodName='runTest'):
        super().__init__(methodName=methodName)
        self.class_to_test = PhotoCatalog()
        self.any_photo_id = 1
        self.photos = [{'id': 1, 'albumId': 2, 'title': 'any-photo'}, {'id': 2, 'albumId': 2, 'title': 'another-photo'}]
        self.albums = [{'id': 1, 'title': 'any-album'}, {'id': 2, 'title': 'another-album'}]

    @requests_mock.mock()
    def test_get_all_photos_yields_all_photos(self, m):
        m.get('https://jsonplaceholder.typicode.com/photos', json=self.photos)
        photos = [p for p in self.class_to_test.get_all_photos()]
        expect(photos).to.have.length(2)
        expect(photos[1].title).to.eq('another-photo')
        expect(m.call_count).to.eq(1)
        expect(m.last_request.path).to.eq('/photos')

    @requests_mock.mock()
    def test_get_photo_filters_request_by_photo_id(self, m):
        m.get('https://jsonplaceholder.typicode.com/photos', json=self.photos)
        p = self.class_to_test.get_photo(99)
        expect(m.call_count).to.eq(1)
        expect(m.last_request.path).to.eq('/photos')
        expect(m.last_request.query).to.eq('id=99')

    @requests_mock.mock()
    def test_get_photo_returns_photo_object(self, m):
        m.get('https://jsonplaceholder.typicode.com/photos', json=self.photos)
        p = self.class_to_test.get_photo(99)
        expect(p.title).to.eq('any-photo')

    @requests_mock.mock()
    def test_get_photos_for_album_filters_photos_by_album_id(self, m):
        m.get('https://jsonplaceholder.typicode.com/photos', json=self.photos)
        photos = [p for p in self.class_to_test.get_photos_for_album(2)]
        expect(m.call_count).to.eq(1)
        expect(m.last_request.path).to.eq('/photos')
        expect(m.last_request.query).to.eq('albumId=2')

    @requests_mock.mock()
    def test_get_photos_for_album_yields_all_album_photos(self, m):
        m.get('https://jsonplaceholder.typicode.com/photos', json=self.photos)
        photos = [p for p in self.class_to_test.get_photos_for_album(2)]
        expect(photos).to.have.length(2)
        expect(photos[0].title).to.eq('any-photo')
        expect(photos[1].title).to.eq('another-photo')

    @requests_mock.mock()
    def test_get_album_filters_request_by_album_id(self, m):
        m.get('https://jsonplaceholder.typicode.com/albums', json=self.albums)
        a = self.class_to_test.get_album(2)
        expect(m.call_count).to.eq(1)
        expect(m.last_request.path).to.eq('/albums')
        expect(m.last_request.query).to.eq('id=2')

    @requests_mock.mock()
    def test_get_album_returns_album_object(self, m):
        m.get('https://jsonplaceholder.typicode.com/albums', json=self.albums)
        a = self.class_to_test.get_album(2)
        expect(a.title).to.eq('any-album')

    @requests_mock.mock()
    def test_get_all_albums_yields_all_albums(self, m):
        m.get('https://jsonplaceholder.typicode.com/albums', json=self.albums)
        albums = [a for a in self.class_to_test.get_all_albums()]
        expect(albums).to.have.length(2)
        expect(albums[0].title).to.eq('any-album')
        expect(albums[1].title).to.eq('another-album')
        expect(m.call_count).to.eq(1)
        expect(m.last_request.path).to.eq('/albums')
