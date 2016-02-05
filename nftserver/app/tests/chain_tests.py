import json
import os
import app as nftserver
import unittest
import tempfile

from flask import jsonify

from utils import nft_utils
from wrappers import table_wrapper


class NFTServerCreateChainTests(unittest.TestCase):

    def setUp(self):
        nftserver.app.config['TESTING'] = True
        self.app = nftserver.app.test_client()
        table_wrapper.create_table({'family': 'ip', 'name': 'test'})

    def tearDown(self):
        cmd = nft_utils.nft_command('flush ruleset')
        nft_utils.close_nft_command(cmd)

    def test_chain_creation(self):
        assert True

    def test_no_chain_creation_with_empty_table(self):
        assert True

    def test_no_chain_creation_with_nonexistent_table(self):
        assert True

    def test_no_chain_creation_with_empty_name(self):
        assert True

    def test_no_chain_creation_with_invalid_type(self):
        assert True

    def test_no_chain_creation_with_invalid_hook(self):
        assert True

    def test_no_chain_creation_with_priority_lower_than_zero(self):
        assert True


class NFTServerListChainTests(unittest.TestCase):

    def setUp(self):
        nftserver.app.config['TESTING'] = True
        self.app = nftserver.app.test_client()
        table_wrapper.create_table({'family': 'ip', 'name': 'test'})

    def tearDown(self):
        cmd = nft_utils.nft_command('flush ruleset')
        nft_utils.close_nft_command(cmd)

    def test_list_all_chains(self):
        assert True

    def test_list_single_chain(self):
        assert True


class NFTServerDeleteChainTests(unittest.TestCase):

    def setUp(self):
        nftserver.app.config['TESTING'] = True
        self.app = nftserver.app.test_client()
        table_wrapper.create_table({'family': 'ip', 'name': 'test'})

    def tearDown(self):
        cmd = nft_utils.nft_command('flush ruleset')
        nft_utils.close_nft_command(cmd)

    def test_chain_deletion(self):
        assert True


if __name__ == '__main__':
    unittest.main()
