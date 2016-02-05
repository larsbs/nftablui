def parse_sets(raw_data):
    family = None
    table = None
    sets = []
    is_set = False
    for line in raw_data:
        if line.startswith('table'):
            family, table = line.split(' ')[1:3]
        if line.startswith('\tset'):
            is_set = True
            sets.append({'items': None})
            sets[-1]['name'] = line.split(' ')[1]
            sets[-1]['table'] = family + ':' + table
            sets[-1]['id'] = sets[-1]['table'] + ':' + sets[-1]['name']
        if line.startswith('\t\ttype') and is_set:
            sets[-1]['dataType'] = line.split(' ')[1]
        if line.startswith('\t\telements') and is_set:
            cleaned_items = line.split(' ', 2)[2].strip().strip('{').strip('}').strip().split(', ')
            sets[-1]['items'] = ','.join(cleaned_items)
            is_set = False
    return sets


def parse_set(set_id, sets):
    for set in sets:
        if set['id'] == set_id:
            return set
