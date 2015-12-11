# List files in this directory
# Pick json-files
# Extract class from filename

import os
import json
import re

# This directory
this_dir = os.path.dirname(os.path.realpath(__file__))

def get_training_and_class_data(dataset_name):
    training_data = []
    class_data = []

    dataset_dir = os.path.join(this_dir, dataset_name)

    for fname in os.listdir(dataset_dir):
        if fname.endswith('.json'):
            # Extract class from file name.
            gazeclass_search = re.search('^(\\w*)-[0-9]+\\.json$', fname)
            if gazeclass_search:
                gazeclass = gazeclass_search.group(1)
            else:
                # Gazeclass not found. Skip.
                continue
            print('Loading ' + fname)
            with open(os.path.join(dataset_dir, fname), 'r') as jsonf:
                training_data.append(json.load(jsonf))
                class_data.append(gazeclass)

    return training_data, class_data
