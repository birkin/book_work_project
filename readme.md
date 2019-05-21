## book-project experimentation

This is a project to see how much open, or at least online info we can get for books.

---

#### thoughts...

- `code` directory can contain scripts for producing files in `data` directory.

- eventually if this proves useful this could be turned into a service, but for now just focusing on finding out resources for getting urls where possible.

- the data file with the most comprehensive info will likely be the last numbered file.

- team -- feel free to use other scripts/languages -- just add the file or directory to the 'code' director, add the output to the data directory, and update this readme.


---

#### data directory contents...

- (not in data-directory) `01_source_booklist_2019-04-26` is the sample initial file.

- (not in data-directory) `02_source_booklist_2019-04-26.json` is above file in more useful json format, made via:

    `$ python3 ./code/source_file_csv_to_json.py`

- `03_snapshot_open_textbook.csv` is an Open Textbook Library [download](https://open.umn.edu/opentextbooks/download.csv) from 2019-May-16-Thursday.

- `04_snapshot_open_textbook.json` is above file in more useful json format, made via:

    `$ python3 ./code/opentextbook_csv_to_json.py`

- `05_source_key_data.json` takes the source file and makes a dictionary using normalized isbn-13 keys, made via:

    `$ python3 ./code/misc.py --function build_keys`

- `05b_after_opentextbook_check.json` uses the above file and adds a check on the `04_snapshot_open_textbook.json` open-textbook file, made via:

    `$ python3 ./code/misc.py --function check_opentextbook`

    Unfortunately, no matches were found.

- [05c_after_link360_check.json](https://github.com/birkin/book_work_project/blob/master/data/05c_after_link360_check.json) uses the above file and adds a check on the serials-solutions link360-api that easyAccess uses. Made via:

    `$ python3 ./code/link360.py`

    Result:

    - Online urls were found for 79 items, but some may not be useful. Example: the title 'ARIEL', by 'PLATH', leads to [this online link](https://login.revproxy.brown.edu/login?url=http://search.ebscohost.com/login.aspx?direct=true&scope=site&db=e000xna&AN=263932) -- for an online book in Spanish. Given that the course is an English course, this is likely not ideal.

    - Also note that sometimes multiple online urls were found. Initially I was only going to show the first, but figured I'd show all found.

    - For reference, the link360-api also returns a list of what appear to be alternate ISBNs. I'm not currently capturing this, but it could be useful. Also for reference, in the past I've found alternate ISBNs to be most useful if associated-metadata can be found so they can be filtered on language, at least.

---
