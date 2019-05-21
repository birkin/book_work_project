# -*- coding: utf-8 -*-


import argparse, json, logging, pathlib, pprint, sys
import isbnlib


log = logging.getLogger(__name__)  # outputs to console
logging.basicConfig(
    level=logging.DEBUG,
    format='[%(asctime)s] %(levelname)s [%(module)s-%(funcName)s()::%(lineno)d] %(message)s', datefmt='%d/%b/%Y %H:%M:%S' )


project_dir = pathlib.Path(__file__).resolve().parent.parent
stuff_dir = project_dir.parent
# sys.path.append( project_dir )


def build_keys():
    """ Takes the hyphenated isbns and builds canonical isbns. """
    new_dct = {}
    with open( f'{stuff_dir}/02_source_booklist_2019-04-26.json', 'r', encoding='utf-8' ) as f:
        lst = json.loads( f.read() )
        for dct in lst:
            if dct['ISBN']:  # some records are empty
                canonical_isbn = isbnlib.get_canonical_isbn( dct['ISBN'], output='isbn13' )
                new_dct[canonical_isbn] = { 'isbn_original': dct['ISBN'], 'title': dct['Title'], 'author': dct['Author'] }
    jsn = json.dumps( new_dct, sort_keys=True, indent=2 )
    log.debug( f'jsn, ```{jsn}```' )
    with open( f'{project_dir}/data/05_source_key_data.json', 'w', encoding='utf-8' ) as f:
        f.write( jsn )


def parse_args():
    """ Parses arguments when module called via __main__. """
    parser = argparse.ArgumentParser( description='Required: function-name.' )
    parser.add_argument( '--function', '-f', help='function name required', required=True )
    args_dict = vars( parser.parse_args() )
    return args_dict

if __name__ == '__main__':
    args = parse_args()
    log.debug( f'args, ```{args}```' )
    if args['function'] == 'build_keys':
        build_keys()
