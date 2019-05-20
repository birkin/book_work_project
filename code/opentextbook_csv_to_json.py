# -*- coding: utf-8 -*-

import csv, datetime, json, logging, os, pathlib, pprint


## setup

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(asctime)s] %(levelname)s [%(module)s-%(funcName)s()::%(lineno)d] %(message)s', datefmt='%d/%b/%Y %H:%M:%S' )
log = logging.getLogger(__name__)  # outputs to console

current_file = pathlib.Path(__file__).resolve()
current_dir = pathlib.Path(__file__).resolve().parent
project_dir = current_dir.parent
log.debug( f'current_file, ```{current_file}```; current_dir, ```{current_dir}```; project_dir, ```{project_dir}```' )


## work

lst = []
with open( f'{project_dir}/data/03_snapshot_open_textbook.csv', 'r', encoding='utf-8-sig' ) as f:  # note: 'utf-8-sig' necessary to handle the BOM-indicator in this file, otherwise all the IDs look like ```"\ufeffOTL ID": "4"```.
    csv_reader = csv.DictReader( f )
    for csv_row in csv_reader:
        lst.append( csv_row )

jsn = json.dumps( lst, indent=2 )
with open( f'{project_dir}/data/04_snapshot_open_textbook.json', 'w' ) as f:
    f.write( jsn )

log.debug( f'jsn, ```{jsn}```' )
