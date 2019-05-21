# -*- coding: utf-8 -*-


import json, logging, pathlib, pprint, string, sys, time
import requests


log = logging.getLogger(__name__)  # outputs to console
logging.basicConfig(
    level=logging.DEBUG,
    format='[%(asctime)s] %(levelname)s [%(module)s-%(funcName)s()::%(lineno)d] %(message)s', datefmt='%d/%b/%Y %H:%M:%S' )


project_dir = pathlib.Path(__file__).resolve().parent.parent
stuff_dir = project_dir.parent


class Link360Checker:

    def check_link360( self ):
        """ Checks serials-solutions link360 knowledgebase. """
        isbn_dct = {}
        with open( f'{project_dir}/data/05b_after_opentextbook_check.json', 'r', encoding='utf-8' ) as f:
            isbn_dct = json.loads( f.read() )
        for (isbn, other_data) in list(isbn_dct.items())[0:10]:
            self.process_item( isbn_dct, isbn, other_data )
        self.write_file( isbn_dct )
        return

    def process_item( self, isbn_dct, isbn, other_data ):
        """ Processes isbn_dct.
            Called by check_link360() """
        open_url = self.make_openurl( isbn, other_data )
        r = requests.get( open_url )
        time.sleep( .5 )
        online_url = self.check_link360_response( r.json() )
        if online_url:
            isbn_dct[isbn]['link360_url'] = online_url
        else:
            isbn_dct[isbn]['link360_url'] = 'no_match_found'
        return

    def make_openurl( self, isbn, other_data ):
        """ Creates openurl.
            Called by check_link360() """
        root = 'https://library.brown.edu/easyaccess/find/link360/'
        openurl = f"{root}?sid=BirkinBookSearch&genre=book&rft.isbn={isbn}&rft.btitle={other_data['title']}&rft.aulast={other_data['author']}"
        log.debug( f'openurl, ```{openurl}```' )
        return openurl

    def check_link360_response( self, jdct ):
        """ Inspects response for online url.
            Called by check_link360() """
        online_url = None
        for result in jdct['results']:
            if 'linkGroups' in result.keys():
                for link_group in result['linkGroups']:
                    if 'url' in link_group.keys():
                        if 'source' in link_group['url']:
                            online_url = link_group['url']['source']
                            break
        log.debug( f'online_url, ```{online_url}```' )
        return online_url

    def write_file( self, isbn_dct ):
        """ Writes output file and logs a count of online urls found.
            Called by check_link360() """
        jsn = json.dumps( isbn_dct, sort_keys=True, indent=2 )
        log.debug( f'jsn, ```{jsn}```' )
        with open( f'{project_dir}/data/05c_after_link360_check.json', 'w', encoding='utf-8' ) as f:
            f.write( jsn )
        online_urls_found = jsn.count( 'link360_url": "https' )
        log.info( f'online_urls_found, `{online_urls_found}`' )
        return

    # def setup_data( self ):
    #     """ Loads two source files.
    #         Called by check_opentextbook() """
    #     with open( f'{project_dir}/data/05_source_key_data.json', 'r', encoding='utf-8' ) as f:
    #         dct = json.loads( f.read() )
    #     with open( f'{project_dir}/data/04_snapshot_open_textbook.json', 'r', encoding='utf-8' ) as f:
    #         lst = json.loads( f.read() )
    #     return ( dct, lst )

    ## end class Link360Checker


if __name__ == '__main__':
    checker = Link360Checker()
    checker.check_link360()
