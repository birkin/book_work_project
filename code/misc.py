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


class OpenTextbookChecker:

    def check_opentextbook( self ):
        """ Checks local snapshot data. """
        ( isbn_dct, open_textbook_lst ) = self.setup_data()
        for (isbn, other_data) in isbn_dct.items():
            for book_dct in open_textbook_lst:
                if isbn == book_dct['ISBN13']:
                    isbn_dct[isbn]['opentextbook_url'] = book_dct['Opentextbooks URL']
                else:
                    isbn_dct[isbn]['opentextbook_url'] = 'no_match_found'
        jsn = json.dumps( isbn_dct, sort_keys=True, indent=2 )
        log.debug( f'jsn, ```{jsn}```' )
        with open( f'{project_dir}/data/05b_after_opentextbook_check.json', 'w', encoding='utf-8' ) as f:
            f.write( jsn )

    def setup_data( self ):
        """ Loads two source files.
            Called by check_opentextbook() """
        with open( f'{project_dir}/data/05_source_key_data.json', 'r', encoding='utf-8' ) as f:
            dct = json.loads( f.read() )
        with open( f'{project_dir}/data/04_snapshot_open_textbook.json', 'r', encoding='utf-8' ) as f:
            lst = json.loads( f.read() )
        return ( dct, lst )

    ## end class OpenTextbookChecker


def parse_args():
    """ Parses arguments when module called via __main__ """
    parser = argparse.ArgumentParser( description='Required: function-name.' )
    parser.add_argument( '--function', '-f', help='function name required', required=True )
    args_dict = vars( parser.parse_args() )
    return args_dict


def call_function( function_name: str ) -> None:
    """ Safely calls function named via input string to __main__
        Credit: <https://stackoverflow.com/a/51456172> """
    log.debug( f'function_name, ```{function_name}```' )
    checker = OpenTextbookChecker()
    safe_dispatcher = { 'build_keys': build_keys, 'check_opentextbook': checker.check_opentextbook }
    try:
        safe_dispatcher[function_name]()
    except:
        raise Exception( 'invalid function' )
    return


if __name__ == '__main__':
    args: dict = parse_args()
    log.debug( f'args, ```{args}```' )
    submitted_function: str = args['function']
    call_function( submitted_function )


# if __name__ == '__main__':
#     args = parse_args()
#     log.debug( f'args, ```{args}```' )
#     if args['function'] == 'build_keys':
#         build_keys()
#     elif args['function'] == 'check_opentextbook':
#         checker = OpenTextbookChecker()
#         checker.check_opentextbook()
#     else:
#         raise Exception( 'unknown function' )
