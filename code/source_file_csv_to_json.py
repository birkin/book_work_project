# -*- coding: utf-8 -*-

import csv, datetime, io, json, logging, os, pathlib, pprint, tempfile


## setup

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(asctime)s] %(levelname)s [%(module)s-%(funcName)s()::%(lineno)d] %(message)s', datefmt='%d/%b/%Y %H:%M:%S' )
log = logging.getLogger(__name__)  # outputs to console

current_file = pathlib.Path(__file__).resolve()
current_dir = pathlib.Path(__file__).resolve().parent
project_dir = current_dir.parent
stuff_dir = project_dir.parent
log.debug( f'current_file, ```{current_file}```; current_dir, ```{current_dir}```; project_dir, ```{project_dir}```' )


## work

## doesn't work because first two lines of csv file need to be removed
# lst = []
# with open( f'{project_dir}/data/01_source_booklist_2019-04-26.csv', 'r', encoding='utf-8' ) as f:
#     csv_reader = csv.DictReader( f )
#     for csv_row in csv_reader:
#         lst.append( csv_row )

lst = []
with open( f'{stuff_dir}/01_source_booklist_2019-04-26.csv', 'r', encoding='utf-8' ) as f:
    lines = f.readlines()
    good_lines = lines[2:]
    io_f = io.StringIO()    # create an in-memory file-like-object
    for line in good_lines:
        io_f.write( line )  # ok, new file written, but pointer is at end-of-file
    io_f.seek( 0 )          # go back to beginning of file
    csv_reader = csv.DictReader( io_f )
    for csv_row in csv_reader:
        lst.append( csv_row )

jsn = json.dumps( lst, indent=2 )
with open( f'{stuff_dir}/02_source_booklist_2019-04-26.json', 'w' ) as f:
    f.write( jsn )

log.debug( f'jsn, ```{jsn}```' )
