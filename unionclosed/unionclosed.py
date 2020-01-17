#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import sys
from itertools import combinations

from unionclosed.utilities import *

logging.basicConfig(level = logging.INFO)
# ------------------------------------------------------------------------------#
# ------------------------------------------------------------------------------#
# ------------------------------------------------------------------------------#

def check(sets):
    # check the union combination of sets
    for set1 in sets:
        for set2 in sets:
            # check for union sets
            if set1.union(set2) in sets:
                continue
            else:
                return 0
    return 1

# ------------------------------------------------------------------------------#

def load_sets(file_out):
    # load data into sets
    sets = []
    for set_in in file_out:
        elements = set_in.strip().split(',')
        set_elements = frozenset(elements)

        # check if there are any duplicates in the individual set data
        if len(elements) != len(set_elements):
            logging.warning(
                'Duplicates in the individual sets found : {}'.format(
                    str(set_in)))

        # family set creation
        if set_elements != {''}:
            sets.append(set_elements)
        else:
            # creates an empty set
            sets.append(frozenset())

    sets = set(sets)

    if len(file_out) != len(sets):
        logging.warning('Duplicates in sets found')

    return sets

# ------------------------------------------------------------------------------#

def is_unionclosed(file_location):
    logging.info('Reading the file')
    try:
        file_out = read_file(file_location)
    except FileNotFoundError:
        logging.error('No file found in the given location')
        sys.exit()

    logging.info('Loading the sets from file')
    sets = load_sets(file_out)

    logging.info('Checking if the sets belong to unionclosed')
    output = check(sets)

    if output:
        return True
    else:
        return False

# ------------------------------------------------------------------------------#

def validate(input_set):
    if type(input_set) == set:
        for i in input_set:
             if type(i)!= int:
                return False
    else:
        return False

    return True

# ------------------------------------------------------------------------------#

def create(input_set, location):
    logging.info('Creating unionclosed sets')

    validation = validate(input_set)
    unionclosed_sets = []

    if validation:
        # Creating union closed lists
        for i in range(len(input_set)+1):
            unionclosed_sets.extend(list(map(list, combinations(input_set, i))))
    else:
        logging.error('Please check the input, elements must be given in set of integers format')

    write_data(unionclosed_sets, location)
