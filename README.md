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

### Config.json:
`config.json` must be placed in the root dir with `__main__.py` (and this README).

The search directory `"SEARCH_DIR"` must be specified in the config.

If the output directory `"OUTPUT_DIR_ROOT"` is not specified, it will default to the same as the search directory.

`Config.json` minimum requirements:

    {
        "APIKEY" :              "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
        "SEARCH_DIR" :          "home/temp_dl_tv/"
    }

See http://thetvdb.com/?tab=apiregister to get your own API key.

The program will work without the API Key for testing, but it's highly recommended you get one if you're using it long-term.

By default the program will dry run and output proposed name changes.

This needs to be turned off by specifying `"DRYRUN" : false` in the config.

An `ignore_list.json` file is created and maintained in the search directory `SEARCH_DIR`. This is to prevent repeated calls
to the api for failed files when the program is run in automation scripts.

### Optional Configs:

    {
        ...
        "OUTPUT_DIR_ROOT" :     "media/TV Shows/",
        "FILE_NAME_TEMPLATE" :  "{series_title} - S{s_no:02d}E{ep_no:02d} - {ep_name}.{ext}",
        "SEASON_DIR_TEMPLATE" : "Season {0:02d}",
        "MAKEWINSAFE" :         (default = true),
        "AUTODELETE" :          (default = false),
        "DRYRUN" :              (default = true)
    }

If `"AUTODELETE"` is true, any file that is not matched for renaming will be deleted. Be careful with this! Additional functionality to only delete files with certain extensions needs to be added in the future. (Though it would be trivial if you wanted to modify the code)

`"FILE_NAME_TEMPLATE"` has the following keywords:
    
-  `series_title`   = The title of the series as given by TVDB
-  `s_no`           = Season number, as integer
-  `ep_no`          = Episode number, as integer
-  `ep_name`        = The name of the episode as given by TVDB
-  `ext`            = filename extension. Probably leave this as it is

The string follows the Python String Format Spec. Mini Language, as given by:
https://docs.python.org/3.4/library/string.html#formatspec

Default  `"SEASON_DIR_TEMPLATE"` and `"FILE_NAME_TEMPLATE"`:

`"Season {0:02d}"` and `"{series_title} - S{s_no:02d}E{ep_no:02d} - {ep_name}.{ext}"`

Which gives:

`OUTPUT_DIR_ROOT\Series Title\Season XX\Series Title - SXXEXX - Episode Title.ext`

### Running the script:
Once the `config.json` is in place, simply run the script as its root directory:

    python3 tv-show-renamer

or in the directory:

    python3 __main__.py

### Automation:

The script can be run on a schedule using Task Scheduler (Win) or cronjobs (UNIX), as long as the config is set up correctly (see above).

If using a virtual environment, it must be activated by the automation script first (and deactivated after).