import re


MATCH_PATTERN = '(?:(?P<match>\{\s?[\w\-\.(,\s)]+\s?\}|[\w\d\.\-]+)|(?P<set>\@\w+))'
ACTION_PATTERN = '(?P<action>(jump\s)?\w+)'
DATA_PATTERN = '(?P<data>.+)?'
STATEMENTS_PATTERN = re.compile(r'' + MATCH_PATTERN + '\s' + ACTION_PATTERN + '\s?' + DATA_PATTERN)


def parse_map_statement(map_statement):
    map_statements = []
    map_statement = map_statement.strip('vmap').strip('map').strip().strip('{').strip('}').strip()
    raw_map_statements = map_statement.split(', ')
    for statement in raw_map_statements:
        statement = statement.split(':')
        map_statements.append({
            'match': statement[0].strip(),
            'action': statement[1].strip()
        })
    return map_statements


def parse_rule_statements(raw_statements):
    if raw_statements.startswith('map'):  # (Map) A map with no actions inside
        r = 'NOT IMPLEMENTED YET'
    elif raw_statements.startswith('vmap'):  # (Verdict Map) A map with actions inside
        r = parse_map_statement(raw_statements)
    else:
        r = STATEMENTS_PATTERN.match(raw_statements).groupdict()
        r.pop('data', None)  # At the moment we don't want to use data key
        if r['match'] and r['match'][0] == '{':
            r['match'] = '{' + r['match'].strip('{').strip('}').strip() + '}'
        r = [r]
    return r


def parse_rules(raw_data):
    family = None
    table = None
    chain = None
    rules = []
    for line in raw_data:
        if line.startswith('table'):
            family, table = line.split(' ')[1:3]
        if line.startswith('\tchain'):
            chain = line.split(' ')[1]
        if line[:2] == '\t\t' and not line.startswith('\t\ttype') and not line.startswith('\t\telements'):
            raw_rule = line.strip()
            raw_rule = raw_rule.split(' ')
            rule = {}
            rule['expression'] = raw_rule[0]
            rule['key'] = raw_rule[1]
            rule['handle'] = raw_rule[-1]
            rule['position'] = 0
            rule['chain'] = family + ':' + table + ':' + chain
            #rule['id'] = rule['chain'] + ':' + rule['handle']
            rule['id'] = family + ':' + table + ':' + chain + ':' + rule['handle']
            rule['statements'] = parse_rule_statements(' '.join(raw_rule[2:-3]))
            rules.append(rule)
    return rules


def parse_rule(rule_id, rules):
    for rule in rules:
        if rule['id'] == rule_id:
            return rule
