experimentation project to see how much open, or at least online info we can get for books.

thoughts...

- `code` directory can contain scripts for producing files in `data` directory.

- eventually if this proves useful this could be turned into a service, but for now just focusing on finding out resources for getting urls where possible.


data directory...

- `01-original-file.csv` is the sample file we were initially given.

- `02-fielded_file.json` is above file in a bit more useful format, made via:

    `$ python3 ./code/source_file_csv_to_json.py`
