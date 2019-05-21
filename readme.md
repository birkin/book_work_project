experimentation project to see how much open, or at least online info we can get for books.

thoughts...

- `code` directory can contain scripts for producing files in `data` directory.

- eventually if this proves useful this could be turned into a service, but for now just focusing on finding out resources for getting urls where possible.


data directory...

- (not in data-directory) `01_source_booklist_2019-04-26` is the sample initial file.

- (not in data-directory) `02_source_booklist_2019-04-26.json` is above file in more useful json format, made via:

    `$ python3 ./code/source_file_csv_to_json.py`

- `03_snapshot_open_textbook.csv` is an Open Textbook Library [download](https://open.umn.edu/opentextbooks/download.csv) from 2019-May-16-Thursday.

- `04_snapshot_open_textbook.json` is above file in more useful json format, made via:

    `$ python3 ./code/opentextbook_csv_to_json.py`

- `05_source_key_data.json` takes the source file and makes a dictionary using normalized isbn-13 keys, made via:

    `$ python3 ./code/misc.py --function build_keys`


