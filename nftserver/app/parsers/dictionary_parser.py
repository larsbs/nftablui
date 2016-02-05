def parse_dictionaries(raw_data):
    family = None
    table = None
    dictionaries = []
    is_map = False
    for line in raw_data:
        if line.startswith('table'):
            family, table = line.split(' ')[1:3]
        if line.startswith('\tmap'):
            is_map = True
            dictionaries.append({'items': None})
            dictionaries[-1]['name'] = line.split(' ')[1]
            dictionaries[-1]['table'] = family + ':' + table
            dictionaries[-1]['id'] = dictionaries[-1]['table'] + ':' + dictionaries[-1]['name']
        if line.startswith('\t\ttype') and is_map:
            line = line.strip('\n')
            dictionaries[-1]['keyDataType'], dictionaries[-1]['valueDataType'] = line.split(' ', 1)[1].split(' : ')
        if line.startswith('\t\telements') and is_map:
            cleaned_items = line.split(' ', 2)[2].strip().strip('{').strip('}').strip().split(', ')
            dictionaries[-1]['items'] = ':'.join(','.join(cleaned_items).split(' : '))
            is_map = False
    return dictionaries


def parse_dictionary(dictionary_id, dictionaries):
    for dictionary in dictionaries:
        if dictionary['id'] == dictionary_id:
            return dictionary
