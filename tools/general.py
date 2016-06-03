import json


def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))
    return results


def read_json(file_name):
    with open(file_name, 'r') as f:
        data = json.load(f)
    return data
