# TODO: Replace ALL references of database in the program to this file
# http://stackoverflow.com/a/32156582

import sys
import os
PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))

# Example of import:

# from django.conf import settings
# sys.path.append(settings.PROJECT_ROOT)
# from master import UNMODELED_DATABASES
# sys.path.remove(settings.PROJECT_ROOT)

UNMODELED_DATABASES = {
    'show_data_individual': {
        'location': os.path.abspath(os.path.join(PROJECT_ROOT,'data/show_data.db')),
    },
##    'show_data_aggregated': {
##        'location': 'data/show_data_aggregated.db',
##    },
    'user_list_indexed': {
        'location': 'data/user_list_indexed.sqlite3',
    },
    'show_indices': {
        'location': os.path.abspath(os.path.join(PROJECT_ROOT,'data/show_indices.db')),
    }
}

SHOW_LIST_TYPES = {
    'empty' : 'empty',
    'nonempty' : 'nonempty'
}

# Make this a lot better
def string_SQL_safe(sql_string):
    if 'drop table' not in sql_string:
        return True

    return False

def string_delimiter_upper(lower_string, delimiter, exception_list = None):
    words = lower_string.split(delimiter)
    for index, word in enumerate(words):
        if word not in exception_list:
            words[index] = word[0].upper() + word[1:]

    return ' '.join(words)
