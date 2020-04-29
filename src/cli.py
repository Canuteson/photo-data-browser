import click

from src.catalog import PhotoCatalog


@click.command()
@click.argument('album-id')
def photo_album(album_id):
    catalog = PhotoCatalog()
    album = catalog.get_album(album_id)
    if album.id is None:
        click.echo("Could not find album for ID:{}".format(album_id))
        return
    for photo in catalog.get_photos_for_album(album.id):
        click.echo("[{}] {}\n".format(photo.id, photo.title))


if __name__ == '__main__':
    photo_album()
