#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import sys
# ------------------------------------------------------------------------------#

def read_file(file_location):

    if not file_location.endswith('.txt'):
        logging.error('Please make sure input file format is txt')
        sys.exit(404)

    # read the data
    f = open(file_location, 'r')
    out = f.readlines()

    return out

# ------------------------------------------------------------------------------#

def write_data(unionclosed_sets, location):

    if not location.endswith('.txt'):
        logging.warning('Preffered file format is txt')

    try:
        with open(location, 'w') as f:
            for item in unionclosed_sets:
                # joining the list of items to string and writing it to a file
                f.write("%s\n" % ",".join(str(i) for i in item))

        logging.info('Union closed sets saved to file')
    except:
        logging.error("Check the file location provided")