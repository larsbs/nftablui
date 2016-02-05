IP_HEADER_OFFSETS = {
    # 0: 'Version',
    # 1: 'TOS',
    # 2: 'Length',
    # 6: 'Identification',
    9: 'protocol',
    # 12: 'checksum',
    12: 'saddr',
    22: 'daddr'
}

IP6_HEADER_OFFSETS = {
    # 0: 'version',
    # 0: 'priority',
    1: 'flowlabel',
    4: 'length',
    6: 'nexthdr',
    7: 'hoplimit',
    8: 'saddr',
    24: 'daddr'
}


NETWORK_PROTOCOL_CODES = {
    6: 'tcp',  # 0x06
    17: 'udp',  # 0x11
}


TCP_HEADER_OFFSETS = {
    0: 'sport',
    2: 'dport',
    4: 'sequence',
    8: 'ackseq',
    # TODO: Complete
}


UDP_HEADER_OFFSETS = {
    0: 'sport',
    1: 'dport',
    2: 'length',
    3: 'checksum'
}


TRANSPORT_HEADER_OFFSETS = {
    'tcp': TCP_HEADER_OFFSETS,
    'udp': UDP_HEADER_OFFSETS
}
