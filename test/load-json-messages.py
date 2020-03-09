#!/usr/bin/env python

import json
import glob
import unittest

class ValidateJSON(unittest.TestCase):
    def test_json_file_loads(self):
        jsonfiles = glob.glob("../*.json")
        for jsonfile in jsonfiles:
            with open(jsonfile) as filehandle:
                data = json.load(filehandle)


if __name__ == "__main__":
    unittest.main()
