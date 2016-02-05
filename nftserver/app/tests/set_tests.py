import json
import os
import unittest
import tempfile

from flask import jsonify

import app as nftserver
from utils import nft_utils


class NFTServerCreateSetTests(unittest.TestCase):

    def setUp(self):
        nftserver.app.config['TESTING'] = True
        self.app = nftserver.app.test_client()

    def tearDown(self):
        cmd = nft_utils.nft_command('flush ruleset')
        nft_utils.close_nft_command(cmd)

    def test_set_creation(self):
        assert True

    def test_no_set_creation_with_empty_table(self):
        assert True

    def test_no_set_creation_with_nonexistent_table(self):
        assert True

    def test_no_set_creation_with_empty_name(self):
        assert True

    def test_no_set_creation_with_empty_data_type(self):
        assert True

    def test_no_set_creation_with_invalid_data_type(self):
        assert True

    def test_no_set_creation_with_invalid_elements(self):
        assert True


class NFTServerListSetTests(unittest.TestCase):

    def setUp(self):
        nftserver.app.config['TESTING'] = True
        self.app = nftserver.app.test_client()

    def tearDown(self):
        cmd = nft_utils.nft_command('flush ruleset')
        nft_utils.close_nft_command(cmd)

    def test_list_all_sets(self):
        assert True

    def test_list_single_set(self):
        assert True


class NFTServerUpdateSetTests(unittest.TestCase):

    def setUp(self):
        nftserver.app.config['TESTING'] = True
        self.app = nftserver.app.test_client()

    def tearDown(self):
        cmd = nft_utils.nft_command('flush ruleset')
        nft_utils.close_nft_command(cmd)

    def test_set_update(self):
        assert True

    def test_no_update_nonexistent_set(self):
        assert True

    def test_only_update_set_elements(self):
        assert True

    def test_no_update_set_with_invalid_new_elements(self):
        assert True


if __name__ == '__main__':
    unittest.main()
