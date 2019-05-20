# -*- coding: utf-8 -*-

import csv, datetime, json, logging, os, pathlib, pprint


## setup

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(asctime)s] %(levelname)s [%(module)s-%(funcName)s()::%(lineno)d] %(message)s', datefmt='%d/%b/%Y %H:%M:%S' )
log = logging.getLogger(__name__)

current_file = pathlib.Path(__file__).resolve()
current_dir = pathlib.Path(__file__).resolve().parent
project_dir = current_dir.parent
log.debug( f'current_file, ```{current_file}```; current_dir, ```{current_dir}```; project_dir, ```{project_dir}```' )


## work

lst = []
with open( f'{project_dir}/data/01_source_booklist_2019-04-26.csv', 'r', encoding='utf-8' ) as f:
    csv_reader = csv.DictReader( f )
    for csv_row in csv_reader:
        lst.append( csv_row )

jsn = json.dumps( lst, indent=2 )
with open( f'{project_dir}/data/02_source_booklist_2019-04-26.json', 'w' ) as f:
    f.write( jsn )

print( jsn )
