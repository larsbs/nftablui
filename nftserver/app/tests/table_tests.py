import json
import os
import unittest
import tempfile

from flask import jsonify

import app as nftserver
from utils import nft_utils


def create_table(name, family):
    return json.dumps({'table': {'name': name, 'family': family}})


class NFTServerCreateTableTests(unittest.TestCase):

    def setUp(self):
        nftserver.app.config['TESTING'] = True
        self.app = nftserver.app.test_client()

    def tearDown(self):
        cmd = nft_utils.nft_command('flush ruleset')
        nft_utils.close_nft_command(cmd)

    def test_table_creation(self):
        response = self.app.post('/api/tables', data=create_table('test', 'ip'), content_type='application/json')
        response_json = json.loads(response.data.decode('utf-8'))
        assert response.status_code == 201

    def test_no_table_creation_with_empty_name(self):
        response = self.app.post('/api/tables', data=create_table('', 'ip'), content_type='application/json')
        response_json = json.loads(response.data.decode('utf-8'))
        assert response.status_code == 400
        assert 'errors' in response_json.keys()
        assert 'name' in response_json['errors'].keys()

    def test_no_table_creation_with_empty_family(self):
        response = self.app.post('/api/tables', data=create_table('test', ''), content_type='application/json')
        response_json = json.loads(response.data.decode('utf-8'))
        assert response.status_code == 400
        assert 'errors' in response_json.keys()
        assert 'family' in response_json['errors'].keys()

    def test_no_table_creation_with_invalid_family(self):
        response = self.app.post('/api/tables', data=create_table('test', 'asdf'), content_type='application/json')
        response_json = json.loads(response.data.decode('utf-8'))
        assert response.status_code == 400
        assert 'errors' in response_json.keys()
        assert 'family' in response_json['errors'].keys()


class NFTServerListTableTests(unittest.TestCase):

    def setUp(self):
        nftserver.app.config['TESTING'] = True
        self.app = nftserver.app.test_client()

    def tearDown(self):
        cmd = nft_utils.nft_command('flush ruleset')
        nft_utils.close_nft_command(cmd)

    def test_list_all_tables(self):
        tables = [create_table('test', 'ip'), create_table('test2', 'ip')]
        for i, table in enumerate(tables):
            response = self.app.post('/api/tables', data=table, content_type='application/json')
            assert response.status_code == 201
            tables[i] = json.loads(response.data.decode('utf-8'))['table']
        response = self.app.get('/api/tables')
        response_json = json.loads(response.data.decode('utf-8'))
        assert response.status_code == 200
        assert 'tables' in response_json.keys()
        assert tables[0] in response_json['tables']
        assert tables[1] in response_json['tables']

    def test_list_single_table(self):
        table = create_table('test', 'ip')
        response = self.app.post('/api/tables', data=table, content_type='application/json')
        assert response.status_code == 201
        table = json.loads(response.data.decode('utf-8'))['table']
        response = self.app.get('/api/tables/ip:test')
        response_json = json.loads(response.data.decode('utf-8'))
        assert response.status_code == 200
        assert 'table' in response_json.keys()
        assert table == response_json['table']


class NFTServerDeleteTableTests(unittest.TestCase):

    def setUp(self):
        nftserver.app.config['TESTING'] = True
        self.app = nftserver.app.test_client()

    def tearDown(self):
        cmd = nft_utils.nft_command('flush ruleset')
        nft_utils.close_nft_command(cmd)

    def test_table_deletion(self):
        table = create_table('test', 'ip')
        response = self.app.post('/api/tables', data=table, content_type='application/json')
        assert response.status_code == 201
        response = self.app.delete('/api/tables/ip:test')
        assert response.status_code == 204
        assert response.data == b''


if __name__ == '__main__':
    unittest.main()
