import json
import os
import unittest
import tempfile

from flask import jsonify

import app as nftserver
from utils import nft_utils


class NFTServerCreateRuleTests(unittest.TestCase):

    def setUp(self):
        nftserver.app.config['TESTING'] = True
        self.app = nftserver.app.test_client()

    def tearDown(self):
        cmd = nft_utils.nft_command('flush ruleset')
        nft_utils.close_nft_command(cmd)

    def test_rule_creation_with_match(self):
        assert True

    def test_rule_creation_with_set(self):
        assert True

    def test_rule_creation_with_dictionary(self):
        assert True

    def test_no_rule_creation_with_empty_chain(self):
        assert True

    def test_no_rule_creation_with_nonexistent_chain(self):
        assert True

    def test_no_rule_creation_with_empty_expression(self):
        assert True

    def test_no_rule_creation_with_invalid_expression(self):
        assert True

    def test_no_rule_creation_with_empty_key(self):
        assert True

    def test_no_rule_creation_with_invalid_key(self):
        assert True

    def test_no_rule_creation_with_empty_statements(self):
        assert True

    def test_no_rule_creation_with_statement_with_empty_match(self):
        assert True

    def test_no_rule_creation_with_statement_with_invalid_match(self):
        assert True

    def test_no_rule_creation_with_statement_with_empty_action(self):
        assert True

    def test_no_rule_creation_with_statement_with_invalid_action(self):
        assert True


class NFTServerListRuleTests(unittest.TestCase):

    def setUp(self):
        nftserver.app.config['TESTING'] = True
        self.app = nftserver.app.test_client()

    def tearDown(self):
        cmd = nft_utils.nft_command('flush ruleset')
        nft_utils.close_nft_command(cmd)

    def test_list_all_rules(self):
        assert True

    def test_list_single_rule(self):
        assert True


class NFTServerDeleteRuleTests(unittest.TestCase):

    def setUp(self):
        nftserver.app.config['TESTING'] = True
        self.app = nftserver.app.test_client()

    def tearDown(self):
        cmd = nft_utils.nft_command('flush ruleset')
        nft_utils.close_nft_command(cmd)

    def test_rule_deletion(self):
        assert True


if __name__ == '__main__':
    unittest.main()
