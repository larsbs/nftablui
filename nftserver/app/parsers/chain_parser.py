from utils import nft_utils


def parse_chains(nft_json):
    chains = []
    for element in nft_json:
        if nft_utils.json_is_a_chain(element):
            chain = element['chain']
            chain['id'] = chain['family'] + ':' + chain['table'] + ':' + chain['name']
            chain['hook'] = chain.pop('hooknum', None)
            chain['priority'] = chain.pop('prio', None)
            chain['table'] = chain.pop('family', None) + ':' + chain.pop('table', None)
            chain.pop('use', None)  # Remove use key
            chain.pop('packets', None)  # Remove packets key
            chain.pop('handle', None)  # Remove handle key
            chain.pop('bytes', None)  # Remove bytes key
            chain.pop('policy', None)  # Remove policy key
            chains.append(chain)
    return chains


def parse_chain(chain_id, chains):
    for chain in chains:
        if chain['id'] == chain_id:
            return chain
