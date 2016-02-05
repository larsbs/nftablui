import json
import os
import unittest
import tempfile

from flask import jsonify

import app as nftserver
from utils import nft_utils


class NFTServerCreateDictionaryTests(unittest.TestCase):

    def setUp(self):
        nftserver.app.config['TESTING'] = True
        self.app = nftserver.app.test_client()

    def tearDown(self):
        cmd = nft_utils.nft_command('flush ruleset')
        nft_utils.close_nft_command(cmd)

    def test_dictionary_creation(self):
        assert True

    def test_no_dictionary_creation_with_empty_table(self):
        assert True

    def test_no_dictionary_creation_with_nonexistent_table(self):
        assert True

    def test_no_dictionary_creation_with_empty_name(self):
        assert True

    def test_no_dictionary_creation_with_empty_key_data_type(self):
        assert True

    def test_no_dictionary_creation_with_invalid_key_data_type(self):
        assert True

    def test_no_dictionary_creation_with_empty_value_data_type(self):
        assert True

    def test_no_dictionary_creation_with_invalid_value_data_type(self):
        assert True

    def test_no_dictionary_creation_with_invalid_elements(self):
        assert True


class NFTServerListDictionaryTests(unittest.TestCase):

    def setUp(self):
        nftserver.app.config['TESTING'] = True
        self.app = nftserver.app.test_client()

    def tearDown(self):
        cmd = nft_utils.nft_command('flush ruleset')
        nft_utils.close_nft_command(cmd)

    def test_list_all_dictionaries(self):
        assert True

    def test_list_single_dictionary(self):
        assert True


class NFTServerUpdateDictionaryTests(unittest.TestCase):

    def setUp(self):
        nftserver.app.config['TESTING'] = True
        self.app = nftserver.app.test_client()

    def tearDown(self):
        cmd = nft_utils.nft_command('flush ruleset')
        nft_utils.close_nft_command(cmd)

    def test_dictionary_update(self):
        assert True

    def test_no_update_nonexistent_dictionary(self):
        assert True

    def test_only_update_dictionary_elements(self):
        assert True

    def test_no_update_dictionary_with_invalid_new_elements(self):
        assert True


if __name__ == '__main__':
    unittest.main()
