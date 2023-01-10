import unittest
from unittest.mock import patch


class TestMain(unittest.TestCase):

    def setUp(self) -> None:

        self.read_data = [
            '12345 | LAST_NAME FIRST_NAME'
        ]

        self.expected_data = {
            '12345': {
                'name': 'LAST_NAME FIRST_NAME',
                'visit': {
                    '2011-12-12': [
                        '21344', 34324
                    ]
                }
            }
        }

    @patch('read_files')
    def test_main(self, read_files):
        read_files.return_value = self.read_data
        res = main(self.path)
        self.assertEqual(self.expected_data, res)
