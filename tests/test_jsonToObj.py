__author__ = 'STH'

import unittest
from JsonToObj import JsonToObj


class TestJsonToObj(unittest.TestCase):

    def test_hasPath(self):
        t = JsonToObj(r"test_data\metanote.json")
        self.assertTrue(t.hasPath())
        t.jsonPath = ''
        self.assertFalse(t.hasPath())
        t.jsonPath = r"test_data\metaboat.json"
        self.assertFalse(t.hasPath())

    def test_validateJson(self):
        return True

if __name__ == '__main__':
    unittest.main()





