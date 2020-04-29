from setuptools import setup

setup(
    name='photo-browser',
    version='0.1',
    py_modules=['src'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        photo-album=src.cli:photo_album
    ''',
)