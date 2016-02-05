import unittest

from tests.table_tests import NFTServerCreateTableTests
from tests.table_tests import NFTServerListTableTests
from tests.table_tests import NFTServerDeleteTableTests
from tests.chain_tests import NFTServerCreateChainTests
from tests.chain_tests import NFTServerListChainTests
from tests.chain_tests import NFTServerDeleteChainTests
from tests.rule_tests import NFTServerCreateRuleTests
from tests.rule_tests import NFTServerListRuleTests
from tests.rule_tests import NFTServerDeleteRuleTests
from tests.set_tests import NFTServerCreateSetTests
from tests.set_tests import NFTServerListSetTests
from tests.set_tests import NFTServerUpdateSetTests
from tests.dictionary_tests import NFTServerCreateDictionaryTests
from tests.dictionary_tests import NFTServerListDictionaryTests
from tests.dictionary_tests import NFTServerUpdateDictionaryTests


if __name__ == '__main__':
    unittest.main()
