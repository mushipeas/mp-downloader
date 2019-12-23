# `mp-downloader`

A simple multi-threaded python downloader, with chunk download support

Written for and tested on Python 3.7.5

## To Initialise the Project

### Recommended:
In the root dir of project, run:

    python -m venv .venv
This should create a virtual environment

### Activate the environment:
    .\.venv\Scripts\activate (Windows)
    source .venv/bin/activate (UNIX)

### Install required packages:
    pip install -r requirements.txt

## Useage

### As a separate module:
Above the base directory:

    usage: mp-downloader [-h] [-d DIRNAME] [-cs CHUNK_SIZE] URL

    A file downloader, which returns the full filepath, basename, and CRC32 hash
    for the downloaded file - if successful.

    positional arguments:
    URL                     URL to be downloaded

    optional arguments:
    -h, --help              show this help message and exit
    -d DIRNAME, --dirname DIRNAME
                            Directory to download to. [d]
    -cs CHUNK_SIZE, --chunk_size CHUNK_SIZE
                            Chunksize in bytes.

### As part of a project:
 ** This needs to be developed.

The project folder needs to be renamed to mp_downloader (the - is not compatible for imports), and then placed in the main project directory. The main function can then be imported as:

    from mp_downloader.__main__ import download_file

download_file can then be used as:

    download_file(URL: str, dirname: str, chunksize=8192)