__author__ = 'STH'

import unittest
import pathInspector

class TestPathInspector(unittest.TestCase):

    def test_validPaths(self):
        self.assertTrue(pathInspector.getWorkingPath(r"test_data\metanote.json"))
        self.assertFalse(pathInspector.getWorkingPath(r"not\a\real\path"))
        self.assertFalse(pathInspector.getWorkingPath(5))
        self.assertFalse(pathInspector.getWorkingPath("abcdefghijklmnopqrstuvwxyz"))
        self.assertFalse(pathInspector.getWorkingPath(""))

    def test_findNearestPathMatch(self):
        self.assertEquals("test_data\\mistake\\",pathInspector.findNearestPathMatch(r"test_data\mistake\metanote.json"))
        self.assertEquals("test_date\\",pathInspector.findNearestPathMatch(r"test_date\mistake\metanote.json"))
        self.assertEquals("\\",pathInspector.findNearestPathMatch("\\"))
        self.assertEquals("..\\",pathInspector.findNearestPathMatch("..\\"))

    def test_fileCount(self):
        self.assertFalse(pathInspector.fileCount(r"test_data") == 0)
        self.assertFalse(pathInspector.fileCount(r"badpath"))


if __name__ == '__main__':
    unittest.main()
