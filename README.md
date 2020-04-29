# Photo Data Browser

A simple cli tool for browsing photo album data


### Getting Started
Clone this repo:  
`git clone https://github.com/canuteson/photo-data-browser`  
`cd photo-data-browser`

### Build and Run

Requirements:
* Linux or MacOS with Python3
* pip - The Python Package Installer

Install virtualenv:  
`sudo pip install virtualenv `

Create and activate a virtual environment:  
`virtualenv -p python3 venv`  
`source venv/bin/activate`

Install dependencies:  
`pip install -Ur requirements.txt`  


Install the CLI:  
`pip install -e .`

Run:  
`photo-album [ALBUM ID]`


### Build in Docker

Requirements:  
* Docker

Build the Docker image:  
`make`

Run:  
`docker run -it --rm photo-album-cli [ALBUM ID]`