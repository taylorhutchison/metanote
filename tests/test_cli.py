__author__ = 'STH'

import unittest
import sys
import clitools

class TestCli_Setup(unittest.TestCase):

    def test_arg1(self):
        sys.argv.clear()
        sys.argv = ['file.py','--path','test path']
        args = clitools.setArgs()
        self.assertGreater(len(args.path),0)
        self.assertFalse(args.overwrite)
        self.assertFalse(args.edit)
        self.assertFalse(args.repair)

    def test_arg2(self):
        sys.argv.clear()
        sys.argv = ['file.py','--overwrite','--repair']
        args = clitools.setArgs()
        self.assertIsNone(args.path)
        self.assertTrue(args.overwrite)
        self.assertFalse(args.edit)
        self.assertTrue(args.repair)







if __name__ == '__main__':
    unittest.main()
